# ADR 0026 — Import & Export als vollständiges, portables Konfigurationspaket

20.10.2026 · Bennis Funktionsumfang beschlossen; Format/Verfahren **A1 / Review**.
Bezug: [ADR 0020](0020-category-room-metadata.md),
[0025](0025-managed-catalog.md), [#24](https://github.com/Levtos/wuschel/issues/24).

## Bedienung und Grenze

Ein Menüpunkt „Import & Export“, kanonisch `/import-export`, ersetzt die zwei
bisherigen Einstiege in Navigation/Änderungen. Alte Routen bleiben Redirects
nach [0022](0022-wuschel-traber-naming.md).
Seitentitel „Import & Export“, Satz „Hier kannst du deine Konfiguration sichern
oder eine gesicherte Konfiguration einlesen.“ Ein Hauptknopf „Konfiguration
sichern“, Dateieinlesen als untergeordnete Aktion im Inhaltsbereich.
Dialoge haben genau ihre eigene Bestätigung. Keine Roh-JSON-Pflicht;
Rohansicht nur ergänzend unter „Technische Details“.

Im Vertrag: Nebenaktion „Diesen Vertrag exportieren“ im Aktionsmenü.
Exportdialog zeigt Wurzelvertrag und alle mitgenommenen Teile, Quelle
„Übernommene Konfiguration“ oder ausdrücklich benannter eigener Entwurf.
Snapshot nie aus vermischter aktiver/Entwurfsbasis bilden.

Pflichthinweis: **„Der Export sichert deine Konfiguration, nicht die
Messwert-Historie.“** Er enthält auch aktuelle Katalogzuordnungen und
redaktionelle Kategorien/Räume, aber keine Laufzeitbeweise, Sichtungen,
Commands, Baselines, Fristen, Installationsidentität, Tokens, App-Optionen,
DB-/MQTT-Zugangsdaten oder HA-Config-Entries. Desaster-Recovery benötigt
zusätzlich das externe Datenbank-Backup und geschützte /data-Sicherung.

## Austauschformat v1 (Vorschlag)

```json
{"format":"wuschel.configuration","format_version":1,"scope":"configuration",
 "producer":{"name":"Wuschel","version":"1.0.0a10"},
 "config":{},"editorial":[],
 "catalog_contents":[],
 "manifest":{"roots":[],"object_digests":{},"config_digest":"…","payload_digest":"…"}}
```

Dies ist ein Strukturbeispiel, keine gültige leere Registry.
`scope=configuration|contract`. `config` ist ein vollständiges validierbares
Registry-Dokument bzw. dessen abgeschlossene Teilregistry im unveränderten
deklarierten Schema 1/2/3. `editorial` referenziert stabile Objektart/ID,
Kategorie und Raum. `catalog_contents` enthält je referenzierter verwalteter
Definition einen logisch vollständigen aktuellen Inhaltssnapshot samt
Definitionsdigest; Quellrevision ist Provenienz, keine Zielrevision.
Bei veränderlichen/dynamischen Lookupschlüsseln wird der gesamte zugehörige
Katalog mitgenommen, damit kein späterer gültiger Schlüssel fehlt.

Die Payload-Prüfsumme umfasst kanonisch config, editorial, catalog_contents,
scope und roots; sie schließt sich selbst und optionale Exportzeit aus.
Prüfsumme belegt Integrität/Konsistenz, keine Authentizität oder Kennung.
Importer validiert Struktur/Semantik unabhängig von behaupteten Hashes.
Ein Export ist ein Datenformat, führt keinen Code und keine URL-Nachladung aus.

Server erzeugt den Export unter einem gemeinsamen konsistenten DB-Snapshot
von Registry, Editorial und Kataloghead. Entwurf verlangt konkrete draft_id,
draft_version, erwartete aktive Basis sowie aktuelle Editorial-/Kataloggeneration.
Änderung während Aufbau: konflikthaft neu lesen, keine zusammengesetzten
Teilstände aus verschiedenen Revisionen. Geprüfte Ausgabe wird vollständig
gebaut, bevor der Download startet; Fehler darf keine scheinbar gültige
abgeschnittene Datei liefern. Vorgeschlagene Grenze 50 MiB/100.000 Katalogeinträge;
Überschreitung sichtbar melden, keine Teilmenge als Ganzsicherung bezeichnen.

## Referenzabschluss eines Vertrags

Start beim gewählten Vertrag; per Besuchsmenge rekursiv einschließen:

- alle referenzierten vorgelagerten Verträge/Felder;
- unmittelbar und transitiv benötigte Sources und ihre Verknüpfungen;
- Abhängigkeiten, Source-Monitore, Liveness-/Sensorreferenzen, Clock-/
  Kalender-/manuelle Quellen samt deklarierter Gültigkeitskonfiguration;
- Vorlagen mit genau benötigter Typ-/Definitionsversion, Formeln,
  Wertschema-/Enum-Wertelisten, Inline-Maps und verwaltete Katalogdefinitionen
  einschließlich aller benötigten Inhalte/Master/Varianten;
- Refresh-Trigger/-Ziele/Stop-Verträge und referenzierte deklarierte
  Kontextproducer, soweit für die ausgewählten Objekte erforderlich;
- Kategorien und Räume aller eingeschlossenen Verträge/Vorlagen.

Gebaute integrierte Typen werden als erforderliche Capability/Version
ausgewiesen; ausführbarer Python-Code wird niemals exportiert.
Fehlende Capability am Ziel = klare Ablehnung vor Übernahme.
Keine unbeteiligten Downstream-Verträge in den Abschluss aufnehmen.
Global erforderliche Konfigurationsblöcke werden explizit genannt; beim
Einzelvertragsimport gelten bestehende lokale Benachrichtigungs- und
Aufbewahrungsregeln weiter. Ihre Überschreibung wird nicht aus einem
Teilpaket abgeleitet. Auf leerem Ziel müssen fehlende globale Pflichtangaben
im geführten Entwurf ergänzt werden; bis dahin keine gültige Übernahme behaupten.

Abschluss wird durch den gleichen Backend-Validator gegen eine leere
Zielregistry (plus deklarierte globale Pflichtblöcke) geprüft; jede offene
Referenz macht den Export ungültig. UI zeigt warum, statt eine defekte
„portable“ Datei herunterzuladen. Zyklen/inkonsistente Referenzen abweisen.

HA-Entity-IDs/MQTT-Topics dürfen als Konfigurationsadressen enthalten sein,
keine Credentials. Auf anderer Installation sind sie möglicherweise
unpassend: Vorschau zeigt „Verknüpfungen auf diesem System prüfen“ und einen
geführten Zielabgleich. Neue Hardwareadressen werden über Formulare bestätigt.
Kein Import schreibt Home-Assistant-Konfiguration oder schaltet Geräte.

## Einlesen, Konflikte und atomare Übernahme

1. Datei lokal auswählen; serverseitig Grenzen, UTF-8, striktes JSON
   (keine doppelten Schlüssel/NaN/Infinity), Formatversion/Hashes prüfen.
   Keine ZIP-/Pfad-/Netzwerkverarbeitung.
2. Vorschau zeigt Umfang, Herkunft, hinzugefügte/wiederverwendete/abweichende
   Objekte, Kategorien/Räume, Katalogänderungen und nötige Fähigkeiten.
   Ganze Konfiguration erzeugt einen neuen Ersatzentwurf; Einzelvertrag
   ergänzt einen konkret geöffneten eigenen Entwurf.
3. Gleiche Identität+gleicher semantischer Inhalt wird wiederverwendet.
   Abweichende ID-/Typversion-/Katalogdefinition ist ein Konflikt, nie stilles
   Überschreiben. Auswahl „Vorhandenes behalten“ oder „Als neues Objekt
   einlesen“; notwendige IDs werden über eine geprüfte Abbildung in **allen**
   Referenzen umgeschrieben und erneut vollständig validiert.
   Unveränderliche Typ-ID/Version mit anderem Inhalt darf nicht ersetzt werden.
4. Importplan bindet Dateidigest, draft_id/version, aktive Basis,
   Editorialversionen und Katalogheads. Keine anderen Entwürfe überschreiben.
   Änderungen nach Vorschau = 409 und neue Vorschau.
5. Konfiguration, Editorialänderungen und geplante Katalogeinträge werden
   zusammen im Entwurf gestaged. Bestehende aktive Inhalte bleiben erhalten.
   Verwerfen entfernt nur Staging. Kein sofortiger Katalogpflegepfad durch
   Dateiimport; dessen direkte Runtimewirkung aus 0025 gilt nur expliziter Pflege.
6. Normales Prüfen → Auswirkungen → Übernehmen. Eine Transaktion aktiviert
   Registry, neue Katalogrevisionen, gewählte Editorialdaten und konsistente
   Laufzeitauswertung/Publication. Scheitern eines Teils übernimmt nichts.
   A-06 nur für semantisch Betroffenes; redaktionelle Änderungen allein
   erzeugen keine neue Baseline. Keine alten Zeitstempel als aktuelle Evidence.

Importanfrage per UUID+Payload-Digest wiederholsicher: verlorene Antwort führt
zum gleichen Plan/Ergebnis, keine doppelten Verträge/Katalogrevisionen.
Revisionen aus der Datei werden auf neue lokale Revisionen abgebildet;
keine Ersetzung vorhandener Auditgeschichte durch Fremd-IDs.

## Kategorien/Räume gemäß ADR 0020

Sie sind im Paket enthalten und werden eingelesen, bleiben aber außerhalb der
fachlichen Registry-Prüfsumme und der Semantik-Fingerprints.
Neue Objekte übernehmen die Angaben atomar mit ihrem Entwurf.
Bei bestehenden Objekten bleibt die aktuelle redaktionelle Zuordnung
standardmäßig erhalten; Vorschau bietet ausdrücklich „Angaben aus Datei
verwenden“ mit expected_editorial_version. Benni sieht beide Stände.
Fehlender Editorialblock, etwa in Alpha 9, bedeutet **erhalten**, niemals löschen.
Rücknahme einer Fachkonfiguration und historische Entwürfe ändern diese Regel nicht.

Freie Raumnamen bleiben freie Namen. HA-area_id ist portabler Hinweis, keine
garantierte Zielidentität: am Ziel über Formular zuordnen oder als bestätigten
freien Namen behalten. Keine geratenen Raumzuordnungen aufgrund ähnlicher Namen.
Unbekannte Symbole verwenden den bestehenden lokalen Fallback.

## Mimir 1.0.0a9 lesen

Im tatsächlichen Alpha-9-Code existiert ein Roh-Registry-Export sowie ein
Parser für `{config,display_name}`. Daher werden genau diese Varianten
unter config_schema_version 1/2 als Altformat erkannt und im unveränderten
Schema validiert. Keine erfundene ältere Paketstruktur.
Benni muss keine alte Datei bereitstellen, um den Parser synthetisch zu testen.

Vorschau: „Älteres Konfigurationsformat erkannt. Kategorien, Räume und
Katalogzuordnungen sind in dieser Datei nicht enthalten.“ Fehlende getrennte
Angaben am Ziel erhalten. Vorhandene Inline-Maps aus dem Dokument sind natürlich
mit enthalten und werden nicht als verwaltete Titelzuordnungen umgedeutet.
Ungültiges/mischformatiges Dokument, unbekannte Format-/Schemaversion oder
fehlende benötigte Capability wird mit konkretem Grund abgelehnt.
Keine silent best-effort-Migration oder Entfernung unbekannter Felder.

## A2-Nachweise

Ganzkonfiguration und Einzelvertrag auf leerem/in befülltem Ziel, transitive
Abhängigkeiten/Monitore/Formeln/Maps, dynamischer Katalogabschluss,
Kategorien/Räume und freie/entfernte HA-Bereiche, stabile Roundtrips,
keine Runtime-/Secret-Felder, Snapshotrace, Definition-/ID-Konflikte,
vollständiges Remapping, Entwurfswechsel/OCC, atomarer Rollback,
Importwiederholung, a9 raw/wrapper, unbekannte Version/ungültige Werte,
Größenlimit und defekte JSON-Dokumente. Oberfläche ohne JSON bedienbar,
genau ein Menü, alte Links erreichbar, geforderter Firefox-Nachweis.
