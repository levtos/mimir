# ADR 0027 — verständliche App-Optionen, MQTT-Hinweis und Alpha-10-Texte

20.10.2026 · Soll durch Benni entschieden; Umsetzungsvorschlag **A1 / Review**.
Grundlage: [ADR 0021](0021-plain-ui-retention-readiness.md), #24 und
Bennis Befund „MQTT ausgeschaltet“.

## Ursache und sicherer Statusvertrag

`mimir/config.yaml` setzt mqtt_mode standardmäßig auf disabled.
`MQTTAdapter.run` wartet bei disabled dauerhaft, bevor er Credentials lädt.
Eingetragene Zugangsdaten aktivieren MQTT deshalb nicht; das ist erwartetes
Modusverhalten. Bennis genannter Optionsstand ist die Befundquelle:
A1 hat **keine** laufenden App-Optionen abgefragt.

Neue sichere Statusfelder: `mqtt_mode` und
`mqtt_external_settings_present:boolean`. Letzteres wird serverintern aus
nichtleerem mqtt_host, mqtt_username oder mqtt_password berechnet.
Keine Werte, Länge, Teilzeichen, Hashes oder maskierten Kopien zurückgeben.
Default-Port/TLS allein zählen nicht als Zugangsdaten.
Ein unbekannter Optionszustand liefert null/„Noch nicht prüfbar“, kein false.
Die UI liest ausschließlich diesen dedizierten Statusvertrag.

Bei disabled + Einstellungen vorhanden unter Einstellungen → Verbindungen:
„MQTT ist ausgeschaltet. Du hast Verbindungsdaten eingetragen; sie werden
erst verwendet, wenn du den MQTT-Modus auf ‚Eigener Broker‘ stellst.“
Ergänzung: „Für die Mosquitto-App in Home Assistant wählst du ‚Home Assistant‘.
Die Zugangsdaten werden dann automatisch übernommen.“
Kein automatischer Moduswechsel, Verbindungsversuch oder Öffnen von Optionen
durch diese Anzeige. Bei supervisor vorhandene externe Daten nicht verwenden.

## Alle 19 App-Optionen

In A2: `wuschel/translations/de.yaml` und `en.yaml`.
Jeder Schemaschlüssel bekommt name und description in beiden Sprachen;
automatischer Schlüsselabgleich gegen schema/options.
Werte und technische Enum-Codes bleiben unverändert, verständliche
Bezeichnungen stehen in der Hilfe. Passwörter behalten Typ password.

| Schlüssel | Deutscher Name | Deutsche Beschreibung | English name / description |
|---|---|---|---|
| postgres_host | Datenbank-Host | Zertifizierter Hostname deiner PostgreSQL-Datenbank. Er muss zum Zertifikat passen. | Database host / Certified PostgreSQL hostname; must match the certificate. |
| postgres_port | Datenbank-Port | Port deiner PostgreSQL-Datenbank, normalerweise 5432. | Database port / PostgreSQL port, usually 5432. |
| postgres_database | Datenbankname | Name der eigenen Wuschel-Datenbank. | Database name / Name of the dedicated Wuschel database. |
| postgres_user | Datenbank-Benutzer | Eigene Rolle für Wuschel, ohne Administratorrechte. | Database user / Dedicated Wuschel role without administrator privileges. |
| postgres_password | Datenbank-Passwort | Passwort der Wuschel-Rolle. Gib es hier selbst ein und teile es nicht in Nachweisen. | Database password / Enter the Wuschel role password here; never include it in evidence. |
| postgres_sslmode | Datenbank-Verschlüsselung | verify-full prüft Verschlüsselung, Zertifikat und Hostnamen. require prüft den Hostnamen nicht; disable schaltet TLS aus. Für deinen Betrieb gilt verify-full. | Database TLS mode / verify-full verifies TLS, certificate and hostname; require skips hostname verification; disable turns TLS off. Use verify-full for this installation. |
| postgres_ca | Datenbank-Zertifikat | Pfad zur öffentlichen CA-Datei unter /ssl, mit der Wuschel den Datenbankserver prüft. Kein privater Schlüssel. | Database CA certificate / Path to the public CA file under /ssl used to verify the server. Never a private key. |
| installation_label | Name dieser Installation | Freier Anzeigename, damit du deine Installation erkennst. Keine technische Kennung. | Installation label / A display name to recognize this installation, not its identifier. |
| initialize_empty_database | Leere Datenbank erstmalig einrichten | Nur für den ersten Start mit neuer leerer Datenbank einschalten. Danach wieder ausschalten. | Initialize empty database / Enable only for the first start with a new empty database, then disable. |
| adopt_installation_id | Vorhandene Installationskennung übernehmen | Nur für einen ausdrücklich geplanten Wiederherstellungsfall. Bei der neuen Wuschel-Installation leer lassen. | Adopt installation ID / Only for an explicitly planned recovery. Leave empty for a new Wuschel installation. |
| mqtt_mode | MQTT-Modus | disabled = ausgeschaltet; supervisor = Mosquitto-App in Home Assistant, Zugangsdaten automatisch; external = eigener Broker mit den folgenden Daten. | MQTT mode / disabled = off; supervisor = Home Assistant Mosquitto app with automatic credentials; external = your own broker using the fields below. |
| mqtt_host | MQTT-Host | Hostname deines eigenen Brokers; nur bei external verwendet. | MQTT host / Hostname of your own broker; used only in external mode. |
| mqtt_port | MQTT-Port | Port deines eigenen Brokers; nur bei external verwendet. | MQTT port / Port of your own broker; used only in external mode. |
| mqtt_username | MQTT-Benutzer | Benutzer deines eigenen Brokers; nur bei external verwendet. | MQTT username / Username for your own broker; used only in external mode. |
| mqtt_password | MQTT-Passwort | Passwort deines eigenen Brokers; nur bei external verwendet. | MQTT password / Password for your own broker; used only in external mode. |
| mqtt_tls | MQTT verschlüsseln | TLS für deinen eigenen Broker einschalten. Der Hostname muss zum Zertifikat passen. | MQTT TLS / Enable TLS for your own broker; its hostname must match the certificate. |
| mqtt_ca | MQTT-Zertifikat | Optionaler Pfad zur öffentlichen CA-Datei deines Brokers; kein privater Schlüssel. | MQTT CA certificate / Optional path to your broker's public CA file, never a private key. |
| log_level | Umfang des Protokolls | INFO für den normalen Betrieb; DEBUG nur gezielt zur Fehlersuche. Zugangsdaten werden nie protokolliert. | Log level / Use INFO normally and DEBUG only for focused diagnostics. Credentials are never logged. |
| log_format | Format des Protokolls | text ist gut lesbar; json ist für die technische Auswertung gedacht. | Log format / text is human readable; json is intended for technical processing. |

Übersetzungsformat gemäß
[HA-App-Übersetzungen](https://developers.home-assistant.io/docs/apps/presentation/#translations):
configuration.<key>.name/description. In A2 mit Supervisor-Schema und Packaging
prüfen, damit Dateien auch im App-Build/Store ankommen.

## Verbindliche Text- und Bedienkorrekturen in A2

- `fields.new_episode` / `fields.ends_episode`: „Durchlauf“ statt „Episode“;
  alle zusammengesetzten Sätze grammatisch anpassen, technische Feldnamen erhalten.
- `validation.version_retired`: „Verknüpfung“ statt „Bindung“, keine neue Semantik.
- Vertragsliste: Suchfeld, Kategorie, Raum, Ein/Aus in dieser Reihenfolge;
  letzter Filter heißt „Verträge“ mit „Alle / Eingeschaltet / Ausgeschaltet“.
  Sichtbare Feldbeschriftung und zugänglicher Name; Reset als Nebenaktion.
- Übersicht: Schnellaktionen ohne zweites „Änderungen übernehmen“.
  Die gemeinsame Entwurfs-/Übernahmeaktion bleibt eindeutig; keine zweite
  globale Hauptaktion im Schnellaktionsbereich.
- Versionen/Entwürfe: Prüfsummenbereich „Technische Details“ mit Satz:
  **„Die Prüfsumme ist ein Fingerabdruck dieses Stands. Damit lassen sich zwei
  Stände vergleichen. Sie ist keine Kennung.“**
- „Erweitert“ bleibt nur dort, wo du eine eigene Kennung eingeben kannst.
  Andere reine technische Offenlegungen heißen „Technische Details“;
  normale fachliche Pflichtfelder bleiben außerhalb.

Jede neue/geänderte Seite einschließlich leerer Zustände:
Titel, ein konkreter Satz „Hier kannst du …“, genau ein Hauptknopf oben rechts.
Deutsch, Du-Form, fachlich nutzbar ohne JSON. Keine Framework-/Designsystemmigration;
die ausdrückliche Alpha-9-Ausnahme für die bestehende React-Oberfläche bleibt.
Mähnenfarben sind Identität, Statusfarben bleiben semantisch.

## Sicherheits- und Testpflicht

Keine Tools/Endpunkte, die Supervisor-App-Details samt Optionen liefern;
auch kein Abholen mit anschließender Redaktion im Modell. Dedizierte sichere
Projektion an der Quelle verwenden oder auf den Befund verzichten.
Passwortdateien auf LXC niemals ausgeben/committen/protokollieren.

A2: Schemaassertion postgres_password=mqtt_password=password, vollständige
19-Schlüssel-Übersetzung in de/en, Names/Descriptions nicht leer,
disabled mit/ohne externe Daten, supervisor ignoriert externe Daten,
external benutzt sie, Statusserialisierung enthält nur die erlaubten Felder.
Sentinel-Geheimnisse dürfen in keiner API-Antwort, Logzeile, Exception,
Diagnose oder Exportdatei auftauchen. Kein echter Credentialwert als Fixture.
Text-/a11y-Tests, i18n-Scan 0 einschließlich alter sichtbarer Produktnamen,
Firefox-Nachweis Verbindungen mit Hinweis und Versionen mit Technische Details.
B: Benni wählt den Modus, sichere Statusseite zeigt verbunden, eine ausdrücklich
benannte synthetische Testquelle liefert über ein Topic einen Wert.
Credentialeingabe allein gilt nicht als MQTT-Abnahme.
