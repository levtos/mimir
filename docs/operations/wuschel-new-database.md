# Wuschel — letzter Reset vor Beta, vorbereiteter DB-Ablauf

20.10.2026 · **Teil A1: Plan, nicht ausgeführt.**
[ADR 0023](../adr/0023-last-reset-identity.md),
[Alpha-10-Gates](../alpha10/README.md). Erst Bennis Teil-B-Go erlaubt
Provisionierung/Installation. Benni führt das Skript selbst aus.

## Ziel und Vorbedingungen

Eigene neue Datenbank `wuschel`, neue Rolle `wuschel_app`, neue UUID und
leeres eigenes /data. `mimir` bleibt einschließlich laufender App unberührt.
Keine bestehende DB umbenennen, leeren, migrieren oder überschreiben.
Kein PostgreSQL-Upgrade/-Neustart; allein HBA-Reload für den neuen Zugriff.
Kein Kopieren einer alten Installationskennung oder ihrer Tokens.

Dieses öffentliche Runbook hält Netzwerte als Parameter. Benni erhält separat
den konkreten Proxmox-Einfügeblock für LXC 108 und ausschließlich die neue
Einhornzentrale-HAOS-IP. Alte Benni-/Eltern-Instanzen sind keine zulässigen Ziele.
Keine echten Hostnamen, Passwortwerte oder privaten Sicherungsinhalte in GitHub.

Vor Ausführung: ausreichender Platz für Custom-Dump der alten DB, Rückweg und
Rootzugriff auf Proxmox/LXC sicherstellen. Lokale PostgreSQL-Peer-Administration
muss funktionieren. Skript verlangt genau einen lokalen Cluster (online),
PostgreSQL ≥14 und vorhandenes TLS; andernfalls sicherer Abbruch.
DB-Hostname/SAN/öffentliche CA müssen für `verify-full` schon passen.
DNS-Probleme meldet Codex an Benni, kein automatisches DNS-/Zertifikatsändern.
Kein Mitschnitt/Screen-Sharing des späteren manuellen Passworteintrags.

Die neue Regelmenge wird vor allgemeine HBA-Regeln gestellt:

```text
local   wuschel postgres peer
local   wuschel all reject
local   all wuschel_app reject
hostssl wuschel wuschel_app <HAOS_IP>/32 scram-sha-256
host    all wuschel_app 0.0.0.0/0 reject
host    all wuschel_app ::/0 reject
host    wuschel all 0.0.0.0/0 reject
host    wuschel all ::/0 reject
```

Die einzige Netzwerkfreigabe ist die neue HAOS-IP/DB/Rolle über TLS;
lokale postgres-Administration ist ausdrücklich separat. Die Ablehnungen
verhindern, dass spätere breite Altregeln neue DB/Rolle versehentlich öffnen.
Bestehende Regeln für Mimir/Terra/Legacy werden weder ersetzt noch neu ausgelegt.
Kein `clientcert=verify-full` verlangen: gemeint ist die **clientseitige**
Prüfung des Servernamens; Clientzertifikate sind kein neuer Produktentscheid.

## Vorbereiteter Einfügeblock (nicht in A1 ausführen)

Benni setzt auf dem Proxmox-Host `WUSCHEL_LXC_ID` und `WUSCHEL_HAOS_IP`
aus dem privaten Betriebsblatt, dann den gesamten Block einfügen.
Er enthält keine Passwortwerte. Keine Ausführung mit `bash -x`, SQL-Echo
oder Debug-Logging. Das Passwort wird ausschließlich im Container erzeugt.

Das Skript prüft die Sitzungseinstellungen vor dem Geheimnis. Unbekannte
Preload-/Auditmodule führen vor Passwortanlage zum Abbruch; deren mögliche
Zusatzprotokollierung muss zuerst separat bewertet werden. Keine stille
Abschaltung globaler Clusterprotokollierung. Session-Logging wird für diese
lokale Provisioniersitzung unterdrückt. Das SCRAM-Verifier-SQL geht nur über
stdin, weder in argv/Environment noch in Dateien oder ausgegebene Fehler.

```bash
set -eu
set +x
umask 077
: "${WUSCHEL_LXC_ID:?LXC-ID aus dem privaten Betriebsblatt setzen}"
: "${WUSCHEL_HAOS_IP:?Neue HAOS-IP aus dem privaten Betriebsblatt setzen}"
pct exec "$WUSCHEL_LXC_ID" -- env WUSCHEL_HAOS_IP="$WUSCHEL_HAOS_IP" python3 - <<'PY'
import base64
import datetime
import fcntl
import hashlib
import hmac
import ipaddress
import os
from pathlib import Path
import secrets
import stat
import subprocess
import sys

os.umask(0o077)
if os.geteuid() != 0:
    sys.exit("Abbruch: Root im Container erforderlich.")
try:
    allowed_ip = str(ipaddress.IPv4Address(os.environ["WUSCHEL_HAOS_IP"]))
except (KeyError, ValueError):
    sys.exit("Abbruch: einzelne IPv4-Adresse erforderlich.")
lock = open("/run/lock/wuschel-alpha10-provision.lock", "a")
try:
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
except BlockingIOError:
    sys.exit("Abbruch: Provisionierung bereits aktiv.")

safe_env = {
    "PATH": "/usr/sbin:/usr/bin:/sbin:/bin", "LANG": "C",
    "PGOPTIONS": "-c log_statement=none -c log_min_error_statement=panic "
                 "-c log_min_duration_statement=-1 -c log_duration=off "
                 "-c log_min_duration_sample=-1 -c log_transaction_sample_rate=0"
}

def command(argv, *, data=None, output=None):
    result = subprocess.run(
        argv, input=data, stdout=output if output is not None else subprocess.PIPE,
        stderr=subprocess.DEVNULL, env=safe_env, check=False
    )
    if result.returncode != 0:
        raise RuntimeError("Lokaler PostgreSQL-Schritt fehlgeschlagen.")
    return result.stdout or b""

clusters = command(["pg_lsclusters", "--no-header"]).decode().splitlines()
if len(clusters) != 1:
    sys.exit("Abbruch: genau ein PostgreSQL-Cluster erforderlich.")
parts = clusters[0].split()
if len(parts) < 4 or parts[3] != "online":
    sys.exit("Abbruch: Cluster nicht eindeutig online.")
port = str(int(parts[2]))

def sql(text, db="postgres"):
    return command(
        ["runuser", "-u", "postgres", "--", "psql", "-X", "-qAt",
         "--no-password", "-v", "ON_ERROR_STOP=1", "-h", "/var/run/postgresql",
         "-p", port, "-U", "postgres", "-d", db],
        data=text.encode()
    ).decode().strip()

password_path = Path("/root/wuschel_app.password")
hba_path = None
old_hba = None
hba_changed = False
created_role = False
try:
    if password_path.exists() or password_path.is_symlink():
        raise RuntimeError("Passwortdatei existiert bereits; keine Rotation.")
    if int(sql("SHOW server_version_num;")) < 140000:
        raise RuntimeError("PostgreSQL mindestens 14 erforderlich.")
    if sql("SHOW ssl;") != "on":
        raise RuntimeError("Vorhandenes Server-TLS erforderlich.")
    if sql("SHOW shared_preload_libraries;"):
        raise RuntimeError("Preload-/Auditmodule zuerst separat reviewen.")
    if sql("SELECT count(*) FROM pg_extension WHERE extname='pgaudit';") != "0":
        raise RuntimeError("Auditmodul zuerst separat reviewen.")
    checks = sql(
        "SELECT current_setting('log_statement')='none' "
        "AND current_setting('log_min_error_statement')='panic' "
        "AND current_setting('log_min_duration_statement')='-1' "
        "AND current_setting('log_duration')='off' "
        "AND current_setting('log_min_duration_sample')='-1' "
        "AND current_setting('log_transaction_sample_rate')::numeric=0;"
    )
    if checks != "t":
        raise RuntimeError("Sichere lokale Sitzung nicht belegt.")
    if sql("SELECT count(*) FROM pg_roles WHERE rolname='wuschel_app';") != "0":
        raise RuntimeError("Rolle existiert bereits; Herkunft manuell klären.")
    if sql("SELECT count(*) FROM pg_database WHERE datname='wuschel';") != "0":
        raise RuntimeError("Datenbank existiert bereits; keine Umwidmung.")
    if sql("SELECT count(*) FROM pg_database WHERE datname='mimir';") != "1":
        raise RuntimeError("Alte Datenbank nicht eindeutig vorhanden.")
    hba_path = Path(sql("SHOW hba_file;"))
    metadata = hba_path.lstat()
    if not stat.S_ISREG(metadata.st_mode):
        raise RuntimeError("HBA ist keine reguläre Datei.")
    old_hba = hba_path.read_bytes()
    if b"BEGIN WUSCHEL ALPHA10" in old_hba:
        raise RuntimeError("Wuschel-HBA-Block bereits vorhanden.")
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    backup = Path("/root") / ("wuschel-alpha10-backup-" + stamp)
    backup.mkdir(mode=0o700)
    hba_backup = backup / "pg_hba.conf"
    hba_backup.write_bytes(old_hba)
    hba_backup.chmod(0o600)
    dump = backup / "mimir.dump"
    with dump.open("xb") as handle:
        os.fchmod(handle.fileno(), 0o600)
        command(
            ["runuser", "-u", "postgres", "--", "pg_dump", "--no-password",
             "-h", "/var/run/postgresql", "-p", port, "-U", "postgres",
             "--format=custom", "--dbname=mimir"], output=handle
        )
    listing = command(["pg_restore", "--list", str(dump)])
    if b"dbname: mimir" not in listing and b"database: mimir" not in listing:
        raise RuntimeError("Custom-Archiv nicht als mimir validiert.")
    dump_hash = hashlib.sha256()
    with dump.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            dump_hash.update(chunk)
    (backup / "mimir.dump.sha256").write_text(dump_hash.hexdigest() + "  mimir.dump\n")
    sql("CREATE ROLE wuschel_app NOLOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE "
        "NOREPLICATION NOBYPASSRLS NOINHERIT;")
    created_role = True
    sql("CREATE DATABASE wuschel OWNER postgres TEMPLATE template0 ENCODING 'UTF8';")
    sql("REVOKE ALL ON DATABASE wuschel FROM PUBLIC; "
        "GRANT CONNECT ON DATABASE wuschel TO wuschel_app;")
    sql("REVOKE ALL ON SCHEMA public FROM PUBLIC; "
        "GRANT USAGE, CREATE ON SCHEMA public TO wuschel_app; "
        "ALTER DEFAULT PRIVILEGES FOR ROLE wuschel_app IN SCHEMA public "
        "REVOKE ALL ON TABLES FROM PUBLIC; "
        "ALTER DEFAULT PRIVILEGES FOR ROLE wuschel_app IN SCHEMA public "
        "REVOKE ALL ON SEQUENCES FROM PUBLIC; "
        "ALTER DEFAULT PRIVILEGES FOR ROLE wuschel_app IN SCHEMA public "
        "REVOKE EXECUTE ON FUNCTIONS FROM PUBLIC;", "wuschel")
    sql("ALTER ROLE wuschel_app IN DATABASE wuschel SET search_path=public;")
    block = (
        "# BEGIN WUSCHEL ALPHA10\n"
        "local wuschel postgres peer\n"
        "local wuschel all reject\n"
        "local all wuschel_app reject\n"
        f"hostssl wuschel wuschel_app {allowed_ip}/32 scram-sha-256\n"
        "host all wuschel_app 0.0.0.0/0 reject\n"
        "host all wuschel_app ::/0 reject\n"
        "host wuschel all 0.0.0.0/0 reject\n"
        "host wuschel all ::/0 reject\n"
        "# END WUSCHEL ALPHA10\n"
    ).encode()
    candidate = hba_path.with_name(hba_path.name + ".wuschel-new")
    with candidate.open("xb") as handle:
        os.fchmod(handle.fileno(), stat.S_IMODE(metadata.st_mode))
        os.fchown(handle.fileno(), metadata.st_uid, metadata.st_gid)
        handle.write(block + old_hba)
        handle.flush()
        os.fsync(handle.fileno())
    if hba_path.read_bytes() != old_hba:
        candidate.unlink()
        raise RuntimeError("HBA wurde gleichzeitig geändert; nichts überschreiben.")
    os.replace(candidate, hba_path)
    hba_changed = True
    if sql("SELECT count(*) FROM pg_hba_file_rules WHERE error IS NOT NULL;") != "0":
        raise RuntimeError("HBA-Prüfung fehlgeschlagen.")
    if sql("SELECT pg_reload_conf();") != "t":
        raise RuntimeError("HBA-Reload fehlgeschlagen.")
    # Nur Datei + Arbeitsspeicher: kein Passwort in argv, Env, SQL oder Ausgabe.
    password = secrets.token_urlsafe(48)
    fd = os.open(password_path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, "w") as handle:
        os.fchmod(handle.fileno(), 0o600)
        handle.write(password + "\n")
        handle.flush()
        os.fsync(handle.fileno())
    salt = secrets.token_bytes(16)
    salted = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 4096)
    client_key = hmac.digest(salted, b"Client Key", "sha256")
    stored_key = hashlib.sha256(client_key).digest()
    server_key = hmac.digest(salted, b"Server Key", "sha256")
    b64 = lambda value: base64.b64encode(value).decode("ascii")
    verifier = "SCRAM-SHA-256$4096:" + b64(salt) + "$" + b64(stored_key) + ":" + b64(server_key)
    sql("ALTER ROLE wuschel_app PASSWORD '" + verifier + "' LOGIN;")
    del password, salted, client_key, stored_key, server_key, verifier
    print("Vorbereitet: neue DB/Rolle, geprüfter HBA-Block, alte DB gesichert.")
    print("Passwort ausschließlich in /root/wuschel_app.password; keine Ausgabe.")
    print("Sicherungsordner: " + str(backup))
except Exception:
    if created_role:
        try:
            sql("ALTER ROLE wuschel_app NOLOGIN;")
        except Exception:
            pass
    if hba_changed and hba_path is not None and old_hba is not None:
        try:
            if hba_path.read_bytes() == block + old_hba:
                hba_path.write_bytes(old_hba)
                sql("SELECT pg_reload_conf();")
            else:
                print("HBA inzwischen fremd geändert; manueller Rückweg erforderlich.")
        except Exception:
            print("HBA-Rückweg manuell prüfen; Rolle bleibt gesperrt, soweit erreichbar.")
    # Keine Exception-/SQL-Details: sie könnten geheime Inhalte enthalten.
    sys.exit("Abbruch. Keine DB/Rolle automatisch gelöscht; Restzustand lokal prüfen.")
PY
```

Das Skript ist absichtlich **nicht blind wiederholbar**: vorhandene DB, Rolle,
Passwortdatei oder eigener HBA-Block führen zum Abbruch, nie zur Rotation oder
Wiederverwendung unbekannter Identität. Nach Teilfehler Zustand anhand
DB-/Rollenexistenz, NOLOGIN, HBA-Hash und Sicherungsdatei prüfen. Passwortdatei
nicht anzeigen. Nur nach geklärtem Rückweg darf Benni einen neuen Versuch planen.

## Passwort und Client-Konfiguration

Benni überträgt das Passwort selbst über seinen geschützten lokalen Weg in
das neue App-Feld. **Keinen cat-/type-/Get-Content-Befehl und keine
Passwortausgabe im Codex-/Proxmox-Nachweis verwenden.**
Der Runbookablauf gibt den Dateiinhalt nicht an Codex zurück.
Datei niemals committen, hochladen, in Tickets kopieren oder gemeinsam mit
einem öffentlichen Nachweis archivieren. Geheimnis bleibt Benni vorbehalten.

Neue Optionen: DB wuschel, User wuschel_app, bestehender zertifizierter
Hostname, Port, öffentliche CA und verify-full. Eigene Installation, keine
Adoption; Erstinitialisierung nur bei leerer DB und anschließend zurücknehmen.
Alle Eingaben der App-Optionen erfolgen ohne Auslese durch Codex.

## Nachweise erst in B

- Archiv vorhanden, root/0600, SHA256 und pg_restore-Verzeichnisprüfung;
  keine Ausgabe des Dumps/Passworts/Verifiers.
- neue Rolle ohne Sonderrechte/Mitgliedschaften; nur CONNECT plus eigene
  Schema-DDL; keine Rechte an anderen DBs durch diese Provisionierung.
- pg_hba_file_rules ohne Fehler; Netzwerk-Login nur exakte HAOS-IP über TLS.
  Syntaxprüfung/pg_reload_conf allein beweisen noch keinen End-to-End-Zugriff.
- Client aus Wuschel mit vorhandener CA und Hostnamenprüfung; eigener
  pg_stat_ssl-Beleg; Negativfall sslmode=disable abgewiesen. Keine
  Verbindungszeichenfolge mit Passwort protokollieren.
- falscher Hostname/fehlende CA scheitert sicher; keine Ausweichoption
  require/disable setzen. DNS-Probleme an Benni melden.
- leere DB-Migrationen, neue UUID, Writer-Lock, sicher gefilterter aktueller
  Startabschnitt. Keine Readiness erzwingen, keine Retention eigenmächtig setzen.

## Rückweg

Wuschel allein stoppen; keine automatische Aktivierung/Änderung von Mimir,
Terra oder Legacy. Falls der HBA-Block zurückgenommen werden muss, Benni
prüft zuerst, dass seit der Sicherung keine fremde HBA-Änderung erfolgte.
Nur dann gesicherte pg_hba.conf mit Originaleigentümer/-modus zurückkopieren,
pg_hba_file_rules prüfen und Reload. Bei fremden Änderungen allein den
eigenen markierten Block entfernen und erneut prüfen; kein Komplettüberschreiben.
Kein Serverrestart. Neue Rolle vor Rücknahme auf NOLOGIN setzen.

Die alte DB benötigt für den normalen Rückweg keinen Restore, da sie unverändert
blieb. Falls ein echter Desasterfall einen Restore verlangt: in **separate**
Recovery-DB einspielen, prüfen, nicht über das erhaltene mimir schreiben.
Neue wuschel-DB/Passwortdatei bleiben bis zur Benni-Entscheidung gesperrt erhalten.
Keine automatische DROP-/Passwortlöschung im Provisionierskript.

## Alte Datenbank erst nach Beta-Abnahme löschen

**Gesperrt bis Bennis gesondertem Go.** Vorher alte App abgenommen/deinstalliert,
aktuelle zusätzliche Sicherung geprüft und keine Sitzung mehr auf mimir.
Benni verwendet in der lokalen Container-Shell den fest benannten alten DB-Namen:

```bash
# Erst nach explizitem Go; bricht bei bestehenden Verbindungen ab.
runuser -u postgres -- dropdb --no-password --if-exists mimir
```

Kein --force, kein DROP OWNED/Schema-Wildcard. Rolle mimir_app und alte
Passwortdateien sind ein gesonderter manueller Aufräumschritt, nachdem Benni
deren verbleibende Verwendung ausgeschlossen hat. Keine Anweisung zur
Ausgabe einer Passwortdatei.

## Primärquellen

[PostgreSQL: HBA-Reihenfolge/hostssl](https://www.postgresql.org/docs/current/auth-pg-hba-conf.html),
[TLS/verify-full](https://www.postgresql.org/docs/current/libpq-ssl.html),
[CREATE ROLE](https://www.postgresql.org/docs/current/sql-createrole.html),
[Custom-Dump](https://www.postgresql.org/docs/current/app-pgdump.html),
[pg_restore](https://www.postgresql.org/docs/current/app-pgrestore.html).
Client verify-full ist die zusätzliche Hostnamenprüfung; hostssl allein
erzwingt nur eine verschlüsselte Transportverbindung.
