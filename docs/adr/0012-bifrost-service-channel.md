# ADR 0012 — Bifröst: begrenzter Servicekanal und Protokoll 2

18.10.2026 · **A2 freigegeben: Claude (Technik), Benni (Texte), 18.10.2026.** Grundlage:
[#24](https://github.com/Levtos/mimir/issues/24), Matrix §4–6, APP-01,
[ADR 0005](0005-ha-outage-connectivity.md) und [0009](0009-prerelease-version-gate.md).
Zahlen/Limits sind technische Vorschläge für den Review, keine bereits beschlossenen Fachparameter.

## Ziel und Modell

Alpha 8 kennt nur `bifrost/info` und `bifrost/subscribe`. Ein gemeinsamer, administrativ
autorisierter Kanal ergänzt Abfragen mit Antwort, Mimir-eigene Hinweise und ausdrücklich
zugelassene Aktualisierungsanforderungen. Bifröst bleibt Transport; Kalenderauswahl,
Benachrichtigungsregeln, Herkunftsbewertung und Wiederholungsplanung gehören Mimir.
Keine Gerätebedienung, freien Service-Namen, Skripte, Templates oder allgemeinen Apply-Aufrufe.

`bifrost/negotiate` erhält `supported_versions:[2,1]`, antwortet mit gewählter Version,
für eigene Hinweise zusätzlich `installation_id` (UUID). Diese bindet die beiden
zulässigen Hinweiskennungen an die Verbindung; fremde Mimir-Installationen sind
ebenfalls gesperrt. Reine Leseverbindungen brauchen keine Installationskennung.
Fähigkeiten und tatsächlicher Programmversion aus dem Manifest. Fehlt das Kommando bei alter
Bridge, darf Mimir `info`/Protokoll 1 verwenden; Funktionen mit erforderlichem Protokoll 2
bleiben sichtbar nicht verfügbar. Unparametrisiertes `bifrost/info` meldet weiterhin
`protocol_version:1`; alte Apps prüfen diese Zahl streng. Alte Subscriptions mit Version 1
behalten ihre Nachrichtenform. Version 2 wird je Verbindung ausgehandelt; ihre erweiterten
Subscriptions enthalten Kontextdaten und unterstützen neue Abfragen. Kein stilles Umdeuten von v1.
Mimir a9 verwendet die höchste gemeinsame Version und zeigt in Diagnose/Einrichtung
die tatsächlich ausgehandelte `protocol_selected` sowie fehlende Fähigkeiten.
Der Release-Nachweis für Alpha 9 verlangt ausdrücklich eine aktive v2-Verbindung.

## Datenformat und feste Freigaben

```json
{"id":17,"type":"bifrost/service_call","protocol_version":2,
 "request_id":"<UUID>","operation":"calendar_events","target_ids":["calendar.example"],
 "arguments":{"start":"2026-10-17T00:00:00+02:00","end":"2026-10-18T00:00:00+02:00"}}
```

Die Bridge übersetzt die geschlossene `operation`-Liste; HA-Adressen kommen ausschließlich
aus validierten Verknüpfungen, niemals aus Vertragswerten oder Kalendertexten.

| Operation | feste HA-Aktion / Grenze |
|---|---|
| `calendar_events` | `calendar.get_events`, Antwort erforderlich, nur ausgewählte Kalender; [ADR 0013](0013-calendar-cache.md) |
| `problem_notice_put` | `persistent_notification.create`, nur eigene Installations-/Achsenkennung, begrenzter Klartext |
| `problem_notice_remove` | `persistent_notification.dismiss`, dieselbe eigene Kennung; niemals dismiss_all |
| `source_refresh` | ausschließlich getestete integrationsspezifische Profile aus [ADR 0018](0018-reconciliation-refresh.md) |

Ergebnis: `{request_id,outcome:completed|rejected|failed|indeterminate,data?,error_code?}`.
`completed` bei Refresh bestätigt den Aufruf, keine neue Messung. `not_allowed`,
`invalid_arguments`, `unsupported_operation`, `busy`, `ha_unavailable`, `timeout` und
`request_conflict` sind feste Fehlercodes; keine Roh-Exceptions/Secrets zurückgeben.
HA selbst liefert Fehler als Exceptions; erst Bifröst bildet sie auf diesen Transportvertrag ab.

Vorschlag: 10 s Service-Zeitlimit, 12 s Client-Frist, höchstens 4 parallele Aufrufe,
16 wartende Anfragen je Verbindung, 64 KiB Anfrage und 1 MiB Antwort. Überschreitung
wird abgewiesen, nie als vollständige Antwort abgeschnitten. Gegenüber HA nur explizite
Ziele, keine Area-/Label-Wildcards. Aufrufprüfung serverseitig und vor HA-Ausführung.

## Fehler, Wiederholung und Neustart

`request_id` bindet kanonischen Aufrufinhalt. Gleiche ID mit anderem Inhalt wird abgelehnt.
Die Bridge hält höchstens 256 Resultate für 5 Minuten pro Verbindung; dies ist keine
dauerhafte Exactly-once-Zusage. Verbindungsverlust nach Versand bedeutet `indeterminate`,
nicht „nicht ausgeführt“. Kein allgemeines automatisches Replay nach Reconnect/Restart.
Nur reine Kalenderabfragen oder idempotentes Setzen/Entfernen des eigenen Hinweises dürfen
nach ihrer jeweiligen Regel erneut versucht werden. Refresh-Wiederholungen gehören dem
begrenzten Lauf aus ADR 0018. Späte Antworten zu ersetzten Revisionen werden verworfen.

Externe Aufrufe laufen außerhalb der Writer-Transaktion; zunächst Auftrag/Generation
persistieren, danach senden und Ergebnis getrennt speichern. Kein Netzwerkaufruf vor
Commit und kein Publish bei Commit-Fehler. Logs enthalten Operation, Ergebnis und Dauer,
keine Kalenderinhalte, Zugangsdaten oder vollständigen HA-Kontexte.

## Beispiele, Tests, betroffene Akte

Beispiel: Kalenderantwort geht verloren → Cache bleibt unverändert, erneute Leseabfrage
mit neuer Anfrage zulässig. Refresh geht verloren → Versuch als unbestimmt verbrauchen;
keine sofortige Transportwiederholung. Fremde Benachrichtigungs-ID → abgewiesen.

A2-Tests: Admin-/Nichtadmin, jede erlaubte/verbotene Aktion, Payload-/Ziellimits,
Zeitlimit/Spätantwort, gleiche/fremde ID, HA-Abbruch vor/nach Versand, überlastete Queue,
Commit-Fehler, v1-App/v2-Bridge, v2-App/v1-Bridge und Manifest = gemeldete Programmversion.
Betroffen: Matrix G2/G7/G15/G16; M30-01, M30-34 §2, M30-41 §2/§9, M30-43 §7;
Build-Spezifikation §8/§13/§14/§19/§21. Nur geplante Tests in A1.

Primärquellen: [HA-Aktionen mit Antworten](https://contributors.home-assistant.io/core/integrations/actions/#return-response-data),
[HA-Kalenderabfrage](https://www.home-assistant.io/actions/calendar.get_events/),
[dauerhafte HA-Hinweise](https://www.home-assistant.io/integrations/persistent_notification/).
