# ADR 0028 — Grenze Wuschel / Engines

21.10.2026 · **Grundsatzentscheidung Benni, 21.10.2026.** Gilt für alle Bereiche der Beta und für 1.0.
Grundlage: Entscheidungsakte Phase 4 (Auditrevision) M03-01, M03-02, M03-05, M03-08, M30-08, M30-23
mit A-10, M30-42 (K3), M30-46 (P4-65 §1, §9, §11.2, §11.4).

## Entscheidung

1. **Jede Wahrheit wird an genau einer Stelle berechnet – in Wuschel – und von dort live
   bereitgestellt: neu berechnet bei jeder Änderung ihrer Eingänge und bei fälligen
   Zeitbedingungen (Dauer, Fristen, Aktualität). Keine Engine berechnet dieselbe Wahrheit ein
   zweites Mal.** Wuschel nutzt dafür Resolver, Vertragsketten und Abläufe (State Machines).
   Engines (Schnüffel, Kuschel, Funkel, Blinzel, Schlummer, Träller, Pförtchen) berechnen keine
   Wahrheiten und lesen keine Rohentitäten.
2. **Wuschel rechnet so weit vor wie möglich.** Engines bekommen fertige, aussagekräftige Wahrheiten,
   zum Beispiel „Fenster Wohnzimmer seit 5 min ganz geschlossen“, „Heizperiode aktiv“, „Benni schläft“,
   keine Rohwerte, die sie selbst interpretieren müssen.
3. **Wünsche, Profile und Komfortwerte gehören in die Engine**, ebenso die Entscheidung „also tun wir X“.
   Beispiele: Wunschtemperatur, Lautstärke, Rollo-Position, Reaktion auf Urlaub oder Besuch.
   In Wuschel gibt es keinen Vertrag „Heizen nötig“, „Rollo runter“ oder Ähnliches.
4. **Jede Engine begründet ihre Entscheidung sichtbar für Benni:** Ziel der Entscheidung und die
   Wuschel-Wahrheiten (Vertrags-ID, Wert, Zustand), auf die sie sich stützt.
5. **Ziel:** Wuschel bleibt überschaubar; jede Engine ist ein kleines, eigenständig wartbares Modul.

## Prüffrage für jeden Einzelfall

„Beschreibt der Wert, wie die Welt ist?“ → Wuschel.
„Beschreibt der Wert, was jemand möchte oder was getan werden soll?“ → Engine.

A-10 bleibt gültig: Eine Schwelle, die eine Wahrheit definiert (hell/dunkel, Gerät aktiv,
Heizperiode), gehört zu Wuschel. Eine Schwelle, die eine Reaktion definiert (unter 20 °C heizen),
gehört zur Engine.

## Regel 1 — Bedarf statt Mehrfachbedarf

Eine Wahrheit über die Welt kommt nach Wuschel, **sobald mindestens eine Engine sie tatsächlich
nutzt**. Keine Verträge auf Vorrat.

Begründung: Verträge sind Konfiguration, kein Code. Wuschels Programmcode wächst durch weitere
Verträge nicht; es wächst nur die Vertragsliste. Ohne diese Regel müsste eine Engine eine Wahrheit,
die nur sie braucht, doch wieder selbst berechnen – das verbietet Punkt 1.

## Regel 2 — Sammel-Wahrheiten enthalten keine engine-spezifische Bewertung

Fasst Wuschel mehrere Verträge zusammen (zum Beispiel alle Öffnungen eines Raums oder einer Zone),
liefert Wuschel **getrennte Fakten, kein fertiges Urteil**. Was ein Zustand für eine Engine bedeutet,
entscheidet die Engine durch Auswahl, nicht durch Rechnen.

Anlass: Für Blinzel ist ein gekipptes Fenster sicher (OS-A4); für Kuschel ist es ein Grund, nicht zu
heizen (K3). Ebenso darf Blinzel einen gehaltenen Wert während der Gnadenfrist weiterbenutzen, Kuschel
nicht („`held` pro Consumer“, P4-65 §1). Ein Urteil „alle zu“ wäre für eine der beiden Engines falsch.

**Öffnungen je Raum/Zone — getrennte Fakten, jeweils mit „seit wann“:**

| Fakt | Bedeutung |
|---|---|
| mindestens eine offen | mindestens eine Öffnung liefert belastbar `open` |
| mindestens eine gekippt | mindestens eine Öffnung liefert belastbar `tilted` |
| Zustand unklar | mindestens eine Öffnung ist `unknown`/`unavailable` oder im Konflikt |
| mindestens eine gehalten | mindestens eine Öffnung steht nur auf ihrem gehaltenen Wert (`held`) |
| alle ganz geschlossen | alle Öffnungen liefern frisch und gültig `closed`, keine davon `held` |

**Auswahl in den Engines (Beispiel):**

- Blinzel: sicher, wenn „keine offen“ und „nicht unklar“. Gekippt und gehalten sind für Blinzel erlaubt.
- Kuschel: Heizen erlaubt, wenn „alle ganz geschlossen“ seit mindestens X min (X ist Kuschel-Einstellung).

Welche Öffnungen zu welchem Raum bzw. welcher Zone gehören, ist **Wuschel-Konfiguration**.
Welche Zone eine Engine benutzt, legt **die Engine** fest.

## Abgelöste und präzisierte Stellen der Akte

| Stelle | Bisher | Ab dieser ADR |
|---|---|---|
| M30-23 | „Zentrale Ableitungen nur bei belegtem Mehrfachbedarf“ | **Abgelöst** durch Regel 1 (Bedarf) |
| OS-A4 (P4-65 §9) | „kein Core-Zonen-/Raumaggregat; Aggregation im Consumer“ | **Abgelöst:** Wuschel liefert Sammel-Fakten nach Regel 2; Engines wählen nur aus. Inhalt „tilted ist für Blind sicher“ bleibt als Blinzel-Auswahl gültig |
| P4-65 §11.2 | „Kein zusätzlicher Core-Zonenaggregat-Contract; der Consumer aggregiert“ | **Abgelöst** wie OS-A4. Unverändert: Zuordnung je Zone, Wohnungstür zählt nicht für Klima, keine Querwirkung unabhängiger Zonen, Fail-Safe-Tabelle K3 (jetzt als Kuschel-Auswahl über „alle ganz geschlossen“) |
| M30-42 K3 | Fail-Safe-Tabelle als Climate-Policy-Regel | **Präzisiert:** Bewertung je Öffnung bleibt Wuschel (ehrlicher Zustand, M15-03); die Freigabe „heizen erlaubt“ bleibt Kuschel-Entscheidung |
| P4-65 §11.4, PA-Zeilen | `effective_outdoor_temperature`, `shower_active`, `humidity_rise_5m` „bleiben Policy/Climate-intern“ | **Offen, im Bereich Klima neu prüfen** mit der Prüffrage oben |
| M30-23, M03-01, M03-04, M03-08 | Core = was ist wahr; Policy = was soll geschehen | **Bestätigt** |

## Folgen

- Vor jedem Bereich wird jede benötigte Wahrheit mit der Prüffrage eingeordnet; die Einordnung steht
  in der Bereichsdokumentation mit Fundstelle.
- Die Begründungspflicht (Punkt 4) ist eine Anforderung an jede Engine, nicht an Wuschel.
  Wuschel liefert dafür Vertrags-ID, Wert, Zustand und Aktualität über die Consumer-Schnittstelle.
- Keine Plattformänderung durch diese ADR. Sammel-Fakten werden mit vorhandenen Bausteinen
  (Verträge auf Verträgen, Und/Oder, Temporal „seit wann“) gebaut; ob das je Fall ohne neuen
  Baustein geht, prüft der jeweilige Bereich (A1).
