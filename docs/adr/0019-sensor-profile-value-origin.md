# ADR 0019 — G8/G9: auffällige Sensorwerte und Art ihrer Herkunft

18.10.2026 · **A2 freigegeben: Claude (Technik), Benni (Texte), 18.10.2026.** Grundlage: M14-05,
M21-17, M30-46 §11 Katalog #8–13, CP-15; Matrix G8/G9.

## Ziel und getrennte Achsen

Erreichbarkeit, Aktualität, Auffälligkeit und Art des Werts beantworten verschiedene
Fragen. Ein regelmäßig meldender Sensor kann festhängen. Ein gleichbleibender
Fensterkontakt oder Bewegungsmelder ist deshalb noch nicht defekt. Modell und
Prognose sind keine Messungen; „Ersatz“ ist keine Behauptung einer Messung am
ursprünglichen Gerät. Installationsherkunft, HA-Kontext und G10 manual bleiben
zusätzliche, getrennte Angaben.

## G8: Profil und Zustand

```json
{"sensor_profile":{"id":"example_temperature","version":1,
 "stuck":{"unchanged_for_s":1814400,"tolerance":0.05,
          "min_reports":10,"recovery_reports":2,
          "reference":{"ref":"example.reference","min_delta":2.0}}}}
```

Nur explizit ausgewähltes Profil aktiviert die Prüfung; kein globales 24-Stunden-
Default. Profilschema/Version sind unveränderlich, Zahlen können G19-Parameter sein.
Mindestanzahl und Dauer müssen zugleich erfüllt sein; Vergleich nur zwischen
normalisierten gültigen Zahlen gleicher Einheit. Optionale Referenzregel:
eine verknüpfte unabhängige Vergleichsquelle muss innerhalb desselben belegten
Zeitraums eine deklarierte Mindeständerung zeigen. Referenz wird kein Ersatzwert.
Bool-/Kontakt-/Bewegungsprofile verwenden standardmäßig keine Gleichwertprüfung.

Zustand: `{plausibility:unchecked|plausible|suspicious,unchanged_since,
report_count,profile_version,reasons,evidence}`. `suspicious` ergänzt
`quality:degraded` und `sensor_stuck_suspected`; ein belegter numerischer Wert bleibt
`valid`, wird nicht als andere Zahl ersetzt. Ein harter Wertebereichsfehler darf
separat `unknown/invalid_value` ergeben. Unbrauchbare Referenz belegt keine
Auffälligkeit und gibt nicht „plausibel“ vor. Wieder gültige echte Abweichungen
beenden den Verdacht nach deklarierter Erholungsregel.

Nur eindeutig belegte neue Reports zählen, auch bei unverändertem Messwert;
nicht identische Delivery-Duplikate,
Snapshots, Neuberechnung oder Re-Publication. Nach Beobachtungslücke/Restart wird
kein unbewiesener Gleichbleibezeitraum fortgeschrieben: vorhandener Kontext nur
mit gleichem Fingerprint und belegter Kontinuität nach §9.3; sonst erneut aufbauen.
Profilwechsel erzeugt A-06 ohne gefälschten Messwert oder neue Fachflanke.

## G9: Format, Intervall und Weitergabe

```json
{"value_origin":{"kind":"forecast","provider":"example",
 "issued_at":"2026-10-17T08:00:00Z","valid_from":"2026-10-18T08:00:00Z",
 "valid_until":"2026-10-18T09:00:00Z","based_on":["evidence:example"]}}
```

Geschlossene Arten: `measured`/„Gemessen“, `replacement`/„Ersatz“, `model`/„Modell“,
`forecast`/„Prognose“. `value_origin` ist je Wert bzw. Reihenpunkt geführt;
`source_origin:local` wird nicht umdefiniert. Bei nichtphysischer manueller Angabe
kann die zusätzliche Wertart fehlen; sie bleibt sichtbar „Manuell eingegeben“.
Alte Daten ohne Herkunft bekommen keine nachträglich erfundene Kennzeichnung.

Gültigkeit ist ein halboffenes UTC-Intervall mit Zeitzone; Ende nach Beginn.
Prognosepunkte brauchen beide Grenzen und `issued_at`; Quellen-/Providerzeit ist
nicht App-Empfangszeit. Eine Prognosereihe darf zukünftige Intervalle enthalten,
aber ein aktueller Verbraucher darf nicht willkürlich den nächsten Punkt als
jetzigen Wert ausgeben. Lücke/außerhalb des angefragten Intervalls = unknown mit
Ursache. Sich überlappende Punkte derselben Größe mit unterschiedlichen Werten
werden abgewiesen; keine heimliche Auswahl nach Listenreihenfolge. Ablauf wird
über Clock neu bewertet. Aktualität des gelieferten
Datenbestands und Gültigkeit des einzelnen Prognosewerts müssen beide passen.

Ein ausgewählter Wert übernimmt die belegte Herkunft; eine Berechnung benennt
ihre Eingangsherkünfte und die eigene explizite Modell-/Berechnungsart.
Bei mehreren Quellen bleibt die Herkunft je ergebnisbestimmendem Beitrag sichtbar;
keine automatische Behauptung „gemessen“, weil irgendein Eingang gemessen ist.
Verwendbares Intervall höchstens die Schnittmenge der benötigten Eingänge und
der eigenen deklarierten Grenzen. Ersatz wird nur über ausdrückliche
Zusammenführungsregel ausgewählt, nie durch den Adapter bei einem Fehler erfunden.

## Oberfläche, Beispiele und Tests

„Sensorprüfung“: Geräteprofil auswählen, Dauer/Toleranz/Berichte einstellen;
„Wert seit ungewöhnlich langer Zeit unverändert“ erklärt den Verdacht.
„Art des Werts“ sowie „Gültig von/bis“ sind im Quellen-/Wertschema ohne JSON
bearbeitbar. Vertragsansicht zeigt Herkunft und Verdacht getrennt von Aktualität.
Technische Provider-/Evidence-Kennungen nur unter Erweitert.

A2: gleiche gerundete Temperatur mit frischen Reports, Änderung über Toleranz,
fehlende/wechselnde Referenz, Duplikate, Kontakt/Bewegung ohne Fehlalarm,
Grenzen/Erholung/Restore/Profilwechsel; alle vier Herkunftsarten, Ersatz sichtbar,
manuelle nichtphysische Angabe, gemischte Eingänge, Prognoselücke/Überlappung,
Intervallende/DST, Timestamp-Fehler, fehlende Alt-Metadaten, Commit-Fehler.
Betroffen: §7/§8/§9/§10/§21 der Build-Spezifikation, Evidence/Envelope,
Profilvalidierung, Processor, History/Retention, API/Client und Formulare.
Fach-Sensorprofile und Klima-Formeln werden nicht produktiv angelegt.

## Umsetzung A2

`Source.sensor_profile` enthält die versionierte Profildefinition; gemeinsam
verwendete ID/Version muss identisch bleiben, auch gegenüber bereits übernommenen
Konfigurationen. `parameter_schema` deklariert Zahlenparameter. Schwellen im
Profil können dieselben typisierten `{op:parameter,name:…}`-Verweise wie G19
nutzen; `Source.sensor_parameters` hält die Werte dieser Quelleninstanz.
Eine Änderung der Parameter setzt nach A-06 die Vergleichsbasis zurück, ohne
eine neue Profilversion zu erfinden. Das Formular schlägt nach ausdrücklichem
Einschalten 21 Tage, 0,05 Toleranz, zehn Meldungen und zwei Erholungsmeldungen vor;
ohne ausgewähltes Profil ist die Prüfung aus. Keine Fachprofile werden angelegt.

Kontext und Referenznachweise sind begrenzt in `service_state` persistiert.
Nur neue Reports mit fortgeschrittener Messzeit zählen. Snapshot, Wiederholung,
Neubewertung, Neustart und Lücken verlängern keinen unbelegten Gleichbleibezeitraum.
Eine optionale Referenz muss unabhängig, gleich dimensioniert und verwendbar
sein; Snapshot und auffällige Referenz beweisen keine Änderung. Verdacht ergänzt
Ursache und `quality:degraded`, ohne den belegten Zahlenwert zu ersetzen.

`Source.value_origin` deklariert Art/Anbieter. Adapter können über
`value_origin_path` pro Meldung die typisierte Herkunft übernehmen: in HA ein
Attributname, bei MQTT ein begrenzter Datenpfad. Alte Sprache-/Konfigurationsstände
werden nicht rückwirkend etikettiert. Prognosereihen sind Listen aus
`{value,value_origin}`. Jeder Punkt hat Ausgabezeit und halboffenes UTC-Intervall;
Wert und Einheit folgen dem Quellschema. Widersprüchliche Überlappungen sind
ungültig; gleichwertige Überlappungen behalten alle Herkunftsbeiträge und die
engsten Grenzen. Auswahl und Frische hängen nicht von Empfangszeit oder
Listenreihenfolge ab. Quellenfrische und Provider-Ausgabezeit werden getrennt
von der Gültigkeit eines einzelnen Punkts geprüft.

`FieldValue.value_origin`, `input_origins`, `valid_from`/`valid_until` und
`plausibility` werden in Nachweis und Verlauf mitgeführt. Auswahl bewahrt die
Herkunft des gewählten Werts; Berechnungen übernehmen die Herkunft ihrer
entscheidenden Beiträge und behaupten keine Messung. Neue Definitionen können
mit `output_origins` ausdrücklich Modell oder Ersatz benennen (Sprachversion 3).
Gültigkeit wird geschnitten; auch eine deklarierte Grace überschreitet das Ende
eines Zeitraums nicht. Clock plant Beginn, Ende und Quellen-/Providerfristen.

Manuelle Prognosen verwenden denselben Eingabeweg aus ADR 0016. Die Oberfläche
hat Zahlen-/Auswahlfelder sowie Kalenderfelder je Zeitraum, ohne JSON-Eingabe.
Vertragsansicht nennt die Art des Werts, verwendete Eingangsarten, Gültigkeitsende
und einen Sensorverdacht getrennt von der Aktualität. Anbieter-/Profilkennungen
stehen unter Erweitert.
