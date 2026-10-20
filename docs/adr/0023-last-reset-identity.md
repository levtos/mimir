# ADR 0023 — letzter Reset vor Beta mit eigener Wuschel-Identität

20.10.2026 · neue DB/Slug durch Benni entschieden; **A1 / technische Review**.
Bezug: [0022](0022-wuschel-traber-naming.md), A-06, APP-01,
[Runbook](../operations/wuschel-new-database.md).

## Entscheidungsvorschlag

Wuschel ist mit `slug:wuschel`, eigener leerer /data-Ablage und neuer DB
`wuschel` eine neue Installation. **Neue installation_id: ja.**
Kein Kopieren von `installation.json`, Tokens, Entwürfen, Laufzeitkontext oder
`adopt_installation_id` aus Mimir/Terra. Es gibt keinen Restore alter Baselines.
Damit werden auch Writer, Hinweis-IDs und Laufzeitepochen eindeutig getrennt.
Der Namenswechsel allein wäre keine A-06-Änderung; der ausdrücklich verlangte
Reset verwirft jedoch die Vergleichsgrundlage. Neue Werte brauchen aktuelle
Evidence, ohne rückwirkende Flanken, Durchläufe oder nachgespielte Befehle.

Die ursprüngliche „letzter Reset ohne Neuinstallation“-Planung in ADR 0008
wird durch Bennis neuen Slug-Auftrag ersetzt. Danach bleibt der Wuschel-Slug
bis Beta-Abnahme stabil; kein weiterer geplanter Reset.

## Daten- und Betriebsgrenzen

Neue Rolle `wuschel_app`: LOGIN erst nach HBA-Prüfung, kein Superuser,
CREATEDB, CREATEROLE, Replication, BYPASSRLS oder Rollenmitgliedschaften.
DB-Eigentümer bleibt postgres, App bekommt CONNECT und USAGE/CREATE nur im
eigenen public-Schema für Migrationen. Kein PUBLIC-CONNECT/TEMP.
Eigene Objekte darf die Rolle verwalten; keine Extension-/Cluster-Rechte.
Mindestens PostgreSQL 14, vorhandenes TLS weiterverwenden; kein Serverupgrade.

Server lässt für neue DB/Rolle nur die benannte HAOS-Quell-IP via hostssl/SCRAM
zu, lokale postgres-Administration bleibt separat. Explizite Reject-Regeln
stehen vor allgemeinen Altregeln. Client `verify-full` prüft CA **und**
Zertifikatshostnamen; hostssl allein ersetzt das nicht. Ein neuer DNS-Name
ist unnötig, wenn der vorhandene zertifizierte DB-Hostname weiter passt.
Fehlende Auflösung/SAN/CA an Benni melden; kein DNS-/Zertifikatsumbau durch Codex.

Das vorbereitete Skript im Runbook wird ausschließlich von Benni in Teil B
ausgeführt. Es erzeugt das Passwort auf dem LXC und schreibt es mit umask 077
nur nach `/root/wuschel_app.password`; keine Ausgabe, Logzeile oder
Prozessargumente mit Passwort. Kein `pg_dumpall --globals-only` mit Rollensecrets.
Ohne sichere lokale Sitzung/Logging-Prüfung vor Passwortvergabe bricht es ab.
Teil A1 führt weder das Skript noch Clusterbefehle aus.

## Start- und Abnahmefolge

Nach Benni-DB-Schritt: neue App mit DB/Rolle wuschel(_app), vorhandenem
Zertifikatshost, CA und `verify-full`; Passwort trägt Benni selbst ein.
Erstinitialisierung ausdrücklich nur für leere DB erlauben, nach Erststart
von Benni zurücknehmen. Keine Adoption. Nachweis liest allein sichere
Status-/Identitätsfelder, niemals die gesamte Optionsstruktur.

A2 testet neue/gleiche/fremde ID, leere DB, Wiederstart ohne erneute ID-Erzeugung,
Migrationen und gemischte DB-/data-Zuordnung mit Abbruch. B belegt neue UUID
ungleich alten UUIDs, TLS/Hostprüfung, hostssl-Negativtest, minimale Rechte,
Migrationen auf leerer DB, Writer-Lock, Ingress. Fehlende aktive Konfiguration
oder Aufbewahrung bleibt als offenes Betriebsgate sichtbar.

## Sicherung und Rückweg

`mimir` bleibt unangetastet bis Beta-Abnahme und gesondertem Lösch-Go.
Vor Anlage: eigene Custom-Sicherung dieser externen DB und HBA-Dateisicherung,
Archive per pg_restore-Verzeichnisprüfung validieren. Nicht allein auf
Supervisor-App-Backup vertrauen. Keine neue Veröffentlichung von Dateninhalten.

Rollback stoppt/entfernt nur Wuschel und nach Benni-Entscheidung Traber,
stellt nötigenfalls nur den gesicherten HBA-Stand wieder her und lässt
Mimir/Terra/Legacy-DBs und Optionen unverändert. Kein Restore über die alte DB,
kein automatisches Löschen einer teilweise angelegten Rolle/DB. Detaillierte
Vorbedingungen und gesonderter Löschbefehl stehen im Runbook.
