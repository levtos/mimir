# ADR 0021 — Bedienung, Aufbewahrung und vollständige Bereitschaft

18.10.2026 · **A2 freigegeben: Claude (Technik), Benni (Texte), 18.10.2026.**
Grundlage: Alpha-9-Auftrag, G14/F1/F2, M30-01/M30-17/M30-30,
[ADR 0009](0009-prerelease-version-gate.md), [Textreview](../alpha9/TEXTE.md).
Kein Oberflächenumbau oder Versionswechsel in A1.

## Ziel und Modell

Eine Person ohne App-Erfahrung kann jede Fähigkeit über Formulare bedienen.
Technische Kennungen und Rohdaten sind zusätzlich unter „Erweitert“ erreichbar,
keine Voraussetzung für Anlegen, Prüfen oder Übernehmen. Vorhandene Import-/Export-
Funktionen werden verständlich beschriftet; ihr fachlicher Ausbau bleibt Alpha 10.
Die Seitenregel gilt einschließlich Einstellungsseiten und leerer Ansichten:
Titel, ein konkreter Satz beginnend mit „Hier kannst du …“, genau ein Hauptknopf
oben rechts. Nebenaktionen bleiben untergeordnet oder im Aktionsmenü; Dialoge
haben ihre eigene eindeutige Bestätigung. Keine zweite globale Hauptaktion aus
Kopfzeile und Seiteninhalt. Die vorhandene Entwurfsleiste bleibt gemeinsame
Arbeitsleiste; auf einer Übernahmeseite verweist sie auf dieselbe Hauptaktion.

## Aufbewahrungsformular

Neue Seite `/settings/retention`, Menü „Aufbewahrung“. Daten bleiben im bestehenden
`history_retention` der Konfiguration; keine zweite Live-Konfiguration.

```json
{"history_retention":{"raw_days":7,"rollup_days":730,"batch_size":1000,"interval_s":3600}}
```

Das bestehende Schema erlaubt raw_days 1–3650, rollup_days 1–36500,
batch_size 1–10000 (Vorgabe 1000), interval_s 60–86400 (Vorgabe 3600).
Vorschlagswerte 7/730 sind durch Benni benannt, keine automatische
Migration. Formularfelder: „Einzelmessungen aufbewahren (Tage)“, „Stundenwerte
aufbewahren (Tage)“. Erklärung unterscheidet einzelne Messungen von verdichteten
Stundenwerten. Positive ganze Tage und `Stundenwerte ≥ Einzelmessungen`; Backend
prüft erneut. `batch_size` und `interval_s` nur unter Erweitert. Die Defaultwerte
dieser technischen Felder werden sichtbar aus dem bestehenden Schema übernommen.

„Im Entwurf speichern“ verändert nur den geöffneten Entwurf; ohne Entwurf wird
der bekannte Anlegedialog geöffnet. Danach Prüfen → Übernehmen mit Auswirkungen
auf Löschung/Verdichtung und Warnung vor nicht rückholbaren entfernten Messungen.
Kein Datenlöschen durch Vorschau oder Öffnen der Seite, kein Setzen einer Regel
bei Installation/Update. Rückkehr zur aktiven Regel/Entwurfswechsel sind eindeutig
beschriftet und gegen fremde Entwurfsstände abgesichert.

## Alle offenen Bedingungen von Anfang an

Die App liefert eine vollständige Liste `conditions:[{code,satisfied,details?}]`;
die UI übersetzt Codes und ordnet feste interne Links zu. Keine HTML- oder
frei gelieferten URLs in Fehlerdetails. Fehlende aktive Konfiguration **und**
fehlende aktive Aufbewahrung werden gleichzeitig ausgewiesen. Eine Regel nur im
Entwurf erfüllt die Betriebsbedingung noch nicht. Datenbank-/HA-/Konfigurations-
und Überlastbedingungen werden unabhängig geprüft, soweit belegbar. Eine wegen
DB-Ausfall nicht prüfbare Bedingung heißt „Noch nicht prüfbar“, niemals erfüllt.

Beispiele mit festen Sprungzielen: „Noch keine Konfiguration“ → Entwürfe;
„Aufbewahrung fehlt“ → Aufbewahrung; „Datenbank nicht erreichbar“ → Verbindungen;
„HA-Anbindung fehlt“ → Verbindungen. Die Plakette zählt alle offenen Bedingungen,
zeigt sie verständlich im Dialog und bietet einen primären Link zum ersten
lösbaren Punkt. Bereitschaft ist Betriebsvoraussetzung; Vertrags-/Wertqualität
und Konfigurationsvollständigkeit bleiben eigene Achsen. Keine künstliche
fachliche Störung nur wegen leerer Ersteinrichtung.

## Kopf, Programmversion und leere Zustände

Kopf zeigt „Konfiguration {n}“ oder „Noch keine Konfiguration“. Eine
Vorlagenversion bleibt „Version“, der Gesamtstand heißt „Konfiguration“.
Einstellungen → System zeigt „Mimir 1.0.0a9 (Alpha 9)“ aus echten Programmmetadaten;
Versionskonstante nicht im Frontend abschreiben. Bifröst meldet seine tatsächliche
Manifestversion; Transportprotokoll ist davon getrennt und nur unter Erweitert.
Übersicht ohne Vollständigkeitsprobleme: „Zurzeit nichts unvollständig“.

## Tests und betroffene Stellen

A2: alle Seiten/Leerstände mit Titel, Hier-kannst-du-Satz und genau einer primären
Headeraktion; Tastatur/zugängliche Namen, kein JSON-Zwang; bestätigte Texte und
Platzhalter unverändert. Aufbewahrung: 7/730-Vorschlag ohne Save, Relation/Grenzen,
Entwurfswechsel, Prüfen/Übernehmen/Fehler/Zurücksetzen, keine direkte Runtime-
Änderung. Bereitschaft: mehrere gleichzeitige Bedingungen ohne aktive Konfiguration,
unbekannte Bedingung, feste Links, Entwurf reicht nicht, Wiederverbindung. Kopf/
Programm-/Bridgeversion, leere Übersicht. Firefox 1568×710 in A2 für die im Auftrag
benannten Flächen; A1 erzeugt keine neuen UI-Bilder oder Produktnachweise.
Betroffen: Build-Spezifikation §7/§12/§21/§23, Readiness-API, Shell/Status,
Aufbewahrungsformular und de.json. Alte Release-Artefakte werden nicht verändert.

## Umsetzung Alpha 9

`service_state.conditions` nennt die Voraussetzungen einzeln mit `satisfied:
true | false | null`: App-Optionen, Datenbank, aktive Konfiguration, aktive
Aufbewahrung, erster HA-Stand, HA-Anbindung, Bestätigung des letzten Stands und
Aufnahmekapazität. `null` kennzeichnet noch nicht prüfbare Punkte. Historische
Überlaufzähler beweisen keine aktuelle Überlast. Die bisherigen `reasons` und
das Bereitschaftsmodell bleiben für bestehende Clients lesbar; die fehlende
Aufbewahrung wird auch vor der ersten Konfiguration unabhängig ausgewiesen.
Die Oberfläche nennt auch jede noch nicht prüfbare Voraussetzung einzeln.
Unbekannte nicht erfüllte Codes gelten ebenfalls nicht als erfüllt. Sprungziele
sind ausschließlich feste interne Routen.

Die Aufbewahrungsseite öffnet ohne Arbeitsentwurf den vorhandenen Anlegedialog.
Die vorgeschlagenen Werte bleiben bis zum ausdrücklichen Speichern unverbindlich.
Speichern erhält vorhandene technische Einstellungen und alle übrigen Teile des
Entwurfs. Konflikt- und Eigentumsprüfung verwenden dieselbe Arbeitsdokument-Grenze
wie andere Entwurfsänderungen. Die Übernahme erklärt den möglichen endgültigen
Verlust älterer Messungen. Der normale Systembereich zeigt Programmversion und
offene Bedingungen; Zähler, Zeitmessungen und Protokollangaben stehen unter
„Erweitert“. Die Stufe wird aus dem tatsächlichen Versionssuffix abgeleitet.
