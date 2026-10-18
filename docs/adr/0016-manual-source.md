# ADR 0016 — G10: ausdrückliche manuelle Quelle

18.10.2026 · **A2 freigegeben: Claude (Technik), Benni (Texte), 18.10.2026.** Grundlage: M30-25,
Matrix G10, [ADR 0006](0006-instance-parameters.md) und [0019](0019-sensor-profile-value-origin.md).

## Ziel und Modell

Manuelle Angaben werden als ausdrücklich angelegte, typisierte Quelle verarbeitet.
Sie ersetzen weder beliebige Vertragswerte noch Source-Observations anderer Adapter.
Mimir kennt weiterhin keine generischen Overrides und kein `set_state`.
Eine Vertragsvorlage muss die Quelle als Eingang zulassen; Priorität/Verknüpfung
werden im Entwurf geprüft und übernommen. SM-Befehle bleiben der getrennte Command-Weg.

## Datenformat und Beispiel

```json
{"source_id":"source.example_manual","origin":"manual","source_type":"numeric",
 "freshness":{"mode":"periodic_ttl","interval_s":3600,"future_tolerance_s":0},
 "value_schema":{"type":"number","unit":"°C","required":true,"physical_state":true}}
```

Eigenes Binding `kind:manual` ohne HA-/MQTT-Adresse. `source_origin:local` bezeichnet
weiter die Installationsherkunft; es wird nicht mit `origin:manual` oder G9s Art
des Werts vermischt. Auswahl/Zahl/Text/Zeitpunkt/strukturierte Werte erhalten
dieselben begrenzten Formulare und Schemaregeln wie andere Eingänge; keine freie
Ausdruckssprache und keine JSON-Pflicht.

API-Vorschlag: `POST /api/v1/manual-sources/{source_id}/observations` mit
`{request_id,expected_active_revision,value,valid_from?,valid_until?,note?}`.
Admin/Ingress mit bestehendem Schreib-/CSRF-Schutz; kein neues HA-Service-Override.
Typ, Grenzen, Einheit und aktive Quellidentität prüfen. `request_id` wiederholsicher,
fremder Inhalt bei gleicher ID = Konflikt. Gleichzeitige Eingaben werden durch
Processor/Commit geordnet; Ergebnis/Fehler über gespeicherte Anfrage abfragbar.

Die bewusste Eingabe ist das Ereignis: Server vergibt `recorded_at` und den
belegten Eingabezeitpunkt. Ein selbst angegebener Messzeitpunkt wird getrennt
als Selbstauskunft gespeichert, niemals als automatisch bewiesene Gerätezeit.
Origin manual, administrative Herkunft und gegebenenfalls G9-Wertart bleiben sichtbar.
Kein automatisches Etikett „gemessen“ für einen manuell erstellten Plan.

## Gültigkeit, Änderung und Restore

Quelle deklariert ausdrücklich `periodic_ttl` oder `event_stateful`; kein Default.
TTL läuft ab Eingabe bzw. explizitem Beginn, begrenzt durch ein optionales absolutes
Ende. `valid_from < valid_until`, Zukunftseingaben nur für bewusst als zeitliche
Angabe deklarierte Sources. Ein zukünftiger Inhalt ist keine aktuelle Messung.
Ohne Eingabe, vor Beginn, nach Ende oder nach Widerruf gilt unknown mit Ursache;
kein Rückfall auf eine andere Quelle außerhalb ausdrücklich definierter Zusammenführung.
Zeitlich unbegrenzte Angaben brauchen eine sichtbare Bestätigung „Bis ich die Angabe ändere“.

„Angabe zurücknehmen“ schreibt eine neue, widerrufende Observation; Historie wird
nicht gelöscht. Restart spielt keine Eingabe erneut ab, erneuert keine TTL und
ändert keine Herkunft. Serverbestätigte manuelle Angaben sind eigene Evidence;
ihre Restore-Verwendbarkeit richtet sich nach deklarierter Gültigkeit und CP-15,
nicht nach einem allgemeinen Freibrief für gespeicherte Werte.

## Oberfläche, Tests, betroffene Akte

Quellen → „Manuelle Quelle hinzufügen“; Name, Werteart, Einheit, Gültigkeit.
Am Vertrag: „Angabe eintragen“, „Gültig bis“, „Von dir eingetragen“, „Angabe
zurücknehmen“. Vor dem Senden werden betroffene Verträge gezeigt. Nur diese
ausdrückliche Laufzeiteingabe wirkt sofort; Bearbeiten der Quellkonfiguration
bleibt Entwurf → Prüfen → Übernehmen. Keine Geräteaktion aus diesem Formular.

A2: ungebundene/fremde/ausgeschaltete Quelle, Typ/Einheiten/Grenzen, Rechte/CSRF,
keine beliebigen Vertragsänderungen, Mehrfach-/konkurrierende Anfrage, verlorene
Antwort, absolute Gültigkeitsgrenzen, TTL/event_stateful, Widerruf, History/Restore,
Commit-Fehler und A-06 bei neuer Verknüpfung. Formulartests ohne JSON.
Betroffen: M30-25, §8/§9/§10/§19/§21 der Build-Spezifikation, Source/Binding,
Observation/Processor, API, History und UI. Keine Wake-Ausnahmeseite oder Fachverträge.

## Umsetzung A2

Eigene Source mit `origin:manual`, eigenem adresslosen `manual`-Binding und
interner Abhängigkeit `kind:manual`. Einheiten stammen ausschließlich aus dem
deklarierten Wertschema. Optionale `manual_minimum`/`manual_maximum` gelten nur
für Zahlen. Zukünftiger Gültigkeitsbeginn benötigt `manual_allow_future:true`;
ein rückdatierter Beginn wird abgewiesen. Alle Angaben müssen endlich, begrenzt
und nach dem aktiven Schema gültig sein.

`POST manual-sources/{source_id}/observations` verwendet das obige Format mit
UUID-`request_id` und optional `action:set|retract` sowie
`confirm_unbounded:true`. `GET manual-sources/{source_id}/requests/{request_id}`
liest das committed Ergebnis. Die append-only Tabelle `manual_request` hält
Prüfsumme und Ergebnis, ohne die Laufzeit mit historischen Anfragen zu belasten.
Anfrage, Observation, Folgezustände und Ergebnis werden atomar committed.

Serverzeit der Eingabe, deklarierter Gültigkeitsbeginn, optionales Ende,
administrative Herkunft, Notiz und Widerruf bleiben getrennt gespeichert.
Kein Gerätezeitpunkt wird erfunden. Die Quellenprüfsumme verhindert die Nutzung
einer alten Angabe nach einer Bedeutungsänderung. Neustart erneuert keine Frist.
Ein absoluter Gültigkeitsbeginn/-schluss wird über Clock geplant; die Grenzen
sind halb offen. Das Formular benennt vor Eingabe betroffene Verträge und
verlangt die Bestätigung einer zeitlich unbegrenzten Angabe. Bei verlorener
Antwort lässt es vor einer weiteren Eingabe das gespeicherte Ergebnis abfragen.
