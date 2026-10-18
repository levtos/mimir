# Alpha 9 — Teil A2: Nachweise für das Review

18.10.2026 · Basis `v1.0.0a8` / `6fcde2a83def3e5cde93d3dea46638d755cbf1e6`.
Branch `agent/codex-alpha9-mimir` · [gemeinsamer PR #26](https://github.com/levtos/mimir/pull/26).
Programmversion **1.0.0a9**. A1-Freigabe von Claude und Benni einschließlich aller
technischen und sprachlichen Auflagen ist eingearbeitet. Technische Umsetzung
und Review-Nachweise sind vom gesondert freizugebenden Teil B getrennt.

| Block | eigener Hauptcommit | Nachweis |
|---|---|---|
| Version zuerst; Gate je maschinell gelesener Slug-Linie | `592e2bb` | [Versionsbericht](versionsgate.json): AwesomeVersion 25.8.0, sieben Tags, keine Fehler; vorhandene und fremde App-Linien getrennt |
| Bifröst-Servicekanal v2 / v1 | `d1dcc71`, `5ebdac9` | `tests/test_alpha9_service_channel.py`, `tests/test_bridge_kernel.py`: Freigaben, Antworten, Grenzen, Zeitlimits, Wiederholungsschutz, Manifestversion und HA-Berechtigungen |
| G2 Kalender | `4881d31` | `tests/test_alpha9_calendar.py`: Cache/Frist, Zeitfenster, lokale Tage/DST, Ausfall ohne künstliche Aktualisierung; `frontend/src/features/sources/calendar.test.tsx` |
| G7 HA-Hinweise | `b444865` | `tests/test_alpha9_notifications.py`: dauerhafte Aufträge, Entprellung, getrennte Achsen, Auflösung; `frontend/src/features/admin/notifications.test.tsx`; [Firefox](bilder/05-benachrichtigungen.png) |
| G15 Herkunft | `652ef5a` | `tests/test_alpha9_context.py`, Bridge-Kernel: Nutzer/Elternkontext, positive automatische Zuordnung, unbekannt bei fehlenden oder widersprüchlichen Belegen |
| G16 erneute Abfrage | `bfc1384` | `tests/test_alpha9_refresh.py`: echte Trigger-Flanke, bestätigte Fähigkeiten, Quoten, begrenzte Wiederholungen, kein Aktualitätsgewinn durch Bestätigung |
| G12 Ablauf-Fristen | `5fba6cc` | `tests/test_alpha9_deadlines.py`, `frontend/src/editors/deadlines.test.tsx`: Reset ohne neue Episode, Parameter/Zustandsdauer, absoluter Eingang, unknown-Hold, Altdefinitionen |
| G10 manuelle Quelle | `1a26906` | `tests/test_alpha9_manual_source.py`, `frontend/src/features/sources/manual.test.tsx`, `frontend/src/editors/manual-source.test.tsx`: typisiert, Gültigkeit, Herkunft, atomare Belege, identische Kennung nach verlorener Antwort, Grenzen ohne JSON; [Firefox](bilder/04-manuelle-quelle.png) |
| G8/G9 Sensorprüfung und Wertherkunft | `13ecc91` | `tests/test_alpha9_sensor_origin.py`: echte Meldungen, Neustart, Vergleichsquelle, Erholung, Halbintervalle/Prognoselücken und überlappende Belege; Formulartests in `frontend/src/editors/` |
| Kategorien/Raum außerhalb der Konfiguration | `3a9ab79` | `tests/test_alpha9_editorial.py`, PostgreSQL-Restore-/Zurücksetzen-Test, `frontend/src/features/editorial/`: unveränderte Prüfsumme und Abläufe, aktuelle Ordnung bleibt bei früherem Stand und historischem Entwurf; [Liste](bilder/01-vertraege-kategorie-raum.png), [Vertrag](bilder/02-vertrag-kategorie-raum.png), [Ändern](bilder/03-vertrag-ordnung-aendern.png) |
| Aufbewahrung, alle Bedingungen, Kopf und Programmversion | `035a95e` | `tests/test_retention.py`, `frontend/src/alpha9/retention-readiness.test.tsx`: 7/730 nur Vorschlag, Stundenwerte ≥ Einzelmessungen, Entwurf → Prüfen → Übernehmen, alle fehlenden Bedingungen ab Erststart, Alpha/Beta dynamisch; [Aufbewahrung](bilder/06-aufbewahrung.png), [System](bilder/07-systemstatus.png), [Kopf](bilder/08-kopfleiste-bereitschaft.png) |
| Freigegebene Texte und Seitenregel | `b042f0d`, `86abebc` | [TEXTE.md](TEXTE.md), `frontend/src/alpha9-pages.test.tsx`: 27 Routen, Lade-/Fehlerfälle, eine Hauptaktion, lesende Verbindungsprüfung; i18n-Scan **0 harte Oberflächentexte**; [Übersicht](bilder/09-uebersicht.png), [Vollständigkeit](bilder/10-vollstaendigkeit.png) |

## Gemeinsame Prüfungen

- Lokal: **649 Python-Tests bestanden**, vier übersprungen, 19 PostgreSQL-bezogene
  Fälle abgewählt. PostgreSQL, MQTT und HA-Kernel laufen in CI.
- Frontend: **343 Tests bestanden**, fünf separat gegen die echte Engine ausgeführte
  Fälle in diesem Lauf übersprungen; TypeScript, Wörterbuchprüfung einschließlich acht
  Scanner-Tests, Build und Paketprüfung. Der Ablauf gegen die echte Test-Engine
  baut Verträge über Formulare, prüft/übernimmt sie und testet Umzug, Zurücksetzen
  und Konflikte. **Alle fünf Fälle bestanden lokal**; sie laufen zusätzlich im eigenen CI-Job.
- Ruff und striktes mypy für Server/Client. CI baut und prüft beide App-Architekturen;
  amd64 durchläuft zusätzlich den isolierten Start-/Migration-/Neustart-Test.
- Verbindlicher CI-Nachweis: [Prüfungen des PR-Heads](https://github.com/levtos/mimir/pull/26/checks).
  Exakter Commit und abgeschlossener Lauf werden im Übergabekommentar des PR
  protokolliert. Ein älterer grüner Lauf gilt nicht für einen neueren Stand.
- [Firefox-Nachweis](bilder/nachweis.json): Firefox 157.0, jedes Bild **1568×710**,
  echte API/Engine mit flüchtigem Speicher und synthetischen Daten. Keine externen
  Browserabrufe und keine JavaScript-Fehler. Die Aufbewahrungsregel wird für die
  Aufnahmen weder gespeichert noch übernommen.

Neue Datenbankmigrationen: 004 (Service-Aufträge/Cache), 005 (manuelle Belege),
006 (redaktionelle Daten). Laufende Installationen wurden in A2 nicht verändert.
Schema 1 und alte Definitionssprachen bleiben lesbar; neue Fähigkeiten benötigen
explizit Schema 2 bzw. Sprache 3. Eine Rückkehr von a9 zu a8 benötigt einen zuvor
geprüften Sicherungs-/Wiederherstellungsweg, keinen stillen Schema-Rückbau.

## Alpha 10 und nächste Freigabe

G4 Titelkatalog und der Ausbau von Import & Export bleiben Alpha 10. Beim späteren
Export/Import müssen Kategorien/Räume mitgenommen werden (ADR 0020). Aktuelle
Kategorien/Räume bleiben jetzt bereits bei Restore, Zurücksetzen und historischen
Entwürfen erhalten. Die Vormerkung steht auch in Issue #24.

**STOPP für Review.** Teil B erst nach Bennis gesondertem „Go“: App-Sicherung,
Update/Pre-Release `v1.0.0a9`, GHCR-Digests und Bifröst via HACS; kein DB-Reset.
Aufbewahrung legt Benni fest. Keine Fachverträge, Policy/Apply oder Legacy-Änderungen.
