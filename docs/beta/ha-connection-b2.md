# Wuschel 1.0.0b2 – HA-Verbindung, A1+A2

Auftrag: [#33](https://github.com/Levtos/wuschel/issues/33), Benni, 22.10.2026.
Agent: `agent:codex`. Basis: `main@11ff615`. Kleiner Verbindungsfix bis PR;
danach **STOPP für Review**. Technisch geprüft bedeutet nicht Live.

## A1: Befund und gewählter Fix

Der App-Client sendete beim Aufbau die IDs `1,6,2,3,4,5`. HA lehnt die
fallende ID bei `get_config` mit `id_reuse` ab; der erste Snapshot fehlt.
FakeHA akzeptierte diese Reihenfolge und verdeckte den Fehler.

Jede authentifizierte WebSocket-Verbindung besitzt jetzt einen eigenen
Zähler ab null und einen mit Lock serialisierten Sendepfad. Aufbau, Discovery
und Dienstaufrufe vergeben IDs ausschließlich dort. Die unabhängige
Discovery-Verbindung kann den Zähler der laufenden Bridge nicht verändern.
Jeder Reconnect erzeugt einen neuen Zähler. Antworten werden gegen die
gesendete ID geprüft; der Leseweg nutzt die bestätigte Subscription-ID.
Dienstaufruf-Futures werden vor dem Senden registriert und anhand der ID
aufgelöst. Parallele Aufrufe behalten dieselbe Sende-/ID-Reihenfolge.

`bridge_request_failed` und `bridge_disconnected` ergänzen `request_type`
und `ha_error_code`. Bekannte Protokollcodes wie `id_reuse` bleiben sichtbar;
beliebige entfernte Codes werden `unknown_error`. Keine Fehlermeldung,
Nutzdaten oder Zugangsdaten werden geloggt. Bei reinen Transportabbrüchen
ohne fehlgeschlagene Anfrage sind die beiden Zusatzfelder null.

## A2: Regressionsnachweise

`tests/test_ha_request_ids.py` verwendet ausschließlich synthetisches FakeHA
und In-Memory-Persistenz:

| Fall | Erwartetes Ergebnis |
|---|---|
| Nur Connectivity, null HA-Verknüpfungen | verbunden, `connectivity.home_assistant=ready`, Bereitschaft erfüllt |
| HA-Verknüpfung | erster Snapshot verarbeitet, `first_bridge_snapshot_pending` entfernt |
| Protokoll 2 | ausgehandelt, Traber-Version im Laufzeit-Verbindungsstatus vorhanden |
| HA-Stop/Abbruch/Reconnect | zunächst starting/unavailable, IDs erneut ab 1, erneuter Snapshot; veraltete Quelle bleibt `unknown/input_stale` |
| Gleichzeitige Dienstaufrufe | größere IDs als beim Aufbau, Antworten korrekt zugeordnet |
| Discovery | Vorschau mit Registry-Listen, unknown_command und unauthorized; 401 Entitäten in drei Metadatenpaketen; separater Metadatenabruf beginnt bei 1 |
| Nicht steigende IDs | FakeHA antwortet mit `success=false`, `error.code=id_reuse` |
| Fehlerdiagnose | beide Logereignisse enthalten Typ/Code; beliebige entfernte Fehlerdaten bleiben privat |

Die bestehende Backend-Suite prüft außerdem MQTT-Quellzeiten, Retain/Replay,
Opening-Grace und Restore. Freshness, Engine und UX wurden nicht verändert.
`tests/test_version_lines.py` sichert die begrenzte Traber-Versionsausnahme ab.

Lokaler A2-Nachweis: `uv run pytest -q --tb=short` mit **842 passed,
27 skipped** (ohne PostgreSQL-/Docker-/HA-Testumgebung), Ruff und mypy strict
grün. Infrastruktur- und Verpackungsnachweise liefert zusätzlich die PR-CI;
Release- und Live-Nachweise sind ausdrücklich offen.

## Version und verbleibende Gates

App/Python/Frontend/Lockdateien: `1.0.0b2`. Traber bleibt `1.0.0b1`, weil
kein Servercode geändert wird. Das Versions-Gate vergleicht bei ungleichen
Versionen den vollständigen getrackten Traber-Inhalt mit seinem Versionstag.
Die älteren Supervisor-App-Linien bleiben unverändert.

Nach Review und Bennis **Go** gilt unverändert der b1-Veröffentlichungsweg:
main-SHA explizit auswählen, striktes Release-Versionsgate, alle CI-Jobs,
Publish der getesteten Images für amd64 und aarch64, unabhängige anonyme
Image-Pulls einschließlich Digest-/Plattform-/Inhaltsprüfung sowie amd64-
Lifecycle-Smoke. Erst mit allen grünen Release-Jobs ist die Distribution
belegt. Diese Phase startet keinen Release-Workflow und erzeugt keinen Tag.

Installation, DB und laufende HA-/MQTT-/Z2M-Systeme wurden nicht angefasst.
Benni besitzt Review, Merge-/Release-Go, Installation und spätere Live-Abnahme.
