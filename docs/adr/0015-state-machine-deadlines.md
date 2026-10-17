# ADR 0015 — G12: Fristen eines Ablaufs

18.10.2026 · **A1-Vorschlag, Review offen; kein Bau.** Bezug: M30-18/19,
M30-41 §5/§8/§9, A-05/A-06; [ADR 0006](0006-instance-parameters.md),
[0010](0010-clock-calendar-inputs.md). Die private Akte wurde am Stand P4-65 abgeglichen;
ihre Fachbeispiele werden nicht als Verträge implementiert.

## Ziel und Modell

Alpha 8 erzeugt eine einzige Frist bei neuer Episode. Die Erweiterung trennt
Friständerung, Zustandswechsel und Episodenbeginn. Weiter höchstens eine laufende
Frist je Ablauf; kein allgemeiner Jobplaner. Alte Sprachversionen 1/2 und ihre
Prüfsummen bleiben unverändert. Nur ausdrücklich neue Definitionen verwenden
`language_version:3` und die Capability `machine_deadline_v2`.

## Datenformat und Beispiele

```json
{"deadline_by_state":{"a":{"duration":{"parameter":"wait_s"}},
                      "b":{"duration":{"parameter":"other_wait_s"}}},
 "transitions":[{"source":"a","target":"a","event":"input",
                 "guard":{"op":"input","name":"interaction_edge"},
                 "deadline_action":"reset","new_episode":false}],
 "absolute_transition":{"states":["a","b"],"target":"c",
                        "at_input":"planned_at"},
 "unknown_deadline":"keep_and_block_transition"}
```

Dies ist ein Ausschnitt des vorgeschlagenen Formular-/Definitionsformats, keine
fertige Registry. Dauer = positive endliche Sekundenzahl oder G19-Parameterreferenz;
je Zustand genau eine deklarierte Fristregel. Dauer wird beim Eintritt/Reset
aufgelöst, kein versteckter Laufzeit-Default. `deadline_action` ist geschlossen:
`keep`, `reset`, `clear`. `reset` setzt `at = now + volle Dauer`, neue
`deadline_generation`, aber **dieselbe** episode_id, episode_started_at und session_id.
Ein reiner Fristreset ändert auch den Zustandsbeginn nicht. Derselbe anhaltende
Ja-Wert darf nicht wiederholt resetten: der Eingang muss ein belegtes Ereignis
oder ein ausdrücklicher Edge-Vertrag sein. Keine erneute Episode durch den Reset.

Ein Zustandswechsel mit anderer deklarierter Dauer setzt genau diese Dauer neu;
ohne Fristregel wird die Frist gelöscht. Mehrdeutige Kombinationen aus `reset`,
neuer Episode und absoluter Regel werden bei Validierung abgewiesen statt durch
Reihenfolge entschieden. Ereignispriorität bei gleichem Clock-Zeitpunkt:
zuerst bestätigte aktuelle Eingänge, dann auf aktuelle Generation geprüfte Alarme.

Absolute Übergangszeit kommt aus einem typisierten verwendbaren Timestamp-Eingang
mit Zeitzone. Sie wird als G1-Zeitpunkt-Erreicht-Eingang ausgewertet, nicht als
zweite SM-Dauerfrist. Über dieselbe Clock-/`time_reached`-Semantik genau einen Alarm
planen; Eingangstermin ändern/entfernen ersetzt/löscht ihn. Vergangenheit bedeutet
„jetzt erreicht“, keinen rückdatierten Übergang. Dauerfrist und absoluter Übergang
dürfen koexistieren: beide benutzen dieselbe Deadline-Auswahl, frühester fälliger
zulässiger Übergang gewinnt; identische Termine mit verschiedenen Zielzuständen
brauchen eine deklarierte Priorität und werden sonst als mehrdeutig abgewiesen.
Die veröffentlichte nächste Fälligkeit benennt Typ und Grund.

## Unknown-Hold, Neustart und Atomarität

M30-41 §5: `unknown` hält den Ablaufzustand, **nicht die Uhr**. Die absolute
Frist läuft unverändert weiter, keine Pause/Restzeitverlängerung und kein Reset.
Wird sie während unbrauchbarer entscheidender Eingänge fällig, bleibt sie als
fällig, aber noch nicht verarbeitet erhalten. Sie ist nicht als erfolgreich
verbraucht zu markieren. Sobald die notwendigen Eingänge wieder verwendbar
sind, regulär entscheiden; `unknown` allein erzeugt niemals einen Übergang.
Der gehaltene interne Temporal-Zustand ist kein frei erfundenes `held`-Ergebnis
und eröffnet keine Grace. Gültige Gegen-Evidence darf den normalen anderen Pfad auslösen.

Persistiert werden Frist-ID/-Generation, absolute UTC-Fälligkeit, Bezug zu
Episode/Zustand, Modus und Verarbeitungsstand. Reset und Übergang werden gemeinsam
mit dem Zustand committed; erst danach Alarme/Publication abgleichen. Alte
Generationsalarme sind wirkungslos. Restart lädt den Originaltermin, plant keine
volle Dauer neu und rekonstruiert keine verpassten Interaktionen. Fälliger Restore
wird mit aktueller Evidence geprüft; fehlender Beleg bleibt sichtbar unbekannt.
G19-Änderungen folgen A-06, nicht einem stillen Reset zur alten Episode.

## Oberfläche, Tests und betroffene Akte

Formulare: je Zustand „Zeit bis zum nächsten Schritt“, „Frist neu beginnen“,
„Zeitpunkt aus einem Eingang“, „Bei fehlenden Werten warten“. Erklärung zeigt das
unveränderte Fristende. Beispiel synthetisch: a ab 10:00 für 120 s; Reset 10:01
→ Ende 10:03, gleiche Episode; unknown 10:02–10:04 → kein Wechsel um 10:03,
erst Prüfung mit belegten Eingängen um 10:04. Keine Fach-SM in Alpha 9.

A2-Tests: voller Reset/gleiche Episode, Dauer je Zustand/Instanz, fehlende/negative
Parameter, genaues Fristende, dauerhaftes Signal ohne Wiederreset, Terminersatz,
absolute Vergangenheit/DST, konkurrierende Fälligkeiten, unknown vor/bei/nach Ende,
gültig on/off nach unknown, Restart/DB-Recovery/Commit-Fehler, alte Alarme,
unveränderte Ergebnisse und gespeicherte Prüfsummen alter Definitionen.
Betroffen: Build-Spezifikation §9/§10/§18/§21; SM, Compiler, Clock, Restore,
Erklärung/Verlauf, Formulare und API. Formate/Tests bleiben A1-Vorschläge.
