# ADR 0024 — Einhorn-Herde und reproduzierbare Bildableitungen

20.10.2026 · Bennis Motive/Verwendung beschlossen; Pipeline **A1 / Review**.
Quelle: [control#60](https://github.com/Levtos/control/issues/60) samt Kommentar
vom 20.10.; bereitgestelltes ZIP und sein Steckbrief Version 4.
Dateiprüfung: neun Figuren 1024×1536 und neun Icons 1254×1254, alle RGBA.
Quell-Prüfsummen im [Inventar](../alpha10/herde-quellen.json).
Die Quelldateien wurden nur gelesen; keine Ableitungen in A1.

## Ablage und Unveränderlichkeit

Control bekommt in A2 `assets/herde/{name}-figur.png`, `{name}-icon.png`,
`herde-steckbrief.md` und README mit #60. Alle 18 PNGs bytegleich zum ZIP;
insbesondere keine Farbkorrektur, Eckensanierung, Quantisierung oder neue
Transparenz für Icons. Die unsichtbaren Pixel der Icon-Ecken tragen bereits
das Kachel-Petrol. Das ist Bestandteil der Quelle und wird nicht „repariert“.

Namen: wuschel, traber, schnueffel, kuschel, funkel, blinzel, schlummer,
traeller, pfoertchen. Schlummer ist gemäß aktueller Quelle junger Erwachsener
(ca. 20); die ältere Teenager-Angabe aus dem Issue ist überholt.
Die Steckbrief-Checkliste wird allein textlich geändert zu:
„Icon als PNG 1254×1254, Petrol-Kachel, abgerundete transparente Ecken,
unsichtbare Pixel im Kachel-Petrol“. Keine SVGs erfinden.

Wuschel referenziert den genauen Control-Commit/Quellhash in einem Manifest.
Originale bleiben außerhalb von frontend/public und src/assets; Build/CI lädt
keine unversionierte Remotequelle. Ein expliziter Eingabepfad zum separat
ausgecheckten Control-Assetordner ist Voraussetzung der A2-Bildgenerierung.
Nur Wuschel-/Traber-Ableitungen werden für diesen App-Scope gebündelt.
Die übrigen sieben sind Vorlagen in Control.

## Skriptvertrag für A2

`dev/build_herd_assets.py --source <control>/assets/herde --manifest <…>`
liest ausschließlich die 18 erwarteten Dateien und die erlaubte Manifeststruktur.
Keine rekursiv gefundenen Fremddateien, keine Netzaufrufe. Es prüft Namen, Maße,
RGBA und SHA-256 und stoppt bei Abweichung. Python/Pillow/WebP-Versionen werden
gepinnt und im Ableitungsmanifest gespeichert. Ausgabe ist deterministisch;
Quellenverzeichnis ist niemals Ausgabeziel.

Das Manifest enthält pro Figur den konservativen Alpha-Zuschnitt, Hufanker,
Zielcanvas und pro Icon/Favicon feste Ausschnitte. Werte werden in A2 auf
hell/dunkel geprüft und danach versioniert; keine willkürlichen Neuberechnungen
zwischen Läufen. Alpha>0 bestimmt den zu erhaltenden Inhalt, Alpha≥8 kann nur
zur Suche nach der Hauptfigur dienen. Ein Randpixel darf keinen Arm/Huf/Horn
abschneiden. Bei niedrigen Alpha-Ausreißern bleibt der größere Inhalt erhalten.
Die Quellen haben teils sichtbaren Inhalt bis zur Bildkante: fehlenden Rand
durch Canvas-Erweiterung schaffen, niemals Bildinhalt ergänzen.

Figurencanvas: Seitenverhältnis 2:3, 1024×1536 beziehungsweise 512×768.
Einheitlicher Mindestfreiraum 48 px links/rechts/oben im großen Canvas,
Hufgrundlinie bei y=1488 (48 px unten), proportional halbiert im kleinen Canvas.
Manifest-Hufanker ist der tiefste tragende Hufkontakt; laufende Figuren dürfen
einen schwebenden Huf haben. Pro Figur größtmöglicher proportionaler Maßstab,
der die gesamten Alpha-Ausdehnungen und den Bodenanker erfüllt; kein Strecken.
Das vereinheitlicht Randregel und Grundlinie, ohne Posen oder Proportionen zu
ändern. Keine Forderung, dass unterschiedlich breite Posen gleich hoch werden.
Falls ein außerhalb des Hufankers liegender Schweif die Bodenregel verletzt,
wird der Canvas-Rand vergrößert und die Manifest-Ausnahme begründet.

Verkleinerung: sRGB nach linear RGB, Alpha auf [0,1]; RGB mit Alpha
multiplizieren; alle vier Kanäle mit identischem Lanczos-Kernel skalieren;
Alpha/Pixelwerte begrenzen; RGB nur für Alpha>0 durch Alpha teilen;
zurück nach sRGB. Transparente Zielpixel erhalten beim Icon das dokumentierte
Petrol, bei Figuren einen festen neutralen RGB-Wert. Dieser letzte Schritt
betrifft ausschließlich Ableitungen. Er verändert keine Originale.
Kein direktes Filtern unvormultiplizierter RGBA-Kanäle, das unsichtbare Farben
in sichtbare Ränder ziehen könnte.

WebP wird erst nach Rückrechnung in gerades Alpha encodiert:
lossless, method=6, exact=True, ohne EXIF/sonstige private Metadaten.
PNG-Ableitungen verlustfrei. Erneuter Lauf mit denselben Eingaben/Tools
muss dieselben Hashes liefern; CI prüft das in A2.

## Größen und Einsatz

| Ziel | Vorgabe |
|---|---|
| `wuschel/icon.png` | 128×128, nur unverändert proportioniertes Wuschel-Icon verkleinert |
| `wuschel/logo.png` | 250×100 transparenter Canvas, Icon innerhalb 100×100 zentriert; kein Einhorn/erfundenes Wortlogo |
| eigene Navigation | Icon 32/64 px je DPR, sichtbarer Modulname; keine Figur in Listen/Navigation |
| Favicon 32 | vollständiges Wuschel-Icon 32×32 |
| Favicon 16 | quadratischer Siegelausschnitt aus dem Icon, initialer Reviewausschnitt (420,355)–(840,775); Ränder in A2 prüfen, dann festschreiben |
| Apple Touch | 180×180, vollständiges Icon; Ableitung mit Petrol-Hinterlegung für die sonst transparenten Ecken |
| Figuren | WebP 512×768 und 1024×1536; responsive srcset, feste aspect-ratio und Lazy Loading außer sichtbarem Kopf |
| Traber-Brand | `custom_components/traber/brand/icon.png` 256×256 und `icon@2x.png` 512×512; logo 250×100 und @2x 500×200 |

HA-App-Icon 128 ist unabhängig von der empfohlenen Integrations-Brandgröße.
Für alle kleinen Fassungen gilt: keine Umzeichnung des Motivs, kein Hinzufügen
von Rand-/Statusfarben. 16 px darf den ausdrücklich gewünschten Ausschnitt
nutzen, 32/128 bleiben Vollmotiv.

Figur im Seitenkopf, bei Einrichtung, leeren Seiten (etwa „Noch keine
Verträge“) und Fehlerseiten; Wuschel ist Standard, Traber kann HA-Anbindung
illustrieren. Pro Ansicht keine konkurrierende Figurenkollektion.
Dekorative Figur `alt=""`; Modul-Icon erhält nur dann Alternativtext, wenn
kein sichtbarer Modulname die gleiche Information vermittelt.
Keine Statusfarbe aus einer Mähne ableiten. Bestehende Token/Typografie,
Deutsch/Du-Form und Alpha-9-Seitenregel bleiben; kein Frameworkwechsel.

HA-Seitenleiste: `panel_icon: mdi:script-text-outline`.
Eigene App-Navigation und Store/Kachel verwenden das Bild; Sidebar-MDI kann
kein benutzerdefiniertes PNG ersetzen.

## Traber: aktueller HA-Weg, geprüft am 20.10.2026

Seit HA 2026.3 können Custom-Integrationen lokale Bilder in `brand/` liefern;
sie haben Vorrang vor dem brands-Repository. Traber nutzt diesen Weg,
kein erforderlicher PR an home-assistant/brands für unterstützte HA-Versionen.
Vor B die tatsächlich installierte HA-Core-Version über einen Statusendpunkt
ohne Optionen lesen. Unter 2026.3: anhalten und Kompatibilitätsentscheidung
melden, kein automatisches HA-Upgrade. Ein brands-PR wäre nur ein separat
freizugebender Rückwärtskompatibilitätsweg.

Primärquellen:
[HA-Ankündigung vom 24.02.2026](https://developers.home-assistant.io/blog/2026/02/24/brands-proxy-api/),
[Integrationsdateien](https://github.com/home-assistant/developers.home-assistant/blob/master/docs/creating_integration_file_structure.md),
[aktuelle Brand-Dokumentation](https://contributors.home-assistant.io/core/integrations/brands/),
[App-Icon/-Logo](https://developers.home-assistant.io/docs/apps/presentation/).
Keine selbst gebauten authentifizierten Brand-URLs mit Tokens in Belegen.

## A2-Abnahme

Originalhashes aller 18 Dateien unverändert, Ableitungsmanifest, zweiter
deterministischer Lauf, keine Originale im Frontend-Bundle, kein Randhalo auf
hell/dunkel, gemeinsame Grundlinie/keine abgeschnittenen Hufe/Hörner.
Kontaktbogen 16/32/128 hell/dunkel; 16-px-Siegel muss erkennbar bleiben.
Firefox-Belege laut Alpha-10-Einstieg. B ergänzt reale Kachel-/Store-/Traber-
Darstellung; lokales Packaging beweist keine Live-Iconanzeige.
