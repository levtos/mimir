# ADR 0020 — Kategorien und Raum ohne Wirkung auf Vertragslogik

18.10.2026 · **A2 freigegeben: Claude (Technik), Benni (Texte), 18.10.2026.** Benni zieht diesen
redaktionellen Teil aus Alpha 10 nach Alpha 9 vor. Grundlage: APP-01, M30-03/A-06,
M30-30, Matrix §5/§6 (Abgrenzung G4), [ADR 0006](0006-instance-parameters.md).

## Ziel und Modell

Verträge und Vorlagen bekommen genau eine Kategorie; jeder Vertrag optional
einen Raum. Beides dient Finden/Ordnen. Keine Routing-, Prioritäts-, Raumklima-
oder Zonenauswertung, keine Consumer-Profile. Bestehende React-Oberfläche bleibt
in diesem Auftrag bestehen; keine Frameworkmigration. Die sechs von Benni
verlangten MDI-Kategoriesymbole sind lokal gebündelte Metadaten-Glyphen, keine
zweite allgemeine Komponenten-/Icon-Bibliothek oder CDN-Abhängigkeit.

| stabile Kategorie | normaler Text | lokal gebündeltes Symbol |
|---|---|---|
| climate | Klima | mdi:thermometer |
| light_cover | Licht & Rollos | mdi:lightbulb |
| presence | Anwesenheit | mdi:account-check |
| sleep_wake | Schlaf & Wecken | mdi:sleep |
| media | Medien | mdi:play-circle |
| other | Sonstiges | mdi:shape |

Kein automatisches Raten aus Vertragskennung. Alte Objekte ohne Kategorie werden
als „Sonstiges“ angezeigt. Beim Anlegen wählbar; Vorschlag aus der ausgewählten
Vorlage, danach unabhängig. Vorlagenkategorie gehört zur stabilen Vorlagenidentität,
nicht zur Formel-Kategorie G6. Sie ändert keine Vorlagenversion.

## Datenformat und Speichergrenze

```json
{"object":{"kind":"contract","id":"example.value"},"editorial_version":3,
 "category":"climate","room":{"mode":"manual","area_id":null,
 "name":"Arbeitszimmer","icon":"mdi:desk"}}
```

Redaktionelle Daten liegen in eigener, versionierter Metadatenhaltung außerhalb
des kanonischen Registry-Dokuments. So ändern Kategorie/Raum **weder** dessen
gespeicherte Prüfsumme **noch** den Semantik-Fingerprint. Vollständiger fachlicher
Restore, Baselines, Fristen und Episoden werden nicht neu gestartet. Eine
Metadatenprüfung/-version zur Konkurrenzkontrolle ist kein neuer Fach-Fingerprint.
Audit protokolliert Vorher/Nachher separat. Backup/Restore, Zurücksetzen auf eine
frühere Konfiguration und Entwurf aus einer früheren Konfiguration behalten die
aktuellen Kategorien und Räume. Die Konfigurationsoperationen dürfen den eigenen
redaktionellen Speicher weder leeren noch mit älteren Angaben überschreiben.
Ein vollständiges Desaster-Recovery sichert den redaktionellen Speicher separat;
beim Einspielen eines älteren Fachstands bleiben neuere redaktionelle Angaben
erhalten. Export/Import nimmt Kategorien/Räume erst in Alpha 10 mit (Folgeauftrag
in #24). Pflichtregression: aktueller Raum/Kategorie bleibt beim Zurücksetzen
und beim Entwurf aus einer früheren Konfiguration unverändert.

Bei neuen Objekten im Entwurf sind Metadaten an draft_id/draft_version gebunden;
erst erfolgreiche Übernahme macht sie gemeinsam mit dem Objekt sichtbar.
Verwerfen löscht nur diesen Entwurfsstand. Bestehende redaktionelle Angaben
können über „Speichern“ ohne neue Fachkonfiguration geändert werden, mit
`expected_editorial_version`; Konflikte dürfen nichts überschreiben.
Gemischte Übernahme ist atomar: schlägt die Fachvalidierung fehl, keine teilweise
übernommenen Metadaten. Die Runtime bewertet bei reiner Metadatenänderung nichts neu.
Dies ist keine Umsetzung von G4s Katalogpflege oder eines Import-/Export-Neuentwurfs.

## Raumvorschlag aus HA

Neue lesende Protokoll-2-Metadatenabfrage in Bifröst liefert ausgewählte
Entity-/Device-Bereichszuordnung, Bereichsname und Bereichssymbol; keine Werte,
Nutzer oder Adressen. Entity-Bereich vor Gerätebereich. Ein eindeutiger Bereich
aller unmittelbar verknüpften HA-Quellen ergibt einen Vorschlag. Mehrere Räume,
fehlende Bereiche oder rein abgeleitete Eingänge ergeben keine erfundene Zuordnung;
Anzeige „Raum auswählen“. Keine Suche durch beliebig lange Vertragsgraphen.

`room.mode = suggested | manual | none`: Vorschlag vor Speichern sichtbar bestätigen;
manuell gewählter Raum wird bei HA-Umbenennung/Reconnect nicht überschrieben.
Bestätigter HA-Bereich behält ID, aktualisierter Anzeigename wird als redaktionelle
Änderung verarbeitet. Entfernte Bereiche bleiben als bisheriger Name mit Hinweis
sichtbar, keine verdeckte Umordnung. Freier eigener Raumname und bewusst „Kein Raum“
sind möglich. MDI-Pfade stammen aus einem vollständig lokal mitgelieferten,
fest gepinnten und lizenzierten MDI-Satz; Bereichssymbole daraus werden bei Bedarf
lokal geladen. Die sechs Kategoriepfade können im kleinen Hauptbundle liegen.
Unbekannter Iconname außerhalb dieses Satzes → lokales Haussymbol; niemals eine
URL oder ein SVG-Dokument aus HA ausführen. Dateigröße/Ladezeit in A2 prüfen.

## Oberfläche, Tests, betroffene Akte

„Meine Verträge“ und Vorlagen: Kategorie-Filter und Gruppierung; Vertragsliste
zusätzlich Raumfilter/-gruppierung. Leere Gruppen nicht anzeigen, „Sonstiges“/
„Kein Raum“ bleiben erreichbar. Kategorie beim Anlegen; Raumvorschlag am Vertrag
mit manueller Auswahl. Symbol und Text zusammen, Farbe nie alleinige Bedeutung.

A2-Tests: alle Kategorien, Vorschlag/Handänderung/none, mehrere Bereiche,
fehlende/entfernte Bereiche, HA-Ausfall, unbekanntes Symbol/kein Netzabruf,
Filter/Gruppen, Draft-Verwerfen/OCC/Atomarität/Backup. Pflichtregression:
nur Kategorie/Raum ändern → Registry-Prüfsumme und alle Semantik-Fingerprints
unverändert; keine Evaluation, Flanke, neue Frist, Episode oder Sitzung.
Betroffen: §9.2/§10/§12/§21/§23 der Build-Spezifikation, Metadaten-API/-Migration,
Bifröst-Erkennung, Draft/Übernahme, Vorlagen-/Vertragsformulare und Listen.

## Umsetzung Alpha 9

Migration 006 legt `editorial_current` und `editorial_draft` separat an. Die
administrative API `GET/PUT editorial` verwendet `expected_editorial_version`.
Bei neuen Objekten trägt `registry/drafts` die Angaben im zusätzlichen Feld
`editorial`; das Feld wird nie Teil des Registry-Dokuments. Eine fehlgeschlagene
Validierung übernimmt auch keine Angaben. Zurücksetzen und historische Entwürfe
lesen diesen Speicher nicht zurück; Recovery behält neuere Angaben je Objekt.
Ein vollständiges Datenbank-Backup muss diese beiden Tabellen einschließen.

Die Bereiche stammen aus der begrenzten, lesenden HA-Bereichsabfrage. Sie enthält
auch leere Bereiche. Nur eine erfolgreiche vollständige Abfrage kann einen
Bereich als entfernt markieren; Ausfall oder fehlende Rechte ändern keine Räume.
Die Quellzuordnung samt Symbol liefert Bifröst. Freie Namen und ausdrücklich
gewählte HA-Bereiche bleiben manuell; nur bestätigte Vorschläge folgen einer
Umbenennung.

Der gepinnte MDI-Satz 7.4.47 (Apache-2.0) wird durch
`frontend/scripts/generate-mdi.mjs` reproduzierbar in 64 lokale Teile aufgeteilt:
7 447 Pfade, zusammen 2 741 249 Bytes JSON, größter Teil 54 368 Bytes. Die sechs
Kategorien und das Haussymbol benötigen anfänglich nur 991 Bytes Pfaddaten.
Bereichssymbole werden über lokale dynamische Imports geladen; unbekannte Namen
und URLs verwenden das Haussymbol. Unit-Test prüft den lokalen Abruf ohne `fetch`.
