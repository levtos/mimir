# ADR 0031 – Belegbare Wartegründe im Kern

- Status: **Entwurf für Bennis A1-Review; nicht beschlossen, nicht implementiert.**
- Datum: 22.10.2026; [Wuschel #35](https://github.com/Levtos/wuschel/issues/35).
- Basis: `c8d4dff35048f0c69290ea500b0609e89d531a60`.
- Ausarbeitung: [UX-A1 §9 und Testliste](../beta/ux/A1.md),
  [Konzept §7](../beta/ux/konzept-2026-10-22.md).
- Voraussetzungen: [ADR-Entwurf 0030](0030-freshness-templates-evidence.md),
  [ADR 0019](0019-sensor-profile-value-origin.md),
  [ADR 0028](0028-grenze-wuschel-engines.md).

## Problem und Entscheidungsvorschlag

Ein pauschales input_stale trennt den ersten gespeicherten Empfang nicht
ausreichend von einem zuvor geeigneten, später veralteten Bericht. Ein UI-Timer
oder Übersetzen eines Fehlerworts kann weder den Beginn der echten Beobachtung
noch einen bereits früher akzeptierten Nachweis beweisen.

Vorgeschlagen wird eine additive, persistierte Quelldiagnose im Kern.
Wuschel berechnet den belegten Zustand genau einmal. Die Oberfläche übersetzt
ihn, Engines bleiben Verbraucher fertiger Wahrheiten. Die Diagnose macht keinen
ungeeigneten Wert verwendbar und ändert keine bestehende Freshness-/Restore-Regel.

## Persistierter Vertrag

Pro source_id und observation_fingerprint: zugehörige Revision/Regel,
observation_started_at mit Belegart, ever_accepted_for_identity, referenzierte
geeignete Evidence und ursprüngliche Messzeit, Art des vorhandenen Nachweises,
waiting_reason, waiting_since, gegebenenfalls expected_at sowie tatsächlicher
Hinderungsgrund. assessment_fingerprint bindet die verwendete aufgelöste Regel.

Ein positiver Beobachtungsbeginn verlangt Aktivierung und tatsächlich begonnene
Beobachtung. Ist beispielsweise die Subscription noch nicht bestätigt, steht
dieses Hindernis statt einer scheinbar laufenden Sensorfrist. Ein unbekannter
Beginn bleibt null mit „Zeitpunkt noch nicht bestimmbar“. Die Oberfläche darf
keinen Timestamp aus dem Öffnen der Seite ergänzen.

waiting_since wird mit dem Quellenkontext durch den vorhandenen Writer
persistiert. Reload, Retain-Replay, Reconnect, Restart und unbeteiligte
Konfiguration setzen es nicht auf jetzt. Eine geänderte Meldefrist rechnet
expected_at aus demselben belegten Beginn neu. Keine Frist für event_stateful
erfinden. Die bestehende Intervallgrenze und deren Clock-Präzision gelten auch
beim Wechsel von Erwartung zu Warnung; Gleichheit allein ist kein vorgezogener Ablauf.

Eine zuvor passende Observation bleibt nach unveränderter Quellenidentität
maßgeblich. Zulässige mqtt_revalidated-Geräte-Evidence trägt weiter ihre
ursprüngliche Messzeit, nicht eine erfundene neue Meldung. Gleicher Wert mit
echter neuer Quellzeit darf Warten beenden; wiederholter Retain/Replays nicht.
Liveness ist nur der ausdrücklich deklarierte Nachweis, keine nachträgliche
Kontaktmessung. Kein Startup erzeugt eine neue fachliche Flanke oder Grace.

## Diagnose und Darstellung

Additiver versionierter Block diagnostic.source_waiting in Quellen-/Vertrags-
diagnosen. Hauptgründe: ungültige Meldung oder Nichterreichbarkeit vor fehlendem
Nachweis beziehungsweise überschrittener Frist. Konflikte bleiben eigene Gründe;
alle belegten Ursachen stehen unter „Details“. Vertragsansicht nennt nur tatsächlich
benötigte ergebnisbestimmende Quellen. Fehlende Diagnosedaten heißen „Aktualität
noch nicht prüfbar“, niemals „bereit“ aufgrund eines UI-Fallbacks.

Ohne je geeigneten neuen Nachweis: „Wartet auf die nächste Meldung des Sensors“;
nach überschrittener belegter Anfangserwartung „Noch keine neue Meldung erhalten“.
Nur ein tatsächlich vormals geeigneter, nun alter Nachweis erhält „Die letzte
Meldung ist zu alt“. Laufende Grace bleibt als vorübergehend gehaltener Wert
sichtbar, kein bestätigtes „zu“. Bereitschaft, Vertragszustand, Aktualität,
Erreichbarkeit und Auffälligkeit bleiben getrennte Achsen.

UTC und Clock im Kern, Europe/Berlin für Uhrzeitdarstellung. Zustandswechsel
werden bei tatsächlichem Grundwechsel gespeichert, nicht bei jedem Abruf.
Diagnoseexport enthält keine Geheimnisse; portabler Konfigurationsexport enthält
keine Wartezeitpunkte, Evidence oder sonstigen Laufzeitnachweise. Bestehende
Consumer-Fachwerte bleiben englisch und unverändert.

## Migration, Tests und Gate

Altbestand bekommt nur nachweisbare Zeitpunkte. Fehlt ein persistierter Beginn,
bleibt er unbekannt; ein Programmupdate erfindet keine Vergangenheit. Neue
Identität beginnt einen neuen Kontext, neutrale Regel-/Metadatenänderung nicht.
Erhalt/Neubewertung folgen der in ADR 0030 vorgeschlagenen Kompatibilität.

Geplant: UX-5-01…08 mit FakeClock, vor/an/nach Deadline, ohne Deadline,
Transportblockade, Reload/Restart/Replay, gleiche echte Meldung, erlaubter Restore,
falsche/future Messzeit, nicht erreichbare Quelle und mehrere Gründe. API,
Quellenliste und Vertragsansicht müssen denselben Grund zeigen.

Empfohlener Release b5; Warn-/Sprachverbesserungen aus b3 bleiben separat.
Kein eigener UI-Nachweisalgorithmus und keine Aufweichung der Sensorregeln.
Diese ADR ist nur Design; kein Code, Release oder Live-Eingriff ohne spätere Gates.
