# ADR 0014 — G7: verständliche HA-Problemmeldungen

18.10.2026 · **A2 freigegeben: Claude (Technik), Benni (Texte), 18.10.2026.** Grundlage: M30-01,
G7/G14, [ADR 0007](0007-hybrid-catalog-decision.md),
[0012](0012-bifrost-service-channel.md). Zeitwerte und Voreinstellungen zur Prüfung vorgeschlagen.

## Ziel und Modell

Bestätigte `unknown`-/`unresolved`-Felder werden zentral in Mimir und als ein
zusammengefasster HA-Hinweis sichtbar. Ein zweiter, ausdrücklich als Hinweis
bezeichneter Kanal behandelt fehlende Konfiguration. Ein gültiger unzugeordneter
Wert wird niemals zum Signalalarm. Keine Endgeräte-/Push-Dienste, frei wählbaren
Empfänger oder Policy-Aktionen in Alpha 9.

```json
{"notifications":{"signal":{"enabled":true,"debounce_s":30,"clear_after_s":10,
 "min_update_s":300},"configuration":{"enabled":false,"debounce_s":60,
 "clear_after_s":10,"min_update_s":300},"max_items":10}}
```

Diese Werte werden im Entwurf über ein Formular gewählt und erst übernommen.
Abwesenheit des neuen Blocks in alten Konfigurationen schaltet nichts automatisch
ein. Der vorgeschlagene Einrichtungswert aktiviert Signalhinweise; Konfigurationshinweise
sind zunächst aus. M30-01 verlangt zentrale Sichtbarkeit unabhängig davon, ob ein
Benutzer die optionale HA-Übertragung ausschaltet. Das Protokoll bleibt immer verfügbar.

Probleme werden aus bestätigter Publication gebildet, mit stabilen Kennungen
`(contract_id,field,axis)` statt Nachrichtentext als Identität. Ausgeschaltete
Verträge, verworfene Entwürfe und `held`/`not_applicable` erzeugen keinen Signalalarm.
Neue Instanzen/Neustarts brauchen erst eine aktuelle bestätigte Auswertung; fehlende
Initialisierung wird im Systemstatus geführt, nicht als Problemsturm je Vertrag.

## Entprellung, Sammelmeldung und Auflösung

Je Achse genau eine eigene `notification_id`, abgeleitet aus installation_id und Achse.
Ein anhaltendes Problem muss die Entprellfrist erreichen. Neue kurze Störungen
verschwinden ohne Meldung; Flattern verlängert nicht bestehende Fach-Grace.
Inhalt: Anzahl, bis zu zehn verständliche Vertragsnamen und Ursachen sowie Link
zur gefilterten Problemliste. Keine Rohwerte, Benutzerdaten, Kalendertexte oder
freien Reason-Details. Beispiel: „Mimir: Signal gestört — 3 Werte sind nicht sicher
bekannt. Prüfe die genannten Quellen.“ Konfigurationsmeldung: „Mimir: Angaben fehlen“.

Unveränderter Problemstand erzeugt keine periodische Erinnerung. Änderungen werden
gebündelt, höchstens einmal pro `min_update_s`; vollständige Auflösung wird nach
`clear_after_s` per dismiss bestätigt, nicht als weitere Warnung versandt. Ein noch
offenes Problem anderer Verträge bleibt erhalten. Bewusstes Wegklicken in HA gilt
als Quittierung des aktuellen Inhalts; gleicher Inhalt wird bis zu einer echten
Problemänderung nicht laufend neu erzeugt. Mimir-Problemliste bleibt sichtbar.

Zustand/Digest, Fälligkeitszeit und zuletzt bestätigter Versand werden persistiert.
Outbox-Auftrag erst nach Commit. HA-Ausfall: jüngsten Sollstand je Achse zusammenfassen;
nach Reconnect nur diesen Zustand abgleichen, keine veralteten Meldungen nachsenden.
Zeitlimit nach Versand = unbestimmt; wiederholsicheres Put/Dismiss auf gleicher eigener
Kennung zulässig. Kein Löschen fremder Hinweise. Ausschalten entfernt nur eigene Hinweise.
Auflösung bei HA-Ausfall wird nach Wiederverbindung abgeschlossen.

## Tests und betroffene Stellen

A2: unknown/unresolved, held ohne Alarm, gültig + unvollständig ohne Signalalarm,
beide Achsen gleichzeitig, Entprellgrenzen, Flattern, Sammelgrenze/Link,
unveränderter Stand, Wegklicken, einzelne/volle Auflösung, Ausschalten,
Neustart/HA-Verlust, verlorene Antwort, Commit-Fehler, getrennte Installationen.
Oberfläche: „Benachrichtigungen“, verständliche Fristen, Vorschau ohne echten Versand;
keine Testmeldung ohne bewusste Aktion. Akte M30-01/M30-27/M30-36, P4-32;
Build-Spezifikation §7/§13/§19/§21, Probleme-API, Runtime/Outbox, Formular.

Quelle: [Persistent Notification](https://www.home-assistant.io/integrations/persistent_notification/).

## Umsetzung A2

Schema-2-Block `notifications`; Abwesenheit bleibt ausgeschaltet. Eigene Tabellen
`service_state` und `service_job` (Migration 004) speichern Problem-Anfänge je
Kennung, gewünschten/übermittelten Digest und den Versandstatus. Der Worker muss
den Auftrag zuerst über den seriellen Writer als gesendet committen. Feste
Hinweiskennungen werden bei der Protokollaushandlung an installation_id gebunden.
Nach dem Ausschalten bleibt die HA-Anbindung bis zum Entfernen des eigenen
Hinweises bestehen. Neustart wartet vor Hinweisversand auf den aktuellen Snapshot.

Das normale Formular liegt unter Einstellungen → Benachrichtigungen. Beide Achsen
haben eigene Sekundenfelder mit Minutenhilfe und eine lokale Vorschau ohne Versand.
Änderungen gehen ausschließlich in den Entwurf; Übernehmen bleibt der gemeinsame
Konfigurationsschritt. Der App-Hostname liefert bei Supervisor-Ausführung den
Ingress-Slug für den Link; keine fest eingebaute Repository-Kennung.
