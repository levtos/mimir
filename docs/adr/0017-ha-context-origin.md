# ADR 0017 — G15: belegbare Herkunft von HA-Änderungen

18.10.2026 · **A2 freigegeben: Claude (Technik), Benni (Texte), 18.10.2026.** Grundlage: M30-34 §2,
M30-41 §2, Matrix G15; [ADR 0012](0012-bifrost-service-channel.md).

## Ziel und Modell

Bifröst transportiert HA-Context vollständig genug, um bekannte automatische
Änderungen positiv zu erkennen. Eine fehlende Kennung wird niemals zu „manuell“.
Die fachliche Regel, ob eine bereits zugelassene Interaktion zählt, bleibt in
der versionierten Vertragsdefinition; die Bridge entscheidet keine Wachheit.
Policy-/Apply-Implementierung und ihre Kontextmarkierung bleiben außerhalb Alpha 9.

## Datenformat, Nachweis und Grenzen

Protokoll 2 ergänzt in `changed`, `reported` und Snapshot-Einträgen
`context:{id,user_id,parent_id}` mit explizitem null bei fehlenden Daten.
Bei Reports ohne nachweisbar zugehörigen vollständigen Context nur bekannte
Felder senden, niemals den zuletzt gesehenen Context eines anderen Ereignisses
unterschieben. `context_id` bleibt im v1-Format unverändert. Observation speichert
die drei Felder samt Ereigniszeit/Art; Aufbewahrung und Diagnoseredaktion gelten.

```json
{"context":{"id":"ctx-a","user_id":null,"parent_id":"ctx-parent"},
 "attribution":{"kind":"known_automatic","basis":"registered_context",
                "matched_context_id":"ctx-parent"}}
```

`attribution.kind = known_automatic | known_user | unknown` ist ein separater
Herkunftsbefund. `known_automatic` verlangt positive Zuordnung zu einem registrierten
Policy-/Apply-Kontext oder einem von HA belegten Automations-/Script-Lauf.
Ein parent_id allein beweist nur einen Zusammenhang. Eine user_id allein belegt
ein Konto, nicht menschliche Bedienung; technische Nutzer/Servicekonten sind
keine manuelle Interaktion. `known_user` nur bei ausdrücklich bekannter interaktiver
Herkunft; andernfalls unknown. Keine Raten anhand von Zeitnähe, Wert oder Gerätename.

Registrierung bekannter automatischer Kontexte nur über authentifizierte,
administrative Schnittstelle mit geprüftem Producer, Ablaufzeit und Bindung an
die aktuelle HA-Laufzeit. Keine frei erfundenen `origin`-Felder aus Geräten oder
vertraglichen Werten. HA-eigene Automationszuordnungen nur über belegte Events/
Registry-Informationen, nicht eine zweite allgemeine Serviceüberwachung. Fehlende
Zuordnung kann keine positive Erkennung liefern. Keine Fremdrepos ändern.
Vorschlag: höchstens 1.024 Kontextzuordnungen, 10 Minuten TTL, maximal 8 Elternstufen;
Zyklus/fehlende Kette → unknown. Neustart verwirft unbelegte Zuordnungscaches.

## Verwendung und Beispiel

Die geschlossene Regelprojektion `known_automatic` ist typisierter Eingang einer
Definition; sie ändert nicht den Gerätewert. Zugelassene Interaktion mit
unknown-Herkunft darf nach M30-41 §2 weiterhin zählen, sofern sie nicht positiv
als Policy/Apply/Automation erkannt ist. Das ändert ihr Herkunftsetikett nicht.
Direkte Sensorereignisse bleiben von zusätzlicher Origin-Prüfung befreit, wenn
die jeweilige Definition diese Interaktionsklasse ausdrücklich festlegt.
Keine allgemeine Hierarchie „alles ohne Nutzer ist Automation“.

Beispiel: Lautstärkeänderung mit belegtem Apply-Elternkontext → keine menschliche
Interaktion für eine entsprechende Regel. Derselbe Wertwechsel ohne belegte
Zuordnung → unknown; die Regel darf ihn zählen, die Diagnose nennt ihn nicht manuell.

## Oberfläche, Tests, betroffene Akte

Normalansicht: „Änderung durch bekannte Automatik“, „Von dir eingetragen“ nur für
G10 oder belegte Benutzeraktion, sonst „Auslöser nicht sicher bekannt“. Technische
Context-IDs und Nutzerkennungen nur unter Erweitert; keine Namen/IDs in HA-Meldungen.
Formulare wählen Herkunftsbedingungen aus einer verständlichen Liste.

A2: vollständiger/teilweiser Context, v1/v2, Report ohne Kontext, bekannte Elternkette,
fehlende/zyklische/abgelaufene Zuordnung, technisches Nutzerkonto, HA-Neustart,
unknown bleibt unknown, positiv bekannte Automatik ausgeschlossen, direkte
Sensorereignisse, unveränderte Werte-/Freshness-Semantik und Datenschutz.
Betroffen: Akte oben; Build-Spezifikation §8/§13/§14/§21, Bridge/HA-Adapter,
Observation/Erklärung, deklarative Projektion und History. Keine neue Aktorsteuerung.
