# Alpha 10 — A2-Abnahme

20.10.2026 · PR [wuschel#27](https://github.com/levtos/wuschel/pull/27),
[control#61](https://github.com/levtos/control/pull/61). Freigabe: Bennis Review A1
mit K1–K8; keine andere Freigabe wird vorausgesetzt. **Teil B bleibt gesperrt.**

## Umsetzung und Block-Commits

| Block | Commit | Nachweis |
|---|---|---|
| Version zuerst, vier Komponenten 1.0.0a10 | 7d5f986 | [Versionsgate](versionsgate.json), Linie wuschel |
| Namen, Traber, Protokoll 2, Hinweise und URLs | bf834e7 | Kanal-/Kerneltests, Namensinventar, docs/naming.md |
| Herde, lokale Brands, 19 Übersetzungen | 6810aa4, f896c07 | [Manifest](herde-ableitungen.json), zweimal identische Hashes, CI herd-assets |
| Rein lesender Title-Classifier-Planer | 955c13c | [Öffentliche Summen](titelkatalog-probelauf-summen.json), nur synthetische Fixtures |
| G4 und atomare portable Importpläne | 3d94ef4, f79d172 | Katalog-/Portable-/PostgreSQL-Regressionen, Migration 007 |
| Pflegeoberfläche, Import & Export, Textkorrekturen | 262a8df, f896c07 | Frontend 355 bestanden, i18n-Scan 0, sechs Firefox-Bilder |
| Auswirkungsvorschau, Restore-Integrität und vollständiger Verlauf | 6ca0191, 1db22b3 | Verspätete Antwort, >1000 Einträge, Seitenwechsel und aktuelle OCC-Basis |
| K5, Betriebs- und Aufräumanleitung | 73462e4 | 14 Runbook-/Assetprüfungen, AST/bash -n, nie ausgeführt |
| Control: 18 Originale und Steckbrief | 70b6e83 | SHA-256 aller PNGs gegen freigegebenes ZIP; nur eine Steckbriefzeile geändert |

## Tests und Grenzen

Lokale Frontend-Suite: 355 bestanden, fünf separate API-E2E-Tests lokal ausgenommen.
TypeScript, JSX-Lint, vollständiger i18n-Scan und dist-Prüfung erfolgreich;
deutsches Wörterbuch ohne sichtbare Mimir/Terra/Bifröst-Produktnamen.
Lokale Backend-Suite: 704 bestanden, 25 umgebungsabhängige Tests ausgenommen.
Ruff/Format und mypy strict erfolgreich. Der vollständige CI-Lauf ist die abschließende
Prüfung. Der verbindliche Head samt erfolgreichem Lauf steht im PR-Abschlussvermerk
und in der abschließenden Übergabe; laufende Jobs gelten nicht als bestanden. [CI](https://github.com/levtos/wuschel/actions/workflows/ci.yml).
PostgreSQL-Tests laufen isoliert gegen Version 18; keine Verbindung zu LXC 108.
Beide Architekturimages werden nur gebaut/geprüft; CI publiziert kein Image.

Katalog: Negative Lookups, Masterfolgen, gleichwertige Elternwechsel, OCC,
Idempotenz/Neustart, gezielte Temporal-Slots, unabhängige Maschinen im selben
Vertrag, Befehls-Guards, Sitzungssperre bei geänderter Basis, Commitfehler und
Historienrücknahme als neue Revision. Vorschau an den genauen Formularinhalt
gebunden; verspätete Antworten geben geänderte Eingaben nicht frei. Restore
prüft den Head gegen die unveränderliche Eintragshistorie. Dedizierte vollständige
Katalogabfragen umgehen die 100-/1000-Zeilen-Grenze allgemeiner Diagnoseabfragen.
Der PostgreSQL-Neustarttest umfasst 1.101 synthetische Einträge. Der Verlauf wird
katalogweise mit Revisionscursor geblättert; Rücknahme verwendet auch auf älteren
Seiten den aktuellen Head als OCC-Basis. Sichtungen zählen nur neue Quellreports;
keine neue Messzeit, künstliche Flanke, Grace oder Sitzung durch Pflege.
Import: volle und abgeschlossene Teilkonfiguration, exakter eigener Zielentwurf,
Referenzabbildung, Kategorien/Räume, Kopf-/Entwurfs-/Aktivierungsraces,
Wiederholung, striktes JSON, unbekannte/defekte Formate und atomarer Katalog mit
mehr als 100 Zeilen. Adressen können vor Übernahme im geführten Entwurf angepasst werden.

## Bildnachweise

Firefox, 1568×710, DPR 1, de-DE, Europe/Berlin. Reale API mit MemoryStore und
synthetischer Konfiguration auf Loopback. Keine externen Browseranfragen oder
JavaScript-Fehler; [maschinenlesbarer Nachweis](bilder/nachweis.json).
Die sechs geforderten Ansichten und der zusätzliche Zuordnungsdialog wurden visuell geprüft.

- [Übersicht mit Figur](bilder/01-uebersicht.png)
- [Leere Vertragsliste](bilder/02-leere-vertragsliste.png)
- [Katalogpflege](bilder/03-katalogpflege.png)
- [Zuordnungsdialog mit schreibfreier Auswirkungsvorschau](bilder/07-katalog-zuordnung.png)
- [Zuordnungsdialog mit schreibfreier Auswirkungsvorschau](bilder/07-katalog-zuordnung.png)
- [Import & Export](bilder/04-import-export.png)
- [Konfigurationen mit Technische Details](bilder/05-versionen.png)
- [Verbindungen mit genauem MQTT-Hinweis](bilder/06-verbindungen-mqtt.png)
- [Icon-Kontaktbogen 16/32/128 hell/dunkel](icon-kontaktbogen.png)
- [Neun Figuren und gemeinsame sichtbare Hufgrundlinie](figuren-kontaktbogen.png)

Pillow 12.1.1, NumPy 2.4.2, libwebp 1.6.0. Linear RGB, vormultipliziertes Alpha,
Lanczos. WebP RGB quality 82, method 6, exact=True, alpha_quality=100;
decodiertes Alpha bytegleich. PNGs/Favicons verlustfrei. Alle Originale
unverändert, keine Originalfigur im Frontend-Bundle. Zweiter vollständiger Lauf
mit identischen Hashes. Schwache Alpha-1–7-Ausläufer bleiben erhalten; sie dürfen
unterhalb des sichtbaren Hufankers im unteren Rand liegen. Details und je Figur
begrenzter Maßstab stehen im Manifest. Keine abgeschnittenen Hufe/Hörner.

| Figur | 512×768 Bytes (≤150.000) | 1024×1536 Bytes (≤400.000) |
|---|---:|---:|
| wuschel | 41.192 | 121.914 |
| traber | 43.334 | 121.048 |
| schnueffel | 54.972 | 158.084 |
| kuschel | 44.810 | 137.524 |
| funkel | 56.842 | 171.772 |
| blinzel | 57.810 | 176.310 |
| schlummer | 49.266 | 143.314 |
| traeller | 56.932 | 162.640 |
| pfoertchen | 41.414 | 115.884 |

## Privater Probelauf

Quelldatei vor Parsing auf 2.676.874 Bytes und SHA-256
`175b94146373e9db638e925fe9c86905236036691f463096ee1f3ea10a564753`
geprüft. 3.181 Zeilen erklärt: 3.119 Klassenabbildungen offen, 56 Ausblendungs-
entscheidungen und sechs Variantenentscheidungen. 568 Varianten, drei app-Signale,
3.185 Kontexte aus zwei Quell-Apps, 1.775 Normalisierungsänderungen,
keine Normalisierungskollision, keine Ablehnung. Klassen je Medienart in der
öffentlichen Summendatei. Klassen 0–3 bleiben Platzhalter; Benni bestimmt die Bedeutung.
Lokaler Parser: 0,335 s / 13.383.351 Bytes Python-Peak (tracemalloc); dies ist
keine Messung einer produktiven DB-Transaktion und keine Live-Abnahme.

Echte Titel, alle sechs Master/Varianten samt Klassen und Entscheidungsalternativen,
56 ausgeblendete Einträge, App-Signale und vollständiger Herkunftsbericht liegen
**ausschließlich im privaten Codex-Ausgabeordner auf Bennis PC**. Kein Titel im
Commit/PR/Issue. Nichts angewendet, kein Zugriff auf media_catalog. Vor B ein
frischer Export über title_classifier/v3/export_entries und eigenes Import-Go.

## Offener Adminschritt und Stop

GitHub-Repobeschreibung noch alt. Actor-Preflight levtos-codex, Berechtigung WRITE;
PATCH der Beschreibung antwortet HTTP 404. Keine Identität gewechselt.
Benni setzt als Repo-Admin: „Wuschel – Home-Assistant-App für Verträge und
Katalogpflege; Traber verbindet Home Assistant über Protokoll 2.“

Kein Merge, Tag, Release, DB-Skriptlauf, App-/HACS-Installation, echter Import,
MQTT-Livetest oder Altkomponentenabbau. LXC-Passwortdateien wurden nie gelesen.
Die gelieferten Live-Fakten wurden nicht erneut abgefragt. Legacy, Terra,
installiertes Mimir a9 und Einhornzentrale-Konfiguration bleiben unberührt.
Benni überträgt DB-Host/CA und Passwörter in B selbst. Technisch geprüft ist nicht Live.
