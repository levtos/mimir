# Alpha 9 — A1: Design und Textreview

18.10.2026 · Auftrag Benni: ALPHA 9, Grundlage
[#24](https://github.com/Levtos/mimir/issues/24),
[Matrix §4–6](../audits/akte-gap-2026-10.md), ADR 0005–0011 und private Akte P4-65.
Basis: `main = v1.0.0a8 = 6fcde2a83def3e5cde93d3dea46638d755cbf1e6`.
Ein Branch `agent/codex-alpha9-mimir`, ein gemeinsamer PR, eigene Commits je Block.
Aktiver Umsetzungsagent bleibt Codex; Claude prüft Technik, Benni die Texte.

**A1 ist freigegeben; A2 läuft seit 18.10.2026.** Claude hat Technik und Benni
TEXTE.md mit sechs Korrekturen freigegeben. ADR 0020 bewahrt aktuelle Kategorien/
Räume auch bei Zurücksetzen, historischem Entwurf und Backup/Restore. Zuerst wurde
die Programmversion synchron auf 1.0.0a9 gestellt; das reguläre Versionsgate ist grün.
Die folgenden A1-Abgrenzungen dokumentieren den historischen Review-Schritt.

**A1 lieferte ausschließlich Vorschläge in Dokumenten.**
Keine neuen Produkttexte, entfernten Übersetzungsschlüssel, Produktversionen,
Tests, Migrationen, Images, HA-Aufrufe oder Live-Änderungen in diesem Schritt.
A2 beginnt erst nach ausdrücklicher Freigabe; Texte nur gemäß Bennis bestätigter
[TEXTE.md](TEXTE.md). Teil B benötigt danach ein gesondertes „Go“.

## Review-Einstieg

| Block | Design | besonders zu prüfen |
|---|---|---|
| Gemeinsamer Unterbau | [ADR 0012 — Servicekanal](../adr/0012-bifrost-service-channel.md) | feste Freigaben, begrenzte Aufrufe, unbestimmte Ergebnisse, v1/v2 |
| G2 | [ADR 0013 — Kalender](../adr/0013-calendar-cache.md) | vollständige Antwort, Cache-Frist, lokale Tage/DST, Ausfall nach ADR 0005 |
| G7 | [ADR 0014 — HA-Hinweise](../adr/0014-problem-notifications.md) | Entprellen, Sammeln/Auflösen, getrennte Achsen, keine Alarmierung gültiger unzugeordneter Werte |
| G12 | [ADR 0015 — Ablauf-Fristen](../adr/0015-state-machine-deadlines.md) | Reset ohne Episode, zustandsabhängige Dauer, absoluter G1-Termin; unknown pausiert die Frist nicht |
| G10 | [ADR 0016 — Manuelle Quelle](../adr/0016-manual-source.md) | explizite Quelle, Herkunft/Gültigkeit, keine Overrides |
| G15 | [ADR 0017 — HA-Herkunft](../adr/0017-ha-context-origin.md) | positive Belege statt Vermutung, Context-Daten ohne automatische manuell-Zuordnung |
| G16 | [ADR 0018 — Erneute Abfrage](../adr/0018-reconciliation-refresh.md) | Trigger ≠ Evidence, integrationsspezifisches Profil, begrenzte Wiederholungen |
| G8/G9 | [ADR 0019 — Sensorprüfung/Herkunftsart](../adr/0019-sensor-profile-value-origin.md) | Meldetakt ≠ gleicher Wert, kein globales Stuck-Default, Prognoseintervalle |
| Kategorien/Raum | [ADR 0020 — Redaktionelle Daten](../adr/0020-category-room-metadata.md) | MDI lokal, Vorschlag/Handänderung, keinerlei Prüfsummen-/Ablaufwirkung |
| Bedienung/Kleinkram | [ADR 0021 — Formulare und Bereitschaft](../adr/0021-plain-ui-retention-readiness.md) | Aufbewahrung, alle Bedingungen ab Erststart, Kopf/Programmversion, Seitenregel |
| Sprache | [TEXTE.md](TEXTE.md) | vollständige Bestandsprüfung, änderbare Vorschläge, Löschliste, neue Texte, Seitenabweichungen |

Zahlen für technische Zeitlimits, Entprellung, Kalenderfenster und Wiederholung
sind ausdrücklich Vorschläge. Bennis feststehende Entscheidungen (Scope,
Wörterbuch, Version a9, 7/730 als Aufbewahrungsvorschlag, neue Kategorien/Raum,
Release-/Live-Gates) werden dadurch nicht neu geöffnet.

## Ist-/Soll-Abgleich und Versionsgrenzen

Belegtes a8: Bifröst kennt info/subscribe mit Protokoll 1, keine Serviceantworten;
SM-Frist hängt an neuer Episode; kein manual-Adapter, keine Context-Eltern-/Nutzer-
Auswertung, kein G8/G9-Modell. G1/G19/G14 und die Aufbewahrungsengine sind vorhanden.
Aufbewahrung hat noch kein eigenes geführtes Formular. Die bekannte Bridge-
Versionskonstante meldet a1 trotz a8-Manifest. Frontend ist React; dieser Auftrag
migriert kein Framework. Der enge MDI-Wunsch für Kategorien folgt Bennis Auftrag.

Neue Semantik wird explizit als Fähigkeit versioniert. Für neue SM-Konstrukte
Sprachversion 3, alte Definitionen 1/2 mit unveränderten Ergebnissen und
Fingerprints weiter lesen. Vorgeschlagen: neues Registry-Schema 2 für die
zusätzlichen manuellen Quellen, Profile, Herkunfts-/Abruf- und Hinweisregeln;
Schema 1 weiterhin lesen, keine automatische Umschreibung aktiver Stände.
Ein Schema-1-Dokument mit neuen Feldern wird abgewiesen. Vor Übernahme eines
Schema-2-Entwurfs erklären, dass a8 es nicht lesen kann; Rückkehr nur über
passenden früheren Stand und nach geprüftem Sicherungs-/Restore-Verfahren.
Neue optionale Schemafelder dürfen historische Prüfsummen beim bloßen Laden
nicht ändern. Redaktionelle Kategorie/Raum liegen deshalb außerhalb der Registry.

Die ADR-JSON-Ausschnitte illustrieren diese neuen, noch nicht implementierten
Formate. Sie sind keine vollständig validierbaren Konfigurationen oder Fachverträge.
Jedes neue Feld erhält A2-Schema, Capability, Formulareingabe, deutsche Erklärung,
API-/Client- und Altformat-Tests. Einzig die Service-Transportfreigabe darf
technische HA-Ziele kennen; Fachregeln benutzen kanonische Quellen/Verträge.

Versionsziel A2/B: **1.0.0a9**, Supervisor-Linie mimir. Vor Tag vollständiger
Versionsbericht gemäß ADR 0009; kein .post/.dev und keine Änderung alter Artefakte.
A1 behält a8-Metadaten. Deshalb ist das Vor-Tag-Gate der a8-Basis gegen den bereits
existierenden eigenen a8-Tag erwartbar rot; dies wird dokumentiert, nicht mit einem
vorzeitigen Versionswechsel oder einer Gate-Ausnahme verdeckt. A2 muss nach dem
expliziten Versionswechsel alle regulären Checks grün bestehen.

## A2-Nachweisplan — noch nicht ausgeführt

A1-Dokumentprüfung: 12 Markdown-Dateien, 32 lokale Links und 11 syntaktisch
gültige JSON-Ausschnitte; alle 2.250 Ausgangsschlüssel in der Textprüfung,
keine unbeabsichtigt geänderten Platzhalter. Bestehender a8-i18n-Scan: 0 harte
Texte; Trockenlauf der Schlüsselbereinigung: 2 sicher unbenutzte Schlüssel.
Das ist keine Implementierungs- oder Oberflächenabnahme für Alpha 9.
Vor-Tag-Gate auf unveränderter a8-Basis: erwarteter Fehler „1.0.0a8 ist nicht
neuer als v1.0.0a8 in Linie mimir“; sieben Tags gelesen. Erst A2 setzt a9.

1. Servicekanal, G2/G7/G15/G16; danach G12/G10/G8/G9; Kategorien/Raum;
   bestätigte Texte und übrige Bedienkorrekturen jeweils in eigenen Block-Commits.
2. Tests je ADR, insbesondere Restore/Commit-Fehler, alte Definitionen, redaktionelle
   Änderungen ohne Prüfsummen-/Ablaufwirkung und typisierte Eingaben ohne JSON.
3. Vollständige CI und i18n-Scan 0 harte Texte. Keine Produktnachweise aus A1 ableiten.
4. Firefox 1568×710: Kategorien/Raum in Liste und Vertrag, manuelle Quelle,
   Benachrichtigung, Aufbewahrung, Systemstatus, Kopfleiste. Echte Formularaktionen.
5. Kurze ABNAHME.md mit Block → Commit → Test/Bild/CI, danach STOPP für Review.

## Releasegrenze und Ausschlüsse

Teil B erst nach Bennis „Go“: v1.0.0a9/Pre-Release, beide GHCR-Architekturen mit
Digests und Versionsbericht, Mimir-Update **mit App-Sicherung**, Bifröst via HACS.
Kein DB-Reset. Migration/Startlog/Version/Ingress und Verbindung über Protokoll 2
prüfen, dann STOPP. Kein automatischer Eingriff in bestehende Fachkonfiguration.

G4 Titelkatalog sowie Ausbau von Import & Export bleiben Alpha 10. Kategorien,
Raum, „Verknüpfung“ und repository.yaml-Name Mimir sind in Alpha 9 vorgezogen.
Keine Fachverträge, Policy/Apply oder Änderungen am Legacy-Repository. Private
Akte und Betriebsdaten werden nicht ins öffentliche Repository kopiert.
