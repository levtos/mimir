# Alpha 10 — Quellen und Prüfung von Teil A1

20.10.2026 · **Designnachweis, keine Produkt-/Installations-/Live-Abnahme**.

## Verifizierte Quellen

- Wuschel main/Commit von v1.0.0a9:
  `f039081a19896e0529d0f508725f7fda97485981`.
  Tagobjekt `bebd3bdad0a9070d5ee97665f6ce0c2216f6b8b7`.
  Frischer Clone, Basis vor Änderungen sauber.
- Control main: `8347af48a908c05aded86c3d29431968abdda86a`.
  Frischer Clone, eigener ergänzender Dokumentationsbranch.
- [wuschel#24](https://github.com/Levtos/wuschel/issues/24): vollständiger
  Body, alle zehn bis Arbeitsbeginn vorhandenen Kommentare, Labels und
  sämtliche Projektfelder gelesen. Eingang: Testing / Feature / Codex /
  Platform / Tests Pass; diese Evidence gehört zum historischen Alpha-9-Stand.
- [control#60](https://github.com/Levtos/control/issues/60): vollständiger
  Body und Kommentar vom 20.10.2026 sowie Projektfelder gelesen.
  Eingang: Projekt zugeordnet, die fachlichen Felder noch leer.
- Control ADR 0001/0002, Bootstrap, Verifikationsregel, aktueller Vertrag
  und sämtliche Kommentare in #17. Die konkrete Alpha-9-React-Ausnahme aus
  ADR 0020 bleibt maßgeblich; Alpha 10 migriert kein Framework.
- [Matrix](../audits/akte-gap-2026-10.md), ADR 0007–0021 und relevante
  Build-Spezifikation zu A-06, Registry, Writer, App und Restore.
- Title-Classifier-Formatbeleg: lokaler lesender Quellstand
  `Entity-Title-Mapper@cd220cf8a78262ca6d7dca54ed0167b99e91064c`,
  `custom_components/title_classifier/io_v3.py` (v3-Export, Identität,
  Elternbezug, Kontexte/Overrides, Telemetrie). Keine Aussage, dass dies
  die aktuelle installierte Version oder der aktuelle produktive Bestand ist.
  Vor realem Import: Quellrelease/-digest und konsistente Datei neu verifizieren.
- Herden-ZIP: 18 RGBA-PNGs mit den beauftragten Maßen plus Steckbrief;
  [Quellmanifest](herde-quellen.json). Nur Metadaten/Hashes und drei Motive
  zur Designprüfung gelesen; Originaldateien nicht im PR übernommen.
  Wuschel-Icon betrachtet, Siegel-Ausschnitt als A2-Reviewwert vorgesehen.

## Sichere Prüfung

CTX für Orientierung, Dateizugriff und Shell verwendet. Exakte Shellbefunde
mit `lean-ctx raw` gesichert; komprimierte Zusammenfassungen nicht als
wörtliche Beweise übernommen. Keine Secrets, kein Supervisor-Optionsabruf,
keine LXC-/HA-Verbindung und kein Passwortdateizugriff in A1.
GitHub-Schreibaktionen setzen jeweils frischen Actor-Preflight
`gh api user --jq .login = levtos-codex` voraus.
Commitautor wird davon separat als Codex Agent dokumentiert.

[Umbenennungsinventar](rename-inventory.md): alle getrackten Basisdateien
und Pfade per case-insensitive Namensmuster geprüft; 229 Dateien/Pfade mit
Treffern, einschließlich historischer Belege, technischer Importpfade und
zu erhaltender Terra-Dateien. Basiszeilen stehen je Datei im Inventar.
Keine pauschale Ersetzung aus einer Trefferzählung.

Die neue App-Konfiguration wurde noch nicht angelegt. Bestehendes
`mimir/config.yaml` deklariert postgres_password und mqtt_password bereits
als password. Das ist ein statischer Quellbefund; A2 ergänzt explizite
Regression und Leaktests. A1 ändert keine Produktoption.

Dokumentationsprüfung: UTF-8, geschlossene Codefences, relative Links,
striktes JSON für die zwei Strukturbeispiele, `git diff --check`.
Der eingebettete Provisionierungsblock wurde nur mit Python-AST und
`bash -n` geprüft; kein import/exec, kein PostgreSQL-/Proxmox-Aufruf.
Hashbildung/Passwortvergabe/SCRAM und Rückweg sind Entwürfe, kein bereits
erprobter Betrieb. Vor B verbleiben Review und sichere Laufzeit-Vorbedingungen.

Nur neue Markdown-/JSON-Designdokumente und der Fortschreibungslink in
ADR 0008 gehören zum Wuschel-Diff. Control enthält allein den Herdenplan.
Produktcode, Tests, Versionen, Workflows und Originalbilder unverändert.
Die CI eines Draft-PRs kann durch GitHub automatisch starten; sie ist weder
eine manuell gestartete Veröffentlichung noch die A2-Produktabnahme.
Insbesondere ist das Vor-Tag-Gate mit unverändertem a9-Kandidaten kein
Nachweis für den erst in A2 einzutragenden a10-Kandidaten.

## Reviewpunkte und offene Nachweise

Review soll insbesondere prüfen: Distributionsname bei erhaltenem Importpfad,
neue UUID/keine Adoption, Protokoll 2 innerhalb neuer Domain, restriktiver
HBA-Block/Logging-Abbruch, Master-/Kontextimport ohne Datenverlust, gezielte
Trace-basierte A-06-Regel, atomare Pflege/Importübernahme und Editorialkonflikte.
Format-/Sprachversion 3/4 und vorgeschlagene Größenlimits sind Detaildesign,
keine nachträglich behauptete bereits beschlossene Fachentscheidung.

Noch nicht erfolgt: Produktimplementierung, neue Migrationen, Bildableitung,
CI-/i18n-/Firefox-Abnahme von Alpha 10, Merge/Tag/Release/Images,
DB-Anlage/Reset, App-/HACS-Installation, MQTT-Livetest, Bestandsimport,
Deinstallation oder Löschen alter DB. Keine DNS-Änderung.
**STOPP für Review; A2 und B bleiben ausdrücklich gesperrt.**
