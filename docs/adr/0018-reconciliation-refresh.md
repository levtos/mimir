# ADR 0018 — G16: begrenzte erneute Quellenabfrage

18.10.2026 · **A2 freigegeben: Claude (Technik), Benni (Texte), 18.10.2026.** Grundlage: M30-43 §7,
Matrix G16, [ADR 0005](0005-ha-outage-connectivity.md),
[0012](0012-bifrost-service-channel.md). Keine Presence-Fachlogik oder Tür-/Unlock-Aktion.

## Ziel und Modell

Ein ausdrücklich verknüpfter Trigger-Vertrag kann eine begrenzte erneute Abfrage
vorhandener Quellen auslösen. Der Trigger ist kein Nachweis für deren Wert;
Abrufbestätigung und neue Evidence bleiben getrennt. Aus vorhandenen und später
tatsächlich eintreffenden Nachweisen entsteht eine normale Neubewertung.

## Datenformat und integrationsspezifische Profile

```json
{"refresh_plan":{"trigger_ref":"example.trigger.edge","targets":["source.example"],
 "attempt_offsets_s":[0,10,30],"window_s":60,"cooldown_s":120,
 "stop_when":{"ref":"example.result","field":"confirmed"}}}
```

Das Beispiel ist synthetisch; Zahlen sind technische Review-Vorschläge und
Instanzparameter nach G19. Validierung: eindeutige nichtnegative aufsteigende
Offsets, höchstens fünf Versuche, Fenster maximal 300 s, letzter Offset kleiner
als Fenster, positiver Cooldown. Ein Ziel benötigt eine freigegebene
Aktualisierungsfähigkeit seiner konkreten Verknüpfung. `stop_when` ist ein optionaler
kanonischer Bool-Eingang, keine HA-Adresse; unbekannt stoppt nicht als Erfolg.

Geschlossene Profile im Bridge-Code, einschließlich Argument-/Integrationsprüfung:

| Profil | festgelegter Aufruf | Voraussetzungen |
|---|---|---|
| `entity_poll` | `homeassistant.update_entity`, ausschließlich die freigegebene Entity | zuständige Integration und Entity unterstützen tatsächlich aktive Abfrage; keine pauschale Zusage für Push-Entities |
| `companion_location` | konkret zugeordnetes `notify.mobile_app_*`, ausschließlich `message:request_location_update` | HA-Companion-Ziel aus registrierter Gerätezuordnung; Plattform/Berechtigung unterstützt die Abfrage; explizit für diese Quelle aktiviert |

Es gibt keine freie Notify-/Service-Auswahl und keine benutzerdefinierten Payloads.
Der dynamische mobile_app-Servicename darf nur aus dem geprüften Profil/Ziel entstehen,
nicht aus Vertragswerten. Weitere Integrationen benötigen ein eigenes getestetes
Codeprofil, bevor die Oberfläche sie anbietet. Ein nicht unterstütztes Ziel wird
als „Diese Quelle kann nicht erneut abgefragt werden“ gezeigt. Keine behauptete
iCloud3-/GPS-Aktualisierung durch einen wirkungslosen allgemeinen Aufruf.
Zusätzlich gelten pro Profil die engeren Anbieter-/HA-Limits und nötigen
Berechtigungen; der Plan darf sie nicht durch kürzeren Cooldown umgehen.
Verbrauchte Kontingente werden über Neustarts berücksichtigt. Die Oberfläche
erklärt notwendige Voraussetzungen, statt sie selbst im Telefon zu ändern.

## Laufzeit, Fehler und Neustart

Nur ein bestätigtes neues Trigger-Ereignis bzw. eine zulässige Flanke startet
einen Lauf. Snapshot, Reconnect und Konfigurationsübernahme spielen keinen Trigger
nach. Pro Plan/Zielgruppe höchstens ein aktiver Lauf; weitere Trigger im Fenster
werden zusammengefasst und verlängern es nicht. Ein neuer Lauf braucht nach Ende
eine neue echte Flanke und abgelaufenen Cooldown. Der erste Versuch ist sofort,
weitere werden durch Clock geplant; kein unbeschränktes Polling.

Run-ID, auslösende Evidence, Revision, Anfang/Ende, bereits verbrauchte Versuche
und Ergebnis werden vor Versand committed. Zeitlimit/Verbindungsverlust nach
Versand verbraucht den Versuch als unbestimmt; kein automatisches sofortiges
Transport-Replay. Weitere planmäßige Versuche nur innerhalb des ursprünglichen
Fensters. Nach HA-Ausfall keine Aufrufwarteschlange nachholen; nur noch zulässige
zukünftige Termine. Nach Core-Neustart keine vergangenen Versuche wiederholen;
ausstehende unbestimmte Versuche werden nicht zu „nicht gesendet“ umgeschrieben.

Abbruch bei gültig erfülltem Stop-Vertrag, Ausschalten, Binding-/Semantikänderung,
Fensterende oder maximaler Versuchszahl. Technischer Fehler bleibt Diagnose,
keine erfundene Home-Evidence. `update_entity`/Location-ACK allein ändert weder
device_time noch Freshness; erst ein tatsächlich neuer Report darf das.

## Oberfläche, Tests und betroffene Akte

Formular „Quellen erneut abfragen“: Trigger-Vertrag, Quellen, unterstütztes
Verfahren, Versuche und Abstände; normale Anzeige „Erneut angefragt“, „Neue Meldung
erhalten“ oder „Keine neue Meldung“. Keine Sicherheitsflanke durch den Trigger.

A2: beide Profilabbildungen und unzulässige Dienste, nicht unterstützte Quelle,
Trigger ≠ Evidence, begrenzte Wiederholung/Flattern/Cooldown, Stop unbekannt/Ja,
Abbruch/HA-Ausfall/Restart/Commit-Fehler, verlorene Antwort, alte Generation,
keine Quellzeit-Erneuerung durch ACK und keine künstliche Zustandsflanke.
Betroffen: M30-43 §7, Build-Spezifikation §8/§9/§13/§14/§18/§21,
Refresh-Orchestrierung, Bridge, Scheduler, Source-Capabilities und Formulare.

Quelle: [HA Companion — Location-Anforderung](https://companion.home-assistant.io/docs/notifications/notification-commands/#request-location-updates).
