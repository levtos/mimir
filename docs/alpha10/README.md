# Alpha 10 — Design zur Review (Teil A1)

20.10.2026 · Agent: `agent:codex`. **A1 dokumentiert; A2 und B gesperrt.**
Verbindlicher Auftrag: Benni, Alpha 10; [wuschel#24](https://github.com/Levtos/wuschel/issues/24)
und [control#60](https://github.com/Levtos/control/issues/60).
Ein Branch `agent/codex-alpha10-wuschel`, ein gemeinsamer Draft-PR in Wuschel,
Block-Commits; ergänzender Draft-PR in Control. Beide bleiben zur Review offen.

## Grundlage und Ist-/Soll-Abgleich

Quellbasis: `main@f039081a19896e0529d0f508725f7fda97485981`,
identisch mit dem Commit von `v1.0.0a9`. Repository jetzt `Levtos/wuschel`;
der Quellstand trägt noch Mimir/Bifröst und Version 1.0.0a9.
Dies ist ein Repository-Befund, keine aktuelle Live-Inventur.
Gelesen: vollständiges Issue #24 samt zehn Kommentaren, Labels/Project-Zuordnung;
Control #60 samt Fortschreibung vom 20.10.; Control #17, ADR 0001/0002,
Bootstrap und Verifikationsregel; [Matrix](../audits/akte-gap-2026-10.md),
ADR 0007–0021 und Build-Spezifikation (relevante Speicher-/Transport-/A-06-Grenzen).
Frühere Varianten/Gates in der Matrix bleiben historisch; ADR 0007/0009 und Bennis
aktueller Auftrag haben für die genannten Punkte Vorrang.

| Bereich | Belegter Ist | Soll Alpha 10 / Design |
|---|---|---|
| Namen | `mimir/config.yaml`, `repository.yaml`, `bifrost/*`, Mimir-Texte | Wuschel/Traber, eigene Slug-Linie; [0022](../adr/0022-wuschel-traber-naming.md) |
| Reset | Identität in /data und DB; alter Datenbestand bleibt getrennt | neue DB/Rolle und neue UUID; [0023](../adr/0023-last-reset-identity.md), [Runbook](../operations/wuschel-new-database.md) |
| Herde | ZIP lokal: neun RGBA-Figuren 1024×1536, neun RGBA-Icons 1254×1254; kein Asset eingebaut | Originale unverändert in Control, reproduzierbare Ableitungen; [0024](../adr/0024-herd-assets.md) |
| G4 | `Catalog(kind=map)` mit Inline-Einträgen; Source-Fingerprint enthält gesamten referenzierten Katalog; keine Pflegehaltung | Hybrid, gezielte A-06-Regel; [0025](../adr/0025-managed-catalog.md) |
| Austausch | Alpha 9 lädt rohe Registry-JSON herunter; Import akzeptiert auch `{config,display_name}`; Editorial separat | ein Menü, vollständiger fachlicher Abschluss, Metadaten/Kataloginhalte; [0026](../adr/0026-import-export.md) |
| MQTT | Default disabled; Adapter wartet dann, statt Credentials zu verwenden | Optionen vollständig übersetzen, credentialfreier Hinweis; [0027](../adr/0027-options-mqtt-ui.md) |
| Geheimnisse | beide Schema-Passwörter schon `password` | durch Tests sichern; keine Optionen-Abfragen/Passwortausgaben |

## Review-Einstieg

1. [0022 — Namen, vollständige Fundstellenmatrix, Protokoll und Bifröst-Abbau](../adr/0022-wuschel-traber-naming.md).
2. [0023 — letzter Reset und Installationskennung](../adr/0023-last-reset-identity.md),
   [DB-Runbook mit vorbereitetem Proxmox-Skript](../operations/wuschel-new-database.md).
3. [0024 — Herde, Bildpipeline, Größen und HA-Branding](../adr/0024-herd-assets.md).
4. [0025 — G4: Daten, A-06, Atomarität, Konkurrenz, Restore und Bestandsimport](../adr/0025-managed-catalog.md).
5. [0026 — Import & Export, Abschluss aller Referenzen und Alpha-9-Kompatibilität](../adr/0026-import-export.md).
6. [0027 — Optionen, MQTT und genaue Text-/Seitenregeln](../adr/0027-options-mqtt-ui.md).
7. [Dateiinventar der Umbenennung](rename-inventory.md),
   [Quellen- und Prüfvermerk](NACHWEIS-A1.md).

Benni hat die Produktnamen, den neuen Slug, die neue Datenbank, das Versionsziel
und G4 Hybrid entschieden. Die konkreten Formate, API-/Tabellenvorschläge,
Grenzen und Algorithmen dieser neuen ADRs sind **Designvorschläge zur Review**.
Keine stillschweigende Freigabe der Umsetzung.

## Bau- und Abnahmeplan nach Freigabe

Eigene Commits für: Namen/Traber, Herde, G4, Austausch, MQTT, Text-/Listenfeinschliff,
Aufräumanleitung, Nachweise. Control erhält in seinem vorhandenen PR erst in A2
`assets/herde/`: alle 18 Original-PNGs, Steckbrief und README zu #60.
Keine neuen Fachverträge oder Klassifikationsregeln; weitere Module nur Vorlage.

Je Block fokussierte Unit-/PostgreSQL-/Restore-/Formulartests; am finalen Head
vollständige bestehende CI, Ruff/Format/mypy, Frontend-Typen/Build/Tests,
beide Architekturpakete und amd64-Lifecycle. Versionsziel synchron 1.0.0a10
in Wuschel-App, Hauptdistribution, Frontend, Traber-Manifest. ADR 0009:
alle Tags, historische Slugs maschinell, Monotonie je Slug-Linie.
Kein grünes Produkt-Gate wird für diesen unveränderten A1-Stand behauptet.

I18n-Nachweis: 0 harte UI-Texte sowie 0 sichtbare alte Produktnamen
Mimir/Terra/Bifröst in ausgelieferten aktuellen Oberflächen, inklusive
Fehlern, Meldungen, Downloads und Einrichtung. Historische Dokumente und
explizite Import-Provenienz sind kein sichtbarer Produktname.

Firefox 1568×710: Übersicht mit Figur, leere Vertragsliste, Katalogpflege,
Import & Export, Versionen mit „Technische Details“, Verbindungen mit
MQTT-Hinweis. Dazu Icon-Vorschau 16/32/128 auf hell/dunkel und
`docs/alpha10/ABNAHME.md` mit Block → Commit → Test/Bild.
Diese ausdrücklich verlangten A2-Bilder erlauben den gezielten lokalen
Abnahmelauf erst nach A2-Freigabe; A1 startet keinen Preview-/Browser-Server.
Dann erneuter STOPP.

## Freigabe- und Betriebsgrenzen

**Jetzt STOPP nach A1.** A2 erst nach Review-Freigabe. B erst nach Bennis
gesondertem „Go“: Vor-Tag-Gate, Pre-Release/Images/Digests, DB-Anlage durch Benni,
neue Wuschel-App und Traber-Installation mit eigener Abnahme.
Kein Merge, Tag, Release, DB-Skriptlauf, Import oder HA-Eingriff aus A1.

Legacy `benni_core_contracts` 0.2.4, Terra, Mimir 1.0.0a9 und die
Einhornzentrale-Konfiguration bleiben unberührt. Kein automatischer Consumer-Cutover.
Passwortdateien auf LXC niemals ausgeben, protokollieren oder in Nachweise kopieren.
Keine Supervisor-App-Details/Optionen abfragen; auch nachträgliches Wegfiltern ist
kein zulässiger Ersatz. Nur Endpunkte verwenden, die schon an der Quelle keine
Optionen liefern. DNS-Bedarf an Benni melden.

Teil B braucht eigene Belege für Version/Start/Migrationen der leeren DB,
Ingress, tatsächliches Traber-Protokoll, Store/Kachel-Icon und MQTT-Testquelle.
Titelbestandsimport ist ein weiterer ausdrücklicher Go-Schritt. Alte Apps werden
erst nach Abnahme von Benni selbst deinstalliert; Löschen von `mimir` erst nach
Beta-Abnahme und gesondertem Go. Technisch fertig, Released, Installed und Live
bleiben getrennte Aussagen.
