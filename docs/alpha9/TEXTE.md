# Alpha 9 — Textvorschläge zur Durchsicht durch Benni

18.10.2026 · Basis: main/tag v1.0.0a8, Commit `6fcde2a83def3e5cde93d3dea46638d755cbf1e6`.
**A1, noch nicht freigegeben.** Diese Datei ändert keine laufende Beschriftung.
Erst nach Bennis Durchsicht werden bestätigte Texte in A2 umgesetzt. Auch die
Löschliste ist bis dahin ein Vorschlag; de.json bleibt in A1 bytegleich.

## Lesereihenfolge und Umfang

Zuerst die Pflichtänderungen und Seitenregel prüfen, dann die Änderungstabelle.
Das vollständige Verzeichnis am Ende erfasst jeden der **2250 Schlüssel** aus
de.json, einschließlich **1855 unterschiedlicher Ausgangstexte**. Gleichlautende
Texte wurden gemeinsam sprachlich geprüft; jede Verwendung bleibt einzeln aufgeführt.
„Unverändert“ ist eine ausdrückliche Beibehaltung, kein ausgelassener Eintrag.
Die Orte stammen aus produktivem Quellcode einschließlich dynamischer Namensräume;
Tests/Beispiele gelten nicht als erreichbare Oberfläche. Dies ist eine Quelltextprüfung,
kein vorweggenommener Bedien- oder Browsernachweis.

Tabellen sind **Änderungsvorschläge**, keine Anweisung zum blinden Ersetzen von
Teilstrings. Zusammengesetzte Sätze werden in A2 zu vollständigen Nachrichten mit
benannten Platzhaltern und Einzahl/Mehrzahl zusammengeführt. Sichtbare Inhalte aus
Namen/Notizen des Benutzers werden nicht übersetzt oder umgeschrieben. Fachliche
Kennungen können unter „Erweitert“ unverändert gezeigt werden.

## Wörterbuch und Grenze zu technischen Angaben

Normal: Vertrag, Vorlage, Entwurf, Übernehmen, Version, Zurücksetzen,
Konfiguration, Quelle, Verknüpfung, Aktualität, Nachweis, Bereitschaft,
Zusammenführung, Berechnung, Ablauf, HA-Anbindung. `du`, `dein`, `dir` klein.
„Konfiguration“ bezeichnet den übernommenen Gesamtstand; „Version“ eine konkrete
Vorlagen-/Berechnungsfassung, „Programmversion“ die installierte Software.

Keine normalen Labels wie Live, Binding, Persistenz, Fingerprint, Lifecycle,
Adapter, Operator, Queue oder Snapshot. Die nötigen Fähigkeiten bleiben vollständig
über deutsch beschriftete Formulare verfügbar. Präzise technische Rohangaben,
Protokollnummern, Prüfsummen, Request-/Context-IDs und JSON gehören unter „Erweitert“.
„Eingang“ wird bei Regelbearbeitung mit Quelle/Vertrag und Name erklärt; keine
Gerätekennung als einzige Beschriftung. Nutzer müssen kein JSON eingeben.

## Pflichtänderungen für die Freigabe

| Schlüssel / Ort | alt | neu | Grund |
|---|---|---|---|
| alpha7.overview.whatCanIDo / Übersicht | Was kann ich tun? | Details | Kurze eindeutige Aktion. |
| alpha7.mode.live / Ansichtsschalter | Live ansehen | Aktueller Stand | Deutscher Begriff. |
| alpha7.nav.dependencies / Menü | Abhängigkeiten (Erweitert) | Abhängigkeiten | Kein Klammerzusatz; technische Inhalte im Bereich Erweitert. |
| alpha7.nav.diagnostics / Menü | Experten-Diagnose | Erweitert | Keine Rolle oder Fachkenntnis voraussetzen. |
| alpha7.status.version / Kopf | Version {count} | Konfiguration {count} | Gesamtstand von Vorlagen- und Programmversion trennen. |
| NEU alpha9.header.noConfiguration / Kopf | Version – | Noch keine Konfiguration | Leere Installation erklären. |
| System / Erklärsatz | Bereitschaft (kann der Dienst auswerten?) ist etwas anderes als die Qualität einzelner Werte. | Diese Punkte müssen erfüllt sein, damit Mimir deine Verträge auswerten kann. | Direkte Bedeutung statt Modellvergleich. |
| System / Grundanzeige | Persistenz | Verbindung zur Datenbank | Verständliche Ursache. |
| System / technische Messgrößen | Speicherung-Dauer, Eingang-Überläufe, Aktualisierung-Überläufe | Zeit zum Speichern, Nicht verarbeitete Eingangsmeldungen, Nicht ausgeführte Aktualisierungsanfragen | Nur unter Erweitert anzeigen. |
| features.registry.DraftPage.fingerprint_version_e46d72 / Erweitert | Version der Berechnungskennung | Verfahren der Prüfsumme | Technische Angabe klar benennen und aus Normalansicht fernhalten. |
| Auswirkungsprüfung / Gesamtstand | vollständiger Stand – Nach dem Übernehmen erhalten 0 Verträge die neue Versionsnummer. | Du übernimmst eine Konfiguration ohne Verträge. | Eigener Leerfall; keine technische Versionsbehauptung. |
| Auswirkungsprüfung / sonst | Nach dem Übernehmen erhalten {n} Verträge die neue Versionsnummer. | Nach dem Übernehmen gilt die neue Konfiguration für {n} Verträge. | Kein Versprechen geänderter Fachlogik für jeden Vertrag. |
| Ereignisse / Zusatz | Verbindungswechsel zu Home Assistant werden seit dem Öffnen dieser Browser-Sitzung angezeigt. | Hier stehen Verbindungsänderungen, seit du Mimir geöffnet hast. | Zeitlichen Umfang ohne Browserbegriff erklären. |
| editors.RegistryObjects.eingange_bindung_an_quellen_und_andere_contracts_c3d83b / Vertragsformular | Eingänge (Bindung an Quellen und andere Verträge) | Verknüpfung | Bennis Wörterbuch. |
| repository.yaml:name / App-Store | Core Contracts Platform | Mimir | In Alpha 9 vorgezogen; A1 ändert die Datei noch nicht. |
| Übersicht / leerer Vollständigkeitsbereich | leer | Zurzeit nichts unvollständig | Bestätigten Leerzustand zeigen; Lade-/Fehlerzustand bleibt getrennt. |

## Seitenregel: Ist-Abweichungen und vorgeschlagener Kopf

Die Ziele gelten auch bei leerem Inhalt und in der Entwurfsansicht. „Im Entwurf
speichern“ ist eine lokale Formularaktion und kein zweites globales Übernehmen.
Gibt es mehrere nötige Schritte, öffnet ein Hauptknopf den passenden geführten
Ablauf. Dialoge behalten ihren eigenen Bestätigungsknopf. Sekundäraktionen sind
im Aktionsmenü oder neutralen Links erreichbar; kein Löschen als Hauptknopf.

| Seite / Route | Abweichung in a8 | Titel · Hier-kannst-du-Satz | genau ein Hauptknopf oben rechts |
|---|---|---|---|
| / | Erklärung beginnt anders; Hauptknöpfe im Schnellaktionen-Panel, abhängig vom Entwurf mehrere | Übersicht · Hier kannst du deine Verträge, offene Probleme und letzte Änderungen ansehen. | Neuer Vertrag |
| /contracts/list/all | Erklärung beginnt anders; Hauptknopf vorhanden | Meine Verträge · Hier kannst du deine Verträge finden, ordnen und neue anlegen. | Neuer Vertrag |
| /contracts/view/:id | Beschreibung ist Kennung; Diagnose/Entfernen statt Hauptknopf | Vertragsname · Hier kannst du den Wert, den Verlauf und die Einstellungen dieses Vertrags ansehen. | Vertrag bearbeiten; im Bearbeiten-Modus: Im Entwurf speichern |
| /contracts/import/json | Erklärung beginnt anders; Einleseaktion nur im Inhalt | Vertrag importieren · Hier kannst du eine gespeicherte Konfiguration einlesen und vor dem Übernehmen prüfen. | Datei oder Text einlesen |
| /contracts/relations/graph | Erklärung beginnt anders; kein Hauptknopf im Kopf | Zusammenhänge · Hier kannst du sehen, welche Quellen und Verträge miteinander verknüpft sind. | Ansicht zurücksetzen |
| /templates/own | Erklärung beginnt anders | Eigene Vorlagen · Hier kannst du eigene Vorlagen finden und ihre Berechnung festlegen. | Neue Vorlage |
| /templates/built-in | kein Hauptknopf; gleiche generische Beschreibung | Eingebaute Vorlagen · Hier kannst du die mitgelieferten Vorlagen ansehen und für einen Vertrag auswählen. | Vertrag anlegen (öffnet Vorlagenauswahl) |
| /templates/details/:id/:version | Kennung als Titel, Versionsdaten als Beschreibung; mehrere Nebenknöpfe | Vorlagenname · Hier kannst du diese Vorlagenversion ansehen und eine neue Version vorbereiten. | Neue Version; beim neuen bearbeitbaren Stand: Im Entwurf speichern |
| /sources/devices | Erklärung fehlt | Quellen · Hier kannst du Geräte verbinden oder manuelle Angaben als Quelle anlegen. | Quelle hinzufügen (geführte Auswahl: Gerät, Kalender, manuell) |
| /sources/bindings | Erklärung und Hauptknopf fehlen; Sammlungsaktion im Inhalt | Verknüpfungen · Hier kannst du festlegen, woher eine Quelle ihre Werte erhält. | Verknüpfung hinzufügen |
| /sources/catalogs | Erklärung und Hauptknopf fehlen | Wertelisten · Hier kannst du erlaubte Werte und ihre Zuordnung festlegen. | Werteliste hinzufügen |
| /sources/dependencies | Erklärung und Hauptknopf fehlen | Abhängigkeiten · Hier kannst du festlegen, welche Verbindung eine Quelle braucht. | Verbindung hinzufügen |
| /changes/drafts | Erklärung beginnt anders; Neuer Entwurf im Inhalt und im Leerzustand zusätzlich hervorgehoben | Entwürfe · Hier kannst du Änderungen sammeln, öffnen und prüfen, bevor sie gelten. | Neuer Entwurf |
| /changes/drafts/:id | Metadaten statt Erklärsatz; Dateiexport im Kopf, Prüfen/Übernehmen verteilt | Entwurfsname · Hier kannst du deinen Entwurf prüfen und die Änderungen übernehmen. | Prüfen; nach unverändert erfolgreicher Prüfung: Übernehmen |
| /changes/versions | Erklärung beginnt anders; Vergleich/Zurücksetzen im Inhalt | Konfigurationen · Hier kannst du frühere Konfigurationen vergleichen oder wieder übernehmen. | Konfigurationen vergleichen (Auswahldialog, nicht stilles Zurücksetzen) |
| /changes/transfer | Erklärung beginnt anders; mehrere Inhaltsaktionen | Import & Export · Hier kannst du eine Konfiguration sichern oder eine gespeicherte Datei einlesen. | Konfiguration sichern; Einlesen als Nebenaktion, keine neue Importfunktion |
| /settings/system | Erklärung und Hauptknopf fehlen | System · Hier kannst du sehen, ob Mimir arbeiten kann und welche Voraussetzungen noch fehlen. | Offene Punkte ansehen (zeigt die vollständige Liste; auch leer sinnvoll) |
| /settings/installation | Erklärung und Hauptknopf fehlen; Assistent im Inhalt | Einrichtung · Hier kannst du die Einrichtung von Mimir prüfen und fortsetzen. | Einrichtung öffnen |
| /settings/connections | Erklärung und Hauptknopf fehlen | Verbindungen · Hier kannst du die Datenbankverbindung und die HA-Anbindung prüfen. | Verbindungen prüfen (nur lesend) |
| /settings/keys | Erklärung und Hauptknopf fehlen; sensible Aktion im Panel | Zugangsschlüssel · Hier kannst du die Zugänge zu Mimir verwalten. | Zugang auswählen (Erneuern erst im bestätigten Dialog) |
| /settings/log | Erklärung und Hauptknopf fehlen | Protokoll · Hier kannst du nachsehen, welche Änderungen Mimir gespeichert hat. | Neu laden |
| /settings/diagnostics | Erklärung beginnt anders; kein Hauptknopf | Erweitert · Hier kannst du Nachweise, Berechnungen und frühere Zustände genauer prüfen. | Vertrag auswählen |
| Ersteinrichtung, Schritte 1–5 | gemeinsamer Titel, wechselnde Untertitel; Weiter/Zurück im Inhalt | Mimir einrichten · Hier kannst du Mimir Schritt für Schritt mit deinen Daten verbinden. | kontextabhängig Weiter / Verbindung prüfen / Einrichtung abschließen; Zurück sekundär |
| Lade- und Fehlerseite | Titel, aber kein einheitlicher Erklärsatz/Hauptknopf | Mimir · Hier kannst du nach dem Laden mit deiner Einrichtung fortfahren. | Erneut versuchen; während Laden deaktiviert mit Erklärung |
| NEU /settings/retention | fehlt | Aufbewahrung · Hier kannst du festlegen, wie lange Mimir Messwerte aufbewahrt. | Im Entwurf speichern |
| NEU /settings/notifications | fehlt | Benachrichtigungen · Hier kannst du festlegen, welche Hinweise Mimir in Home Assistant zeigt. | Im Entwurf speichern |
| NEU manuelle Quelle / Eingabe | fehlt | Name der Quelle · Hier kannst du eine eigene Angabe eintragen und ihre Gültigkeit festlegen. | Angabe eintragen |

Legacy-Routen leiten auf diese Ziele weiter; keine zweite Seitenregel pro Alias.
Filter, Kategorie und Raum erhalten verständliche leere Zustände. Für nur lesende
Benutzer bleibt die Hauptaktion sichtbar deaktiviert mit verständlichem Grund.

## Hinweise im Code und strukturelle Textprobleme

| Fundstelle | alt / Problem | neu / geplante Maßnahme | Grund |
|---|---|---|---|
| components/ContractLiveState.tsx, Nachweis-Absatz | Wortfragmente und Pluralsuffix `en`; daraus entstehen grammatisch falsche neue Sätze | Ganze Nachrichten: „1 gespeicherter Nachweis“ / „{count} gespeicherte Nachweise“ und Link „Nachweise ansehen“ | Nicht mit Teilübersetzungen oder Suffixen zusammensetzen. |
| features/registry/ActivationDialogs.tsx / DiffView.tsx | Konfigurationsnummer, Anzahl und Satzfragmente werden getrennt zusammengesetzt | Vollständige Einzahl-/Mehrzahl-/Nullnachrichten mit benannten Platzhaltern | Gerade der Nullfall darf keine neue Fachversion behaupten. |
| features/contracts/DefinitionDetailPage.tsx | typeId als Titel, Fachkennungen in der Normalansicht | Anzeigename als Titel; Kennung nur Erweitert | Ohne App-Erfahrung verständlich. |
| features/admin/AdminPage.tsx, ReadinessPanel | technische Einzelwerte neben unvollständiger Bereitschaft | Vollständige verständliche Bedingungen mit Links; Queue/Dauer/Überläufe unter Erweitert | Alltagssprache und konkrete nächste Schritte. |
| components/ReadinessBadge.tsx und lib/status.ts | Gründe können nach erstem Fehler verdeckt bleiben; fehlende Aufbewahrung ohne aktive Konfiguration nicht vollständig sichtbar | Alle offenen und noch nicht prüfbaren Bedingungen getrennt aufführen | Keine falsche Bereitschaft; siehe ADR 0021. |
| features/overview/OverviewPage.tsx | Leerer Vollständigkeitsabschnitt ohne Bestätigung | „Zurzeit nichts unvollständig“ nur nach erfolgreichem Laden | Leere, ladende und fehlerhafte Anzeige nicht verwechseln. |
| editors/RegistryObjects.tsx / Formularlabels | technische Feldnamen als mögliche Auffangbeschriftung | Verständliche Bezeichnung aus Wörterbuch; technische Kennung unter Erweitert | Auch neue/seltene Felder ohne JSON bedienen. |
| lib/api.ts, i18n/codes.ts und API-Fehleranzeigen | unbekannte technische Meldung kann über eine generische Fehleranzeige weitergereicht werden | „Diese Einstellung konnte nicht verarbeitet werden. Prüfe die markierten Felder.“; technische Ursache nur Erweitert | Keine rohen Exceptions oder englischen Meldungen in normalen Formularen. |
| custom_components/bifrost/__init__.py | VERSION = 1.0.0a1, obwohl Manifest a8 | Manifestversion als einzige Quelle, Test Gleichheit; Programmanzeige Mimir/Bifröst getrennt von Protokoll | In A2 beheben, kein Ersetzen veröffentlichter a8-Artefakte. |
| repository.yaml:name | Core Contracts Platform | Mimir | Aus Alpha 10 vorgezogen. |

Kommentare, Typnamen, API-Schlüssel und technische Protokollwerte selbst sind
keine sichtbaren Texte. Sie werden nicht pauschal übersetzt. Ihre Darstellung
in der Normalansicht bekommt ausdrücklich eine deutsche Bezeichnung. Der
vorhandene i18n-Scan prüft harte Texte, nicht die Verständlichkeit vorhandener
Übersetzungen; beides bleibt in A2 getrennt nachzuweisen.

## Löschliste und Nachweis der Verwendung

Die vorhandene AST-Prüfung `node scripts/prune-i18n.mjs` liest produktive
Quelldateien und berücksichtigt dynamische Präfixe. Sie weist genau zwei sicher
unbenutzte Schlüssel aus:

- `editors.RegistryObjects.parameter_dd066e`
- `editors.RegistryObjects.deklarative_typen_haben_keine_instanzparameter_r_67dbe1`

Sie werden in A2 entfernt. Der zweite Text behauptet außerdem fälschlich, es gebe
keine Instanzparameter. `fields.parameters` bleibt als dynamisch verwendetes
Formularlabel erhalten und wird „Einstellungen“. Das Pluralsuffix
`components.ContractLiveState.en_dbd3a4` ist derzeit benutzt und darf erst nach
Umstellung auf ganze Sätze entfernt werden. Kein Löschen nur wegen fehlenden
wörtlichen Aufrufs; insbesondere codes.*, fields.* und collection.* sind dynamisch.

Die Zahlen und Orte beziehen sich auf a8. A2 prüft nach dem Umbau erneut auf
fehlende/unbenutzte Schlüssel, erhält Platzhalter oder ersetzt sie bewusst durch
vollständige Nachrichten und bestätigt alle neuen Seiten im echten Formularablauf.

## Änderungstabelle — 405 bestehende Schlüssel

| Schlüssel | Ort in der Oberfläche | alt | neu | Grund |
|---|---|---|---|---|
| post1.validation.sourceConflict | Gemeinsame Oberfläche / Wertanzeige | Quelle „{source}“: {field} war in Version {revision} „{oldValue}“ und soll jetzt „{newValue}“ sein. Lege für einen anderen Typ oder eine andere Einheit eine neue Quelle an. Eine Werteliste darfst du nur ergänzen. | Quelle „{source}“: {field} war in Konfiguration {revision} „{oldValue}“ und soll „{newValue}“ werden. Für eine andere Werteart oder Einheit brauchst du eine neue Quelle. Eine Werteliste darfst du ergänzen. | Übernommenen Gesamtstand von Vorlagen- und Programmversion unterscheiden. |
| alpha7.versions.explanation | Entwürfe und Konfigurationen | Hier findest du die bisher übernommenen Konfigurationen. Eine ältere Version kannst du prüfen und erneut übernehmen. | Hier kannst du frühere Konfigurationen ansehen, vergleichen und wieder übernehmen. | Übernommenen Gesamtstand von Vorlagen- und Programmversion unterscheiden. |
| alpha7.versions.affectedOne | Entwürfe und Konfigurationen | Nach dem Übernehmen erhält 1 Vertrag die neue Versionsnummer. | Nach dem Übernehmen gilt die neue Konfiguration für einen Vertrag. | Übernommenen Gesamtstand von Vorlagen- und Programmversion unterscheiden. |
| alpha7.evidence.help | Erweitert / Nachweise | Wähle eine Quelle. Die Tabelle zeigt ihre zuletzt gespeicherten Beobachtungen je Verknüpfung. Empfangszeit und Messzeit bleiben getrennt. | Wähle eine Quelle. Hier siehst du ihre gespeicherten Meldungen. Messzeit und Empfangszeit werden getrennt angezeigt. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| alpha7.evidence.advanced | Erweitert / Nachweise | Erweitert: einzelnen Nachweis über Referenz suchen | Erweitert: gespeicherten Nachweis suchen | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| alpha7.evidence.referenceHelp | Erweitert / Nachweise | Für einen bestimmten historischen Nachweis kannst du hier eine gespeicherte Referenz einsetzen. | Du kannst einen früher gespeicherten Nachweis über seine Kennung suchen. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| alpha7.evidence.enterReference | Erweitert / Nachweise | Setze zuerst eine Nachweis-Referenz ein. | Gib zuerst die Kennung des Nachweises ein. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| alpha7.graph.live | Zusammenhänge | Live | Aktueller Stand | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.graph.draftHelp | Zusammenhänge | Geplante Zusammenhänge. Der Entwurf wird noch nicht ausgewertet; deshalb werden keine Live-Farben zugemischt. | Hier siehst du die geplanten Verknüpfungen. Der Entwurf liefert noch keine aktuellen Werte. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.graph.liveHelp | Zusammenhänge | Laufende Konfiguration in Version {n}. Ziehe die Fläche, um weitere Zusammenhänge zu sehen. | Verknüpfungen der Konfiguration {n}. Ziehe die Fläche, um weitere Einträge zu sehen. | Übernommenen Gesamtstand von Vorlagen- und Programmversion unterscheiden. |
| alpha7.graph.searchFirst | Zusammenhänge | Gib zuerst den Namen eines Objekts ein. | Gib zuerst einen Namen in die Suche ein. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.graph.selectFirst | Zusammenhänge | Wähle einen Knoten, um seine Nachbarschaft einzuschränken. | Wähle einen Eintrag, um nur seine direkten Zusammenhänge zu sehen. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.versions.activePending | Entwürfe und Konfigurationen | Mimir prüft die aktive Version. Danach kannst du auf eine ältere Version zurücksetzen. | Mimir prüft die aktuelle Konfiguration. Danach kannst du einen früheren Stand wieder übernehmen. | Übernommenen Gesamtstand von Vorlagen- und Programmversion unterscheiden. |
| alpha7.versions.name | Entwürfe und Konfigurationen | Version {n} | Konfiguration {n} | Übernommenen Gesamtstand von Vorlagen- und Programmversion unterscheiden. |
| alpha7.versions.firstStart | Entwürfe und Konfigurationen | Diese Objekte sind neu. Sie beginnen nach dem Übernehmen zum ersten Mal; es geht kein bisheriger Verlauf verloren. | Diese Verträge kommen neu hinzu. Ihre Aufzeichnung beginnt nach dem Übernehmen. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.versions.affected | Entwürfe und Konfigurationen | Nach dem Übernehmen erhalten {n} Verträge die neue Versionsnummer. | Nach dem Übernehmen gilt die neue Konfiguration für {n} Verträge. | Übernommenen Gesamtstand von Vorlagen- und Programmversion unterscheiden. |
| alpha7.restart.target | Vertrag und Vorlage | „{name}“ beginnt im Zustand „{state}“ eine neue Episode. Geprüfte Konfiguration: Version {version}. | „{name}“ beginnt einen neuen Durchlauf im Zustand „{state}“. Geprüft wurde Konfiguration {version}. | Übernommenen Gesamtstand von Vorlagen- und Programmversion unterscheiden. |
| alpha7.restart.success | Vertrag und Vorlage | Der Ablauf wurde manuell neu gestartet. Eine neue Episode beginnt; die Bestätigung durch gültige Daten steht noch aus. | Der Ablauf wurde manuell neu gestartet. Ein neuer Durchlauf beginnt; gültige Daten müssen den Zustand noch bestätigen. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.move.templateAdvanced | Quellen und Verknüpfungen | Erweitert: Vorlage für diesen Vertrag | Vorlage für diesen Vertrag | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.move.samePathRemaining | Quellen und Verknüpfungen | Das bisherige Gerät wird noch gebraucht: Wähle alle betroffenen Verträge oder ein anderes Gerät. Verwendungen als Lebenszeichen oder Überwachung musst du zuerst umstellen. Eine Messung darf nicht doppelt zählen. | Das bisherige Gerät wird noch gebraucht. Wähle alle betroffenen Verträge oder ein anderes Gerät. Stelle zuerst Verwendungen als Lebenszeichen oder Verbindungsprüfung um. Dieselbe Messung darf nicht doppelt zählen. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.move.apply | Quellen und Verknüpfungen | In Entwurf übernehmen | Im Entwurf speichern | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.template.prefix | Vertrag und Vorlage | Mimir ergänzt bei Bedarf vertrag. vor deiner Kennung. Leer lassen, um die Kennung aus dem Namen zu bilden. | Mimir erstellt die Kennung aus dem Namen. Unter Erweitert kannst du eine eigene Kennung eingeben. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.device.applyPreset | Formular für Vorlage / Quelle / Vertrag | Aktualitätsvorlage anwenden | Vorgaben für die Aktualität verwenden | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.device.willCreate | Quellen und Verknüpfungen | Quelle, Abhängigkeit und Verknüpfung werden zusammen eingerichtet. Die Typumwandlung wird passend ergänzt. | Mimir richtet die Quelle, ihre Verknüpfung und die nötige Verbindungsprüfung gemeinsam ein. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.device.willCreateContract | Quellen und Verknüpfungen | Quelle, Abhängigkeit, Verknüpfung und ein Vertrag mit passender Vorlage werden zusammen angelegt. Du musst keine Fachkennung eingeben. | Mimir legt die Quelle, ihre Verknüpfung und einen passenden Vertrag gemeinsam an. Du brauchst keine technische Kennung einzugeben. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.device.sourceId | Quellen und Verknüpfungen | Eigene Quellenkennung (optional) | Eigene Quellenkennung (freiwillig) | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.device.contractId | Quellen und Verknüpfungen | Eigene Vertragskennung (optional) | Eigene Vertragskennung (freiwillig) | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.device.badIdentifier | Quellen und Verknüpfungen | Prüfe die Fachkennung unter Erweitert. Quellenkennungen beginnen mit source.; Vertragskennungen mit einem Buchstaben. | Prüfe die Kennungen unter Erweitert. Mimir kann sie aus dem Gerätenamen erstellen. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.device.existingTypeLocked | Quellen und Verknüpfungen | Typ und Einheit einer vorhandenen Quelle sind gesperrt. Nutze für eine andere Werteart den geführten Quellenumzug. | Werteart und Einheit einer vorhandenen Quelle sind gesperrt. Mit „Quelle umziehen“ kannst du eine passende neue Quelle anlegen. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.freshness.event_statefulHelp | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Der Wert bleibt gültig, bis das Gerät eine Änderung meldet; die Verbindung wird weiter geprüft. | Der Wert bleibt bis zur nächsten Änderung gültig. Ein Verbindungsabbruch macht ihn allein noch nicht ungültig. Für wichtige Sicherheitswerte brauchst du zusätzlich regelmäßige Lebenszeichen. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.contract.state.limitedHelp | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Der Server meldet fehlende oder eingeschränkte Angaben für diesen Vertrag. | Mimir hat für diesen Vertrag noch nicht alle benötigten Angaben. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.contract.state.healthyHelp | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Die benötigten Angaben sind vorhanden und der Server meldet einen gesunden Wert. | Alle benötigten Angaben sind vorhanden und verwendbar. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.contract.historyScope | Vertrag und Vorlage | Bis zu 60 zuletzt gespeicherte Änderungen der aktuellen Version. So werden unterschiedliche Einheiten nicht vermischt. Lücken bleiben sichtbar; ältere Versionen findest du in der Experten-Diagnose. | Hier siehst du bis zu 60 Änderungen aus der aktuellen Konfiguration. Lücken bleiben sichtbar. Frühere Konfigurationen findest du unter Erweitert. | Übernommenen Gesamtstand von Vorlagen- und Programmversion unterscheiden. |
| alpha7.contract.liveVersion | Vertrag und Vorlage | Laufender Wert aus Version {version} · gemeldet am {time} | Wert aus Konfiguration {version} · gemeldet am {time} | Übernommenen Gesamtstand von Vorlagen- und Programmversion unterscheiden. |
| alpha7.overview.explanation | Übersicht | Deine Verträge und die wichtigsten Änderungen auf einen Blick. | Hier kannst du deine Verträge, offene Probleme und letzte Änderungen ansehen. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.overview.whatCanIDo | Übersicht | Was kann ich tun? | Details | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.overview.thisSession | Übersicht | in dieser Sitzung | seit dem Öffnen von Mimir | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.overview.connectionScope | Übersicht | Verbindungswechsel zu Home Assistant werden seit dem Öffnen dieser Browser-Sitzung angezeigt. | Hier stehen Verbindungsänderungen, seit du Mimir geöffnet hast. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.mode.live | Entwurf und Bearbeitung | Live ansehen | Aktueller Stand | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.status.version | Kopfleiste / offene Bedingungen | Version {count} | Konfiguration {count} | Übernommenen Gesamtstand von Vorlagen- und Programmversion unterscheiden. |
| alpha7.status.publication | Kopfleiste / offene Bedingungen → Erweitert | Der zuletzt gespeicherte Stand wurde noch nicht bestätigt. | Die angezeigten Werte sind noch nicht mit dem gespeicherten Stand abgeglichen. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| alpha7.status.disconnected | Kopfleiste / offene Bedingungen | Die Live-Verbindung ist unterbrochen und gezeigt wird der letzte bekannte Stand. | Die Verbindung zu Mimir ist unterbrochen. Du siehst den letzten bekannten Stand. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.nav.dependencies | Menü | Abhängigkeiten (Erweitert) | Abhängigkeiten | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.nav.changes | Menü | Entwürfe &amp; Versionen | Entwürfe &amp; Konfigurationen | Übernommenen Gesamtstand von Vorlagen- und Programmversion unterscheiden. |
| alpha7.nav.versions | Menü; Entwürfe und Konfigurationen | Versionen | Konfigurationen | Übernommenen Gesamtstand von Vorlagen- und Programmversion unterscheiden. |
| alpha7.nav.transfer | Menü; Entwürfe und Konfigurationen | Import/Export | Import &amp; Export | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.nav.system | Menü; Einstellungen | Systemstatus | System | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.nav.installation | Menü | Installation &amp; Einrichtung | Einrichtung | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.nav.diagnostics | Menü | Experten-Diagnose | Erweitert | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.contract.choose | Vertrag und Vorlage | Wähle einen Vertrag. Hier siehst du seinen Wert, die Erklärung und den Verlauf. | Hier kannst du einen Vertrag auswählen und seinen Wert, seine Erklärung und seinen Verlauf ansehen. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.draft.explanation | Entwürfe und Konfigurationen | Ein Entwurf sammelt Änderungen. Sie gelten erst nach Übernehmen. | Hier kannst du Änderungen als Entwurf sammeln. Sie gelten erst, wenn du ihn übernimmst. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.import.explanation | Entwürfe und Konfigurationen | Lade eine Datei oder füge den Import-Text ein. Du prüfst die Änderungen, bevor sie gelten. | Hier kannst du eine gespeicherte Konfiguration einlesen. Du prüfst sie, bevor du sie übernimmst. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.import.file | Entwürfe und Konfigurationen | Datei auswählen (JSON) | Datei auswählen | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.import.text | Entwürfe und Konfigurationen | Oder Import-Text einfügen (JSON) | Oder gespeicherten Text einfügen | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.import.name | Entwürfe und Konfigurationen | Entwurfsname (optional) | Name des Entwurfs (freiwillig) | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| components.ContractLiveState.die_live_verbindung_ist_unterbrochen_oder_synchr_6baea2 | Gemeinsame Oberfläche / Wertanzeige | Die Verbindung zur App ist unterbrochen oder synchronisiert; gezeigt wird der letzte bekannte Stand. | Die Verbindung zu Mimir wird wiederhergestellt. Du siehst den letzten bekannten Stand. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| components.ContractLiveState.veroffentlicht_16f085 | Gemeinsame Oberfläche / Wertanzeige | Veröffentlicht | Bereitgestellt | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| components.ContractLiveState.publication_15fc65 | Gemeinsame Oberfläche / Wertanzeige → Erweitert | Veröffentlichung | Bereitstellung der Werte | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| components.ContractLiveState.revision_2e516d | Gemeinsame Oberfläche / Wertanzeige | Version | Konfiguration | Übernommenen Gesamtstand von Vorlagen- und Programmversion unterscheiden. |
| components.ContractLiveState.status_qualitat_und_grunde_stammen_unverandert_v_dd46c4 | Gemeinsame Oberfläche / Wertanzeige | Status, Qualität und Gründe stammen unverändert von der App. | Mimir liefert für jeden Wert den Zustand, die Verwendbarkeit und die Ursachen. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| components.ContractLiveState.gehalten_bis_c18ae5 | Gemeinsame Oberfläche / Wertanzeige | Gehalten bis | Letzter Wert verwendbar bis | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| components.ContractLiveState.evidenz_referenz_2c494f | Gemeinsame Oberfläche / Wertanzeige | Nachweis-Referenz | Kennung des Nachweises | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| components.MachineRecovery.der_bisherige_zustand_kann_nicht_sicher_wiederhe_687282 | Gemeinsame Oberfläche / Wertanzeige | Der bisherige Zustand kann nicht sicher wiederhergestellt werden. Ein Neustart wartet auf eine erfüllte Bedingung mit gültigen Nachweisen. | Der bisherige Ablaufzustand ist nicht sicher bekannt. Mimir wartet auf gültige Angaben für einen neuen Start. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| components.MachineRecovery.die_neustart_bedingung_muss_auf_gultige_eingange_9c2c15 | Gemeinsame Oberfläche / Wertanzeige | Die Neustart-Bedingung muss auf gültige Eingänge verweisen. Ohne Nachweis bleibt der Ablauf unbekannt. | Für einen neuen Start brauchst du eine Bedingung mit gültigen Eingängen. Bis dahin bleibt der Zustand unbekannt. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| components.MasterDetail.ohne_id_3527bd | Gemeinsame Oberfläche / Wertanzeige | (ohne ID) | Ohne Kennung | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| components.MasterDetail.v0_editor_fe0bb3 | Gemeinsame Oberfläche / Wertanzeige | {v0}-Editor | {v0} bearbeiten | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| components.PanelLayout.funktionspanels_82acad | Anordnung der Seitenbereiche | Funktionspanels | Seitenbereiche | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| components.PanelLayout.standardlayout_wiederhergestellt_6a6783 | Anordnung der Seitenbereiche | Standardlayout wiederhergestellt. | Die ursprüngliche Anordnung wurde wiederhergestellt. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| components.PanelLayout.panels_am_griff_ziehen_oder_mit_den_pfeiltasten__f2377c | Anordnung der Seitenbereiche | Panels am Griff ziehen oder mit den Pfeiltasten am Griff verschieben. Die Breite lässt sich separat wählen. | Ziehe einen Bereich am Griff oder verschiebe ihn dort mit den Pfeiltasten. Die Breite kannst du getrennt wählen. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| components.PanelLayout.panel_v0_verschieben_ee4a83 | Anordnung der Seitenbereiche | Panel {v0} verschieben | Bereich {v0} verschieben | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| components.PanelLayout.v0_panelbreite_116978 | Anordnung der Seitenbereiche | {v0}: Panelbreite | {v0}: Breite des Bereichs | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| components.RouteError.ein_unerwarteter_fehler_ist_aufgetreten_die_date_95b04b | Gemeinsame Oberfläche / Wertanzeige | Ein unerwarteter Fehler ist aufgetreten. Die Daten auf dem App sind nicht betroffen. | Ein unerwarteter Fehler ist aufgetreten. Deine gespeicherten Daten sind nicht betroffen. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.common.wert_enter_a30cc4 | Formular für Vorlage / Quelle / Vertrag | Wert + Enter | Wert eingeben und Eingabetaste drücken | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.common.wahr_167f97 | Formular für Vorlage / Quelle / Vertrag | wahr | Ja | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.common.falsch_b3c3e0 | Formular für Vorlage / Quelle / Vertrag | falsch | Nein | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.common.zeitpunkt_mit_zeitzone_rfc_3339_z_b_2026_01_01t1_ccb975 | Formular für Vorlage / Quelle / Vertrag | Zeitpunkt mit Zeitzone (RFC 3339), z. B. 2026-01-01T12:00:00+00:00 | Datum und Uhrzeit mit Zeitzone | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.DefinitionEditor.typ_id_b7db41 | Formular für Vorlage / Quelle / Vertrag | Typ-ID | Vorlagenkennung | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.DefinitionEditor.logikanderungen_neue_version_28d5cf | Formular für Vorlage / Quelle / Vertrag | Logikänderungen = neue Version | Andere Berechnung benötigt neue Version | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.DefinitionEditor.sprachversion_4adccf | Formular für Vorlage / Quelle / Vertrag | Sprachversion | Format der Vorlage | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.DefinitionEditor.anzeigename_redaktionell_44433b | Formular für Vorlage / Quelle / Vertrag | Anzeigename (redaktionell) | Anzeigename | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.DefinitionEditor.beschreibung_redaktionell_d5700f | Formular für Vorlage / Quelle / Vertrag | Beschreibung (redaktionell) | Beschreibung | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.DefinitionEditor.refresh_eingange_f326cb | Formular für Vorlage / Quelle / Vertrag | Aktualisierung-Eingänge | Erneut abfragbare Eingänge | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.DefinitionEditor.deklarierte_ha_eingange_die_nach_einem_commit_ne_ab47d2 | Formular für Vorlage / Quelle / Vertrag | Deklarierte HA-Eingänge, die nach einer Speicherung neu angefordert werden dürfen. | Hier wählst du Eingänge, die Mimir ausdrücklich erneut abfragen darf. Eine Anfrage ist noch kein neuer Messwert. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.DefinitionEditor.typisierte_eingange_1ca67c | Formular für Vorlage / Quelle / Vertrag | Typisierte Eingänge | Eingänge und ihre Wertearten | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.DefinitionEditor.interne_zwischenausdrucke_55311a | Formular für Vorlage / Quelle / Vertrag | Interne Zwischenausdrücke | Wiederverwendbare Rechenschritte | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.DefinitionEditor.benannte_regeln_werden_pro_auswertung_einmal_ber_2306fc | Formular für Vorlage / Quelle / Vertrag | Benannte Regeln werden pro Auswertung einmal berechnet und können über „Interne Regel (Verweis)“ mehrfach verwendet werden. Zyklen werden von der App abgelehnt. | Ein benannter Rechenschritt kann mehrfach verwendet werden. Mimir berechnet ihn je Auswertung nur einmal. Verweise im Kreis sind nicht erlaubt. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.DefinitionEditor.diese_definition_hat_keine_state_machine_eine_ma_eb27c0 | Formular für Vorlage / Quelle / Vertrag | Diese Vorlage hat keinen Ablauf. Ein Ablauf bringt Zustände, Episoden, Sitzungen, eine Frist und Befehle mit. Ein Ausgabefeld muss ihn über „Zustand des Ablaufs“ verwenden. | Ein Ablauf beschreibt Zustände und deren Wechsel. Du kannst Fristen und erlaubte Befehle ergänzen. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.DefinitionEditor.json_experte_99d21a | Formular für Vorlage / Quelle / Vertrag | JSON (Experte) | Erweitert: Daten als JSON | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.DefinitionEditor.optionale_expertenansicht_derselben_daten_ungult_e2b8d0 | Formular für Vorlage / Quelle / Vertrag | Optionale Expertenansicht derselben Daten. Ungültiges JSON wird nicht übernommen; alle Änderungen erscheinen sofort in den Formularen. | Zusätzliche Textansicht derselben Daten. Du kannst alle Einstellungen auch über die Formulare bearbeiten. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.DefinitionEditor.aktivierte_version_semantisch_unveranderlich_8bfc17 | Formular für Vorlage / Quelle / Vertrag | Aktivierte Version – semantisch unveränderlich | Übernommene Vorlagenversion | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.DefinitionEditor.redaktionelle_felder_name_beschreibung_bleiben_a_a99fa7 | Formular für Vorlage / Quelle / Vertrag | Redaktionelle Felder (Name, Beschreibung) bleiben änderbar. Für Logikänderungen eine neue Version anlegen. | Name und Beschreibung bleiben änderbar. Für eine andere Berechnung legst du eine neue Version an. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.DefinitionEditor.diese_version_war_bereits_aktiv_und_ist_semantis_b868d2 | Formular für Vorlage / Quelle / Vertrag | Diese Version war bereits aktiv und ist semantisch unveränderlich. | Diese Vorlagenversion wurde bereits übernommen. Für eine andere Berechnung brauchst du eine neue Version. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.Extras.v0_dem_schema_unbekannt_erhalten_beffb5 | Formular für Vorlage / Quelle / Vertrag | {v0} (dem Schema unbekannt, erhalten) | {v0} (zusätzliche Angabe, bleibt erhalten) | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.MachineEditor.maschinen_id_bdfa88 | Formular für Vorlage / Quelle / Vertrag | Maschinen-ID | Kennung des Ablaufs | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.MachineEditor.ein_befehl_fordert_eine_benannte_transition_an_d_878ba3 | Formular für Vorlage / Quelle / Vertrag | Ein Befehl fordert eine benannte Übergang an; der Bedingung entscheidet. Es gibt kein direktes Setzen von Zuständen. | Ein Befehl fragt einen erlaubten Zustandswechsel an. Der Ablauf prüft seine Bedingungen, bevor er wechselt. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.MachineEditor.typisierte_argumente_a38ea4 | Formular für Vorlage / Quelle / Vertrag | Typisierte Argumente | Angaben zum Befehl | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.MachineEditor.zustandsloser_ausdruck_zeitliche_wahrheiten_als__a67920 | Formular für Vorlage / Quelle / Vertrag | Zustandsloser Ausdruck. Zeitliche Wahrheiten als Vertrag-Eingang einspeisen. | Die Bedingung prüft die vorhandenen Eingänge. Eine Wartezeit richtest du in einem eigenen Vertrag ein. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.MachineEditor.pro_quellzustand_und_ereignis_ist_genau_eine_tra_5c73e8 | Formular für Vorlage / Quelle / Vertrag | Pro Quellzustand und Ereignis ist genau eine Übergang zulässig. Die Reihenfolge ändert keine Alternativen. | Für denselben Zustand und Auslöser darf nur ein passender Wechsel festgelegt sein. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.MachineEditor.deadline_dfc8ae | Formular für Vorlage / Quelle / Vertrag | deadline | Frist abgelaufen | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.MachineEditor.input_eingangsanderung_eec32a | Formular für Vorlage / Quelle / Vertrag | input (Eingangsänderung) | Eingang geändert | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.MachineEditor.beginnt_neue_episode_aa43cc | Formular für Vorlage / Quelle / Vertrag | Beginnt neue Episode | Neuen Durchlauf beginnen | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.MachineEditor.beendet_episode_92986e | Formular für Vorlage / Quelle / Vertrag | Beendet Episode | Durchlauf beenden | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.MachineEditor.guard_zustandslos_96238a | Formular für Vorlage / Quelle / Vertrag | Bedingung (zustandslos) | Bedingung | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.dependency_id_62578d | Formular für Vorlage / Quelle / Vertrag | Abhängigkeit-ID | Kennung der Verbindung | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.source_id_a3a484 | Formular für Vorlage / Quelle / Vertrag | Quelle-ID | Quellenkennung | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.z_b_local_f170b9 | Formular für Vorlage / Quelle / Vertrag | z. B. local | Zum Beispiel: diese Installation | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.physischer_schlussel_36a2c7 | Formular für Vorlage / Quelle / Vertrag | Physischer Schlüssel | Kennung der Messquelle | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.identitat_der_physischen_messung_verhindert_dopp_afdbad | Formular für Vorlage / Quelle / Vertrag | Identität der physischen Messung; verhindert doppelte Nachweis. | Diese Kennung verhindert, dass dieselbe Messung über mehrere Verbindungen doppelt zählt. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.zukunftstoleranz_s_a11f48 | Formular für Vorlage / Quelle / Vertrag | Zukunftstoleranz (s) | Erlaubte Abweichung einer zukünftigen Messzeit (Sekunden) | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.liveness_quelle_66259e | Formular für Vorlage / Quelle / Vertrag | Erreichbarkeitsquelle * | Quelle für das Lebenszeichen * | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.eigenes_wertschema_deklarieren_value_schema_82fd15 | Formular für Vorlage / Quelle / Vertrag | Eigenes Wertschema deklarieren | Werteart festlegen | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.quellen_der_typen_boolean_numeric_text_haben_ihr_e970bc | Formular für Vorlage / Quelle / Vertrag | Zahl-, Ja/Nein- und Textquellen legen ihren Eingangstyp fest. Andere Quellen benötigen ein Wertschema, bevor sie einen typisierten Eingang speisen. | Lege fest, welche Werte diese Quelle liefern darf. Mimir prüft damit, ob sie zum gewählten Eingang passt. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.binding_id_45ba45 | Formular für Vorlage / Quelle / Vertrag | Verknüpfung-ID | Kennung der Verknüpfung | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.adapter_0252b8 | Formular für Vorlage / Quelle / Vertrag | Adapter | Art der Verbindung | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.ha_entitat_96b970 | Formular für Vorlage / Quelle / Vertrag | HA-Entität * | Gerät oder Wert in Home Assistant * | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.auswahl_uber_die_schreibgeschutzte_ha_erkennung__c0d877 | Formular für Vorlage / Quelle / Vertrag | Auswahl über die schreibgeschützte HA-Erkennung oder direkte Eingabe. | Wähle einen Eintrag aus Home Assistant. Unter Erweitert kannst du seine Kennung eingeben. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.ha_entitat_auswahlen_bed2ae | Formular für Vorlage / Quelle / Vertrag | HA-Entität auswählen | Eintrag aus Home Assistant auswählen | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.topic_7b08c3 | Formular für Vorlage / Quelle / Vertrag; Quellen und Verknüpfungen | Topic * | MQTT-Kanal * | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.pfad_im_json_payload_5eecf1 | Formular für Vorlage / Quelle / Vertrag | Pfad im JSON-Nachricht | Stelle des Werts in der Nachricht | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.der_scheduler_ist_kein_quellen_adapter_und_wird__39b766 | Formular für Vorlage / Quelle / Vertrag | Der Scheduler ist kein Quellen-Adapter und wird von der App abgelehnt, sofern er als Verknüpfung verwendet wird. | Uhr und Kalender liefern Zeitwerte direkt aus Mimir. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.transformation_cf2a63 | Formular für Vorlage / Quelle / Vertrag; Quellen und Verknüpfungen | Transformation | Umwandlung | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.home_assistant_entitat_wahlen_6ad8d6 | Formular für Vorlage / Quelle / Vertrag | Home-Assistant-Entität wählen | Eintrag aus Home Assistant wählen | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.schreibgeschutzte_erkennung_es_werden_nur_kennun_776d6f | Formular für Vorlage / Quelle / Vertrag | Schreibgeschützte Erkennung: es werden nur Kennungen und Attributnamen gelesen, keine Werte; in Home Assistant wird nichts angelegt oder geändert. | Mimir liest die Einträge aus Home Assistant. Dabei wird dort nichts angelegt oder geändert. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.entitaten_durchsuchen_4437b8 | Formular für Vorlage / Quelle / Vertrag | Entitäten durchsuchen | Einträge durchsuchen | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.suchen_nach_name_oder_entity_id_61f175 | Formular für Vorlage / Quelle / Vertrag | Suchen nach Name oder Entitäts-ID … | Nach Namen oder Kennung suchen … | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.entitaten_werden_gelesen_c2b17f | Formular für Vorlage / Quelle / Vertrag | Entitäten werden gelesen … | Einträge werden geladen … | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.die_entitaten_id_kann_trotzdem_direkt_im_feld_ei_6ffc69 | Formular für Vorlage / Quelle / Vertrag | Die Entitäten-ID kann trotzdem direkt im Feld eingegeben werden. | Unter Erweitert kannst du die Kennung direkt eingeben. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.katalog_id_e6aea3 | Formular für Vorlage / Quelle / Vertrag | Wertelisten-ID | Kennung der Werteliste | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.schlussel_sind_die_rohwerte_der_quelle_als_text__256b6c | Formular für Vorlage / Quelle / Vertrag | Schlüssel sind die Rohwerte der Quelle als Text (z. B.  | Der ursprüngliche Wert der Quelle steht links, zum Beispiel  | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.werte_werden_per_map_ref_eingesetzt_1dbcfa | Formular für Vorlage / Quelle / Vertrag | ); Werte werden über eine Wertelisten-Zuordnung eingesetzt. | . Rechts wählst du den zugehörigen Wert aus. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.contract_id_f9f7ff | Formular für Vorlage / Quelle / Vertrag | Vertrag-ID | Vertragskennung | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.typ_version_1b7183 | Formular für Vorlage / Quelle / Vertrag | Typ &amp; Version | Vorlage und Version | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.dieser_typ_ist_weder_als_paket_typ_noch_als_defi_0b1092 | Formular für Vorlage / Quelle / Vertrag | Dieser Typ ist weder als Paket-Typ noch als Vorlage bekannt. | Die ausgewählte Vorlage wurde nicht gefunden. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.eingange_bindung_an_quellen_und_andere_contracts_c3d83b | Formular für Vorlage / Quelle / Vertrag | Eingänge (Bindung an Quellen und andere Verträge) | Verknüpfung | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.dieser_typ_deklariert_keine_eingange_8d0dc9 | Formular für Vorlage / Quelle / Vertrag | Dieser Typ deklariert keine Eingänge. | Diese Vorlage benötigt keine Eingänge. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.referenz_e13113 | Formular für Vorlage / Quelle / Vertrag | Referenz | Verknüpfter Wert | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.nicht_gebunden_4105e9 | Formular für Vorlage / Quelle / Vertrag | — nicht gebunden — | Noch nicht verknüpft | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.ungultige_oder_unbekannte_referenz_f8a620 | Formular für Vorlage / Quelle / Vertrag | (ungültige oder unbekannte Referenz) | Verknüpfung nicht gefunden oder ungültig | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.eingang_v0_ist_im_typ_nicht_deklariert_d04398 | Formular für Vorlage / Quelle / Vertrag | Eingang „{v0}“ ist im Typ nicht deklariert | Die Vorlage kennt den Eingang „{v0}“ nicht. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RegistryObjects.parameter_dd066e | Keine Oberfläche – unbenutzt | Parameter | — entfernen | Sicher unbenutzt; AST-Prüfung mit dynamischen Präfixen. |
| editors.RegistryObjects.deklarative_typen_haben_keine_instanzparameter_r_67dbe1 | Keine Oberfläche – unbenutzt | Deklarative Typen haben keine Vertragsparameter: Regelparameter gehören zur unveränderlichen Vorlagenversion. | — entfernen | Sicher unbenutzt; AST-Prüfung mit dynamischen Präfixen. |
| editors.RuleEditor.ruleenvprovider_fehlt_4c1afc | Formular für Vorlage / Quelle / Vertrag | RuleEnvProvider fehlt | Die Einstellungen für die Regel sind gerade nicht verfügbar. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RuleEditor.interne_regel_verweis | Formular für Vorlage / Quelle / Vertrag | Interne Regel (Verweis) | Benannten Rechenschritt verwenden | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RuleEditor.zuordnung_map_5ecf05 | Formular für Vorlage / Quelle / Vertrag | Zuordnung (Zuordnung) | Wert zuordnen | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RuleEditor.hysterese_bucket_688e48 | Formular für Vorlage / Quelle / Vertrag | Hysterese (Hysterese) | Schaltschwellen | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RuleEditor.zeitlich_temporal_542f27 | Formular für Vorlage / Quelle / Vertrag | Zeitlich (Zeitregel) | Zeitregel | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RuleEditor.operator_v0_e1f310 | Formular für Vorlage / Quelle / Vertrag | Operator{v0} | Rechenschritt{v0} | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RuleEditor.in_nicht_einpacken_f78273 | Formular für Vorlage / Quelle / Vertrag | In NICHT einpacken | Ergebnis umkehren | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RuleEditor.in_und_einpacken_ad37d5 | Formular für Vorlage / Quelle / Vertrag | In UND einpacken | Mit einer UND-Regel verbinden | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RuleEditor.in_oder_einpacken_6e76ab | Formular für Vorlage / Quelle / Vertrag | In ODER einpacken | Mit einer ODER-Regel verbinden | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RuleEditor.knoten_duplizieren_json_in_zwischenablage_060036 | Formular für Vorlage / Quelle / Vertrag | Knoten duplizieren (JSON in Zwischenablage) | Rechenschritt kopieren | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RuleEditor.ausdruck_fehlt_oder_ist_ungultig_427904 | Formular für Vorlage / Quelle / Vertrag | Ausdruck fehlt oder ist ungültig. | Die Regel fehlt oder ist ungültig. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RuleEditor.dieser_name_ist_in_der_definition_nicht_als_eing_bd4b8c | Formular für Vorlage / Quelle / Vertrag | Dieser Name ist in der Vorlage nicht als Eingang deklariert. | Dieser Eingang fehlt in der Vorlage. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RuleEditor.interne_regel_744cdc | Formular für Vorlage / Quelle / Vertrag | Interne Regel | Benannter Rechenschritt | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RuleEditor.benannte_regeln_werden_pro_auswertung_nur_einmal_5ec5f3 | Formular für Vorlage / Quelle / Vertrag | Benannte Regeln werden pro Auswertung nur einmal berechnet; Zustandsregeln schreiten so nur einmal fort. | Mimir berechnet einen benannten Rechenschritt je Auswertung nur einmal. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RuleEditor.operand_c81de8 | Formular für Vorlage / Quelle / Vertrag | Operand | Eingangswert | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RuleEditor.bedingung_trifft_nicht_zu_wenn_wahr_cb4a34 | Formular für Vorlage / Quelle / Vertrag | Bedingung (trifft nicht zu, wenn wahr) | Trifft nicht zu, wenn diese Bedingung erfüllt ist | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RuleEditor.hysterese_schaltet_erst_uber_oben_ein_und_erst_u_629b5d | Formular für Vorlage / Quelle / Vertrag | Hysterese: schaltet erst über „oben“ ein und erst unter „unten“ aus. Der Zustand ist flüchtig und startet nach Neustart wieder bei „Startzustand“. | Der Wert schaltet erst an der oberen Grenze ein und unter der unteren Grenze aus. Nach einem Neustart beginnt er im festgelegten Anfangszustand. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RuleEditor.id_eindeutig_df6df9 | Formular für Vorlage / Quelle / Vertrag | ID (eindeutig) | Eindeutige Kennung | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RuleEditor.initial_1f3974 | Formular für Vorlage / Quelle / Vertrag | Initial | Anfangszustand | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RuleEditor.gehaltene_werte_akzeptieren_034eb1 | Formular für Vorlage / Quelle / Vertrag | Gehaltene Werte akzeptieren | Werte innerhalb ihrer Haltefrist verwenden | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RuleEditor.unbekannter_operator_json_a20a96 | Formular für Vorlage / Quelle / Vertrag | Unbekannter Operator (JSON) | Unbekannter Rechenschritt – Daten unter Erweitert prüfen | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RuleEditor.schlussel_sind_kanonische_json_skalare_2c69e1 | Formular für Vorlage / Quelle / Vertrag | Die Zuordnung verwendet einfache Werte, zum Beispiel  | Bei der Zuordnung verwendest du einfache Werte, zum Beispiel  | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RuleEditor.quot_text_quot_dc8483 | Formular für Vorlage / Quelle / Vertrag | &amp;quot;text&amp;quot; | Text | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RuleEditor.in_anfuhrungszeichen_ab3cf1 | Formular für Vorlage / Quelle / Vertrag | (in Anführungszeichen). | . | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RuleEditor.wahr_167f97 | Formular für Vorlage / Quelle / Vertrag | wahr | Ja | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.RuleEditor.falsch_b3c3e0 | Formular für Vorlage / Quelle / Vertrag | falsch | Nein | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.SchemaForm.auf_null_setzen_cc2a5b | Formular für Vorlage / Quelle / Vertrag | Auf null setzen | Keinen Wert setzen | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.ValueEditor.wahrheitswert_7dc5d8 | Formular für Vorlage / Quelle / Vertrag | Wahrheitswert | Ja/Nein | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.ValueEditor.null_leer_5eb672 | Formular für Vorlage / Quelle / Vertrag | Null (leer) | Kein Wert | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.ValueEditor.objekt_fe41f9 | Formular für Vorlage / Quelle / Vertrag | Objekt | Zusammengesetzte Angaben | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.ValueEditor.wahr_167f97 | Formular für Vorlage / Quelle / Vertrag | wahr | Ja | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.ValueEditor.falsch_b3c3e0 | Formular für Vorlage / Quelle / Vertrag | falsch | Nein | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.ValueEditor.null_kein_wert_gesetzt_a2f805 | Formular für Vorlage / Quelle / Vertrag | null – kein Wert gesetzt | Kein Wert gesetzt | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| editors.ValueEditor.json_ansicht_optional_experte_cb2cb8 | Formular für Vorlage / Quelle / Vertrag | JSON-Ansicht (freiwillig, Experte) | Erweitert: Daten als JSON | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.admin.AdminPage.installation_einrichtung_342651 | Einstellungen | Installation &amp; Einrichtung | Einrichtung | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.admin.AdminPage.version_dd1679 | Einstellungen | Version | Programmversion | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.admin.AdminPage.epoche_8a2707 | Einstellungen → Erweitert | Epoche | Laufzeitabschnitt | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.admin.AdminPage.aktive_revision_90097f | Einstellungen | Aktive Version | Aktuelle Konfiguration | Übernommenen Gesamtstand von Vorlagen- und Programmversion unterscheiden. |
| features.admin.AdminPage.serverzeit_utc_123303 | Einstellungen | Appzeit (UTC) | Uhrzeit von Mimir | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.admin.AdminPage.readiness_komponenten_565aea | Einstellungen | Bereitschaft &amp; Komponenten | Kann Mimir arbeiten? | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.admin.AdminPage.bereitschaft_kann_der_dienst_auswerten_ist_etwas_9bcf04 | Einstellungen | Bereitschaft (kann der Dienst auswerten?) ist etwas anderes als die Qualität einzelner Werte. | Diese Punkte müssen erfüllt sein, damit Mimir deine Verträge auswerten kann. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.admin.AdminPage.persistenz_774960 | Einstellungen | Persistenz | Verbindung zur Datenbank | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.admin.AdminPage.veroffentlichung_cb618e | Einstellungen | Veröffentlichung | Bereitstellung der Werte | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.admin.AdminPage.commit_dauer_72559c | Einstellungen | Speicherung-Dauer | Zeit zum Speichern | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.admin.AdminPage.ingest_uberlaufe_91547b | Einstellungen | Eingang-Überläufe | Nicht verarbeitete Eingangsmeldungen | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.admin.AdminPage.refresh_uberlaufe_e9c45a | Einstellungen | Aktualisierung-Überläufe | Nicht ausgeführte Aktualisierungsanfragen | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.admin.AdminPage.bridge_verbindungsdiagnose_9a2dd6 | Einstellungen | HA-Anbindung &amp; Verbindungsdiagnose | HA-Anbindung | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.admin.AdminPage.bridge_zustand_einrichtung_72ab84 | Einstellungen | HA-Anbindung-Zustand (Einrichtung) | Stand der Einrichtung | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.admin.AdminPage.bridge_version_12d174 | Einstellungen | HA-Anbindung-Version | Programmversion von Bifröst | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.admin.AdminPage.bridge_abonnements_4ce4ee | Einstellungen | HA-Anbindung-Abonnements | Verknüpfte Quellen | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.admin.AdminPage.resyncs_634ca6 | Einstellungen | Neu synchronisiert | Zuletzt abgeglichen | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.admin.AdminPage.ha_erkennung_testen_nur_lesend_34b8be | Einstellungen | HA-Erkennung testen (nur lesend) | Einträge aus Home Assistant erneut lesen | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.admin.AdminPage.tokens_werden_nie_angezeigt_oder_gespeichert_au__7dbaa2 | Einstellungen | Zugangsschlüssel werden nie angezeigt oder gespeichert, außer einmalig nach einer Rotation. | Ein neuer Zugangsschlüssel wird nur einmal angezeigt. Mimir speichert ihn nicht in deinem Browser. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.admin.AdminPage.token_rotieren_ce44a8 | Einstellungen | Zugangsschlüssel rotieren … | Zugangsschlüssel erneuern … | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.admin.AdminPage.rotation_nicht_bestatigt_7a441b | Einstellungen | Rotation nicht bestätigt | Erneuerung nicht bestätigt | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.admin.AdminPage.das_ergebnis_ist_unbestimmt_falls_die_antwort_ve_f7ba98 | Einstellungen | Das Ergebnis ist unbestimmt, falls die Antwort verloren ging: die Rotation  | Es ist noch unklar, ob der Schlüssel erneuert wurde.  | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.admin.AdminPage.zugriff_prufen_und_ggf_uber_die_vertrauenswurdig_5d01cc | Einstellungen | . Zugriff prüfen und ggf. über die vertrauenswürdige lokale Einstellungen wiederherstellen. | . Prüfe den Zugriff. Falls nötig, stelle ihn über die lokalen App-Einstellungen wieder her. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.admin.AdminPage.v0_token_rotiert_376829 | Einstellungen | {v0}-Zugangsschlüssel rotiert | {v0}-Zugangsschlüssel erneuert | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.admin.AdminPage.neues_token_wird_nur_jetzt_angezeigt_und_nicht_i_f57447 | Einstellungen | Neuer Zugangsschlüssel – wird nur jetzt angezeigt und nicht im Browser gespeichert. Alle Clients dieser Rolle müssen es erhalten. | Dieser neue Schlüssel wird nur jetzt angezeigt. Gib ihn allen Anwendungen, die diesen Zugang verwenden. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.admin.AdminPage.rotations_id_0f1c11 | Einstellungen | Rotations-ID  | Kennung der Erneuerung  | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.admin.AdminPage.ich_habe_das_token_gesichert_ausblenden_d2c4e8 | Einstellungen | Ich habe das Zugangsschlüssel gesichert – ausblenden | Ich habe den Zugangsschlüssel gesichert – ausblenden | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.admin.AdminPage.v0_token_rotieren_b5584c | Einstellungen | {v0}-Zugangsschlüssel rotieren? | {v0}-Zugangsschlüssel erneuern? | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.admin.AdminPage.das_bisherige_token_wird_sofort_ungultig_verbund_973d41 | Einstellungen | Der bisherige Zugangsschlüssel wird sofort ungültig; verbundene Clients verlieren den Zugriff, bis sie der neue Zugangsschlüssel erhalten.  | Der bisherige Schlüssel wird sofort ungültig. Anwendungen mit diesem Zugang brauchen danach den neuen Schlüssel.  | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.admin.AdminPage.jetzt_rotieren_622965 | Einstellungen | Jetzt rotieren | Jetzt erneuern | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.admin.AdminPage.ich_habe_verstanden_dass_bestehende_clients_dana_70d245 | Einstellungen | Ich habe verstanden, dass bestehende Clients danach aktualisiert werden müssen. | Ich habe verstanden, dass Anwendungen mit diesem Zugang danach den neuen Schlüssel brauchen. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.admin.AdminPage.administrative_operationen_mit_rolle_vertrauensg_2a53f4 | Einstellungen | Administratoristrative Operationen mit Rolle/Vertrauensgrenze, Objekt und Version. Zugangsschlüssel und Argumente werden nie aufgezeichnet. | Hier siehst du Verwaltungsaktionen, ihre Auslöser und Ergebnisse. Zugangsschlüssel und eingegebene Werte werden nicht angezeigt. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.admin.AdminPage.objekt_fe41f9 | Einstellungen | Objekt | Zusammengesetzte Angaben | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.admin.AdminPage.revision_2e516d | Einstellungen | Version | Konfiguration | Übernommenen Gesamtstand von Vorlagen- und Programmversion unterscheiden. |
| features.authoring.CreateDraftDialog.datei_oder_text_wird_wie_jeder_draft_validiert_u_33784f | Entwurf und Bearbeitung | Datei oder Text; wird wie jeder Entwurf validiert und ist danach vollständig grafisch bearbeitbar. | Lies eine Datei oder gespeicherten Text ein. Danach kannst du die Angaben über Formulare bearbeiten. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.authoring.CreateDraftDialog.duplikat_dieses_drafts_97f0da | Entwurf und Bearbeitung | Duplikat dieses Entwürfe. | Kopie dieses Entwurfs. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.authoring.CreateDraftDialog.ein_draft_ist_niemals_live_erst_die_ausdrucklich_e2171f | Entwurf und Bearbeitung | Ein Entwurf ist niemals aktiv. Erst die ausdrückliche Übernahme einer validierten Version verändert den aktiven Zustand. | Änderungen im Entwurf gelten noch nicht. Prüfe ihn und wähle Übernehmen, damit sie wirksam werden. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.authoring.CreateDraftDialog.registry_datei_json_be6006 | Entwurf und Bearbeitung | Konfiguration-Datei (.json) | Datei mit der Konfiguration (.json) | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.authoring.DraftBar.arbeits_draft_wahlen_d0f546 | Entwurf und Bearbeitung | Arbeits-Entwurf wählen | Entwurf auswählen | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.authoring.DraftBar.authoring_bereiche_bearbeiten_immer_genau_einen__3bfed3 | Entwurf und Bearbeitung | Bearbeitung-Bereiche bearbeiten immer genau einen Entwurf. Entwürfe sind nie aktiv. | Du bearbeitest immer genau den ausgewählten Entwurf. Seine Änderungen gelten erst nach dem Übernehmen. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.authoring.DraftBar.die_zwischenzeitlichen_anderungen_am_server_draf_1417b3 | Entwurf und Bearbeitung | Die zwischenzeitlichen Änderungen an der App-Entwurf gehen verloren. Zum Fortfahren erneut klicken. | Die inzwischen gespeicherten Änderungen des Entwurfs gehen verloren. Bestätige das Überschreiben erneut. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.authoring.DraftBar.arbeits_draft_00218f | Entwurf und Bearbeitung | Arbeits-Entwurf | Geöffneter Entwurf | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.authoring.issues.die_quelle_hat_kein_binding_a917c9 | Entwurf und Bearbeitung | Die Quelle hat kein Verknüpfung. | Die Quelle hat keine Verknüpfung. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.authoring.issues.das_binding_verweist_auf_keine_vorhandene_quelle_82115e | Entwurf und Bearbeitung | Das Verknüpfung verweist auf keine vorhandene Quelle. | Die Verknüpfung verweist auf keine vorhandene Quelle. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.authoring.issues.deklarative_definitionen_erfordern_fingerprint_v_04509f | Entwurf und Bearbeitung → Erweitert | Deklarative Vorlagen erfordern Berechnungskennung Version 2. | Das Format dieser Vorlage passt nicht zur verwendeten Konfiguration. Prüfe die Vorlagenversion unter Erweitert. | Übernommenen Gesamtstand von Vorlagen- und Programmversion unterscheiden. Technische Angabe nur unter Erweitert. |
| features.authoring.issues.die_typen_von_operator_und_ausgabe_passen_nicht__6c3171 | Entwurf und Bearbeitung | Die Typen von Operator und Ausgabe passen nicht zusammen. | Die Regel liefert eine andere Werteart als das Ausgabefeld erwartet. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.authoring.issues.die_id_eines_bucket_temporal_knotens_muss_in_der_ccd952 | Entwurf und Bearbeitung | Die ID eines Hysterese-/Zeitregel-Knotens muss in der Vorlage eindeutig sein. | Jede Schaltschwellen- oder Zeitregel braucht innerhalb der Vorlage eine eindeutige Kennung. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.authoring.issues.pro_quellzustand_und_ereignis_ist_nur_eine_trans_aee3c9 | Entwurf und Bearbeitung | Pro Quellzustand und Ereignis ist nur eine Übergang erlaubt. | Für denselben Zustand und Auslöser ist nur ein passender Wechsel erlaubt. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.authoring.issues.guards_mussen_zustandslos_sein_zeitliche_wahrhei_8935df | Entwurf und Bearbeitung | Bedingung müssen zustandslos sein; zeitliche Wahrheiten als Vertrag-Eingang einspeisen. | Die Bedingung darf nur vorhandene Eingänge prüfen. Eine Wartezeit richtest du in einem eigenen Vertrag ein. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.authoring.issues.map_schlussel_mussen_kanonische_json_skalare_sei_70986e | Entwurf und Bearbeitung | Zuordnung-Schlüssel müssen kanonische JSON-Skalare sein, die zum Eingangstyp und Werteliste passen. | Die Zuordnung muss einfache Werte enthalten, die zur Werteart und zur Werteliste des Eingangs passen. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.authoring.issues.ordnungsvergleiche_gelten_nur_fur_zahl_text_und__d224d3 | Entwurf und Bearbeitung | Ordnungsvergleiche gelten nur für Zahl, Text und Zeitpunkt. | Größer-/Kleiner-Vergleiche sind nur für Zahlen, Texte und Zeitpunkte möglich. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.authoring.locate.registry_dokument_fb6686 | Entwurf und Bearbeitung | Konfiguration-Dokument | Konfiguration | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.authoring.model.wahrheitswert_7dc5d8 | Entwurf und Bearbeitung | Wahrheitswert | Ja/Nein | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.authoring.model.objekt_fe41f9 | Entwurf und Bearbeitung | Objekt | Zusammengesetzte Angaben | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.authoring.WorkingDocument.workingdocumentprovider_fehlt_950e4e | Entwurf und Bearbeitung | WorkingDocumentProvider fehlt | Der Entwurf ist gerade nicht verfügbar. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.contracts.ContractDetailPage.contract_konfiguration_d1e14f | Vertrag und Vorlage | Vertrag-Konfiguration | Einstellungen des Vertrags | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.contracts.ContractDetailPage.eingange_hangt_ab_von_24b089 | Vertrag und Vorlage | Eingänge (hängt ab von) | Verknüpfung | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.contracts.ContractDetailPage.keine_eingange_gebunden_b03857 | Vertrag und Vorlage | Keine Eingänge gebunden. | Noch keine Eingänge verknüpft. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.contracts.ContractDetailPage.deklarative_definition_b0121f | Vertrag und Vorlage | Deklarative Vorlage  | Eigene Vorlage  | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.contracts.ContractDetailPage.paket_typ_44867a | Vertrag und Vorlage | Paket-Typ  | Eingebaute Vorlage  | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.contracts.ContractDetailPage.fest_im_code_nicht_uber_die_workbench_anderbar_ee4ae9 | Vertrag und Vorlage | (fest im Code, nicht über Mimir änderbar) | Wird mit Mimir geliefert und kann hier nicht geändert werden. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.contracts.ContractDetailPage.wird_aus_dem_draft_entfernt_contracts_die_ihn_al_932341 | Vertrag und Vorlage | “ wird aus dem Entwurf entfernt. Verträge, die ihn als Eingang nutzen, werden bei der Validierung als fehlerhaft markiert. | “ wird aus dem Entwurf entfernt. Die Prüfung zeigt dir Verträge, die ihn noch verwenden. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.contracts.ContractsPage.eine_instanz_bindet_einen_typ_paket_typ_oder_dek_e77e04 | Vertrag und Vorlage | Ein Vertrag verbindet eine Vorlage mit den Quellen seiner Eingänge. | Hier kannst du deine Verträge finden, ordnen und neue anlegen. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.contracts.ContractsPage.contract_id_f9f7ff | Vertrag und Vorlage | Vertrag-ID | Vertragskennung | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.contracts.ContractsPage.typ_version_1b7183 | Vertrag und Vorlage | Typ &amp; Version | Vorlage und Version | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.contracts.ContractsPage.suchen_nach_id_name_typ_43b8d8 | Vertrag und Vorlage | Suchen nach ID, Name, Typ … | Nach Namen oder Vorlage suchen … | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.contracts.ContractsPage.alle_typen_83162a | Vertrag und Vorlage | Alle Typen | Alle Vorlagen | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.contracts.ContractsPage.legen_sie_in_einem_draft_die_erste_instanz_an_od_1842ad | Vertrag und Vorlage | Lege deinen ersten Vertrag an oder lies unter „Vertrag importieren“ eine Konfiguration ein. | Lege deinen ersten Vertrag an. Du kannst dabei eine vorhandene Vorlage auswählen. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.contracts.DefinitionDetailPage.diese_version_war_in_revision_v0_aktiv_7f3ad4 | Vertrag und Vorlage | Diese Version war in Version {v0} aktiv. | Diese Vorlagenversion wurde in Konfiguration {v0} verwendet. | Übernommenen Gesamtstand von Vorlagen- und Programmversion unterscheiden. |
| features.contracts.DefinitionDetailPage.keiner_instanz_86ff43 | Vertrag und Vorlage | keiner Vertrag | keinem Vertrag | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.contracts.DefinitionsPage.typ_id_b7db41 | Vertrag und Vorlage | Typ-ID | Vorlagenkennung | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.contracts.DefinitionsPage.seit_rev_6ccd9c | Vertrag und Vorlage | seit Rev.  | seit Konfiguration  | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.contracts.DefinitionsPage.definitionen_sind_deklarative_typen_mit_unverand_5b643c | Vertrag und Vorlage | Eine Vorlage beschreibt, wie ein Vertrag seine Werte berechnet. Eine neue Logik erhält eine neue Version. | Hier kannst du Vorlagen finden und festlegen, wie Verträge ihre Werte berechnen. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.contracts.DefinitionsPage.deklarative_definitionen_3a5155 | Vertrag und Vorlage | Deklarative Vorlagen | Eigene Vorlagen | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.contracts.DefinitionsPage.aktivierte_versionen_sind_gesperrt_eine_logikand_5deacf | Vertrag und Vorlage | Aktivierte Versionen sind gesperrt; eine Logikänderung erfordert eine neue Version. | Eine übernommene Berechnung bleibt erhalten. Für Änderungen legst du eine neue Vorlagenversion an. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.contracts.DefinitionsPage.legen_sie_in_einem_draft_die_erste_deklarative_d_063da9 | Vertrag und Vorlage | Lege in einem Entwurf die erste deklarative Vorlage an – ohne JSON, direkt im Editor. | Lege im Entwurf deine erste Vorlage an. Alle Einstellungen kannst du über Formulare bearbeiten. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.contracts.DefinitionsPage.paket_typen_a517d6 | Vertrag und Vorlage | Paket-Typen | Eingebaute Vorlagen | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.contracts.DefinitionsPage.fest_im_code_der_app_nicht_uber_die_workbench_an_49f18f | Vertrag und Vorlage | Fest im Code der App; nicht über Mimir änderbar, aber als Typ für Verträge verwendbar. | Diese Vorlagen werden mit Mimir geliefert. Du kannst sie für Verträge auswählen, aber hier nicht ändern. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.contracts.DefinitionsPage.keine_paket_typen_gemeldet_e04f62 | Vertrag und Vorlage | Keine Paket-Typen gemeldet. | Keine eingebauten Vorlagen vorhanden. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.diagnostics.CommandsPanel.angenommen_die_transition_wurde_ausgefuhrt_833e56 | Erweitert / Nachweise | Angenommen: Die Übergang wurde ausgeführt. | Angenommen: Der Zustandswechsel wurde ausgeführt. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.CommandsPanel.command_id_konflikt_dieselbe_id_wurde_mit_andere_d2b1a5 | Erweitert / Nachweise | Befehle-ID-Konflikt: dieselbe ID wurde mit anderem Inhalt verwendet. | Diese Befehlskennung wurde bereits für einen anderen Inhalt verwendet. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.CommandsPanel.nur_fur_die_aktive_registry_ein_command_fordert__3a3fc2 | Erweitert / Nachweise | Nur für die aktive Konfiguration. Ein Befehle fordert eine benannte Übergang an; es gibt kein direktes Setzen von Werten. | Ein Befehl fragt einen erlaubten Zustandswechsel an. Du kannst damit keinen beliebigen Wert setzen. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.CommandsPanel.command_senden_8e5910 | Erweitert / Nachweise | Befehle senden … | Befehl senden … | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.CommandsPanel.noch_kein_command_gesendet_a8eea1 | Erweitert / Nachweise | Noch kein Befehle gesendet. | Noch kein Befehl gesendet. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.CommandsPanel.der_command_kann_trotzdem_verarbeitet_worden_sei_a1e8f2 | Erweitert / Nachweise | Der Befehle kann trotzdem verarbeitet worden sein. Nicht erneut senden – stattdessen das gespeicherte Ergebnis dieser ID abfragen. | Der Befehl kann bereits verarbeitet worden sein. Sende ihn nicht erneut. Frage zuerst sein gespeichertes Ergebnis ab. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.CommandsPanel.command_id_8aab8c | Erweitert / Nachweise | Befehle-ID | Befehlskennung | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.CommandsPanel.command_wirklich_senden_dfa28f | Erweitert / Nachweise | Befehle wirklich senden? | Befehl wirklich senden? | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.ContractDiagnosis.ein_deaktivierter_oder_entfernter_zustand_erford_d6eacd | Erweitert / Nachweise | Ein deaktivierter oder entfernter Zustand erfordert Neuinitialisierung. | Der gespeicherte Zustand ist ausgeschaltet oder wurde entfernt. Mimir braucht gültige Daten für einen neuen Start. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.ContractDiagnosis.es_fehlen_teile_des_erforderlichen_kontexts_a92686 | Erweitert / Nachweise | Es fehlen Teile des erforderlichen Kontexts. | Es fehlen Angaben zum gespeicherten Zustand. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.ContractDiagnosis.kontext_fehlt_8c5f5c | Erweitert / Nachweise | Kontext fehlt | Gespeicherter Zustand fehlt | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.ContractDiagnosis.es_war_aktiv_aber_es_liegt_kein_kontext_vor_170a8e | Erweitert / Nachweise | Es war aktiv, aber es liegt kein Kontext vor. | Der Ablauf war bereits aktiv, aber sein gespeicherter Zustand fehlt. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.ContractDiagnosis.fingerprint_kompatibel_fffc88 | Erweitert / Nachweise → Erweitert | Berechnungskennung kompatibel | Berechnungsgrundlage passt | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.ContractDiagnosis.fingerprint_abweichend_671e2b | Erweitert / Nachweise → Erweitert | Berechnungskennung abweichend | Berechnungsgrundlage hat sich geändert | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.ContractDiagnosis.registry_revision_70bc45 | Erweitert / Nachweise | Konfiguration-Version | Konfiguration | Übernommenen Gesamtstand von Vorlagen- und Programmversion unterscheiden. Technische Angabe nur unter Erweitert. |
| features.diagnostics.ContractDiagnosis.temporal_kontexte_0c5527 | Erweitert / Nachweise | Zeitregel-Kontexte | Gespeicherte Zeitregeln | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.ContractDiagnosis.keine_temporal_kontexte_1f1c1c | Erweitert / Nachweise | Keine Zeitregel-Kontexte | Keine gespeicherten Zeitregeln | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.ContractDiagnosis.dieser_contract_hat_keine_zeit_knoten_mit_gespei_747fb8 | Erweitert / Nachweise | Dieser Vertrag hat keine Zeit-Knoten mit gespeichertem Kontext. | Dieser Vertrag hat keine Zeitregel, deren Zustand gespeichert wird. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.ContractDiagnosis.episode_b19c45 | Erweitert / Nachweise | Episode | Durchlauf | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.DiagnosticsPage.snapshot_wird_erwartet_8f2bea | Erweitert / Nachweise | vollständiger Stand wird erwartet … | Wartet auf den aktuellen Stand … | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.DiagnosticsPage.noch_kein_live_zustand_d31d85 | Erweitert / Nachweise | Noch kein Aktueller Zustand | Noch kein aktueller Zustand | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.DiagnosticsPage.aktuelle_veroffentlichung_38f9d7 | Erweitert / Nachweise | Aktuelle Veröffentlichung | Aktuell bereitgestellter Stand | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.DiagnosticsPage.epoche_8a2707 | Erweitert / Nachweise → Erweitert | Epoche | Laufzeitabschnitt | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.DiagnosticsPage.publication_sequenz_48deb8 | Erweitert / Nachweise → Erweitert | Veröffentlichung-Sequenz | Laufende Nummer des Stands | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.DiagnosticsPage.registry_revision_70bc45 | Erweitert / Nachweise | Konfiguration-Version | Konfiguration | Übernommenen Gesamtstand von Vorlagen- und Programmversion unterscheiden. Technische Angabe nur unter Erweitert. |
| features.diagnostics.DiagnosticsPage.neu_synchronisiert_073e42 | Erweitert / Nachweise | Neu synchronisiert | Zuletzt abgeglichen | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.DiagnosticsPage.aus_den_geladenen_historienzeilen_abgeleitet_ein_8d83d0 | Erweitert / Nachweise | Aus den geladenen Historienzeilen abgeleitet; eine neue Epoche erzwingt für Clients einen frischen vollständiger Stand. | Nach einem Neustart gleicht Mimir den vollständigen Stand erneut ab. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.DiagnosticsPage.unterbrechungen_der_beobachtungs_kontinuitat_bet_cb4453 | Erweitert / Nachweise | Unterbrechungen der Beobachtungskontinuität; betroffene Felder melden eine Historienlücke. | In diesen Zeiträumen fehlen bestätigte Meldungen. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.DiagnosticsPage.lucke_n_im_laufzeitspeicher_c38399 | Erweitert / Nachweise | Lücke(n) im Laufzeitspeicher. | Unterbrechungen in der aktuellen Laufzeit. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.DiagnosticsPage.veroffentlichungen_2f573d | Erweitert / Nachweise | Veröffentlichungen | Bereitgestellte Stände | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.DiagnosticsPage.persistierte_contract_zustande_mit_epoche_und_se_30b8f1 | Erweitert / Nachweise → Erweitert | Persistierte Vertrag-Zustände mit Epoche und Sequenz. | Gespeicherte Vertragszustände mit Laufzeitabschnitt und laufender Nummer. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.DiagnosticsPage.revision_2e516d | Erweitert / Nachweise | Version | Konfiguration | Übernommenen Gesamtstand von Vorlagen- und Programmversion unterscheiden. Technische Angabe nur unter Erweitert. |
| features.diagnostics.DiagnosticsPage.diagnose_historie_63b2ee | Erweitert / Nachweise | Diagnose &amp; Historie | Erweitert | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.DiagnosticsPage.was_der_server_tatsachlich_wei_werte_quality_rea_24aab3 | Erweitert / Nachweise | Was die App tatsächlich weiß: Werte, Qualität, Gründe, Nachweis, Erklärung, Zeitregel-/Wiederherstellung-Zustand, Ablauf, Historie und Befehle. Es werden keine Werte oder Übergänge erfunden. | Hier kannst du gespeicherte Nachweise, Berechnungen und frühere Zustände genauer prüfen. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.DiagnosticsPage.contract_diagnose_314975 | Erweitert / Nachweise | Vertrag-Diagnose | Vertrag genauer prüfen | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.DiagnosticsPage.historie_4eaa80 | Erweitert / Nachweise | Historie | Verlauf | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.DiagnosticsPage.publikationen_lucken_44dc70 | Erweitert / Nachweise | Publikationen &amp; Lücken | Gespeicherte Stände und Lücken | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.EvidenceLookup.evidence_referenz_fd58d0 | Erweitert / Nachweise | Nachweis-Referenz | Kennung des Nachweises | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.ExplainPanel.paket_typen_und_noch_nicht_ausgewertete_contract_b1993f | Erweitert / Nachweise | Paket-Typen und noch nicht ausgewertete Verträge haben keinen aufgezeichneten Erklärungsverlauf. Die App liefert nur Erklärungsverlauf deklarativer Vorlagen. | Für eingebaute Vorlagen oder noch nicht ausgewertete Verträge liegt hier noch keine schrittweise Erklärung vor. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.ExplainPanel.letzte_relevante_bestatigte_auswertung_kein_herz_703fce | Erweitert / Nachweise | Letzte relevante, bestätigte Auswertung – kein Herzschlag und keine Historie. Die Schritte stehen in Auswertungsreihenfolge (Teilausdrücke vor ihrem Operator). | Hier siehst du die letzte bestätigte Berechnung Schritt für Schritt. Das ist kein vollständiger Verlauf aller Meldungen. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.ExplainPanel.explain_schritte_3eeba4 | Erweitert / Nachweise | Erklärung-Schritte | Berechnungsschritte | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.ExplainPanel.operator_291101 | Erweitert / Nachweise | Operator | Rechenschritt | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.HistoryTab.contract_zustande_cbb892 | Erweitert / Nachweise | Vertrag-Zustände | Vertragszustände | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.HistoryTab.machine_transitionen_29ddde | Erweitert / Nachweise | Ablauf-Übergänge | Zustandswechsel | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.HistoryTab.episoden_f859be | Erweitert / Nachweise | Episoden | Durchläufe | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.HistoryTab.historienlucken_5be036 | Erweitert / Nachweise | Historienlücken | Lücken im Verlauf | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.HistoryTab.revisionen_e0511e | Erweitert / Nachweise | Versionen | Übernommene Konfigurationen | Übernommenen Gesamtstand von Vorlagen- und Programmversion unterscheiden. Technische Angabe nur unter Erweitert. |
| features.diagnostics.HistoryTab.cursor_seiten_sind_kein_datenbank_snapshot_episo_66bc2a | Erweitert / Nachweise | Cursor-Seiten sind kein Datenbank-vollständiger Stand: Episoden/Fristen können sich zwischen den Abrufen ändern. | Während du ältere Einträge lädst, können neue hinzukommen. Die Anzeige ist eine Auswahl des Verlaufs. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.HistoryTab.historie_4eaa80 | Erweitert / Nachweise | Historie | Verlauf | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.HistoryTab.admin_lesezugriff_auf_die_dauerhaft_gespeicherte_b083b5 | Erweitert / Nachweise | Administrator-Lesezugriff auf die dauerhaft gespeicherte Historie, seitenweise mit opakem Cursor. | Hier kannst du den gespeicherten Verlauf nach Zeitraum und Eintrag durchsuchen. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.HistoryTab.contract_id_f9f7ff | Erweitert / Nachweise | Vertrag-ID | Vertragskennung | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.HistoryTab.source_id_a3a484 | Erweitert / Nachweise | Quelle-ID | Quellenkennung | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.HistoryTab.zeiten_werden_als_utc_instants_verglichen_grenze_96c2fd | Erweitert / Nachweise | Zeiten werden als UTC-Instants verglichen; Grenzen sind inklusive. | Beginn und Ende zählen zum gewählten Zeitraum. Mimir berücksichtigt die Zeitzone. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.graph.GraphPage.quellen_contracts_und_abgeleitete_ergebnisse_kan_5cf87d | Zusammenhänge | Quellen, Verträge und abgeleitete Ergebnisse. Kanten zeigen, welcher Eingang woraus gespeist wird; Farbe und Rand folgen dem Zustand, den der App meldet. | Hier kannst du sehen, welche Quellen und Verträge miteinander verknüpft sind. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.graph.GraphPage.gesamter_graph_ce5753 | Zusammenhänge | Gesamter Graph | Alle Zusammenhänge | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.graph.GraphPage.der_graph_entsteht_aus_sources_und_contracts_der_ff3f8d | Zusammenhänge | Der Graph entsteht aus Quellen und Verträge der aktiven Konfiguration oder des geöffneten Entwürfe. | Hier erscheinen die Quellen und Verträge der aktuellen Konfiguration oder des geöffneten Entwurfs. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.registry.ActivationDialogs.gespeicherter_draft_v0_v_v1_wird_als_neue_revisi_1cd2fe | Entwürfe und Konfigurationen | Der gespeicherte Entwurf „{v0}“ (Stand {v1}) wird als neue Version übernommen. | Du übernimmst den gespeicherten Entwurf „{v0}“ (Stand {v1}) als neue Konfiguration. | Übernommenen Gesamtstand von Vorlagen- und Programmversion unterscheiden. |
| features.registry.ActivationDialogs.revision_v0_ist_aktiv_ffe993 | Entwürfe und Konfigurationen | Version {v0} ist aktiv | Konfiguration {v0} ist aktiv | Übernommenen Gesamtstand von Vorlagen- und Programmversion unterscheiden. |
| features.registry.ActivationDialogs.die_live_zustande_werden_mit_der_neuen_revision__d6f83f | Entwürfe und Konfigurationen | Die aktuellen Werte werden mit der neuen Version veröffentlicht. Die Abnahme in Home Assistant bleibt ein eigener Schritt. | Mimir verwendet jetzt die neue Konfiguration. Prüfe danach die Werte deiner Verträge. | Übernommenen Gesamtstand von Vorlagen- und Programmversion unterscheiden. |
| features.registry.ActivationDialogs.aktive_revision_v0_d363db | Entwürfe und Konfigurationen | aktive Version {v0} | Konfiguration {v0} | Übernommenen Gesamtstand von Vorlagen- und Programmversion unterscheiden. |
| features.registry.ActivationDialogs.auf_revision_v0_zuruckrollen_1c608b | Entwürfe und Konfigurationen | Auf Version {v0} zurücksetzen | Auf Konfiguration {v0} zurücksetzen | Übernommenen Gesamtstand von Vorlagen- und Programmversion unterscheiden. |
| features.registry.ActivationDialogs.dieser_historische_stand_ist_unter_der_aktuellen_e1e6a7 | Entwürfe und Konfigurationen | Dieser historische Stand ist unter der aktuellen Software nicht mehr gültig | Dieser frühere Stand passt nicht mehr zur aktuellen Programmversion. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.registry.DiffView.geanderte_fingerprints_eb5466 | Entwürfe und Konfigurationen → Erweitert | Geänderte Berechnungskennung | Geänderte Berechnungsgrundlage | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.registry.DiffView.mogliche_neuinitialisierung_2361a0 | Entwürfe und Konfigurationen | Mögliche Neuinitialisierung | Abläufe können neu beginnen | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.registry.DiffView.snapshot_6ad27b | Entwürfe und Konfigurationen | vollständiger Stand | Vollständiger aktueller Stand | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.registry.DraftPage.optionale_expertenansicht_des_gesamten_dokuments_c2d8aa | Entwürfe und Konfigurationen | Optionale Expertenansicht des gesamten Dokuments. Es gibt keinen Einlesen-Sonderweg: übernommenes JSON ist danach ein gewöhnlicher Entwurf-Stand und vollständig grafisch bearbeitbar. | Hier kannst du die Konfigurationsdaten zusätzlich als Text bearbeiten. Die Formulare bleiben vollständig nutzbar. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.registry.DraftPage.die_ungespeicherten_anderungen_des_geoffneten_dr_9242f0 | Entwürfe und Konfigurationen | Die ungespeicherten Änderungen des geöffneten Entwürfe gehen verloren. | Die ungespeicherten Änderungen des geöffneten Entwurfs gehen verloren. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.registry.DraftPage.draft_v0_v_v1_basis_revision_v2_zuletzt_gespeich_24aa87 | Entwürfe und Konfigurationen | Entwurfsstand {v1} · auf Grundlage von Version {v2} · zuletzt gespeichert {v3} | Entwurfsstand {v1} · Grundlage: Konfiguration {v2} · zuletzt gespeichert {v3} | Übernommenen Gesamtstand von Vorlagen- und Programmversion unterscheiden. |
| features.registry.DraftPage.jeder_eintrag_verweist_auf_das_betroffene_objekt_8d552f | Entwürfe und Konfigurationen | Jeder Eintrag verweist auf das betroffene Objekt; im jeweiligen Editor steht der Fehler direkt am Feld. | Öffne einen Eintrag, um die betroffene Einstellung zu korrigieren. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.registry.DraftPage.draft_name_026ddb | Entwürfe und Konfigurationen | Entwurf-Name | Name des Entwurfs | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.registry.DraftPage.registry_inhalt_4f888f | Entwürfe und Konfigurationen | Konfiguration-Inhalt | Inhalt der Konfiguration | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.registry.DraftPage.fingerprint_version_e46d72 | Entwürfe und Konfigurationen → Erweitert | Version der Berechnungskennung | Verfahren der Prüfsumme | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.registry.RegistryPage.von_100_drafts_drafts_sind_niemals_live_sie_durf_c3fc1f | Entwürfe und Konfigurationen | von 100 Entwürfe. Entwürfe sind niemals aktiv; sie dürfen unvollständig sein. | von 100 Entwürfen. Deine Änderungen gelten erst nach dem Übernehmen. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.registry.RegistryPage.legen_sie_einen_leeren_draft_an_kopieren_sie_die_ecb749 | Entwürfe und Konfigurationen | Lege einen leeren Entwurf an, kopiere die aktive Konfiguration oder importiere eine JSON-Datei. | Lege einen leeren Entwurf an oder kopiere die aktuelle Konfiguration. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.registry.RegistryPage.revision_v0_5db9ad | Entwürfe und Konfigurationen | Version {v0} | Konfiguration {v0} | Übernommenen Gesamtstand von Vorlagen- und Programmversion unterscheiden. |
| features.sources.SourcesPage.wird_aus_dem_draft_entfernt_verweise_darauf_werd_295ba2 | Quellen und Verknüpfungen | “ wird aus dem Entwurf entfernt. Verweise darauf werden nicht automatisch angepasst; die Validierung zeigt offene Referenzen. | “ wird aus dem Entwurf entfernt. Die Prüfung zeigt dir, wo dieser Eintrag noch verwendet wird. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| lib.api.invalid_f1234d | Gemeinsame Oberfläche / Wertanzeige | invalid | ungültig | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| lib.api.persistenz_derzeit_nicht_erreichbar_es_wurde_nic_1c4a47 | Gemeinsame Oberfläche / Wertanzeige | Persistenz derzeit nicht erreichbar. Es wurde nichts geändert. | Die Datenbank ist gerade nicht erreichbar. Es wurde nichts geändert. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| lib.api.zu_dieser_referenz_liegt_keine_aufgezeichnete_ev_a4cab9 | Gemeinsame Oberfläche / Wertanzeige | Zu dieser Referenz liegt keine aufgezeichnete Nachweis vor. | Zu dieser Kennung ist kein Nachweis gespeichert. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| lib.live-context.liveprovider_fehlt_509518 | Gemeinsame Oberfläche / Wertanzeige | AktuellProvider fehlt | Der aktuelle Stand ist gerade nicht verfügbar. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| lib.request-budget.gemeinsames_anfragebudget_ist_nicht_verfugbar_b99b92 | Gemeinsame Oberfläche / Wertanzeige | Gemeinsames Anfragebudget ist nicht verfügbar. | Die Anfrage kann gerade nicht vorbereitet werden. Lade die Seite erneut. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| lib.status.letzter_gultiger_wert_wird_bis_zum_ende_der_grac_763ba7 | Gemeinsame Oberfläche / Wertanzeige | Letzter gültiger Wert wird bis zum Ende der Haltefrist-Frist gehalten. | Der letzte gültige Wert bleibt bis zum Ende seiner erlaubten Haltefrist verwendbar. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| lib.status.positiv_festgestellt_trifft_in_dieser_lage_nicht_96ea6e | Gemeinsame Oberfläche / Wertanzeige | Positiv festgestellt: trifft in dieser Lage nicht zu. | Es ist sicher festgestellt, dass dieser Wert hier nicht gebraucht wird. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| lib.status.persistenzfehler_f91758 | Gemeinsame Oberfläche / Wertanzeige | Persistenzfehler | Datenbank nicht erreichbar | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| lib.status.der_erste_snapshot_der_home_assistant_bridge_ste_9e13ec | Gemeinsame Oberfläche / Wertanzeige | Der erste vollständiger Stand der Mimir HA-Anbindung steht noch aus. | Mimir wartet auf die ersten vollständigen Daten von Home Assistant. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| lib.status.die_letzte_veroffentlichung_wurde_nicht_bestatig_a93e9b | Gemeinsame Oberfläche / Wertanzeige | Die letzte Veröffentlichung wurde nicht bestätigt; angezeigte Werte können vom persistierten Stand abweichen. | Die aktuellen Werte sind noch nicht mit dem gespeicherten Stand abgeglichen. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| lib.status.offline_8e2c7a | Gemeinsame Oberfläche / Wertanzeige | offline | ohne Verbindung | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| lib.status.der_dienst_antwortet_fehlerhaft_details_in_diagn_8a3550 | Gemeinsame Oberfläche / Wertanzeige | Der Dienst antwortet fehlerhaft. Details in Diagnose &amp; Historie bzw. im App-Log. | Mimir kann die Anfrage gerade nicht beantworten. Weitere Angaben findest du unter Erweitert oder im App-Protokoll. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| lib.status.persistenz_nicht_erreichbar_fd7b31 | Gemeinsame Oberfläche / Wertanzeige | Persistenz nicht erreichbar | Datenbank nicht erreichbar | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| lib.status.erster_bridge_snapshot_steht_aus_9a084a | Gemeinsame Oberfläche / Wertanzeige | Erster HA-Anbindung-vollständiger Stand steht aus | Erste Daten von Home Assistant fehlen | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| setup.setup.bridge_noch_nicht_aktiv_einrichtung_bleibt_offen_e255f6 | Ersteinrichtung | HA-Anbindung noch nicht aktiv. Einrichtung bleibt offen; Konfiguration-Bereitschaft folgt separat. | Die HA-Anbindung ist noch nicht eingerichtet. Deine Einrichtung bleibt gespeichert. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| setup.setup.bridge_config_flow_entspricht_nicht_dem_erwartet_2b24e0 | Ersteinrichtung | HA-Anbindung-Config-Flow entspricht nicht dem erwarteten leeren Formular. In HA prüfen. | Die Einrichtung von Bifröst kann nicht automatisch abgeschlossen werden. Prüfe den Eintrag in Home Assistant. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| setup.setup.einrichtung_nicht_verfugbar_ingress_sitzung_erne_14a439 | Ersteinrichtung | Einrichtung nicht verfügbar. Ingress-Sitzung erneuern und erneut prüfen. | Die Einrichtung ist gerade nicht erreichbar. Öffne Mimir erneut über Home Assistant. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| setup.SetupWizard.postgresql_verbinden_b6e00c | Ersteinrichtung | PostgreSQL verbinden | Datenbank verbinden | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| setup.SetupWizard.skript_und_import_5ad228 | Ersteinrichtung | Skript und Einlesen | Datenbank einrichten | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| setup.SetupWizard.bridge_aktiv_protokoll_1_89e62f | Ersteinrichtung | HA-Anbindung aktiv (Protokoll 1) | HA-Anbindung aktiv | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| setup.SetupWizard.bridge_protokoll_inkompatibel_2f4ecc | Ersteinrichtung | HA-Anbindung-Protokoll inkompatibel | Die Version der HA-Anbindung passt nicht zu Mimir | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| setup.SetupWizard.vorhandene_app_optionen_sind_ungultig_bitte_in_d_33e2cc | Ersteinrichtung | Vorhandene App-Optionen sind ungültig. Bitte in der Supervisor-Konfiguration korrigieren und anschließend nur diese App neu starten. Die bestehende Datenbankkonfiguration wird nicht vom Assistent übernommen. | Prüfe die Optionen der Mimir-App in Home Assistant. Starte danach nur Mimir neu. Deine bisherige Datenbank wird nicht überschrieben. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| setup.SetupWizard.benotigt_werden_postgresql_14_oder_neuer_in_eine_6d642d | Ersteinrichtung | Benötigt werden PostgreSQL 14 oder neuer in einer eigenen Datenbank sowie die Mimir HA-Anbindung in Home Assistant. Die Bereitstellung des PostgreSQL-LXC erfolgt separat. | Mimir braucht eine eigene Datenbank und Bifröst als HA-Anbindung. Unter Erweitert findest du die technischen Voraussetzungen. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| setup.SetupWizard.konfigurationsquelle_a3d30a | Ersteinrichtung | Konfigurationsquelle: | Einstellungen stammen aus: | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| setup.SetupWizard.vorhandene_supervisor_optionen_057912 | Ersteinrichtung | Vorhandene Supervisor-Optionen | Optionen der Mimir-App | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| setup.SetupWizard.privater_app_einrichtungszustand_09ec0b | Ersteinrichtung | Privater App-Einrichtungszustand | Gespeicherte Einrichtung von Mimir | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| setup.SetupWizard.neue_dedizierte_rolle_und_datenbank_f428fe | Ersteinrichtung | Neue dedizierte Rolle und Datenbank | Neue eigene Datenbank mit eigenem Benutzer | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| setup.SetupWizard.serveradresse_hostname_1325fc | Ersteinrichtung | Appadresse / Hostname | Adresse der Datenbank | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| setup.SetupWizard.anwendungsrolle_8e381b | Ersteinrichtung | Anwendungsrolle | Datenbankbenutzer | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| setup.SetupWizard.tls_modus_560328 | Ersteinrichtung | TLS-Modus | Schutz der Verbindung | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| setup.SetupWizard.verify_full_ca_und_hostname_prufen_a35ddf | Ersteinrichtung | verify-full – CA und Hostname prüfen | Verschlüsselt, Zertifikat und Namen prüfen (empfohlen) | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| setup.SetupWizard.require_verschlusselung_ohne_serverprufung_ee62c5 | Ersteinrichtung | require – Verschlüsselung ohne Appprüfung | Nur verschlüsseln, Zertifikat nicht prüfen | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| setup.SetupWizard.disable_unverschlusselt_e678cc | Ersteinrichtung | disable – unverschlüsselt | Unverschlüsselt | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| setup.SetupWizard.ca_datei_unter_ssl_optional_fa3385 | Ersteinrichtung | CA-Datei unter /ssl (freiwillig) | Datei mit dem öffentlichen Zertifikat unter /ssl | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| setup.SetupWizard.einrichtungsskript_und_geheimer_import_1c2ce9 | Ersteinrichtung | Einrichtungsskript und geheimer Einlesen | Datenbank einrichten und Verbindung einlesen | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| setup.SetupWizard.importcode_enthalt_das_passwort_nur_hier_einfuge_27cbc8 | Ersteinrichtung | Einlesencode enthält das Passwort. Nur hier einfügen; keine URLs, Shell-Befehle, Logs oder Issues. Privater Resume-Zustand verbleibt für Wiederholung im LXC. | Der Einlesecode enthält dein Passwort. Füge ihn nur hier ein. Teile ihn nicht in Links, Protokollen oder GitHub-Kommentaren. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| setup.SetupWizard.home_assistant_bridge_47a4b2 | Ersteinrichtung | Mimir HA-Anbindung | Bifröst: HA-Anbindung für Mimir | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| setup.SetupWizard.offener_release_blocker_self_install_01_app_kann_ac9f1d | Ersteinrichtung | Offener Release-Blocker SELF-INSTALL-01: App kann unter vorhandenen Berechtigungen keine Custom-Integration-Dateien installieren. Unterstützter Weg: HACS. | Installiere Bifröst über HACS in Home Assistant. Mimir kann diese Installation nicht selbst übernehmen. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| setup.SetupWizard.als_benutzerdefinierte_integration_hinzufugen_un_a896fe | Ersteinrichtung | als benutzerdefinierte Integration hinzufügen und Mimir HA-Anbindung installieren. Ein kompatibler veröffentlichter HACS-Stand muss verfügbar sein. | als benutzerdefiniertes Repository hinzufügen und Bifröst installieren. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| setup.SetupWizard.ha_core_neustart_selbst_nach_prufung_des_wartung_195f96 | Ersteinrichtung | HA-Core-Neustart selbst nach Prüfung des Wartungsfensters bestätigen. Er unterbricht auch die Legacy-Integration vorübergehend. | Starte Home Assistant nach der Installation neu. Dabei sind deine Automationen und Integrationen kurz unterbrochen. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| setup.SetupWizard.in_ha_bifrost_hinzufugen_domain_34a2b1 | Ersteinrichtung | In HA „Mimir HA-Anbindung“ hinzufügen. Domain:  | Füge in Home Assistant „Bifröst“ hinzu. Die technische Kennung lautet  | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| setup.SetupWizard.ersteinrichtung_und_runtime_readiness_sind_getre_f1f378 | Ersteinrichtung | Ersteinrichtung und Runtime-Bereitschaft sind getrennt.  | Nach der Einrichtung siehst du, welche Voraussetzungen für den Betrieb noch fehlen.  | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| setup.SetupWizard.zur_administration_offene_einrichtung_bleibt_erh_5faa3c | Ersteinrichtung | Zur Einstellungen (offene Einrichtung bleibt erhalten) | Zu den Einstellungen | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| components.ContractLiveState.en_dbd3a4 | Gemeinsame Oberfläche / Wertanzeige | en | — durch vollständige Einzahl-/Mehrzahltexte ersetzen | Benutzter Satzbaustein entfällt erst nach Einführung vollständiger Einzahl-/Mehrzahltexte. |
| editors.MachineEditor.deadline_fristablauf_ae4d9c | Formular für Vorlage / Quelle / Vertrag | deadline (Fristablauf) | Frist abgelaufen | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.diagnostics.ExplainPanel.engine_auswahl_dd7a28 | Erweitert / Nachweise | Berechnung-Auswahl | Ausgewählte Berechnung | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.graph.GraphPage.contract_deklarativ_4bb04f | Zusammenhänge | Vertrag (deklarativ) | Vertrag mit eigener Vorlage | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.graph.GraphPage.contract_paket_typ_ad3d17 | Zusammenhänge | Vertrag (Paket-Typ) | Vertrag mit eingebauter Vorlage | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| codes.object | Wert-/Ursachenanzeige, dynamisch | Objekt | Zusammengesetzte Angaben | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| codes.bucket | Wert-/Ursachenanzeige, dynamisch | Hysterese | Schaltschwellen | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| fields.catalog_id | Dynamische Formularbeschriftung | Wertelisten-ID | Kennung der Werteliste | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| fields.parameters | Dynamische Formularbeschriftung | Parameter | Einstellungen | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| fields.published_at | Dynamische Formularbeschriftung | Veröffentlicht | Bereitgestellt | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| fields.held_until | Dynamische Formularbeschriftung | Gehalten bis | Letzter Wert verwendbar bis | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| fields.revision | Dynamische Formularbeschriftung | Version | Konfiguration | Übernommenen Gesamtstand von Vorlagen- und Programmversion unterscheiden. |
| fields.publication_seq | Dynamische Formularbeschriftung → Erweitert | Veröffentlichung | Bereitstellung der Werte | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| fields.episode_id | Dynamische Formularbeschriftung | Episode | Durchlauf | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| fields.fingerprint | Dynamische Formularbeschriftung → Erweitert | Berechnungskennung | Berechnungsgrundlage | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| fields.fingerprint_version | Dynamische Formularbeschriftung → Erweitert | Verfahren der Berechnungskennung | Verfahren der Prüfsumme | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.ExplainPanel.interne_regel | Erweitert / Nachweise | Interne Regel | Benannter Rechenschritt | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| features.diagnostics.ExplainPanel.hysterese_221523 | Erweitert / Nachweise | Hysterese | Schaltschwellen | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| codes.publication_pending | Wert-/Ursachenanzeige, dynamisch → Erweitert | Veröffentlichung ausstehend | Aktueller Stand noch nicht bestätigt | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. Technische Angabe nur unter Erweitert. |
| editors.SchemaForm.leer_null_ce1303 | Formular für Vorlage / Quelle / Vertrag | leer (null) | Kein Wert | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| features.contracts.DefinitionDetailPage.deklarative_definition_07f53d | Vertrag und Vorlage | Deklarative Vorlage | Eigene Vorlage | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| fields.ReferenceRule | Dynamische Formularbeschriftung | Interne Regel | Benannter Rechenschritt | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| fields.language_version | Dynamische Formularbeschriftung | Version der Regelsprache | Format der Vorlage | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha7.diff.explanation | Entwürfe und Konfigurationen | Hier siehst du, was sich beim Übernehmen ändert. Aktuelle Werte werden dabei nicht neu berechnet. | Hier siehst du die geplanten Änderungen. Die aktuellen Vertragswerte ändern sich erst nach dem Übernehmen. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha8.configuration.validHint | Vertrag und Vorlage; Übersicht | Die Vollständigkeit deiner Konfiguration wird getrennt vom Signalzustand angezeigt. Ergänze die noch fehlende Zuordnung. | Der Wert ist verwendbar. Für seine vollständige Zuordnung fehlen noch Angaben. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| codes.compound_key | Wert-/Ursachenanzeige, dynamisch | Zusammengesetzter Schlüssel | Werte zu einer Kennung verbinden | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| fields.quantity | Dynamische Formularbeschriftung | Physikalische Größe | Art der Messung | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| validation.lifecycle_transition | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Für diesen Wechsel brauchst du die nächste Lebenszyklusstufe oder eine neue Begründung für die Wiederfreigabe. | Wähle die nächste erlaubte Stufe. Wenn du eine Version wieder freigibst, gib eine Begründung an. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| fields.raw_days | Dynamische Formularbeschriftung | Einzelmessungen in Tagen | Einzelmessungen aufbewahren (Tage) | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| fields.rollup_days | Dynamische Formularbeschriftung | Stundenwerte in Tagen | Stundenwerte aufbewahren (Tage) | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| alpha8.retention.configure | Gemeinsame Oberfläche / Wertanzeige | Lege in deinem Entwurf fest, wie lange Mimir Einzelmessungen und Stundenwerte aufbewahrt. Erst wenn du diese Aufbewahrungsregel übernimmst, ist Mimir für den Betrieb bereit. | Lege im Entwurf fest, wie lange Mimir Messungen aufbewahrt. Die Regel gilt erst nach dem Übernehmen. | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |
| codes.anniversary | Wert-/Ursachenanzeige, dynamisch | Nächster Jahrestag | Jahrestag | Verständlicher formulieren, Wörterbuch beachten und/oder Grammatik berichtigen. |

## Neue Texte für Alpha 9 — 123 Vorschläge

Die Schlüssel sind vorgeschlagen und noch nicht im Produkt angelegt. Neue Seitenköpfe stehen zusätzlich in der Seitenregel.

| Schlüssel | Ort in der Oberfläche | alt | neu | Grund |
|---|---|---|---|---|
| alpha9.header.noConfiguration | Kopfleiste | — neu | Noch keine Konfiguration | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.system.programVersion | Einstellungen → System | — neu | Programmversion | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.system.programVersionValue | Einstellungen → System | — neu | Mimir {version} (Alpha 9) | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.system.bridgeVersion | Einstellungen → System → Erweitert | — neu | Bifröst {version} | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.configuration.noContracts | Entwurf → Auswirkungen | — neu | Du übernimmst eine Konfiguration ohne Verträge. | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.configuration.emptySection | Übersicht → Konfiguration unvollständig | — neu | Zurzeit nichts unvollständig | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.evidence.one | Vertrag → Nachweise | — neu | 1 gespeicherter Nachweis | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.evidence.many | Vertrag → Nachweise | — neu | {count} gespeicherte Nachweise | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.evidence.open | Vertrag → Nachweise | — neu | Nachweise ansehen | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.category.label | Vertrag und Vorlage → Anlegen/Einstellungen | — neu | Kategorie | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.category.climate | Kategorieauswahl | — neu | Klima | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.category.lightCover | Kategorieauswahl | — neu | Licht &amp; Rollos | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.category.presence | Kategorieauswahl | — neu | Anwesenheit | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.category.sleepWake | Kategorieauswahl | — neu | Schlaf &amp; Wecken | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.category.media | Kategorieauswahl | — neu | Medien | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.category.other | Kategorieauswahl | — neu | Sonstiges | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.category.all | Vertrags-/Vorlagenliste → Filter | — neu | Alle Kategorien | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.category.group | Vertrags-/Vorlagenliste → Gruppierung | — neu | Nach Kategorie ordnen | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.room.label | Vertrag → Einstellungen und Listenfilter | — neu | Raum | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.room.choose | Vertrag → Einstellungen | — neu | Raum auswählen | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.room.none | Vertrag → Einstellungen und Listenfilter | — neu | Kein Raum | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.room.suggestion | Vertrag → Einstellungen | — neu | Vorschlag aus Home Assistant: {room} | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.room.accept | Vertrag → Einstellungen | — neu | Vorschlag verwenden | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.room.custom | Vertrag → Einstellungen | — neu | Eigenen Raumnamen eingeben | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.room.multiple | Vertrag → Einstellungen | — neu | Die Quellen gehören zu verschiedenen Räumen. Wähle einen Raum aus. | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.room.missing | Vertrag → Einstellungen | — neu | Dieser Bereich ist in Home Assistant nicht mehr vorhanden. Der bisherige Name bleibt erhalten. | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.room.group | Vertragsliste → Gruppierung | — neu | Nach Raum ordnen | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.room.all | Vertragsliste → Filter | — neu | Alle Räume | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.retention.title | Einstellungen → Menü und Seite | — neu | Aufbewahrung | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.retention.description | Aufbewahrung → Kopf | — neu | Hier kannst du festlegen, wie lange Mimir Messwerte aufbewahrt. | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.retention.rawDays | Aufbewahrung → Formular | — neu | Einzelmessungen aufbewahren (Tage) | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.retention.rawHelp | Aufbewahrung → Formular | — neu | So lange bleiben einzelne Messungen und ihre Nachweise im Verlauf erhalten. Bereits benötigte Nachweise können länger erhalten bleiben. | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.retention.rollupDays | Aufbewahrung → Formular | — neu | Stundenwerte aufbewahren (Tage) | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.retention.rollupHelp | Aufbewahrung → Formular | — neu | Mimir fasst ältere Zahlenwerte stündlich zusammen. Diese Zusammenfassungen ersetzen keine einzelnen Messungen. | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.retention.suggestion | Aufbewahrung → Formular | — neu | Vorschlag: 7 Tage für Einzelmessungen und 730 Tage für Stundenwerte. Noch ist nichts gespeichert. | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.retention.relationError | Aufbewahrung → Feldfehler | — neu | Bewahre Stundenwerte mindestens so lange auf wie Einzelmessungen. | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.retention.rawRange | Aufbewahrung → Feldfehler | — neu | Gib eine ganze Zahl zwischen 1 und 3650 ein. | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.retention.rollupRange | Aufbewahrung → Feldfehler | — neu | Gib eine ganze Zahl zwischen 1 und 36500 ein. | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.retention.save | Aufbewahrung → Hauptknopf | — neu | Im Entwurf speichern | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.retention.pending | Aufbewahrung → Bestätigung | — neu | Die Regel ist im Entwurf gespeichert. Sie gilt erst, wenn du ihn prüfst und übernimmst. | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.retention.deleteEffect | Übernehmen → Aufbewahrung | — neu | Messungen außerhalb der neuen Frist können endgültig entfernt werden. Späteres Verlängern holt entfernte Messungen nicht zurück. | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.retention.batch | Aufbewahrung → Erweitert | — neu | Messungen je Verarbeitungsschritt | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.retention.interval | Aufbewahrung → Erweitert | — neu | Abstand der Verarbeitungsschritte (Sekunden) | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.readiness.retentionMissing | Plakette und System | — neu | Aufbewahrung fehlt | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.readiness.retentionLink | Plakette und System | — neu | Aufbewahrung festlegen | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.readiness.noConfiguration | Plakette und System | — neu | Noch keine Konfiguration übernommen | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.readiness.configurationLink | Plakette und System | — neu | Entwurf öffnen | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.readiness.notCheckable | Plakette und System | — neu | Noch nicht prüfbar | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.readiness.open | System → Hauptknopf | — neu | Offene Punkte ansehen | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.readiness.empty | Plakette und System | — neu | Alle Voraussetzungen sind erfüllt. | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.manual.title | Quellen → Hinzufügen | — neu | Manuelle Quelle hinzufügen | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.manual.description | Manuelle Quelle → Kopf | — neu | Hier kannst du eine eigene Angabe eintragen und ihre Gültigkeit festlegen. | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.manual.enter | Manuelle Quelle → Hauptknopf | — neu | Angabe eintragen | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.manual.value | Manuelle Quelle → Formular | — neu | Deine Angabe | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.manual.validFrom | Manuelle Quelle → Formular | — neu | Gültig ab | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.manual.validUntil | Manuelle Quelle → Formular | — neu | Gültig bis | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.manual.unbounded | Manuelle Quelle → Formular | — neu | Bis ich die Angabe ändere | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.manual.unboundedConfirm | Manuelle Quelle → Bestätigung | — neu | Diese Angabe bleibt ohne Frist gültig. Ich nehme sie selbst zurück, wenn sie nicht mehr stimmt. | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.manual.origin | Vertrag und Quelle → Herkunft | — neu | Manuell eingegeben | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.manual.recorded | Manuelle Quelle → Bestätigung | — neu | Deine Angabe wurde gespeichert. Die verknüpften Verträge werden damit neu ausgewertet. | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.manual.retract | Manuelle Quelle → Nebenaktion | — neu | Angabe zurücknehmen | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.manual.expired | Manuelle Quelle und Vertrag | — neu | Diese Angabe ist nicht mehr gültig. | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.manual.notYet | Manuelle Quelle und Vertrag | — neu | Diese Angabe gilt erst ab {time}. | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.manual.unknownResult | Manuelle Quelle → Ergebnis | — neu | Das Ergebnis ist noch unklar. Frage zuerst den gespeicherten Stand ab, bevor du die Angabe erneut sendest. | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.notifications.title | Einstellungen → Menü und Seite | — neu | Benachrichtigungen | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.notifications.description | Benachrichtigungen → Kopf | — neu | Hier kannst du festlegen, welche Hinweise Mimir in Home Assistant zeigt. | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.notifications.signal | Benachrichtigungen → Formular | — neu | Bei gestörten Signalen benachrichtigen | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.notifications.configuration | Benachrichtigungen → Formular | — neu | Auf fehlende Angaben hinweisen | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.notifications.configurationHelp | Benachrichtigungen → Formular | — neu | Ein verwendbarer Wert mit fehlender Zuordnung ist kein gestörtes Signal. Hinweise dazu werden getrennt gesammelt. | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.notifications.delay | Benachrichtigungen → Formular | — neu | Erst melden, wenn das Problem so lange besteht (Sekunden) | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.notifications.clearDelay | Benachrichtigungen → Formular | — neu | Als behoben melden nach (Sekunden) | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.notifications.updateDelay | Benachrichtigungen → Formular | — neu | Geänderte Meldung frühestens nach (Sekunden) | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.notifications.maxItems | Benachrichtigungen → Formular | — neu | Höchstens so viele Verträge in einer Meldung nennen | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.notifications.preview | Benachrichtigungen → Vorschau | — neu | So sieht der Hinweis aus. Es wird keine Nachricht gesendet. | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.notifications.signalTitle | HA-Hinweis | — neu | Mimir: Signal gestört | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.notifications.configTitle | HA-Hinweis | — neu | Mimir: Angaben fehlen | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.notifications.signalSummary | HA-Hinweis | — neu | {count} Werte sind nicht sicher bekannt. Öffne die Problemliste, um die Ursachen zu prüfen. | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.notifications.configSummary | HA-Hinweis | — neu | Bei {count} Werten fehlen noch Angaben. Die Hinweise stehen getrennt von gestörten Signalen. | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.calendar.add | Quellen → Hinzufügen | — neu | Kalender hinzufügen | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.calendar.windowPast | Kalenderquelle → Formular | — neu | Vergangene Tage einlesen | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.calendar.windowFuture | Kalenderquelle → Formular | — neu | Kommende Tage einlesen | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.calendar.refresh | Kalenderquelle → Formular | — neu | Neu lesen nach (Minuten) | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.calendar.validFor | Kalenderquelle → Formular | — neu | Ohne neue Antwort gültig für (Minuten) | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.calendar.lastRead | Kalenderquelle → Status | — neu | Zuletzt gelesen | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.calendar.readAgain | Kalenderquelle → Nebenaktion | — neu | Kalender erneut lesen | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.calendar.expired | Kalenderquelle → Status | — neu | Der Kalender konnte nicht rechtzeitig neu gelesen werden. Die bisherigen Termine sind nicht mehr als aktuell bestätigt. | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.calendar.empty | Kalenderquelle → Vorschau | — neu | Für diesen Zeitraum sind keine Termine eingetragen. | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.sensor.profile | Quelle → Einstellungen | — neu | Sensorprüfung | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.sensor.unchangedFor | Quelle → Sensorprüfung | — neu | Verdacht nach unverändertem Wert für (Tage) | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.sensor.tolerance | Quelle → Sensorprüfung | — neu | Unterschiede bis zu diesem Wert ignorieren | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.sensor.minReports | Quelle → Sensorprüfung | — neu | Mindestens so viele neue Meldungen prüfen | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.sensor.recovery | Quelle → Sensorprüfung | — neu | So viele abweichende Meldungen beenden den Verdacht | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.sensor.reference | Quelle → Sensorprüfung | — neu | Zusätzlich mit dieser Quelle vergleichen | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.sensor.suspicious | Quelle und Vertrag → Wert | — neu | Wert seit ungewöhnlich langer Zeit unverändert | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.sensor.help | Quelle → Sensorprüfung | — neu | Gleiche Werte sind nicht automatisch falsch. Regelmäßige Meldungen und die Art des Sensors werden getrennt geprüft. | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.valueOrigin.label | Quelle und Vertrag → Herkunft | — neu | Art des Werts | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.valueOrigin.measured | Herkunftsauswahl und Wert | — neu | Gemessen | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.valueOrigin.replacement | Herkunftsauswahl und Wert | — neu | Ersatz | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.valueOrigin.model | Herkunftsauswahl und Wert | — neu | Modell | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.valueOrigin.forecast | Herkunftsauswahl und Wert | — neu | Prognose | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.valueOrigin.modelHelp | Herkunft → Erklärung | — neu | Der Wert wurde aus einem Modell berechnet und nicht direkt am Gerät gemessen. | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.valueOrigin.replacementHelp | Herkunft → Erklärung | — neu | Eine ausdrücklich gewählte andere Quelle liefert diesen Wert. | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.valueOrigin.forecastHelp | Herkunft → Erklärung | — neu | Der Wert ist eine Vorhersage für den angegebenen Zeitraum. | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.valueOrigin.unknown | Vertrag → Herkunft | — neu | Art der Herkunft nicht bekannt | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.context.automatic | Vertrag → Auslöser | — neu | Änderung durch bekannte Automatik | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.context.unknown | Vertrag → Auslöser | — neu | Auslöser nicht sicher bekannt | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.refresh.title | Vertrag → Einstellungen | — neu | Quellen erneut abfragen | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.refresh.trigger | Erneute Abfrage → Formular | — neu | Dieser Vertrag löst die Abfrage aus | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.refresh.targets | Erneute Abfrage → Formular | — neu | Diese Quellen abfragen | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.refresh.attempts | Erneute Abfrage → Formular | — neu | Versuche und Wartezeiten | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.refresh.window | Erneute Abfrage → Formular | — neu | Nach dieser Zeit keine weiteren Versuche (Sekunden) | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.refresh.cooldown | Erneute Abfrage → Formular | — neu | Frühester neuer Abfragelauf nach (Sekunden) | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.refresh.unsupported | Erneute Abfrage → Auswahl | — neu | Diese Quelle kann nicht erneut abgefragt werden. | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.refresh.requested | Erneute Abfrage → Status | — neu | Erneut angefragt | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.refresh.received | Erneute Abfrage → Status | — neu | Neue Meldung erhalten | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.refresh.noReport | Erneute Abfrage → Status | — neu | Keine neue Meldung | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.refresh.help | Erneute Abfrage → Erklärung | — neu | Eine Anfrage macht den bisherigen Wert nicht aktueller. Dafür muss die Quelle eine neue Meldung liefern. | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.deadline.duration | Vorlage → Ablauf → Zustand | — neu | Zeit bis zum nächsten Schritt | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.deadline.reset | Vorlage → Ablauf → Übergang | — neu | Frist neu beginnen | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.deadline.absolute | Vorlage → Ablauf → Übergang | — neu | Zeitpunkt aus einem Eingang | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.deadline.unknown | Vorlage → Ablauf | — neu | Bei fehlenden Werten warten | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.deadline.unknownHelp | Vorlage → Ablauf | — neu | Der Ablauf wartet auf gültige Werte. Das bisherige Fristende bleibt bestehen; die Frist beginnt nicht von vorn. | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |
| alpha9.form.unavailable | Alle normalen Formulare → unbekannter Fehler | — neu | Diese Einstellung konnte nicht verarbeitet werden. Prüfe die markierten Felder. | Neue Fähigkeit / verständlicher Leer-, Fehler- oder Bestätigungszustand; Benni-Review offen. |

## Geprüfte unveränderte Texte

Zusammen mit der Änderungstabelle oben ist dies das vollständige Verzeichnis aller bisherigen Schlüssel. „wie bisher“ übernimmt den vollständigen Text aus der Spalte alt. Jeder Schlüssel erscheint in genau einer dieser beiden Bestandstabellen.

| Schlüssel | Ort in der Oberfläche | alt | neu | Grund |
|---|---|---|---|---|
| post1.state.staleExtra | Vertrag und Vorlage | Zusätzlicher Hinweis: Ein Eingang hat einen veralteten Wert. | wie bisher | Geprüft; beibehalten. |
| post1.state.fieldExtra | Vertrag und Vorlage | Wert „{name}“: {state}. | wie bisher | Geprüft; beibehalten. |
| post1.freshness.livenessRequired | Formular für Vorlage / Quelle / Vertrag | Nur bei diesem Modus nötig: Wähle eine Ja/Nein-Quelle, die meldet, ob das Gerät erreichbar ist. | wie bisher | Geprüft; beibehalten. |
| post1.why.inputAge | Vertrag und Vorlage | Eingang „{name}“: Der zuletzt gemessene Wert ist {age} alt. | wie bisher | Geprüft; beibehalten. |
| post1.why.inputAgeUnknown | Vertrag und Vorlage | Eingang „{name}“: Das Alter seines Werts ist nicht bekannt. | wie bisher | Geprüft; beibehalten. |
| post1.draft.countAfterErrors | Entwurf und Bearbeitung | erst nach Fehlerkorrektur | wie bisher | Geprüft; beibehalten. |
| post1.sourceField.source_type | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Quellenart | wie bisher | Geprüft; beibehalten. |
| post1.sourceField.value_schema/type | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Werttyp | wie bisher | Geprüft; beibehalten. |
| post1.sourceField.value_schema/unit | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Einheit | wie bisher | Geprüft; beibehalten. |
| post1.sourceField.value_schema/value_catalog | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Werteliste | wie bisher | Geprüft; beibehalten. |
| alpha7.freshness.oneMinute | Formular für Vorlage / Quelle / Vertrag; Quellen und Verknüpfungen | = 1 Minute | wie bisher | Geprüft; beibehalten. |
| alpha7.freshness.minutes | Formular für Vorlage / Quelle / Vertrag; Quellen und Verknüpfungen | = {minutes} Minuten | wie bisher | Geprüft; beibehalten. |
| alpha7.draft.changeCount | Entwurf und Bearbeitung; Entwürfe und Konfigurationen | Anzahl der Änderungen | wie bisher | Geprüft; beibehalten. |
| common.file.choose | Gemeinsame Oberfläche / Wertanzeige | Datei auswählen | wie bisher | Geprüft; beibehalten. |
| common.file.empty | Gemeinsame Oberfläche / Wertanzeige | Keine Datei ausgewählt | wie bisher | Geprüft; beibehalten. |
| alpha7.copy.newContractId | Vertrag und Vorlage | vertrag.neu | wie bisher | Geprüft; beibehalten. |
| alpha7.copy.checkIdentifier | Vertrag und Vorlage | Prüfe die Kennung unter Erweitert: nur einfache Buchstaben ohne Umlaute, Zahlen, Punkt und Unterstrich; kein Punkt am Ende. | wie bisher | Geprüft; beibehalten. |
| alpha7.evidence.indexed | Erweitert / Nachweise | {label} {n} | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| alpha7.graph.tooltip | Zusammenhänge | {name} · {id} | wie bisher | Geprüft; beibehalten. |
| alpha7.evidence.table | Erweitert / Nachweise | Gespeicherter Nachweis | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| alpha7.evidence.field | Erweitert / Nachweise | Angabe | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| alpha7.evidence.value | Erweitert / Nachweise | Gespeicherter Wert | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| alpha7.evidence.title | Erweitert / Nachweise | Nachweis einer Quelle | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| alpha7.evidence.source | Erweitert / Nachweise | Quelle auswählen | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| alpha7.evidence.choose | Erweitert / Nachweise | Bitte eine Quelle wählen … | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| alpha7.evidence.noSources | Erweitert / Nachweise | Es gibt noch keine übernommene Quelle. | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| alpha7.evidence.sourcesFailed | Erweitert / Nachweise | Quellen konnten nicht geladen werden | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| alpha7.evidence.observation | Erweitert / Nachweise | Beobachtung {n} | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| alpha7.graph.sourceDetail | Zusammenhänge | Quelle für Vertragswerte | wie bisher | Geprüft; beibehalten. |
| alpha7.graph.templateVersion | Zusammenhänge | Vorlage in Version {n} | wie bisher | Geprüft; beibehalten. |
| alpha7.graph.view | Zusammenhänge | Ansicht der Zusammenhänge | wie bisher | Geprüft; beibehalten. |
| alpha7.graph.zoomIn | Zusammenhänge | Vergrößern | wie bisher | Geprüft; beibehalten. |
| alpha7.graph.zoomOut | Zusammenhänge | Verkleinern | wie bisher | Geprüft; beibehalten. |
| alpha7.graph.readable | Zusammenhänge | Lesbare Ansicht | wie bisher | Geprüft; beibehalten. |
| alpha7.graph.draft | Zusammenhänge | Entwurf | wie bisher | Geprüft; beibehalten. |
| alpha7.graph.noMatch | Zusammenhänge | Für diese Suche gibt es keinen Treffer. | wie bisher | Geprüft; beibehalten. |
| alpha7.versions.note | Entwürfe und Konfigurationen | Notiz zur neuen Version (freiwillig) | wie bisher | Geprüft; beibehalten. |
| alpha7.versions.noteHelp | Entwürfe und Konfigurationen | Zum Beispiel: Temperatursensor im Wohnzimmer ergänzt. Bis zu 256 Zeichen. Die Notiz ändert keine Vertragswerte. | wie bisher | Geprüft; beibehalten. |
| alpha7.versions.advanced | Entwürfe und Konfigurationen | Erweitert: Prüfsumme | wie bisher | Geprüft; beibehalten. |
| alpha7.versions.technicalDiff | Entwürfe und Konfigurationen | Erweitert: technische Änderungen | wie bisher | Geprüft; beibehalten. |
| alpha7.versions.olderOnly | Entwürfe und Konfigurationen | Zurücksetzen ist nur auf eine ältere Version möglich. | wie bisher | Geprüft; beibehalten. |
| alpha7.versions.selectTwo | Entwürfe und Konfigurationen | Wähle zwei Versionen über die Kästchen links aus. | wie bisher | Geprüft; beibehalten. |
| alpha7.versions.activeFailed | Entwürfe und Konfigurationen | Die aktive Version konnte nicht geladen werden. Lade die Seite neu, bevor du eine Version zurücksetzt. | wie bisher | Geprüft; beibehalten. |
| alpha7.versions.actorSystem | Entwürfe und Konfigurationen | System | wie bisher | Geprüft; beibehalten. |
| alpha7.versions.actorToken | Entwürfe und Konfigurationen | Administrator · Zugangsschlüssel | wie bisher | Geprüft; beibehalten. |
| alpha7.versions.actorApp | Entwürfe und Konfigurationen | Administrator · App-Oberfläche | wie bisher | Geprüft; beibehalten. |
| alpha7.versions.actorUnknown | Entwürfe und Konfigurationen | Wer: nicht bekannt | wie bisher | Geprüft; beibehalten. |
| alpha7.restart.title | Vertrag und Vorlage | Ablauf neu starten | wie bisher | Geprüft; beibehalten. |
| alpha7.restart.allow | Formular für Vorlage / Quelle / Vertrag | Administratoren dürfen diesen Ablauf manuell neu starten | wie bisher | Geprüft; beibehalten. |
| alpha7.restart.allowHelp | Formular für Vorlage / Quelle / Vertrag | Standardmäßig aus. Ein manueller Neustart beginnt im festgelegten Startzustand. Er ist bis zur Bestätigung durch gültige Daten ausdrücklich als manuell gekennzeichnet. | wie bisher | Geprüft; beibehalten. |
| alpha7.restart.scope | Vertrag und Vorlage | Nur für einen freigegebenen Ablauf der laufenden Konfiguration. Ein Entwurf erteilt keine Freigabe. | wie bisher | Geprüft; beibehalten. |
| alpha7.restart.marker | Vertrag und Vorlage; Erweitert / Nachweise; Übersicht | Manuell neu gestartet – noch nicht durch Sensordaten bestätigt. | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| alpha7.restart.historyManual | Erweitert / Nachweise | Manueller Neustart; Datenbestätigung war zu diesem Zeitpunkt noch offen. | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| alpha7.restart.historyRequest | Erweitert / Nachweise | Manueller Neustart angefragt | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| alpha7.restart.markerHelp | Übersicht | Prüfe das Gerät und die Neustart-Bedingung. Gültige Daten können den Ablauf bestätigen. Starte ihn nicht wiederholt auf Verdacht neu. | wie bisher | Geprüft; beibehalten. |
| alpha7.restart.warning | Vertrag und Vorlage | Der Startzustand wird manuell gesetzt und ist nicht durch Sensordaten bestätigt. | wie bisher | Geprüft; beibehalten. |
| alpha7.restart.unknown | Vertrag und Vorlage | unbekannt | wie bisher | Geprüft; beibehalten. |
| alpha7.restart.direct_contracts | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Direkt betroffene Verträge | wie bisher | Geprüft; beibehalten. |
| alpha7.restart.indirect_contracts | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Weitere abhängige Verträge | wie bisher | Geprüft; beibehalten. |
| alpha7.restart.noContracts | Vertrag und Vorlage | Keine weiteren Verträge. | wie bisher | Geprüft; beibehalten. |
| alpha7.restart.external | Vertrag und Vorlage | Externe Automationen sind Mimir nicht vollständig bekannt. Prüfe selbst, welche Automationen auf diesen Ablauf oder auf abhängige Verträge reagieren. | wie bisher | Geprüft; beibehalten. |
| alpha7.restart.reason | Vertrag und Vorlage | Warum startest du den Ablauf neu? | wie bisher | Geprüft; beibehalten. |
| alpha7.restart.reasonRequired | Vertrag und Vorlage | Gib einen kurzen Grund für den Neustart an. Er wird im Protokoll gespeichert. | wie bisher | Geprüft; beibehalten. |
| alpha7.restart.confirm | Vertrag und Vorlage | Ich habe die Auswirkungen geprüft. Der Startzustand wird manuell gesetzt und ist nicht durch Sensordaten bestätigt. | wie bisher | Geprüft; beibehalten. |
| alpha7.restart.confirmFirst | Vertrag und Vorlage | Bestätige zuerst die Auswirkungen des manuellen Neustarts. | wie bisher | Geprüft; beibehalten. |
| alpha7.restart.loading | Vertrag und Vorlage | Mimir prüft die Freigabe des laufenden Ablaufs … | wie bisher | Geprüft; beibehalten. |
| alpha7.restart.unavailable | Vertrag und Vorlage | Die Freigabe konnte nicht geprüft werden. Die Aktion benötigt Administratorzugang und eine erreichbare App. | wie bisher | Geprüft; beibehalten. |
| alpha7.restart.reviewAgain | Vertrag und Vorlage | Prüfe und bestätige den Neustart erneut. | wie bisher | Geprüft; beibehalten. |
| alpha7.restart.changed | Vertrag und Vorlage | Der Ablauf oder die Konfigurationsversion hat sich geändert. Schließe das Fenster und prüfe die neue Vorschau. | wie bisher | Geprüft; beibehalten. |
| alpha7.restart.sending | Vertrag und Vorlage | Der Neustart wird verarbeitet … | wie bisher | Geprüft; beibehalten. |
| alpha7.restart.sent | Vertrag und Vorlage | Die Anfrage wurde gesendet. Ihr Ergebnis steht unten. Für eine weitere Aktion ist eine neue Vorschau nötig. | wie bisher | Geprüft; beibehalten. |
| alpha7.restart.rejected | Vertrag und Vorlage | Der Neustart wurde nicht ausgeführt: {reason} | wie bisher | Geprüft; beibehalten. |
| alpha7.restart.execute | Vertrag und Vorlage | Jetzt manuell neu starten | wie bisher | Geprüft; beibehalten. |
| alpha7.restart.close | Vertrag und Vorlage | Schließen | wie bisher | Geprüft; beibehalten. |
| alpha7.restart.lostResponse | Vertrag und Vorlage | Es ist noch unklar, ob die Anfrage ausgeführt wurde. Frage ihr gespeichertes Ergebnis ab, bevor du eine weitere Aktion prüfst. | wie bisher | Geprüft; beibehalten. |
| alpha7.restart.recover | Vertrag und Vorlage | Ergebnis abfragen | wie bisher | Geprüft; beibehalten. |
| alpha7.restart.recovering | Vertrag und Vorlage | Das gespeicherte Ergebnis wird abgefragt … | wie bisher | Geprüft; beibehalten. |
| alpha7.contract.state.manualHelp | Vertrag und Vorlage | Der Ablauf wurde manuell neu gestartet und ist noch nicht durch gültige Sensordaten bestätigt. | wie bisher | Geprüft; beibehalten. |
| codes.manual_restart | Wert-/Ursachenanzeige, dynamisch | Startzustand manuell gesetzt; noch nicht durch Daten bestätigt | wie bisher | Geprüft; beibehalten. |
| codes.restart_not_enabled | Wert-/Ursachenanzeige, dynamisch | Die laufende Ablauf-Vorlage erlaubt keinen manuellen Neustart. Die Freigabe muss zuerst als neue Vorlagenversion übernommen werden. | wie bisher | Geprüft; beibehalten. |
| codes.machine_state_conflict | Wert-/Ursachenanzeige, dynamisch | Der Ablauf hat sich seit der Vorschau verändert. Prüfe und bestätige die neue Vorschau. | wie bisher | Geprüft; beibehalten. |
| codes.contract_disabled | Wert-/Ursachenanzeige, dynamisch | Dieser Vertrag ist ausgeschaltet. | wie bisher | Geprüft; beibehalten. |
| alpha7.move.title | Quellen und Verknüpfungen | Quelle umziehen | wie bisher | Geprüft; beibehalten. |
| alpha7.move.action | Entwürfe und Konfigurationen; Quellen und Verknüpfungen | Quelle mit anderem Typ anlegen | wie bisher | Geprüft; beibehalten. |
| alpha7.move.explanation | Quellen und Verknüpfungen | Lege eine neue Quelle mit anderer Werteart oder Einheit an. Wähle, welche Verträge du umstellen möchtest. Die alte Quelle und ihr Verlauf bleiben erhalten. | wie bisher | Geprüft; beibehalten. |
| alpha7.move.defaultName | Quellen und Verknüpfungen | Neue Quelle | wie bisher | Geprüft; beibehalten. |
| alpha7.move.name | Quellen und Verknüpfungen | Name der neuen Quelle | wie bisher | Geprüft; beibehalten. |
| alpha7.move.type | Quellen und Verknüpfungen | Neue Werteart | wie bisher | Geprüft; beibehalten. |
| alpha7.move.unit | Quellen und Verknüpfungen | Neue Einheit (freiwillig) | wie bisher | Geprüft; beibehalten. |
| alpha7.move.unitHelp | Quellen und Verknüpfungen | Die Einheit beschreibt den Wert. Sie rechnet ihn nicht um. Falls nötig, lege unter Erweitert eine Umrechnung fest. | wie bisher | Geprüft; beibehalten. |
| alpha7.move.device | Quellen und Verknüpfungen | Gerät für die neue Quelle | wie bisher | Geprüft; beibehalten. |
| alpha7.move.deviceHelp | Quellen und Verknüpfungen | Beim selben Gerät müssen alle bisherigen Verwendungen mit umziehen. Für einen Teilumzug wähle ein anderes Gerät. | wie bisher | Geprüft; beibehalten. |
| alpha7.move.currentDevice | Quellen und Verknüpfungen | Bisheriges Gerät beibehalten | wie bisher | Geprüft; beibehalten. |
| alpha7.move.devicesUnavailable | Quellen und Verknüpfungen | Die Geräteliste ist gerade nicht erreichbar. Die bisherige Verbindung bleibt ausgewählt. | wie bisher | Geprüft; beibehalten. |
| alpha7.move.contracts | Quellen und Verknüpfungen | Diese Verträge umstellen | wie bisher | Geprüft; beibehalten. |
| alpha7.move.noContracts | Quellen und Verknüpfungen | Noch kein Vertrag verwendet diese Quelle direkt. | wie bisher | Geprüft; beibehalten. |
| alpha7.move.templateFor | Quellen und Verknüpfungen | Vorlage für {name} | wie bisher | Geprüft; beibehalten. |
| alpha7.move.keepTemplate | Quellen und Verknüpfungen | Bisherige Vorlage beibehalten | wie bisher | Geprüft; beibehalten. |
| alpha7.move.version | Quellen und Verknüpfungen | Version {version} | wie bisher | Geprüft; beibehalten. |
| alpha7.move.adaptTemplate | Quellen und Verknüpfungen | Einfache Gerätevorlagen als neue Version passend anlegen | wie bisher | Geprüft; beibehalten. |
| alpha7.move.templateHelp | Quellen und Verknüpfungen | Mimir kann Vorlagen anpassen, die nur einen Gerätewert weitergeben. Bei eigenen Berechnungen wähle eine passende Vorlagenversion oder bereite sie zuerst vor. | wie bisher | Geprüft; beibehalten. |
| alpha7.move.catalog | Quellen und Verknüpfungen | Erlaubte Werte der neuen Quelle | wie bisher | Geprüft; beibehalten. |
| alpha7.move.catalogRequired | Quellen und Verknüpfungen | Ergänze mindestens einen erlaubten Wert für die Auswahl. | wie bisher | Geprüft; beibehalten. |
| alpha7.move.mapping | Quellen und Verknüpfungen | Werteliste für die Zuordnung | wie bisher | Geprüft; beibehalten. |
| alpha7.move.chooseMapping | Quellen und Verknüpfungen | Werteliste wählen | wie bisher | Geprüft; beibehalten. |
| alpha7.move.mappingRequired | Quellen und Verknüpfungen | Wähle unter Erweitert eine Werteliste, die die Gerätewerte den erlaubten Werten zuordnet. | wie bisher | Geprüft; beibehalten. |
| alpha7.move.sourceGone | Quellen und Verknüpfungen | Die Quelle ist in diesem Entwurf nicht mehr vorhanden. Schließe das Fenster und wähle die Quelle erneut. | wie bisher | Geprüft; beibehalten. |
| alpha7.move.idUsed | Quellen und Verknüpfungen | Diese Kennung wurde schon verwendet. Wähle unter Erweitert eine neue Kennung, damit alte und neue Werte getrennt bleiben. | wie bisher | Geprüft; beibehalten. |
| alpha7.move.loadingHistory | Quellen und Verknüpfungen | Die bisherigen Versionen werden geladen, damit alte Kennungen geschützt bleiben. | wie bisher | Geprüft; beibehalten. |
| alpha7.move.historyUnavailable | Quellen und Verknüpfungen | Die bisherigen Versionen konnten nicht geladen werden. Versuche es erneut, bevor du die neue Quelle anlegst. | wie bisher | Geprüft; beibehalten. |
| alpha7.move.checking | Quellen und Verknüpfungen | Mimir prüft den vollständigen Umzug … | wie bisher | Geprüft; beibehalten. |
| alpha7.move.check | Quellen und Verknüpfungen | Umzug prüfen | wie bisher | Geprüft; beibehalten. |
| alpha7.move.changed | Quellen und Verknüpfungen | Der Entwurf oder die Auswahl hat sich geändert. Prüfe den Umzug erneut. | wie bisher | Geprüft; beibehalten. |
| alpha7.move.fixBeforeMove | Quellen und Verknüpfungen | Der Umzug passt noch nicht zur Konfiguration. Behebe diese Punkte und prüfe erneut. | wie bisher | Geprüft; beibehalten. |
| alpha7.move.checked | Quellen und Verknüpfungen | Umzug geprüft. Direkt umgestellte Verträge: {direct}. Weitere abhängige Verträge: {indirect}. Neue passende Vorlagenversionen: {versions}. | wie bisher | Geprüft; beibehalten. |
| alpha7.move.retained | Quellen und Verknüpfungen | Die alte Quelle und ihr Verlauf bleiben erhalten. Beim selben Gerät wandert die Verbindung zur neuen Quelle. Es werden keine alten Messwerte umgedeutet. | wie bisher | Geprüft; beibehalten. |
| alpha7.move.onlyDraft | Quellen und Verknüpfungen | Du änderst nur den Entwurf. Die laufenden Verträge ändern sich erst nach Prüfen und Übernehmen in der Kopfzeile. | wie bisher | Geprüft; beibehalten. |
| alpha7.move.reviewFirst | Quellen und Verknüpfungen | Prüfe den Umzug, bevor du ihn in den Entwurf übernimmst. | wie bisher | Geprüft; beibehalten. |
| alpha7.template.name | Vertrag und Vorlage | Name (freiwillig) | wie bisher | Geprüft; beibehalten. |
| alpha7.template.nameExample | Vertrag und Vorlage | Zum Beispiel: Fenster offen | wie bisher | Geprüft; beibehalten. |
| alpha7.template.initial | Vertrag und Vorlage | Die neue Vorlage gibt einen Ja/Nein-Eingang unverändert weiter. Danach kannst du ihre Regeln anpassen. | wie bisher | Geprüft; beibehalten. |
| alpha7.template.oneField | Vertrag und Vorlage | 1 Feld | wie bisher | Geprüft; beibehalten. |
| alpha7.template.fields | Vertrag und Vorlage | {count} Felder | wie bisher | Geprüft; beibehalten. |
| alpha7.template.constantAdvanced | Formular für Vorlage / Quelle / Vertrag | Erweitert: Werteart | wie bisher | Geprüft; beibehalten. |
| alpha7.device.keepSettings | Formular für Vorlage / Quelle / Vertrag | Eigene Einstellungen beibehalten | wie bisher | Geprüft; beibehalten. |
| alpha7.device.schemaDetails | Formular für Vorlage / Quelle / Vertrag | Erweitert: Werteart und Einheit | wie bisher | Geprüft; beibehalten. |
| alpha7.device.title | Quellen und Verknüpfungen | Gerät aus Home Assistant hinzufügen | wie bisher | Geprüft; beibehalten. |
| alpha7.device.explanation | Quellen und Verknüpfungen | Wähle ein Gerät. Mimir richtet die nötigen Verbindungen für dich ein. | wie bisher | Geprüft; beibehalten. |
| alpha7.device.withoutDevice | Vertrag und Vorlage; Quellen und Verknüpfungen | Ohne Gerät anlegen | wie bisher | Geprüft; beibehalten. |
| alpha7.device.missingSource | Formular für Vorlage / Quelle / Vertrag | Quelle fehlt? Gerät hinzufügen | wie bisher | Geprüft; beibehalten. |
| alpha7.device.search | Quellen und Verknüpfungen | Gerät suchen | wie bisher | Geprüft; beibehalten. |
| alpha7.device.area | Quellen und Verknüpfungen | Bereich | wie bisher | Geprüft; beibehalten. |
| alpha7.device.domain | Quellen und Verknüpfungen | Geräteart | wie bisher | Geprüft; beibehalten. |
| alpha7.device.allAreas | Quellen und Verknüpfungen | Alle Bereiche | wie bisher | Geprüft; beibehalten. |
| alpha7.device.noArea | Quellen und Verknüpfungen | Ohne Bereich | wie bisher | Geprüft; beibehalten. |
| alpha7.device.allDomains | Quellen und Verknüpfungen | Alle Gerätearten | wie bisher | Geprüft; beibehalten. |
| alpha7.device.domain.sensor | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Messgeräte | wie bisher | Geprüft; beibehalten. |
| alpha7.device.domain.binary_sensor | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Ja/Nein-Sensoren | wie bisher | Geprüft; beibehalten. |
| alpha7.device.domain.light | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Lampen | wie bisher | Geprüft; beibehalten. |
| alpha7.device.domain.switch | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Schalter | wie bisher | Geprüft; beibehalten. |
| alpha7.device.domain.climate | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Heizung und Klima | wie bisher | Geprüft; beibehalten. |
| alpha7.device.domain.cover | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Rollos und Tore | wie bisher | Geprüft; beibehalten. |
| alpha7.device.domain.input_boolean | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Ja/Nein-Helfer | wie bisher | Geprüft; beibehalten. |
| alpha7.device.domain.input_number | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Zahlen-Helfer | wie bisher | Geprüft; beibehalten. |
| alpha7.device.domain.number | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Zahlenwerte | wie bisher | Geprüft; beibehalten. |
| alpha7.device.domain.select | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Auswahllisten | wie bisher | Geprüft; beibehalten. |
| alpha7.device.domain.other | Quellen und Verknüpfungen | Weitere Geräte | wie bisher | Geprüft; beibehalten. |
| alpha7.device.entities | Quellen und Verknüpfungen | Geräte aus Home Assistant | wie bisher | Geprüft; beibehalten. |
| alpha7.device.selectFirst | Quellen und Verknüpfungen | Wähle zuerst links ein Gerät aus. | wie bisher | Geprüft; beibehalten. |
| alpha7.device.unavailable | Quellen und Verknüpfungen | Home Assistant liefert gerade keine Geräteliste. Prüfe die HA-Anbindung unter Einstellungen → Verbindungen. | wie bisher | Geprüft; beibehalten. |
| alpha7.device.noMatches | Quellen und Verknüpfungen | Kein passendes Gerät gefunden. Ändere die Suche oder den Filter. | wie bisher | Geprüft; beibehalten. |
| alpha7.device.previewScope | Quellen und Verknüpfungen | Der angezeigte Gerätewert stammt aus Home Assistant und kann bis zu 15 Sekunden alt sein. Er ersetzt keine Vertragsprüfung. | wie bisher | Geprüft; beibehalten. |
| alpha7.device.name | Formular für Vorlage / Quelle / Vertrag; Quellen und Verknüpfungen | Name | wie bisher | Geprüft; beibehalten. |
| alpha7.device.preset | Formular für Vorlage / Quelle / Vertrag; Quellen und Verknüpfungen | Gerätetyp für die Aktualität | wie bisher | Geprüft; beibehalten. |
| alpha7.device.preset.temperature | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Temperatursensor | wie bisher | Geprüft; beibehalten. |
| alpha7.device.preset.contact | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Fenster-/Türkontakt | wie bisher | Geprüft; beibehalten. |
| alpha7.device.preset.motion | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Bewegungsmelder | wie bisher | Geprüft; beibehalten. |
| alpha7.device.preset.counter | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Zähler | wie bisher | Geprüft; beibehalten. |
| alpha7.device.preset.other | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Anderes Gerät | wie bisher | Geprüft; beibehalten. |
| alpha7.device.contactHelp | Quellen und Verknüpfungen | Ein geschlossenes Fenster kann lange denselben Wert haben. Das Alter allein ist kein Mangel. Prüfe das Lebenszeichen des Geräts oder die HA-Anbindung. | wie bisher | Geprüft; beibehalten. |
| alpha7.device.reused | Quellen und Verknüpfungen | Dieses Gerät ist bereits verknüpft. Seine Quelle wird weiterverwendet; fehlende Typumwandlungen werden ergänzt. Typ und Einheit bleiben erhalten. | wie bisher | Geprüft; beibehalten. |
| alpha7.device.advanced | Formular für Vorlage / Quelle / Vertrag; Quellen und Verknüpfungen | Erweitert | wie bisher | Geprüft; beibehalten. |
| alpha7.device.type | Quellen und Verknüpfungen | Werteart | wie bisher | Geprüft; beibehalten. |
| alpha7.device.idsAutomatic | Quellen und Verknüpfungen | Leere Kennungen ergänzt Mimir automatisch aus dem Namen des Geräts. | wie bisher | Geprüft; beibehalten. |
| alpha7.device.incompatible | Quellen und Verknüpfungen | Dieses Gerät passt nicht zur Werteart oder Einheit des gewählten Eingangs. Wähle ein passendes Gerät. | wie bisher | Geprüft; beibehalten. |
| alpha7.device.badFreshness | Quellen und Verknüpfungen | Gib eine Frist größer als null und bei Bedarf eine Quelle für das Lebenszeichen an. | wie bisher | Geprüft; beibehalten. |
| alpha7.device.saving | Quellen und Verknüpfungen | Das Gerät wird im Entwurf eingerichtet … | wie bisher | Geprüft; beibehalten. |
| alpha7.device.add | Quellen und Verknüpfungen | Gerät hinzufügen | wie bisher | Geprüft; beibehalten. |
| alpha7.device.createContract | Quellen und Verknüpfungen | Vertrag anlegen | wie bisher | Geprüft; beibehalten. |
| alpha7.device.cancel | Quellen und Verknüpfungen | Abbrechen | wie bisher | Geprüft; beibehalten. |
| alpha7.device.choose | Quellen und Verknüpfungen | Bitte wählen | wie bisher | Geprüft; beibehalten. |
| alpha7.device.yes | Quellen und Verknüpfungen | Ja | wie bisher | Geprüft; beibehalten. |
| alpha7.device.no | Quellen und Verknüpfungen | Nein | wie bisher | Geprüft; beibehalten. |
| alpha7.device.valueMissing | Quellen und Verknüpfungen | Wert noch nicht bekannt | wie bisher | Geprüft; beibehalten. |
| alpha7.device.duplicateSource | Quellen und Verknüpfungen | Diese Quellenkennung ist bereits vergeben. Wähle unter Erweitert eine andere oder lasse das Feld leer. | wie bisher | Geprüft; beibehalten. |
| alpha7.device.duplicateContract | Quellen und Verknüpfungen | Diese Vertragskennung ist bereits vergeben. Wähle unter Erweitert eine andere oder lasse das Feld leer. | wie bisher | Geprüft; beibehalten. |
| alpha7.device.advancedMapping | Quellen und Verknüpfungen | Diese Quelle benötigt eine eigene Werteliste. Prüfe ihre Verknüpfung unter Quellen → Verknüpfungen. | wie bisher | Geprüft; beibehalten. |
| alpha7.device.passthroughName | Quellen und Verknüpfungen | Gerätewert: {name} | wie bisher | Geprüft; beibehalten. |
| alpha7.device.contractGone | Quellen und Verknüpfungen | Der Vertrag fehlt im aktuellen Entwurf. Öffne den gewünschten Vertrag erneut. | wie bisher | Geprüft; beibehalten. |
| alpha7.device.invalidConfig | Quellen und Verknüpfungen | Der Entwurf enthält noch unvollständige Listen. Prüfe und korrigiere ihn vor dem Hinzufügen eines Geräts. | wie bisher | Geprüft; beibehalten. |
| alpha7.device.missingConfiguredSource | Quellen und Verknüpfungen | Die vorhandene Verknüpfung verweist auf eine fehlende Quelle. Prüfe zuerst diese Verknüpfung. | wie bisher | Geprüft; beibehalten. |
| alpha7.freshness.mode | Quellen und Verknüpfungen | Wann gilt der Wert als aktuell? | wie bisher | Geprüft; beibehalten. |
| alpha7.freshness.interval | Quellen und Verknüpfungen | Frist in Sekunden | wie bisher | Geprüft; beibehalten. |
| alpha7.freshness.liveness | Quellen und Verknüpfungen | Quelle für das Lebenszeichen | wie bisher | Geprüft; beibehalten. |
| alpha7.freshness.event_stateful | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Bis zur nächsten Änderung | wie bisher | Geprüft; beibehalten. |
| alpha7.freshness.report_heartbeat | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Regelmäßiges Lebenszeichen | wie bisher | Geprüft; beibehalten. |
| alpha7.freshness.report_heartbeatHelp | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Das Gerät muss innerhalb der Frist eine Meldung senden, auch wenn sein Wert gleich bleibt. | wie bisher | Geprüft; beibehalten. |
| alpha7.freshness.periodic_ttl | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Regelmäßiger Messwert | wie bisher | Geprüft; beibehalten. |
| alpha7.freshness.periodic_ttlHelp | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Der Messzeitpunkt darf höchstens so lange zurückliegen wie die Frist. | wie bisher | Geprüft; beibehalten. |
| alpha7.freshness.liveness_source | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Lebenszeichen eines anderen Geräts | wie bisher | Geprüft; beibehalten. |
| alpha7.freshness.liveness_sourceHelp | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Eine andere Ja/Nein-Quelle bestätigt, dass dieses Gerät noch erreichbar ist. | wie bisher | Geprüft; beibehalten. |
| alpha7.import.openFirst | Entwürfe und Konfigurationen | Öffne zuerst den eingelesenen Entwurf. Bestätige dafür den Wechsel oder wähle ihn unter Entwürfe aus. | wie bisher | Geprüft; beibehalten. |
| codes.request_b | Wert-/Ursachenanzeige, dynamisch | Zustand B anfordern | wie bisher | Geprüft; beibehalten. |
| codes.request_b_if | Wert-/Ursachenanzeige, dynamisch | Zustand B nach Bestätigung anfordern | wie bisher | Geprüft; beibehalten. |
| alpha7.contract.name | Vertrag und Vorlage | Name | wie bisher | Geprüft; beibehalten. |
| alpha7.contract.value | Vertrag und Vorlage | Wert | wie bisher | Geprüft; beibehalten. |
| alpha7.contract.state | Vertrag und Vorlage | Zustand | wie bisher | Geprüft; beibehalten. |
| alpha7.contract.source | Vertrag und Vorlage; Quellen und Verknüpfungen | Quelle | wie bisher | Geprüft; beibehalten. |
| alpha7.contract.noValue | Vertrag und Vorlage | Noch kein Wert | wie bisher | Geprüft; beibehalten. |
| alpha7.contract.noSource | Vertrag und Vorlage | Kein Gerät verknüpft | wie bisher | Geprüft; beibehalten. |
| alpha7.contract.state.draft | Vertrag und Vorlage | Entwurf | wie bisher | Geprüft; beibehalten. |
| alpha7.contract.state.draftHelp | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Dieser Vertrag gehört zum Entwurf und liefert erst nach dem Übernehmen Werte. | wie bisher | Geprüft; beibehalten. |
| alpha7.contract.state.off | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Ausgeschaltet | wie bisher | Geprüft; beibehalten. |
| alpha7.contract.state.offHelp | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Dieser Vertrag ist ausgeschaltet und liefert keine neuen Werte. | wie bisher | Geprüft; beibehalten. |
| alpha7.contract.state.unknown | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Unbekannt | wie bisher | Geprüft; beibehalten. |
| alpha7.contract.state.unknownHelp | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Ein benötigter Wert ist noch nicht sicher bekannt. | wie bisher | Geprüft; beibehalten. |
| alpha7.contract.state.oldConnectionHelp | Vertrag und Vorlage | Die Verbindung wird geprüft; der angezeigte Wert ist der letzte bekannte Stand. | wie bisher | Geprüft; beibehalten. |
| alpha7.contract.state.limited | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Eingeschränkt | wie bisher | Geprüft; beibehalten. |
| alpha7.contract.state.healthy | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Gesund | wie bisher | Geprüft; beibehalten. |
| alpha7.contract.now | Vertrag und Vorlage | Wert jetzt | wie bisher | Geprüft; beibehalten. |
| alpha7.contract.why | Vertrag und Vorlage | Warum? | wie bisher | Geprüft; beibehalten. |
| alpha7.contract.where | Vertrag und Vorlage | Woher? | wie bisher | Geprüft; beibehalten. |
| alpha7.contract.history | Vertrag und Vorlage | Verlauf | wie bisher | Geprüft; beibehalten. |
| alpha7.contract.advanced | Vertrag und Vorlage | Erweitert | wie bisher | Geprüft; beibehalten. |
| alpha7.contract.chart | Vertrag und Vorlage | Verlauf: {name} | wie bisher | Geprüft; beibehalten. |
| alpha7.contract.noHistoryValue | Vertrag und Vorlage | Hier gibt es noch keine darstellbaren Werte. | wie bisher | Geprüft; beibehalten. |
| alpha7.contract.historyTable | Vertrag und Vorlage | Messpunkte als Tabelle | wie bisher | Geprüft; beibehalten. |
| alpha7.contract.time | Vertrag und Vorlage | Zeit | wie bisher | Geprüft; beibehalten. |
| alpha7.contract.historyUnavailable | Vertrag und Vorlage | Der Verlauf konnte nicht geladen werden. | wie bisher | Geprüft; beibehalten. |
| alpha7.contract.namesUnavailable | Vertrag und Vorlage | Die Namen aus Home Assistant sind gerade nicht erreichbar. Gespeicherte Namen werden angezeigt. | wie bisher | Geprüft; beibehalten. |
| alpha7.contract.draftHelp | Vertrag und Vorlage | Dieser Vertrag gehört zum Entwurf. Prüfe ihn und wähle Übernehmen, damit er Werte liefern kann. | wie bisher | Geprüft; beibehalten. |
| alpha7.overview.actions | Übersicht | Schnellaktionen | wie bisher | Geprüft; beibehalten. |
| alpha7.overview.newContract | Vertrag und Vorlage; Übersicht | Neuer Vertrag | wie bisher | Geprüft; beibehalten. |
| alpha7.overview.apply | Übersicht | Änderungen übernehmen | wie bisher | Geprüft; beibehalten. |
| alpha7.overview.activeOnly | Übersicht | Gesund und eingeschränkt zählen nur eingeschaltete Verträge. | wie bisher | Geprüft; beibehalten. |
| alpha7.overview.active | Übersicht | eingeschaltet | wie bisher | Geprüft; beibehalten. |
| alpha7.overview.healthy | Dynamische Beschriftung; Namensraum im Quellcode erhalten | gesund | wie bisher | Geprüft; beibehalten. |
| alpha7.overview.degraded | Dynamische Beschriftung; Namensraum im Quellcode erhalten | eingeschränkt | wie bisher | Geprüft; beibehalten. |
| alpha7.overview.off | Dynamische Beschriftung; Namensraum im Quellcode erhalten | ausgeschaltet | wie bisher | Geprüft; beibehalten. |
| alpha7.overview.contractsUnavailable | Übersicht | Die Vertragsliste konnte nicht geladen werden. | wie bisher | Geprüft; beibehalten. |
| alpha7.overview.waitingValues | Übersicht | Die aktuellen Werte sind noch nicht bekannt. | wie bisher | Geprüft; beibehalten. |
| alpha7.overview.needHelp | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Diese Verträge brauchen Hilfe | wie bisher | Geprüft; beibehalten. |
| alpha7.overview.problemsUnavailable | Übersicht | Die Probleme konnten nicht geladen werden. | wie bisher | Geprüft; beibehalten. |
| alpha7.overview.noProblems | Übersicht | Zurzeit sind keine Probleme gemeldet. | wie bisher | Geprüft; beibehalten. |
| alpha7.overview.moreProblems | Übersicht | {count} weitere Verträge mit Problemen ansehen | wie bisher | Geprüft; beibehalten. |
| alpha7.overview.events | Übersicht | Letzte Ereignisse | wie bisher | Geprüft; beibehalten. |
| alpha7.overview.eventsUnavailable | Übersicht | Ein Teil der Ereignisse konnte nicht geladen werden. | wie bisher | Geprüft; beibehalten. |
| alpha7.overview.noEvents | Übersicht | Hier gibt es noch keine Ereignisse. | wie bisher | Geprüft; beibehalten. |
| alpha7.overview.allLog | Übersicht | Alle im Protokoll | wie bisher | Geprüft; beibehalten. |
| alpha7.problem.invalid | Übersicht | Ein Wert passt nicht zu den Regeln dieses Vertrags. | wie bisher | Geprüft; beibehalten. |
| alpha7.problem.invalidHelp | Übersicht | Prüfe die Eingänge und die Berechnung des Vertrags. | wie bisher | Geprüft; beibehalten. |
| alpha7.problem.inputs | Übersicht | Eingänge prüfen | wie bisher | Geprüft; beibehalten. |
| alpha7.problem.machine | Übersicht | Der Ablauf kennt seinen Zustand noch nicht sicher. | wie bisher | Geprüft; beibehalten. |
| alpha7.problem.machineHelp | Übersicht | Öffne den Vertrag und prüfe, welche Angaben dem Ablauf fehlen. | wie bisher | Geprüft; beibehalten. |
| alpha7.problem.contract | Übersicht | Vertrag öffnen | wie bisher | Geprüft; beibehalten. |
| alpha7.problem.stale | Übersicht | Ein benötigter Wert ist zu alt. | wie bisher | Geprüft; beibehalten. |
| alpha7.problem.staleHelp | Übersicht | Prüfe, ob das Gerät neue Werte sendet und ob die Frist zur Art des Geräts passt. | wie bisher | Geprüft; beibehalten. |
| alpha7.problem.source | Übersicht | Quelle prüfen | wie bisher | Geprüft; beibehalten. |
| alpha7.problem.unavailable | Übersicht | Ein benötigtes Gerät ist gerade nicht erreichbar. | wie bisher | Geprüft; beibehalten. |
| alpha7.problem.connectionHelp | Übersicht | Prüfe die Verbindung zu Home Assistant und danach das betroffene Gerät. | wie bisher | Geprüft; beibehalten. |
| alpha7.problem.connection | Übersicht | Verbindungen prüfen | wie bisher | Geprüft; beibehalten. |
| alpha7.problem.partial | Übersicht | Für diesen Wert fehlen noch Angaben. | wie bisher | Geprüft; beibehalten. |
| alpha7.problem.partialHelp | Übersicht | Prüfe, ob alle benötigten Geräte verbunden sind und Werte liefern. | wie bisher | Geprüft; beibehalten. |
| alpha7.problem.unknown | Übersicht | Ein benötigter Wert ist noch nicht sicher bekannt. | wie bisher | Geprüft; beibehalten. |
| alpha7.problem.unknownHelp | Übersicht | Prüfe die Quelle und ihre Verbindung zum Gerät. | wie bisher | Geprüft; beibehalten. |
| alpha7.event.activate | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Version {version} übernommen | wie bisher | Geprüft; beibehalten. |
| alpha7.event.rollback | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Version {version} durch Zurücksetzen übernommen | wie bisher | Geprüft; beibehalten. |
| alpha7.event.contract_stale | Dynamische Beschriftung; Namensraum im Quellcode erhalten | {name}: Wert veraltet | wie bisher | Geprüft; beibehalten. |
| alpha7.event.contract_error | Dynamische Beschriftung; Namensraum im Quellcode erhalten | {name}: Fehler erkannt | wie bisher | Geprüft; beibehalten. |
| alpha7.event.ha_connected | Dynamische Beschriftung; Namensraum im Quellcode erhalten | HA-Anbindung verbunden | wie bisher | Geprüft; beibehalten. |
| alpha7.event.ha_disconnected | Dynamische Beschriftung; Namensraum im Quellcode erhalten | HA-Anbindung getrennt | wie bisher | Geprüft; beibehalten. |
| alpha7.time.now | Gemeinsame Oberfläche / Wertanzeige | gerade eben | wie bisher | Geprüft; beibehalten. |
| alpha7.time.unknown | Gemeinsame Oberfläche / Wertanzeige | Zeit unbekannt | wie bisher | Geprüft; beibehalten. |
| alpha7.time.minutes | Gemeinsame Oberfläche / Wertanzeige | vor {count} Min. | wie bisher | Geprüft; beibehalten. |
| alpha7.time.hours | Gemeinsame Oberfläche / Wertanzeige | vor {count} Std. | wie bisher | Geprüft; beibehalten. |
| alpha7.time.days | Gemeinsame Oberfläche / Wertanzeige | vor {count} Tagen | wie bisher | Geprüft; beibehalten. |
| alpha7.draft.saving | Entwurf und Bearbeitung | Speichert … | wie bisher | Geprüft; beibehalten. |
| alpha7.draft.templateMissing | Vertrag und Vorlage | Diese Vorlage fehlt im offenen Entwurf. Wähle dort eine vorhandene Vorlage oder lege eine neue an. | wie bisher | Geprüft; beibehalten. |
| alpha7.mode.label | Entwurf und Bearbeitung | Ansicht | wie bisher | Geprüft; beibehalten. |
| alpha7.mode.edit | Entwurf und Bearbeitung | Bearbeiten | wie bisher | Geprüft; beibehalten. |
| alpha7.draft.changedDuringAction | Entwurf und Bearbeitung | Der Entwurf hat sich während der Vorbereitung geändert. Bitte erneut prüfen. | wie bisher | Geprüft; beibehalten. |
| alpha7.draft.noDraft | Entwurf und Bearbeitung | Öffne zuerst einen Entwurf. | wie bisher | Geprüft; beibehalten. |
| alpha7.draft.saveBeforeReview | Entwurf und Bearbeitung | Der Entwurf konnte nicht gespeichert werden. Kläre zuerst die angezeigte Meldung. | wie bisher | Geprüft; beibehalten. |
| alpha7.draft.preparing | Entwurf und Bearbeitung; Vertrag und Vorlage | Ein Entwurf wird vorbereitet. | wie bisher | Geprüft; beibehalten. |
| alpha7.draft.checking | Entwurf und Bearbeitung; Entwürfe und Konfigurationen | Prüfung läuft … | wie bisher | Geprüft; beibehalten. |
| alpha7.draft.checkFailed | Entwurf und Bearbeitung | Prüfung nicht möglich | wie bisher | Geprüft; beibehalten. |
| alpha7.draft.errors | Entwurf und Bearbeitung | {count} Fehler | wie bisher | Geprüft; beibehalten. |
| alpha7.draft.recheck | Entwurf und Bearbeitung |  · erneut prüfen | wie bisher | Geprüft; beibehalten. |
| alpha7.draft.changed | Entwurf und Bearbeitung; Entwürfe und Konfigurationen | Änderungen noch einmal prüfen | wie bisher | Geprüft; beibehalten. |
| alpha7.draft.noErrors | Entwurf und Bearbeitung | Keine Fehler | wie bisher | Geprüft; beibehalten. |
| alpha7.draft.checkResult | Entwurf und Bearbeitung | Prüfergebnis | wie bisher | Geprüft; beibehalten. |
| alpha7.draft.close | Entwurf und Bearbeitung | Schließen | wie bisher | Geprüft; beibehalten. |
| alpha7.draft.preparingReview | Entwurf und Bearbeitung | Übernehmen wird vorbereitet … | wie bisher | Geprüft; beibehalten. |
| alpha7.draft.apply | Entwurf und Bearbeitung | Übernehmen | wie bisher | Geprüft; beibehalten. |
| alpha7.draft.oneChange | Entwurf und Bearbeitung; Entwürfe und Konfigurationen | 1 Änderung | wie bisher | Geprüft; beibehalten. |
| alpha7.draft.changes | Entwurf und Bearbeitung; Entwürfe und Konfigurationen | {count} Änderungen | wie bisher | Geprüft; beibehalten. |
| alpha7.draft.notSaved | Entwurf und Bearbeitung | noch nicht gespeichert | wie bisher | Geprüft; beibehalten. |
| alpha7.draft.saved | Entwurf und Bearbeitung | im Entwurf gespeichert | wie bisher | Geprüft; beibehalten. |
| alpha7.draft.more | Entwurf und Bearbeitung | Weitere Entwurfsaktionen | wie bisher | Geprüft; beibehalten. |
| alpha7.draft.switch | Entwurf und Bearbeitung | Entwurf wechseln | wie bisher | Geprüft; beibehalten. |
| alpha7.draft.kept | Entwurf und Bearbeitung | Deine Änderungen bleiben im Entwurf erhalten. | wie bisher | Geprüft; beibehalten. |
| alpha7.status.ready | Kopfleiste / offene Bedingungen | Bereit | wie bisher | Geprüft; beibehalten. |
| alpha7.status.notReady | Kopfleiste / offene Bedingungen | Nicht bereit · {count} | wie bisher | Geprüft; beibehalten. |
| alpha7.status.conditions | Kopfleiste / offene Bedingungen | Offene Bedingungen | wie bisher | Geprüft; beibehalten. |
| alpha7.status.close | Kopfleiste / offene Bedingungen | Statusfenster schließen | wie bisher | Geprüft; beibehalten. |
| alpha7.status.allGood | Kopfleiste / offene Bedingungen | Alle Bedingungen sind erfüllt. | wie bisher | Geprüft; beibehalten. |
| alpha7.status.waiting | Kopfleiste / offene Bedingungen | Die Verbindung wird geprüft. | wie bisher | Geprüft; beibehalten. |
| alpha7.status.empty | Kopfleiste / offene Bedingungen | Lege einen Vertrag an, damit Mimir seine Werte anzeigen kann. | wie bisher | Geprüft; beibehalten. |
| alpha7.status.create | Kopfleiste / offene Bedingungen | Vertrag anlegen | wie bisher | Geprüft; beibehalten. |
| alpha7.status.setup | Kopfleiste / offene Bedingungen | Die Einrichtung ist noch nicht abgeschlossen. | wie bisher | Geprüft; beibehalten. |
| alpha7.status.configure | Kopfleiste / offene Bedingungen | Einrichten | wie bisher | Geprüft; beibehalten. |
| alpha7.status.snapshot | Kopfleiste / offene Bedingungen | Die HA-Anbindung wartet auf die ersten Gerätedaten. | wie bisher | Geprüft; beibehalten. |
| alpha7.status.ha | Kopfleiste / offene Bedingungen | Die HA-Anbindung ist unterbrochen und einige Verträge warten auf aktuelle Werte. | wie bisher | Geprüft; beibehalten. |
| alpha7.status.connection | Kopfleiste / offene Bedingungen | Verbindung prüfen | wie bisher | Geprüft; beibehalten. |
| alpha7.status.system | Kopfleiste / offene Bedingungen | Systemstatus ansehen | wie bisher | Geprüft; beibehalten. |
| alpha7.status.database | Kopfleiste / offene Bedingungen | Mimir erreicht die Datenbank nicht. | wie bisher | Geprüft; beibehalten. |
| alpha7.status.fault | Kopfleiste / offene Bedingungen | Mimir kann gerade einige Anfragen nicht beantworten. | wie bisher | Geprüft; beibehalten. |
| alpha7.status.diagnose | Kopfleiste / offene Bedingungen | Diagnose ansehen | wie bisher | Geprüft; beibehalten. |
| alpha7.nav.overview | Gemeinsame Oberfläche / Wertanzeige; Übersicht | Übersicht | wie bisher | Geprüft; beibehalten. |
| alpha7.nav.contracts | Menü; Übersicht; Quellen und Verknüpfungen | Verträge | wie bisher | Geprüft; beibehalten. |
| alpha7.nav.mine | Menü; Vertrag und Vorlage | Meine Verträge | wie bisher | Geprüft; beibehalten. |
| alpha7.nav.contract | Menü; Vertrag und Vorlage; Übersicht; Entwürfe und Konfigurationen; Quellen und Verknüpfungen | Vertrag | wie bisher | Geprüft; beibehalten. |
| alpha7.nav.contractImport | Menü; Übersicht; Entwürfe und Konfigurationen | Vertrag importieren | wie bisher | Geprüft; beibehalten. |
| alpha7.nav.relations | Menü | Zusammenhänge | wie bisher | Geprüft; beibehalten. |
| alpha7.nav.templates | Menü | Vorlagen | wie bisher | Geprüft; beibehalten. |
| alpha7.nav.ownTemplates | Menü; Vertrag und Vorlage; Quellen und Verknüpfungen | Eigene Vorlagen | wie bisher | Geprüft; beibehalten. |
| alpha7.nav.builtinTemplates | Menü; Vertrag und Vorlage | Eingebaute Vorlagen | wie bisher | Geprüft; beibehalten. |
| alpha7.nav.sources | Menü; Quellen und Verknüpfungen | Quellen | wie bisher | Geprüft; beibehalten. |
| alpha7.nav.devices | Menü; Quellen und Verknüpfungen | Geräte aus Home Assistant | wie bisher | Geprüft; beibehalten. |
| alpha7.nav.bindings | Menü; Quellen und Verknüpfungen | Verknüpfungen | wie bisher | Geprüft; beibehalten. |
| alpha7.nav.catalogs | Menü | Wertelisten | wie bisher | Geprüft; beibehalten. |
| alpha7.nav.drafts | Menü; Entwürfe und Konfigurationen | Entwürfe | wie bisher | Geprüft; beibehalten. |
| alpha7.nav.settings | Menü | Einstellungen | wie bisher | Geprüft; beibehalten. |
| alpha7.nav.connections | Menü | Verbindungen | wie bisher | Geprüft; beibehalten. |
| alpha7.nav.keys | Menü | Zugangsschlüssel | wie bisher | Geprüft; beibehalten. |
| alpha7.nav.log | Menü | Protokoll | wie bisher | Geprüft; beibehalten. |
| alpha7.contract.empty | Vertrag und Vorlage | Noch keine Verträge vorhanden | wie bisher | Geprüft; beibehalten. |
| alpha7.layout.menu | Anordnung der Seitenbereiche | Weitere Seitenaktionen | wie bisher | Geprüft; beibehalten. |
| alpha7.draft.defaultName | Entwurf und Bearbeitung; Entwürfe und Konfigurationen | Änderungen vom {date} | wie bisher | Geprüft; beibehalten. |
| alpha7.import.title | Entwürfe und Konfigurationen | Datei oder Text einlesen | wie bisher | Geprüft; beibehalten. |
| alpha7.import.start | Entwürfe und Konfigurationen | Als Entwurf einlesen und prüfen | wie bisher | Geprüft; beibehalten. |
| alpha7.import.checking | Entwürfe und Konfigurationen | Die Datei wird eingelesen und geprüft. | wie bisher | Geprüft; beibehalten. |
| alpha7.import.limit | Entwurf und Bearbeitung; Entwürfe und Konfigurationen | Es gibt bereits 100 Entwürfe. Entferne zuerst einen nicht mehr benötigten Entwurf. | wie bisher | Geprüft; beibehalten. |
| alpha7.import.empty | Entwurf und Bearbeitung; Entwürfe und Konfigurationen | Wähle eine Datei oder füge den Import-Text ein. | wie bisher | Geprüft; beibehalten. |
| alpha7.import.errors | Entwürfe und Konfigurationen | Der Entwurf enthält {count} Fehler. Korrigiere sie vor dem Übernehmen. | wie bisher | Geprüft; beibehalten. |
| alpha7.import.valid | Entwürfe und Konfigurationen | Prüfung abgeschlossen: keine Fehler. Noch gelten diese Änderungen nicht. | wie bisher | Geprüft; beibehalten. |
| alpha7.import.review | Entwürfe und Konfigurationen | Änderungen ansehen und übernehmen | wie bisher | Geprüft; beibehalten. |
| alpha7.import.fix | Entwürfe und Konfigurationen | Öffne die betroffenen Felder über die Fehlerliste und prüfe den korrigierten Entwurf erneut. | wie bisher | Geprüft; beibehalten. |
| alpha7.export.title | Entwürfe und Konfigurationen | Konfiguration sichern | wie bisher | Geprüft; beibehalten. |
| alpha7.export.active | Entwürfe und Konfigurationen | Übernommene Konfiguration herunterladen | wie bisher | Geprüft; beibehalten. |
| alpha7.export.noActive | Entwürfe und Konfigurationen | Es wurde noch keine Konfiguration übernommen. | wie bisher | Geprüft; beibehalten. |
| alpha7.export.draft | Entwürfe und Konfigurationen | Offenen Entwurf herunterladen | wie bisher | Geprüft; beibehalten. |
| alpha7.settings.databaseMqtt | Einstellungen | Datenbank und MQTT-Verbindung | wie bisher | Geprüft; beibehalten. |
| alpha7.settings.database | Einstellungen | Datenbank | wie bisher | Geprüft; beibehalten. |
| alpha7.settings.mqtt | Einstellungen | MQTT-Verbindung | wie bisher | Geprüft; beibehalten. |
| App.einrichtungsstatus_nicht_erreichbar_weboberflach_04e47b | Gemeinsame Oberfläche / Wertanzeige | Einrichtungsstatus nicht erreichbar. Weboberfläche erneut über Home Assistant öffnen. | wie bisher | Geprüft; beibehalten. |
| App.terra_workbench_7ad523 | Gemeinsame Oberfläche / Wertanzeige | Mimir | wie bisher | Geprüft; beibehalten. |
| App.installationszustand_wird_gepruft_d072db | Gemeinsame Oberfläche / Wertanzeige | Installationszustand wird geprüft … | wie bisher | Geprüft; beibehalten. |
| components.ContractLiveState.stand_moglicherweise_veraltet_42a607 | Gemeinsame Oberfläche / Wertanzeige | Stand möglicherweise veraltet | wie bisher | Geprüft; beibehalten. |
| components.ContractLiveState.contract_a6f5b0 | Gemeinsame Oberfläche / Wertanzeige | Vertrag | wie bisher | Geprüft; beibehalten. |
| components.ContractLiveState.verfugbar_e5a644 | Gemeinsame Oberfläche / Wertanzeige | verfügbar | wie bisher | Geprüft; beibehalten. |
| components.ContractLiveState.nicht_verfugbar_9a98b3 | Gemeinsame Oberfläche / Wertanzeige | nicht verfügbar | wie bisher | Geprüft; beibehalten. |
| components.ContractLiveState.berechnet_65097b | Gemeinsame Oberfläche / Wertanzeige | Berechnet | wie bisher | Geprüft; beibehalten. |
| components.ContractLiveState.felder_b26f0b | Gemeinsame Oberfläche / Wertanzeige | Felder | wie bisher | Geprüft; beibehalten. |
| components.ContractLiveState.frische_b42690 | Gemeinsame Oberfläche / Wertanzeige | Aktualität:  | wie bisher | Geprüft; beibehalten. |
| components.ContractLiveState.gemessen_a9d62c | Gemeinsame Oberfläche / Wertanzeige | Gemessen | wie bisher | Geprüft; beibehalten. |
| components.ContractLiveState.seit_b00312 | Gemeinsame Oberfläche / Wertanzeige | Seit | wie bisher | Geprüft; beibehalten. |
| components.ContractLiveState.eingang_ea63c1 | Gemeinsame Oberfläche / Wertanzeige | Eingang  | wie bisher | Geprüft; beibehalten. |
| components.ContractLiveState.seit_905c7f | Gemeinsame Oberfläche / Wertanzeige | · seit  | wie bisher | Geprüft; beibehalten. |
| components.ContractLiveState.in_der_9c92b1 | Gemeinsame Oberfläche / Wertanzeige | – in der  | wie bisher | Geprüft; beibehalten. |
| components.ContractLiveState.diagnose_64dd65 | Gemeinsame Oberfläche / Wertanzeige | Diagnose | wie bisher | Geprüft; beibehalten. |
| components.ContractLiveState.auflosbar_ac9e6e | Gemeinsame Oberfläche / Wertanzeige | auflösbar. | wie bisher | Geprüft; beibehalten. |
| components.ContractLiveState.state_machine_801376 | Gemeinsame Oberfläche / Wertanzeige | Ablauf | wie bisher | Geprüft; beibehalten. |
| components.MachineRecovery.ablauf_ohne_gultigen_zustand_831755 | Gemeinsame Oberfläche / Wertanzeige | Ablauf ohne gültigen Zustand | wie bisher | Geprüft; beibehalten. |
| components.MachineRecovery.benotigte_eingange_4a111b | Gemeinsame Oberfläche / Wertanzeige | Benötigte Eingänge:  | wie bisher | Geprüft; beibehalten. |
| components.MachineRecovery.gultig_bedingung_noch_nicht_erfullt_a448de | Gemeinsame Oberfläche / Wertanzeige | gültig; Bedingung noch nicht erfüllt | wie bisher | Geprüft; beibehalten. |
| components.MachineRecovery.kein_gultiger_nachweis_7be0f3 | Gemeinsame Oberfläche / Wertanzeige | kein gültiger Nachweis | wie bisher | Geprüft; beibehalten. |
| components.MasterDetail.v0_liste_4816c1 | Gemeinsame Oberfläche / Wertanzeige | {v0}-Liste | wie bisher | Geprüft; beibehalten. |
| components.MasterDetail.v0_suchen_d98fc3 | Gemeinsame Oberfläche / Wertanzeige | {v0} suchen | wie bisher | Geprüft; beibehalten. |
| components.MasterDetail.suchen_51942c | Gemeinsame Oberfläche / Wertanzeige | Suchen … | wie bisher | Geprüft; beibehalten. |
| components.MasterDetail.hinzufugen_cbb95c | Gemeinsame Oberfläche / Wertanzeige | Hinzufügen | wie bisher | Geprüft; beibehalten. |
| components.MasterDetail.noch_keine_eintrage_cce9ab | Gemeinsame Oberfläche / Wertanzeige | Noch keine Einträge. | wie bisher | Geprüft; beibehalten. |
| components.MasterDetail.keine_treffer_5fa5cc | Gemeinsame Oberfläche / Wertanzeige | Keine Treffer. | wie bisher | Geprüft; beibehalten. |
| components.PanelLayout.layout_anpassen_9d4ca3 | Anordnung der Seitenbereiche | Anordnung anpassen | wie bisher | Geprüft; beibehalten. |
| components.PanelLayout.layout_zurucksetzen_5c6f02 | Anordnung der Seitenbereiche | Anordnung zurücksetzen | wie bisher | Geprüft; beibehalten. |
| components.PanelLayout.v0_nach_vorne_f637f0 | Anordnung der Seitenbereiche | {v0}: nach vorne | wie bisher | Geprüft; beibehalten. |
| components.PanelLayout.v0_nach_hinten_9b7af0 | Anordnung der Seitenbereiche | {v0}: nach hinten | wie bisher | Geprüft; beibehalten. |
| components.PanelLayout.schmal_ec22ce | Anordnung der Seitenbereiche | Schmal | wie bisher | Geprüft; beibehalten. |
| components.PanelLayout.mittel_660427 | Anordnung der Seitenbereiche | Mittel | wie bisher | Geprüft; beibehalten. |
| components.PanelLayout.ganze_zeile_701a57 | Anordnung der Seitenbereiche | Ganze Zeile | wie bisher | Geprüft; beibehalten. |
| components.RouteError.die_oberflache_wurde_aktualisiert_121896 | Gemeinsame Oberfläche / Wertanzeige | Die Oberfläche wurde aktualisiert | wie bisher | Geprüft; beibehalten. |
| components.RouteError.dieser_bereich_konnte_nicht_angezeigt_werden_c3b50c | Gemeinsame Oberfläche / Wertanzeige | Dieser Bereich konnte nicht angezeigt werden | wie bisher | Geprüft; beibehalten. |
| components.RouteError.die_geoffnete_seite_stammt_aus_einer_alteren_ver_5380c5 | Gemeinsame Oberfläche / Wertanzeige | Die geöffnete Seite stammt aus einer älteren Version. Bitte neu laden; ungespeicherte Entwurf-Änderungen gehen dabei verloren. | wie bisher | Geprüft; beibehalten. |
| components.RouteError.seite_neu_laden_61e2c2 | Gemeinsame Oberfläche / Wertanzeige | Seite neu laden | wie bisher | Geprüft; beibehalten. |
| components.RouteError.zur_ubersicht_22bfde | Gemeinsame Oberfläche / Wertanzeige | Zur Übersicht | wie bisher | Geprüft; beibehalten. |
| components.Shell.t_e632b7 | Gemeinsame Oberfläche / Wertanzeige | M | wie bisher | Geprüft; beibehalten. |
| components.Shell.terra_workbench_7ad523 | Gemeinsame Oberfläche / Wertanzeige | Mimir | wie bisher | Geprüft; beibehalten. |
| components.Shell.core_contracts_57c8c1 | Gemeinsame Oberfläche / Wertanzeige | Mimir | wie bisher | Geprüft; beibehalten. |
| components.Shell.hauptnavigation_e8fc66 | Gemeinsame Oberfläche / Wertanzeige | Hauptnavigation | wie bisher | Geprüft; beibehalten. |
| components.Shell.navigation_ausklappen_9adc95 | Gemeinsame Oberfläche / Wertanzeige | Navigation ausklappen | wie bisher | Geprüft; beibehalten. |
| components.Shell.navigation_einklappen_6b094c | Gemeinsame Oberfläche / Wertanzeige | Navigation einklappen | wie bisher | Geprüft; beibehalten. |
| components.status-parts.keine_offenen_bedingungen_4c615b | Gemeinsame Oberfläche / Wertanzeige | Keine offenen Bedingungen | wie bisher | Geprüft; beibehalten. |
| components.ui.dialog.schlie_en_b808f6 | Gemeinsame Oberfläche / Wertanzeige | Schließen | wie bisher | Geprüft; beibehalten. |
| components.ui.dialog.abbrechen_f7ff11 | Gemeinsame Oberfläche / Wertanzeige | Abbrechen | wie bisher | Geprüft; beibehalten. |
| components.ui.layout.ladt_c8ebc9 | Gemeinsame Oberfläche / Wertanzeige | Lädt … | wie bisher | Geprüft; beibehalten. |
| editors.common.nach_oben_ed1652 | Formular für Vorlage / Quelle / Vertrag | Nach oben | wie bisher | Geprüft; beibehalten. |
| editors.common.nach_unten_542457 | Formular für Vorlage / Quelle / Vertrag | Nach unten | wie bisher | Geprüft; beibehalten. |
| editors.common.entfernen_382837 | Formular für Vorlage / Quelle / Vertrag | Entfernen | wie bisher | Geprüft; beibehalten. |
| editors.common.v0_entfernen_92fea7 | Formular für Vorlage / Quelle / Vertrag | {v0} entfernen | wie bisher | Geprüft; beibehalten. |
| editors.common.leer_f13f8e | Formular für Vorlage / Quelle / Vertrag | leer | wie bisher | Geprüft; beibehalten. |
| editors.common.hinzufugen_cbb95c | Formular für Vorlage / Quelle / Vertrag | Hinzufügen | wie bisher | Geprüft; beibehalten. |
| editors.common.nicht_im_katalog_fa85e6 | Formular für Vorlage / Quelle / Vertrag | (nicht in der Werteliste) | wie bisher | Geprüft; beibehalten. |
| editors.common.v0_kalender_4c1966 | Formular für Vorlage / Quelle / Vertrag | {v0} (Kalender) | wie bisher | Geprüft; beibehalten. |
| editors.common.ungultiges_json_anderung_noch_nicht_ubernommen_ffa9c9 | Formular für Vorlage / Quelle / Vertrag | Ungültiges JSON – Änderung noch nicht übernommen:  | wie bisher | Geprüft; beibehalten. |
| editors.DefinitionEditor.regel_fur_69dffb | Formular für Vorlage / Quelle / Vertrag | Regel für „ | wie bisher | Geprüft; beibehalten. |
| editors.DefinitionEditor.allgemein_24eddd | Formular für Vorlage / Quelle / Vertrag | Allgemein | wie bisher | Geprüft; beibehalten. |
| editors.DefinitionEditor.synthetischer_test_namensraum_8ac977 | Formular für Vorlage / Quelle / Vertrag | Verwende eine eindeutige Kennung mit mindestens zwei Teilen, zum Beispiel vertrag.temperatur. | wie bisher | Geprüft; beibehalten. |
| editors.DefinitionEditor.muss_mit_test_beginnen_01622a | Formular für Vorlage / Quelle / Vertrag | Trenne die Teile der Kennung mit einem Punkt, zum Beispiel vertrag.temperatur. | wie bisher | Geprüft; beibehalten. |
| editors.DefinitionEditor.version_dd1679 | Formular für Vorlage / Quelle / Vertrag | Version | wie bisher | Geprüft; beibehalten. |
| editors.DefinitionEditor.redaktionelle_felder_andern_die_semantik_nicht_u_20b198 | Formular für Vorlage / Quelle / Vertrag | Name und Beschreibung ändern die Berechnung nicht und bleiben auch nach dem Übernehmen änderbar. | wie bisher | Geprüft; beibehalten. |
| editors.DefinitionEditor.noch_keine_eingange_63d0b8 | Formular für Vorlage / Quelle / Vertrag | Noch keine Eingänge. | wie bisher | Geprüft; beibehalten. |
| editors.DefinitionEditor.eingange_aaae23 | Formular für Vorlage / Quelle / Vertrag | Eingänge  | wie bisher | Geprüft; beibehalten. |
| editors.DefinitionEditor.eingang_d8af5e | Formular für Vorlage / Quelle / Vertrag | Eingang | wie bisher | Geprüft; beibehalten. |
| editors.DefinitionEditor.ohne_eingange_liefert_die_definition_nur_konstan_25c31a | Formular für Vorlage / Quelle / Vertrag | Ohne Eingänge liefert die Vorlage nur Konstanten. | wie bisher | Geprüft; beibehalten. |
| editors.DefinitionEditor.verwendet_cf0908 | Formular für Vorlage / Quelle / Vertrag | × verwendet | wie bisher | Geprüft; beibehalten. |
| editors.DefinitionEditor.name_dcd1d5 | Formular für Vorlage / Quelle / Vertrag | Name | wie bisher | Geprüft; beibehalten. |
| editors.DefinitionEditor.umbenennen_aktualisiert_alle_verweise_in_dieser__746da1 | Formular für Vorlage / Quelle / Vertrag | Umbenennen aktualisiert alle Verweise in dieser Vorlage. Entfernen ist erst ohne Verwendung möglich. | wie bisher | Geprüft; beibehalten. |
| editors.DefinitionEditor.ausgaben_c20af5 | Formular für Vorlage / Quelle / Vertrag | Ausgaben  | wie bisher | Geprüft; beibehalten. |
| editors.DefinitionEditor.benannte_regeln_2d1254 | Formular für Vorlage / Quelle / Vertrag | Benannte Regeln  | wie bisher | Geprüft; beibehalten. |
| editors.DefinitionEditor.regel_4b09cd | Formular für Vorlage / Quelle / Vertrag | Regel | wie bisher | Geprüft; beibehalten. |
| editors.DefinitionEditor.noch_keine_benannten_regeln_161f59 | Formular für Vorlage / Quelle / Vertrag | Noch keine benannten Regeln. | wie bisher | Geprüft; beibehalten. |
| editors.DefinitionEditor.v0_wird_verwendet_e5d823 | Formular für Vorlage / Quelle / Vertrag | {v0} wird verwendet | wie bisher | Geprüft; beibehalten. |
| editors.DefinitionEditor.regel_v0_entfernen_df07a9 | Formular für Vorlage / Quelle / Vertrag | Regel {v0} entfernen | wie bisher | Geprüft; beibehalten. |
| editors.DefinitionEditor.state_machine_670ced | Formular für Vorlage / Quelle / Vertrag | Ablauf  | wie bisher | Geprüft; beibehalten. |
| editors.DefinitionEditor.aktiv_3139fc | Formular für Vorlage / Quelle / Vertrag | aktiv | wie bisher | Geprüft; beibehalten. |
| editors.DefinitionEditor.keine_db028e | Formular für Vorlage / Quelle / Vertrag | keine | wie bisher | Geprüft; beibehalten. |
| editors.DefinitionEditor.state_machine_aus_dieser_definition_entfernen_46ef4d | Formular für Vorlage / Quelle / Vertrag | Ablauf aus dieser Vorlage entfernen | wie bisher | Geprüft; beibehalten. |
| editors.DefinitionEditor.state_machine_hinzufugen_c9125d | Formular für Vorlage / Quelle / Vertrag | Ablauf hinzufügen | wie bisher | Geprüft; beibehalten. |
| editors.DefinitionEditor.definition_9813fa | Formular für Vorlage / Quelle / Vertrag | Vorlage | wie bisher | Geprüft; beibehalten. |
| editors.DefinitionEditor.diese_version_war_bereits_aktiv_faa77f | Formular für Vorlage / Quelle / Vertrag | Diese Version war bereits aktiv. | wie bisher | Geprüft; beibehalten. |
| editors.DefinitionEditor.gesperrt_4a76d6 | Formular für Vorlage / Quelle / Vertrag | gesperrt | wie bisher | Geprüft; beibehalten. |
| editors.Extras.weitere_eigenschaften_v0_b0c6ee | Formular für Vorlage / Quelle / Vertrag | Weitere Eigenschaften ({v0}) | wie bisher | Geprüft; beibehalten. |
| editors.Extras.v0_entfernen_92fea7 | Formular für Vorlage / Quelle / Vertrag | {v0} entfernen | wie bisher | Geprüft; beibehalten. |
| editors.FieldSchemaEditor.typ_1b0241 | Formular für Vorlage / Quelle / Vertrag | Typ | wie bisher | Geprüft; beibehalten. |
| editors.FieldSchemaEditor.einheit_optional_330bf9 | Formular für Vorlage / Quelle / Vertrag | Einheit (freiwillig) | wie bisher | Geprüft; beibehalten. |
| editors.FieldSchemaEditor.z_b_w_c_b73aab | Formular für Vorlage / Quelle / Vertrag | z. B. W, °C | wie bisher | Geprüft; beibehalten. |
| editors.FieldSchemaEditor.pflichtwert_eb4e10 | Formular für Vorlage / Quelle / Vertrag | Pflichtwert | wie bisher | Geprüft; beibehalten. |
| editors.FieldSchemaEditor.physischer_zustand_be93d1 | Formular für Vorlage / Quelle / Vertrag | Physischer Zustand | wie bisher | Geprüft; beibehalten. |
| editors.FieldSchemaEditor.auf_feste_textwerte_einschranken_wertekatalog_29c7a2 | Formular für Vorlage / Quelle / Vertrag | Auf feste Textwerte einschränken (Werteliste) | wie bisher | Geprüft; beibehalten. |
| editors.FieldSchemaEditor.wertekatalog_pflicht_fur_enum_78abf7 | Formular für Vorlage / Quelle / Vertrag | Werteliste (Pflicht für Auswahl) | wie bisher | Geprüft; beibehalten. |
| editors.FieldSchemaEditor.wertekatalog_schrankt_werte_ein_953952 | Formular für Vorlage / Quelle / Vertrag | Werteliste (schränkt Werte ein) | wie bisher | Geprüft; beibehalten. |
| editors.MachineEditor.anfangszustand_da00a2 | Formular für Vorlage / Quelle / Vertrag | Anfangszustand | wie bisher | Geprüft; beibehalten. |
| editors.MachineEditor.sessions_fuhren_a20d63 | Formular für Vorlage / Quelle / Vertrag | Sitzungen führen | wie bisher | Geprüft; beibehalten. |
| editors.MachineEditor.deadline_verwenden_f1deab | Formular für Vorlage / Quelle / Vertrag | Frist verwenden | wie bisher | Geprüft; beibehalten. |
| editors.MachineEditor.deadline_s_5ebf14 | Formular für Vorlage / Quelle / Vertrag | Frist (s) | wie bisher | Geprüft; beibehalten. |
| editors.MachineEditor.eine_deadline_pro_contract_994bde | Formular für Vorlage / Quelle / Vertrag | eine Frist pro Vertrag | wie bisher | Geprüft; beibehalten. |
| editors.MachineEditor.zustand_630d1a | Formular für Vorlage / Quelle / Vertrag | Zustand | wie bisher | Geprüft; beibehalten. |
| editors.MachineEditor.zustande_f5ef55 | Formular für Vorlage / Quelle / Vertrag | Zustände | wie bisher | Geprüft; beibehalten. |
| editors.MachineEditor.zustand_v0_871457 | Formular für Vorlage / Quelle / Vertrag | Zustand {v0} | wie bisher | Geprüft; beibehalten. |
| editors.MachineEditor.v0_wird_verwendet_e5d823 | Formular für Vorlage / Quelle / Vertrag | {v0} wird verwendet | wie bisher | Geprüft; beibehalten. |
| editors.MachineEditor.v0_entfernen_92fea7 | Formular für Vorlage / Quelle / Vertrag | {v0} entfernen | wie bisher | Geprüft; beibehalten. |
| editors.MachineEditor.befehl_c8505b | Formular für Vorlage / Quelle / Vertrag | Befehl | wie bisher | Geprüft; beibehalten. |
| editors.MachineEditor.befehle_23a3b7 | Formular für Vorlage / Quelle / Vertrag | Befehle | wie bisher | Geprüft; beibehalten. |
| editors.MachineEditor.befehl_v0_entfernen_54de54 | Formular für Vorlage / Quelle / Vertrag | Befehl {v0} entfernen | wie bisher | Geprüft; beibehalten. |
| editors.MachineEditor.befehlsname_439d2d | Formular für Vorlage / Quelle / Vertrag | Befehlsname | wie bisher | Geprüft; beibehalten. |
| editors.MachineEditor.argument_481da3 | Formular für Vorlage / Quelle / Vertrag | Argument | wie bisher | Geprüft; beibehalten. |
| editors.MachineEditor.keine_argumente_98a370 | Formular für Vorlage / Quelle / Vertrag | Keine Argumente. | wie bisher | Geprüft; beibehalten. |
| editors.MachineEditor.argument_entfernen_c60b1a | Formular für Vorlage / Quelle / Vertrag | Argument entfernen | wie bisher | Geprüft; beibehalten. |
| editors.MachineEditor.neu_initialisieren_wenn_dd14f7 | Formular für Vorlage / Quelle / Vertrag | Neu initialisieren, wenn … | wie bisher | Geprüft; beibehalten. |
| editors.MachineEditor.neustart_bedingung_fehlt_f0544a | Formular für Vorlage / Quelle / Vertrag | Neustart-Bedingung fehlt | wie bisher | Geprüft; beibehalten. |
| editors.MachineEditor.bedingung_festlegen_0513ca | Formular für Vorlage / Quelle / Vertrag | Bedingung festlegen | wie bisher | Geprüft; beibehalten. |
| editors.MachineEditor.dieser_ablauf_kann_sich_nach_einer_anderung_nie__670fc4 | Formular für Vorlage / Quelle / Vertrag | Dieser Ablauf kann sich nach einer Änderung nie selbst erholen | wie bisher | Geprüft; beibehalten. |
| editors.MachineEditor.legen_sie_eine_bedingung_aus_gultigen_eingangen__95fb96 | Formular für Vorlage / Quelle / Vertrag | Lege eine Bedingung aus gültigen Eingängen fest. | wie bisher | Geprüft; beibehalten. |
| editors.MachineEditor.neustart_wenn_ef87e7 | Formular für Vorlage / Quelle / Vertrag | Neustart, wenn  | wie bisher | Geprüft; beibehalten. |
| editors.MachineEditor.nein_ist_79608c | Formular für Vorlage / Quelle / Vertrag | Nein ist | wie bisher | Geprüft; beibehalten. |
| editors.MachineEditor.transition_2fe704 | Formular für Vorlage / Quelle / Vertrag | Übergang | wie bisher | Geprüft; beibehalten. |
| editors.MachineEditor.transitionen_41ef48 | Formular für Vorlage / Quelle / Vertrag | Übergänge | wie bisher | Geprüft; beibehalten. |
| editors.MachineEditor.von_640e86 | Formular für Vorlage / Quelle / Vertrag | Von | wie bisher | Geprüft; beibehalten. |
| editors.MachineEditor.nach_0ea777 | Formular für Vorlage / Quelle / Vertrag | Nach | wie bisher | Geprüft; beibehalten. |
| editors.MachineEditor.ereignis_af9e77 | Formular für Vorlage / Quelle / Vertrag | Ereignis | wie bisher | Geprüft; beibehalten. |
| editors.MachineEditor.deadline_transitionen_benotigen_eine_deadline_d8a6d2 | Formular für Vorlage / Quelle / Vertrag | Frist-Übergänge benötigen eine Frist. | wie bisher | Geprüft; beibehalten. |
| editors.MachineEditor.grund_b45f40 | Formular für Vorlage / Quelle / Vertrag | Grund | wie bisher | Geprüft; beibehalten. |
| editors.MachineEditor.bedingungen_an_die_befehlsargumente_08ced2 | Formular für Vorlage / Quelle / Vertrag | Bedingungen an die Befehlsargumente | wie bisher | Geprüft; beibehalten. |
| editors.MachineEditor.muss_gleich_sein_4c42df | Formular für Vorlage / Quelle / Vertrag | muss gleich sein | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.art_75df35 | Formular für Vorlage / Quelle / Vertrag | Art | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.uberwachung_93542e | Formular für Vorlage / Quelle / Vertrag | Überwachung | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.internal_die_app_uberwacht_selbst_source_eine_qu_135fdc | Formular für Vorlage / Quelle / Vertrag | Die App kann die Verbindung selbst prüfen. Alternativ meldet eine ausgewählte Quelle, ob das Gerät erreichbar ist. | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.uberwachende_quelle_4f9c7d | Formular für Vorlage / Quelle / Vertrag | Überwachende Quelle | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.wahlen_602246 | Formular für Vorlage / Quelle / Vertrag | — wählen — | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.beginnt_mit_source_ea3ff7 | Formular für Vorlage / Quelle / Vertrag | Beginnt mit „source.“ | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.anzeigename_3ab2ea | Formular für Vorlage / Quelle / Vertrag | Anzeigename | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.typ_1b0241 | Formular für Vorlage / Quelle / Vertrag | Typ | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.zahl_654eb4 | Formular für Vorlage / Quelle / Vertrag | Zahl | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.ja_nein_0d2c61 | Formular für Vorlage / Quelle / Vertrag | Ja/Nein | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.text_71988c | Formular für Vorlage / Quelle / Vertrag | Text | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.auswahl_e8b7ad | Formular für Vorlage / Quelle / Vertrag | Auswahl | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.herkunft_514fce | Formular für Vorlage / Quelle / Vertrag | Herkunft | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.dependency_711595 | Formular für Vorlage / Quelle / Vertrag | Abhängigkeit | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.erweitert_25e56e | Formular für Vorlage / Quelle / Vertrag | Erweitert | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.technische_quellenart_e949b0 | Formular für Vorlage / Quelle / Vertrag | Technische Quellenart | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.frische_freshness_be29ab | Formular für Vorlage / Quelle / Vertrag | Aktualität | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.modus_45517c | Formular für Vorlage / Quelle / Vertrag | Modus | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.intervall_s_v0_3a6c0e | Formular für Vorlage / Quelle / Vertrag | Intervall (s){v0} | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.zustandsbasiert_gilt_bis_ein_neues_ereignis_eint_8c5c3d | Formular für Vorlage / Quelle / Vertrag | Zustandsbasiert: gilt, bis ein neues Ereignis eintrifft; kein Intervall nötig. | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.quelle_037889 | Formular für Vorlage / Quelle / Vertrag | Quelle | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.sensor_beispiel_be295b | Formular für Vorlage / Quelle / Vertrag | sensor.beispiel | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.wahlen_eda09c | Formular für Vorlage / Quelle / Vertrag | Wählen | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.attribut_ac1f2f | Formular für Vorlage / Quelle / Vertrag; Quellen und Verknüpfungen | Attribut * | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.zeit_attribut_optional_6aedff | Formular für Vorlage / Quelle / Vertrag | Zeit-Attribut (freiwillig) | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.attribut_mit_dem_messzeitpunkt_falls_vorhanden_296ae8 | Formular für Vorlage / Quelle / Vertrag | Attribut mit dem Messzeitpunkt, falls vorhanden. | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.wertpfad_optional_bf35e4 | Formular für Vorlage / Quelle / Vertrag; Quellen und Verknüpfungen | Wertpfad (freiwillig) | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.zeitpfad_optional_790a47 | Formular für Vorlage / Quelle / Vertrag | Zeitpfad (freiwillig) | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.umwandlung_erganzen_bb9be5 | Formular für Vorlage / Quelle / Vertrag | Umwandlung ergänzen | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.keine_db028e | Formular für Vorlage / Quelle / Vertrag | keine | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.einheit_skalieren_f57b15 | Formular für Vorlage / Quelle / Vertrag; Quellen und Verknüpfungen | Einheit skalieren | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.zieltyp_46a669 | Formular für Vorlage / Quelle / Vertrag | Zieltyp | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.faktor_105199 | Formular für Vorlage / Quelle / Vertrag; Quellen und Verknüpfungen | Faktor | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.wert_faktor_offset_d0477e | Formular für Vorlage / Quelle / Vertrag | wert × Faktor + Verschiebung | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.offset_b1a1e8 | Formular für Vorlage / Quelle / Vertrag; Quellen und Verknüpfungen | Verschiebung | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.katalog_1c58e0 | Formular für Vorlage / Quelle / Vertrag | Werteliste | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.erkennung_derzeit_nicht_verfugbar_521c30 | Formular für Vorlage / Quelle / Vertrag | Erkennung derzeit nicht verfügbar | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.attribute_8a0a7a | Formular für Vorlage / Quelle / Vertrag | Attribute:  | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.keine_treffer_6df7e9 | Formular für Vorlage / Quelle / Vertrag | Keine Treffer | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.weitere_seiten_werden_geladen_f45e5e | Formular für Vorlage / Quelle / Vertrag |  (weitere Seiten werden geladen) | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.weitere_laden_f77bb3 | Formular für Vorlage / Quelle / Vertrag | Weitere laden | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.version_dd1679 | Formular für Vorlage / Quelle / Vertrag | Version | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.eintrag_99b925 | Formular für Vorlage / Quelle / Vertrag | Eintrag | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.zuordnungen_rohwert_wert_656ea9 | Formular für Vorlage / Quelle / Vertrag | Zuordnungen (Rohwert → Wert) | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.on_b8d31e | Formular für Vorlage / Quelle / Vertrag | on | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.rohwert_a3deeb | Formular für Vorlage / Quelle / Vertrag | Rohwert | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.wert_fur_v0_a5063f | Formular für Vorlage / Quelle / Vertrag | Wert für {v0} | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.eintrag_entfernen_706a15 | Formular für Vorlage / Quelle / Vertrag | Eintrag entfernen | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.z_b_wohnzimmer_licht_807245 | Formular für Vorlage / Quelle / Vertrag | z. B. wohnzimmer.licht | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.v_0bb917 | Formular für Vorlage / Quelle / Vertrag | · v | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.aktiviert_10639c | Formular für Vorlage / Quelle / Vertrag | Eingeschaltet | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.beschreibung_e9262f | Formular für Vorlage / Quelle / Vertrag | Beschreibung | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.quellen_c78600 | Formular für Vorlage / Quelle / Vertrag | Quellen | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.contracts_0488ac | Formular für Vorlage / Quelle / Vertrag | Verträge | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.entfernen_382837 | Formular für Vorlage / Quelle / Vertrag | Entfernen | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.keine_parameter_bekannt_272f5e | Formular für Vorlage / Quelle / Vertrag | Keine Parameter bekannt. | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.eingang_d8af5e | Formular für Vorlage / Quelle / Vertrag | Eingang | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.konstante_2e2736 | Formular für Vorlage / Quelle / Vertrag | Konstante | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.und_fd2908 | Formular für Vorlage / Quelle / Vertrag | UND | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.oder_43e406 | Formular für Vorlage / Quelle / Vertrag | ODER | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.nicht_774d65 | Formular für Vorlage / Quelle / Vertrag | NICHT | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.vergleich_79a63c | Formular für Vorlage / Quelle / Vertrag | Vergleich | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.erster_treffer_e8c4e8 | Formular für Vorlage / Quelle / Vertrag | Erster Treffer | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.formel_244289 | Formular für Vorlage / Quelle / Vertrag | Formel | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.fusion_09d751 | Formular für Vorlage / Quelle / Vertrag | Zusammenführung | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.zustand_der_state_machine_2b1f38 | Formular für Vorlage / Quelle / Vertrag | Zustand des Ablaufs | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.nicht_anwendbar_af8969 | Formular für Vorlage / Quelle / Vertrag | Nicht anwendbar | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.werte_6fac44 | Formular für Vorlage / Quelle / Vertrag | Werte | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.logik_eff656 | Formular für Vorlage / Quelle / Vertrag | Logik | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.berechnung_fusion_55d3b1 | Formular für Vorlage / Quelle / Vertrag | Berechnung &amp; Zusammenführung | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.zeit_zustand_6dfc62 | Formular für Vorlage / Quelle / Vertrag | Zeit &amp; Zustand | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.gleich_dcabf6 | Formular für Vorlage / Quelle / Vertrag | = gleich | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.ungleich_d4ec9a | Formular für Vorlage / Quelle / Vertrag | ≠ ungleich | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.kleiner_fa34fb | Formular für Vorlage / Quelle / Vertrag | &lt; kleiner | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.hochstens_a9e2ae | Formular für Vorlage / Quelle / Vertrag | ≤ höchstens | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.gro_er_ccbed1 | Formular für Vorlage / Quelle / Vertrag | &gt; größer | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.mindestens_dc2ecc | Formular für Vorlage / Quelle / Vertrag | ≥ mindestens | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.wahr_erst_wenn_der_wahrheitswert_uber_die_dauer__cdd9b0 | Formular für Vorlage / Quelle / Vertrag | Ergibt erst Ja, wenn der Eingang die ganze angegebene Zeit ohne Unterbrechung Ja war. | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.verweildauer_des_wahrheitswerts_wahrheitswert_ei_37f3bf | Formular für Vorlage / Quelle / Vertrag | Wartet die angegebene Zeit mit durchgehendem Ja ab und ergibt dann Ja. | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.halt_den_letzten_gultigen_wert_bis_zum_ursprungl_05d8ca | Formular für Vorlage / Quelle / Vertrag | Behält bei einer erlaubten Unterbrechung den letzten gültigen Wert bis zum ursprünglichen Fristende bei. | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.flankenerkennung_eines_wahrheitswerts_0325ea | Formular für Vorlage / Quelle / Vertrag | Ergibt bei einem neu gemeldeten Wechsel zwischen Ja und Nein einmal Ja. | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.differenz_zweier_zahlen_5cc0dd | Formular für Vorlage / Quelle / Vertrag | Zieht die Vergleichszahl von der aktuellen Zahl ab und zeigt den Unterschied. | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.alter_der_messung_benotigt_messzeitpunkt_evidenz_ce2c48 | Formular für Vorlage / Quelle / Vertrag | Zeigt, wie viele Sekunden seit der belegten Messung vergangen sind. | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.zuklappen_41b22f | Formular für Vorlage / Quelle / Vertrag | Zuklappen | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.aufklappen_0f644f | Formular für Vorlage / Quelle / Vertrag | Aufklappen | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.unbekannt_319b5c | Formular für Vorlage / Quelle / Vertrag | (unbekannt) | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.entfernen_382837 | Formular für Vorlage / Quelle / Vertrag | Entfernen | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.v0_383901 | Formular für Vorlage / Quelle / Vertrag | {v0}. | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.typ_v0_v1_e5ef47 | Formular für Vorlage / Quelle / Vertrag | Typ: {v0}{v1} | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.wahlen_602246 | Formular für Vorlage / Quelle / Vertrag | — wählen — | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.links_9024c1 | Formular für Vorlage / Quelle / Vertrag | Links | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.rechts_00e9e5 | Formular für Vorlage / Quelle / Vertrag | Rechts | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.die_erste_zeile_deren_wenn_wahr_ist_bestimmt_das_300b11 | Formular für Vorlage / Quelle / Vertrag | Die erste Zeile, deren „Wenn“ erfüllt ist, bestimmt das Ergebnis. Ein unbekanntes „Wenn“ blockiert die Auswahl. | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.wenn_312fc0 | Formular für Vorlage / Quelle / Vertrag | Wenn | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.dann_612577 | Formular für Vorlage / Quelle / Vertrag | Dann | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.fall_e85a64 | Formular für Vorlage / Quelle / Vertrag | Fall | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.unten_39c51d | Formular für Vorlage / Quelle / Vertrag | Unten | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.oben_0d7d94 | Formular für Vorlage / Quelle / Vertrag | Oben | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.aus_2337c3 | Formular für Vorlage / Quelle / Vertrag | aus | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.an_ea325d | Formular für Vorlage / Quelle / Vertrag | an | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.zahl_654eb4 | Formular für Vorlage / Quelle / Vertrag | Zahl | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.eingange_v0_v1_v2_cd9f97 | Formular für Vorlage / Quelle / Vertrag | Eingänge: {v0}{v1} → {v2} | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.version_dd1679 | Formular für Vorlage / Quelle / Vertrag | Version | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.strategie_bfecce | Formular für Vorlage / Quelle / Vertrag | Strategie | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.die_reihenfolge_der_argumente_ist_die_prioritat_09f0f4 | Formular für Vorlage / Quelle / Vertrag | Die Reihenfolge der Argumente ist die Priorität. | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.erkennt_konflikte_zwischen_gleich_gewichteten_ka_e83977 | Formular für Vorlage / Quelle / Vertrag | Erkennt Konflikte zwischen gleich gewichteten Kandidaten. | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.kandidat_3c49ac | Formular für Vorlage / Quelle / Vertrag | Kandidat | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.operation_0f044f | Formular für Vorlage / Quelle / Vertrag | Operation | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.dauer_s_e59ef1 | Formular für Vorlage / Quelle / Vertrag | Dauer (s) | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.gro_er_0_2ae790 | Formular für Vorlage / Quelle / Vertrag | größer 0 | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.liefert_den_aktuellen_zustand_der_state_machine__723ee5 | Formular für Vorlage / Quelle / Vertrag | Liefert den aktuellen Zustand des Ablaufs dieser Vorlage. | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.die_definition_hat_noch_keine_state_machine_im_r_062ddc | Formular für Vorlage / Quelle / Vertrag | Die Vorlage hat noch keinen Ablauf – im Reiter „Ablauf“ anlegen. | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.eingang_der_zuordnung_b6a678 | Formular für Vorlage / Quelle / Vertrag | Eingang der Zuordnung | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.ergebnistyp_a0907a | Formular für Vorlage / Quelle / Vertrag | Ergebnistyp | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.eintrag_99b925 | Formular für Vorlage / Quelle / Vertrag | Eintrag | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.zuordnungen_6382c7 | Formular für Vorlage / Quelle / Vertrag | Zuordnungen | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.true_b5bea4 | Formular für Vorlage / Quelle / Vertrag | Ja | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.oder_7e3b22 | Formular für Vorlage / Quelle / Vertrag | oder  | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.wenn_eingang_53a1cc | Formular für Vorlage / Quelle / Vertrag | Wenn Eingang = | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.dann_06cb6c | Formular für Vorlage / Quelle / Vertrag | dann | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.eintrag_entfernen_706a15 | Formular für Vorlage / Quelle / Vertrag | Eintrag entfernen | wie bisher | Geprüft; beibehalten. |
| editors.SchemaEditor.ausgabefeld_894864 | Formular für Vorlage / Quelle / Vertrag | Ausgabefeld | wie bisher | Geprüft; beibehalten. |
| editors.SchemaEditor.ausgabefelder_e646ec | Formular für Vorlage / Quelle / Vertrag | Ausgabefelder | wie bisher | Geprüft; beibehalten. |
| editors.SchemaEditor.feld_v0_entfernen_3a5487 | Formular für Vorlage / Quelle / Vertrag | Feld {v0} entfernen | wie bisher | Geprüft; beibehalten. |
| editors.SchemaEditor.feldname_bc85f6 | Formular für Vorlage / Quelle / Vertrag | Feldname | wie bisher | Geprüft; beibehalten. |
| editors.SchemaEditor.zahlt_zur_verfugbarkeit_available_projection_0fd998 | Formular für Vorlage / Quelle / Vertrag | Zählt zur Verfügbarkeit | wie bisher | Geprüft; beibehalten. |
| editors.SchemaForm.wert_7e347d | Formular für Vorlage / Quelle / Vertrag | Wert | wie bisher | Geprüft; beibehalten. |
| editors.SchemaForm.wert_festlegen_55b559 | Formular für Vorlage / Quelle / Vertrag | Wert festlegen | wie bisher | Geprüft; beibehalten. |
| editors.SchemaForm.v0_variante_d57948 | Formular für Vorlage / Quelle / Vertrag | {v0}: Variante | wie bisher | Geprüft; beibehalten. |
| editors.SchemaForm.wert_wahlen_c1328a | Formular für Vorlage / Quelle / Vertrag | Wert wählen | wie bisher | Geprüft; beibehalten. |
| editors.SchemaForm.gro_er_als_v0_f2a9b6 | Formular für Vorlage / Quelle / Vertrag | größer als {v0} | wie bisher | Geprüft; beibehalten. |
| editors.SchemaForm.muster_905f9d | Formular für Vorlage / Quelle / Vertrag | Muster:  | wie bisher | Geprüft; beibehalten. |
| editors.SchemaForm.eintrag_99b925 | Formular für Vorlage / Quelle / Vertrag | Eintrag | wie bisher | Geprüft; beibehalten. |
| editors.SchemaForm.v0_cdb96d | Formular für Vorlage / Quelle / Vertrag | #{v0} | wie bisher | Geprüft; beibehalten. |
| editors.SchemaForm.eintrag_entfernen_706a15 | Formular für Vorlage / Quelle / Vertrag | Eintrag entfernen | wie bisher | Geprüft; beibehalten. |
| editors.SchemaForm.leer_f13f8e | Formular für Vorlage / Quelle / Vertrag | leer | wie bisher | Geprüft; beibehalten. |
| editors.SchemaForm.eigenschaft_f854ee | Formular für Vorlage / Quelle / Vertrag | Eigenschaft | wie bisher | Geprüft; beibehalten. |
| editors.SchemaForm.weitere_eigenschaften_5d81c5 | Formular für Vorlage / Quelle / Vertrag | Weitere Eigenschaften | wie bisher | Geprüft; beibehalten. |
| editors.SchemaForm.v0_schlussel_v1_59f39d | Formular für Vorlage / Quelle / Vertrag | {v0}: Schlüssel {v1} | wie bisher | Geprüft; beibehalten. |
| editors.SchemaForm.v0_entfernen_92fea7 | Formular für Vorlage / Quelle / Vertrag | {v0} entfernen | wie bisher | Geprüft; beibehalten. |
| editors.ValueEditor.text_71988c | Formular für Vorlage / Quelle / Vertrag | Text | wie bisher | Geprüft; beibehalten. |
| editors.ValueEditor.zahl_654eb4 | Formular für Vorlage / Quelle / Vertrag | Zahl | wie bisher | Geprüft; beibehalten. |
| editors.ValueEditor.liste_734384 | Formular für Vorlage / Quelle / Vertrag | Liste | wie bisher | Geprüft; beibehalten. |
| editors.ValueEditor.v0_bereich_d9749c | Formular für Vorlage / Quelle / Vertrag | {v0} – Bereich | wie bisher | Geprüft; beibehalten. |
| editors.ValueEditor.v0_typ_d4f718 | Formular für Vorlage / Quelle / Vertrag | {v0}: Typ | wie bisher | Geprüft; beibehalten. |
| editors.ValueEditor.keine_eigenschaften_36c4dd | Formular für Vorlage / Quelle / Vertrag | Keine Eigenschaften. | wie bisher | Geprüft; beibehalten. |
| editors.ValueEditor.v0_schlussel_v1_59f39d | Formular für Vorlage / Quelle / Vertrag | {v0}: Schlüssel {v1} | wie bisher | Geprüft; beibehalten. |
| editors.ValueEditor.der_schlussel_v0_existiert_bereits_99dc5d | Formular für Vorlage / Quelle / Vertrag | Der Schlüssel „{v0}“ existiert bereits. | wie bisher | Geprüft; beibehalten. |
| editors.ValueEditor.v0_v1_a30df1 | Formular für Vorlage / Quelle / Vertrag | {v0}.{v1} | wie bisher | Geprüft; beibehalten. |
| editors.ValueEditor.eigenschaft_v0_entfernen_7fded9 | Formular für Vorlage / Quelle / Vertrag | Eigenschaft {v0} entfernen | wie bisher | Geprüft; beibehalten. |
| editors.ValueEditor.v0_eigenschaft_hinzufugen_a918ab | Formular für Vorlage / Quelle / Vertrag | {v0}: Eigenschaft hinzufügen | wie bisher | Geprüft; beibehalten. |
| editors.ValueEditor.eigenschaft_f854ee | Formular für Vorlage / Quelle / Vertrag | Eigenschaft | wie bisher | Geprüft; beibehalten. |
| editors.ValueEditor.leere_liste_523d40 | Formular für Vorlage / Quelle / Vertrag | Leere Liste. | wie bisher | Geprüft; beibehalten. |
| editors.ValueEditor.v0_v1_6f0604 | Formular für Vorlage / Quelle / Vertrag | {v0}[{v1}] | wie bisher | Geprüft; beibehalten. |
| editors.ValueEditor.element_v0_nach_oben_b1686b | Formular für Vorlage / Quelle / Vertrag | Element {v0} nach oben | wie bisher | Geprüft; beibehalten. |
| editors.ValueEditor.element_v0_nach_unten_0f3f34 | Formular für Vorlage / Quelle / Vertrag | Element {v0} nach unten | wie bisher | Geprüft; beibehalten. |
| editors.ValueEditor.element_v0_entfernen_d4285b | Formular für Vorlage / Quelle / Vertrag | Element {v0} entfernen | wie bisher | Geprüft; beibehalten. |
| editors.ValueEditor.v0_element_hinzufugen_e37d2b | Formular für Vorlage / Quelle / Vertrag | {v0}: Element hinzufügen | wie bisher | Geprüft; beibehalten. |
| editors.ValueEditor.element_4e5b54 | Formular für Vorlage / Quelle / Vertrag | Element | wie bisher | Geprüft; beibehalten. |
| editors.ValueEditor.v0_json_df53e7 | Formular für Vorlage / Quelle / Vertrag | {v0}: JSON | wie bisher | Geprüft; beibehalten. |
| editors.ValueEditor.ungultiges_json_nicht_ubernommen_37858e | Formular für Vorlage / Quelle / Vertrag | Ungültiges JSON – nicht übernommen:  | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.einrichtungsassistent_offnen_3e1fc4 | Einstellungen | Einrichtungsassistent öffnen | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.installations_id_fc5797 | Einstellungen | Installations-ID | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.bezeichnung_97d1e6 | Einstellungen | Bezeichnung | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.protokolle_b4026e | Einstellungen | Protokolle | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.installationsdaten_nicht_lesbar_5882af | Einstellungen | Installationsdaten nicht lesbar | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.der_assistent_andert_nichts_bevor_sie_ausdruckli_89e424 | Einstellungen | Der Assistent ändert erst nach deiner Bestätigung etwas. Er übernimmt keine Konfiguration, installiert nichts in Home Assistant und startet nichts neu. | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.nicht_bereit_05674c | Einstellungen | nicht bereit | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.home_assistant_2a366a | Einstellungen | Home Assistant | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.bridge_3892e1 | Einstellungen | HA-Anbindung | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.mqtt_51b197 | Einstellungen | MQTT | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.offene_grunde_da9e40 | Einstellungen | Offene Gründe | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.queue_3b2fe0 | Einstellungen → Erweitert | Warteschlange | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.admin.AdminPage.dependencies_2e41b1 | Einstellungen | Abhängigkeiten | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.andere_installation_616cdb | Einstellungen | andere Installation | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.live_websocket_74b350 | Einstellungen | Verbindung zur App | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.letztes_ereignis_b141fd | Einstellungen | Letztes Ereignis | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.erreichbar_fb6263 | Einstellungen | erreichbar | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.rollen_tokens_9fcf59 | Einstellungen | Rollen &amp; Zugangsschlüssel | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.nicht_automatisch_wiederholen_008a18 | Einstellungen | nicht automatisch wiederholen | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.neues_token_f72672 | Einstellungen | Neuer Zugangsschlüssel | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.audit_2e2f9c | Einstellungen | · Protokoll:  | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.vollstandig_c1bea4 | Einstellungen | vollständig | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.abschluss_unbestatigt_token_trotzdem_sichern_90957f | Einstellungen | Abschluss unbestätigt – Zugangsschlüssel trotzdem sichern | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.beim_admin_token_betrifft_das_alle_administrativ_5abdbf | Einstellungen | Beim Administrator-Zugangsschlüssel betrifft das alle administrativen Werkzeuge außerhalb dieser Ingress-Oberfläche.  | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.es_gibt_keine_automatische_wiederholung_das_neue_ddf90c | Einstellungen | Es gibt keine automatische Wiederholung. Der neue Zugangsschlüssel wird einmalig angezeigt. | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.audit_verlauf_843625 | Einstellungen | Protokoll-Verlauf | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.operation_0f044f | Einstellungen | Operation | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.ausgang_unbestimmt_ef46c4 | Einstellungen | Ausgang unbestimmt | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.akteur_30711f | Einstellungen | Ausgelöst von | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.eintrage_ohne_zeitstempel_stammen_aus_alteren_la_516fef | Einstellungen | Einträge ohne Zeitstempel stammen aus älteren Laufzeiten. | wie bisher | Geprüft; beibehalten. |
| features.authoring.catalog.wert_7e347d | Entwurf und Bearbeitung | Wert | wie bisher | Geprüft; beibehalten. |
| features.authoring.catalog.v0_v1_a30df1 | Entwurf und Bearbeitung | {v0}.{v1} | wie bisher | Geprüft; beibehalten. |
| features.authoring.CreateDraftDialog.leere_registry_eb1ce9 | Entwurf und Bearbeitung | Leere Konfiguration | wie bisher | Geprüft; beibehalten. |
| features.authoring.CreateDraftDialog.von_grund_auf_neu_aufbauen_fingerprint_version_2_56e79f | Entwurf und Bearbeitung → Erweitert | Mit einer leeren Konfiguration beginnen. | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.authoring.CreateDraftDialog.kopie_der_aktiven_registry_728e01 | Entwurf und Bearbeitung | Kopie der aktiven Konfiguration | wie bisher | Geprüft; beibehalten. |
| features.authoring.CreateDraftDialog.bestehende_konfiguration_weiterentwickeln_3e5423 | Entwurf und Bearbeitung | Bestehende Konfiguration weiterentwickeln. | wie bisher | Geprüft; beibehalten. |
| features.authoring.CreateDraftDialog.es_ist_keine_registry_aktiv_767a4d | Entwurf und Bearbeitung | Es ist keine Konfiguration aktiv. | wie bisher | Geprüft; beibehalten. |
| features.authoring.CreateDraftDialog.import_json_c4b92a | Entwurf und Bearbeitung | Einlesen (JSON) | wie bisher | Geprüft; beibehalten. |
| features.authoring.CreateDraftDialog.kopie_von_v0_8bb123 | Entwurf und Bearbeitung | Kopie von „{v0}“ | wie bisher | Geprüft; beibehalten. |
| features.authoring.CreateDraftDialog.neuer_draft_610fb2 | Entwurf und Bearbeitung | Neuer Entwurf | wie bisher | Geprüft; beibehalten. |
| features.authoring.CreateDraftDialog.abbrechen_f7ff11 | Entwurf und Bearbeitung | Abbrechen | wie bisher | Geprüft; beibehalten. |
| features.authoring.CreateDraftDialog.draft_anlegen_0355d8 | Entwurf und Bearbeitung | Entwurf anlegen | wie bisher | Geprüft; beibehalten. |
| features.authoring.CreateDraftDialog.es_sind_bereits_100_entwurfe_vorhanden_entfernen_f89be6 | Entwurf und Bearbeitung | Es sind bereits 100 Entwürfe vorhanden. Entferne zuerst einen nicht mehr benötigten Entwurf. | wie bisher | Geprüft; beibehalten. |
| features.authoring.CreateDraftDialog.name_optional_e09b37 | Entwurf und Bearbeitung | Name (freiwillig) | wie bisher | Geprüft; beibehalten. |
| features.authoring.CreateDraftDialog.z_b_licht_umbau_ed3d21 | Entwurf und Bearbeitung | z. B. Licht-Umbau | wie bisher | Geprüft; beibehalten. |
| features.authoring.CreateDraftDialog.ausgangspunkt_4c2d40 | Entwurf und Bearbeitung | Ausgangspunkt | wie bisher | Geprüft; beibehalten. |
| features.authoring.CreateDraftDialog.oder_json_einfugen_403a9d | Entwurf und Bearbeitung | oder JSON einfügen | wie bisher | Geprüft; beibehalten. |
| features.authoring.CreateDraftDialog.draft_konnte_nicht_angelegt_werden_ef809e | Entwurf und Bearbeitung | Entwurf konnte nicht angelegt werden | wie bisher | Geprüft; beibehalten. |
| features.authoring.DraftBar.neuer_draft_1d7ef0 | Entwurf und Bearbeitung | Neuer Entwurf … | wie bisher | Geprüft; beibehalten. |
| features.authoring.DraftBar.noch_keine_drafts_vorhanden_8f793b | Entwurf und Bearbeitung | Noch keine Entwürfe vorhanden. | wie bisher | Geprüft; beibehalten. |
| features.authoring.DraftBar.v_4c9448 | Entwurf und Bearbeitung | Stand  | wie bisher | Geprüft; beibehalten. |
| features.authoring.DraftBar.basis_revision_cb2fb5 | Entwurf und Bearbeitung | · auf Grundlage von Version  | wie bisher | Geprüft; beibehalten. |
| features.authoring.DraftBar.geoffnet_ungespeichert_62ba6c | Entwurf und Bearbeitung | geöffnet · ungespeichert | wie bisher | Geprüft; beibehalten. |
| features.authoring.DraftBar.geoffnet_ec5e95 | Entwurf und Bearbeitung | geöffnet | wie bisher | Geprüft; beibehalten. |
| features.authoring.DraftBar.ungespeicherte_anderungen_verwerfen_2630c0 | Entwurf und Bearbeitung | Ungespeicherte Änderungen verwerfen? | wie bisher | Geprüft; beibehalten. |
| features.authoring.DraftBar.hat_ungespeicherte_anderungen_beim_wechsel_zu_52f14b | Entwurf und Bearbeitung | “ hat ungespeicherte Änderungen. Beim Wechsel zu „ | wie bisher | Geprüft; beibehalten. |
| features.authoring.DraftBar.gehen_sie_samt_ruckgangig_verlauf_verloren_f437b8 | Entwurf und Bearbeitung | “ gehen sie samt Rückgängig-Verlauf verloren. | wie bisher | Geprüft; beibehalten. |
| features.authoring.DraftBar.verwerfen_und_wechseln_88c2d1 | Entwurf und Bearbeitung | Verwerfen und wechseln | wie bisher | Geprüft; beibehalten. |
| features.authoring.DraftBar.versionskonflikt_beim_speichern_b52e2a | Entwurf und Bearbeitung | Versionskonflikt beim Speichern | wie bisher | Geprüft; beibehalten. |
| features.authoring.DraftBar.der_draft_wurde_seit_dem_laden_verandert_server__3341e6 | Entwurf und Bearbeitung | Der Entwurf wurde seit dem Laden verändert (App: v{v0}, lokal: v{v1}). Nichts wurde überschrieben. | wie bisher | Geprüft; beibehalten. |
| features.authoring.DraftBar.abbrechen_f7ff11 | Entwurf und Bearbeitung | Abbrechen | wie bisher | Geprüft; beibehalten. |
| features.authoring.DraftBar.meine_anderungen_als_neuen_draft_sichern_ef820d | Entwurf und Bearbeitung | Meine Änderungen als neuen Entwurf sichern | wie bisher | Geprüft; beibehalten. |
| features.authoring.DraftBar.server_stand_ubernehmen_2f2a5e | Entwurf und Bearbeitung | Gespeicherten Stand laden | wie bisher | Geprüft; beibehalten. |
| features.authoring.DraftBar.wirklich_uberschreiben_ad728b | Entwurf und Bearbeitung | Wirklich überschreiben | wie bisher | Geprüft; beibehalten. |
| features.authoring.DraftBar.server_stand_uberschreiben_613729 | Entwurf und Bearbeitung | Gespeicherten Stand überschreiben … | wie bisher | Geprüft; beibehalten. |
| features.authoring.DraftBar.beide_stande_sind_inhaltlich_gleich_ein_ubernehm_d8a22e | Entwurf und Bearbeitung | Beide Stände sind inhaltlich gleich. Du kannst den gespeicherten Stand ohne Verlust laden. | wie bisher | Geprüft; beibehalten. |
| features.authoring.DraftBar.die_stande_unterscheiden_sich_0b65e1 | Entwurf und Bearbeitung | Die Stände unterscheiden sich | wie bisher | Geprüft; beibehalten. |
| features.authoring.DraftBar.server_stand_ubernehmen_verwirft_ihre_lokalen_an_59393c | Entwurf und Bearbeitung | „Gespeicherten Stand laden“ verwirft deine lokalen Änderungen. „Als neuen Entwurf sichern“ bewahrt sie getrennt auf. Überschreiben ersetzt die Änderungen der anderen Sitzung. | wie bisher | Geprüft; beibehalten. |
| features.authoring.DraftBar.uberschreiben_bestatigen_a69a90 | Entwurf und Bearbeitung | Überschreiben bestätigen | wie bisher | Geprüft; beibehalten. |
| features.authoring.DraftBar.wird_gepruft_90f584 | Entwurf und Bearbeitung | wird geprüft | wie bisher | Geprüft; beibehalten. |
| features.authoring.DraftBar.ungepruft_08112f | Entwurf und Bearbeitung | ungeprüft | wie bisher | Geprüft; beibehalten. |
| features.authoring.DraftBar.ruckgangig_dd7bd2 | Entwurf und Bearbeitung | Rückgängig | wie bisher | Geprüft; beibehalten. |
| features.authoring.DraftBar.wiederholen_e0ef00 | Entwurf und Bearbeitung | Wiederholen | wie bisher | Geprüft; beibehalten. |
| features.authoring.DraftBar.strg_s_bda7e5 | Entwurf und Bearbeitung | Strg+S | wie bisher | Geprüft; beibehalten. |
| features.authoring.DraftBar.speichern_f6b2ff | Entwurf und Bearbeitung | Speichern | wie bisher | Geprüft; beibehalten. |
| features.authoring.DraftBar.prufen_a1ca13 | Entwurf und Bearbeitung | Prüfen | wie bisher | Geprüft; beibehalten. |
| features.authoring.DraftBar.draft_schlie_en_e8650e | Entwurf und Bearbeitung | Entwurf schließen | wie bisher | Geprüft; beibehalten. |
| features.authoring.DraftBar.draft_schlie_en_f5ae17 | Entwurf und Bearbeitung | Entwurf schließen? | wie bisher | Geprüft; beibehalten. |
| features.authoring.DraftBar.es_gibt_ungespeicherte_anderungen_sie_gehen_verl_002e77 | Entwurf und Bearbeitung | Es gibt ungespeicherte Änderungen. Sie gehen verloren. | wie bisher | Geprüft; beibehalten. |
| features.authoring.DraftBar.verwerfen_und_schlie_en_6dcb36 | Entwurf und Bearbeitung | Verwerfen und schließen | wie bisher | Geprüft; beibehalten. |
| features.authoring.importExport.eine_registry_ist_ein_json_objekt_kein_array_ska_85abe7 | Entwurf und Bearbeitung | Eine Konfiguration ist ein JSON-Objekt (kein Array, Skalar oder null). | wie bisher | Geprüft; beibehalten. |
| features.authoring.issues.diese_id_ist_bereits_vergeben_20f34e | Entwurf und Bearbeitung | Diese ID ist bereits vergeben. | wie bisher | Geprüft; beibehalten. |
| features.authoring.issues.diese_definition_ist_als_version_bereits_aktivie_d64870 | Entwurf und Bearbeitung | Diese Vorlagenversion wurde bereits übernommen und kann nicht mehr inhaltlich geändert werden. Lege eine neue Version an. | wie bisher | Geprüft; beibehalten. |
| features.authoring.issues.typ_katalog_oder_einheit_passen_nicht_zum_erwart_6a5b1f | Entwurf und Bearbeitung | Typ, Werteliste oder Einheit passen nicht zum erwarteten Eingang. | wie bisher | Geprüft; beibehalten. |
| features.authoring.issues.die_referenz_ist_nicht_eindeutig_oder_unbekannt_3be019 | Entwurf und Bearbeitung | Die Referenz ist nicht eindeutig oder unbekannt. | wie bisher | Geprüft; beibehalten. |
| features.authoring.issues.typ_und_version_sind_nicht_registriert_599b2c | Entwurf und Bearbeitung | Typ und Version sind nicht registriert. | wie bisher | Geprüft; beibehalten. |
| features.authoring.issues.die_contracts_bilden_einen_zyklus_b02297 | Entwurf und Bearbeitung | Die Verträge bilden einen Zyklus. | wie bisher | Geprüft; beibehalten. |
| features.authoring.issues.das_referenzierte_feld_existiert_nicht_aaa234 | Entwurf und Bearbeitung | Das referenzierte Feld existiert nicht. | wie bisher | Geprüft; beibehalten. |
| features.authoring.issues.der_eingang_ist_in_dieser_definition_nicht_dekla_901b2e | Entwurf und Bearbeitung | Der Eingang ist in dieser Vorlage nicht deklariert. | wie bisher | Geprüft; beibehalten. |
| features.authoring.issues.die_interne_regel_existiert_nicht_47d7f3 | Entwurf und Bearbeitung | Die interne Regel existiert nicht. | wie bisher | Geprüft; beibehalten. |
| features.authoring.issues.die_benannten_regeln_verweisen_im_kreis_aufeinan_2f903a | Entwurf und Bearbeitung | Die benannten Regeln verweisen im Kreis aufeinander. | wie bisher | Geprüft; beibehalten. |
| features.authoring.issues.die_state_machine_wird_von_keiner_ausgabe_verwen_63e564 | Entwurf und Bearbeitung | Der Ablauf wird von keiner Ausgabe verwendet. | wie bisher | Geprüft; beibehalten. |
| features.authoring.issues.diese_formel_version_ist_nicht_registriert_8bbb4e | Entwurf und Bearbeitung | Diese Formel/Version ist nicht registriert. | wie bisher | Geprüft; beibehalten. |
| features.authoring.issues.diese_fusionsstrategie_ist_nicht_registriert_4a6f9a | Entwurf und Bearbeitung | Diese Zusammenführungsstrategie ist nicht registriert. | wie bisher | Geprüft; beibehalten. |
| features.authoring.issues.die_operanden_sind_nicht_vergleichbar_250187 | Entwurf und Bearbeitung | Die Operanden sind nicht vergleichbar. | wie bisher | Geprüft; beibehalten. |
| features.authoring.locate.source_0e570c | Entwurf und Bearbeitung | Quelle | wie bisher | Geprüft; beibehalten. |
| features.authoring.locate.binding_164c69 | Entwurf und Bearbeitung | Verknüpfung | wie bisher | Geprüft; beibehalten. |
| features.authoring.locate.katalog_1c58e0 | Entwurf und Bearbeitung | Werteliste | wie bisher | Geprüft; beibehalten. |
| features.authoring.locate.dependency_711595 | Entwurf und Bearbeitung | Abhängigkeit | wie bisher | Geprüft; beibehalten. |
| features.authoring.locate.v0_v1_24a420 | Entwurf und Bearbeitung | {v0} {v1} | wie bisher | Geprüft; beibehalten. |
| features.authoring.locate.contract_v0_fef1f2 | Entwurf und Bearbeitung | Vertrag {v0} | wie bisher | Geprüft; beibehalten. |
| features.authoring.locate.contracts_0488ac | Entwurf und Bearbeitung | Verträge | wie bisher | Geprüft; beibehalten. |
| features.authoring.locate.definition_v0_v1_71ce19 | Entwurf und Bearbeitung | Vorlage {v0}@{v1} | wie bisher | Geprüft; beibehalten. |
| features.authoring.model.zahl_654eb4 | Entwurf und Bearbeitung | Zahl | wie bisher | Geprüft; beibehalten. |
| features.authoring.model.auswahl_enum_ae155a | Entwurf und Bearbeitung | Auswahl | wie bisher | Geprüft; beibehalten. |
| features.authoring.model.text_71988c | Entwurf und Bearbeitung | Text | wie bisher | Geprüft; beibehalten. |
| features.authoring.model.zeitpunkt_9d91e4 | Entwurf und Bearbeitung | Zeitpunkt | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractDetailPage.contract_v0_nicht_gefunden_c09b7a | Vertrag und Vorlage | Vertrag „{v0}“ nicht gefunden | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractDetailPage.er_existiert_im_geoffneten_draft_nicht_cb5eb3 | Vertrag und Vorlage | Er existiert im geöffneten Entwurf nicht. | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractDetailPage.er_existiert_in_der_aktiven_registry_nicht_25b321 | Vertrag und Vorlage | Er existiert in der aktiven Konfiguration nicht. | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractDetailPage.der_server_liefert_dennoch_einen_zustand_dafur_0cfd01 | Vertrag und Vorlage |  Die App liefert dennoch einen Zustand dafür. | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractDetailPage.diagnose_64dd65 | Vertrag und Vorlage | Diagnose | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractDetailPage.entfernen_382837 | Vertrag und Vorlage | Entfernen | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractDetailPage.zustand_630d1a | Vertrag und Vorlage | Zustand | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractDetailPage.contract_deaktiviert_f0d824 | Vertrag und Vorlage | Vertrag ausgeschaltet | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractDetailPage.deaktivierte_contracts_liefern_keinen_zustand_de_a31528 | Vertrag und Vorlage | Ausgeschaltete Verträge liefern keine neuen Werte. | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractDetailPage.kein_live_zustand_85efdc | Vertrag und Vorlage | Kein aktueller Zustand | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractDetailPage.es_wurde_noch_kein_snapshot_empfangen_e56b2e | Vertrag und Vorlage | Es wurde noch kein vollständiger Stand empfangen. | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractDetailPage.der_aktive_stand_enthalt_diesen_contract_nicht_e_15aef3 | Vertrag und Vorlage | Dieser Vertrag existiert bisher nur im Entwurf. Er liefert Werte, sobald du den Entwurf übernimmst. | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractDetailPage.konfiguration_8df29d | Vertrag und Vorlage | Konfiguration | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractDetailPage.abhangigkeiten_327cb1 | Vertrag und Vorlage | Abhängigkeiten | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractDetailPage.eingange_53fb39 | Vertrag und Vorlage | Eingänge | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractDetailPage.verwendet_von_656221 | Vertrag und Vorlage | Verwendet von | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractDetailPage.contracts_die_diesen_contract_als_eingang_nutzen_763bf2 | Vertrag und Vorlage | Verträge, die diesen Vertrag als Eingang nutzen. | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractDetailPage.kein_anderer_contract_nutzt_ihn_4582b8 | Vertrag und Vorlage | Kein anderer Vertrag nutzt ihn. | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractDetailPage.typ_1b0241 | Vertrag und Vorlage | Typ | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractDetailPage.contract_entfernen_f6bc55 | Vertrag und Vorlage | Vertrag entfernen? | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractDetailPage.betroffen_c20137 | Vertrag und Vorlage | Betroffen:  | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractDetailPage.alle_contracts_67b49f | Vertrag und Vorlage | Alle Verträge | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractsPage.neue_contract_instanz_a62401 | Vertrag und Vorlage | Neuer Vertrag | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractsPage.abbrechen_f7ff11 | Vertrag und Vorlage | Abbrechen | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractsPage.anlegen_d34c0e | Vertrag und Vorlage | Anlegen | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractsPage.diese_id_ist_bereits_vergeben_20f34e | Vertrag und Vorlage | Diese ID ist bereits vergeben. | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractsPage.v_0bb917 | Vertrag und Vorlage | · v | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractsPage.typ_1b0241 | Vertrag und Vorlage | Typ | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractsPage.aktiviert_acb27b | Vertrag und Vorlage | eingeschaltet | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractsPage.deaktiviert_10f33e | Vertrag und Vorlage | ausgeschaltet | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractsPage.gesundheit_1c7f2f | Vertrag und Vorlage | Zustand | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractsPage.contracts_definitionen_499616 | Vertrag und Vorlage | Meine Verträge | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractsPage.instanzen_binden_einen_typ_an_quellen_definition_c07fc7 | Vertrag und Vorlage | Öffne einen Vertrag, um seinen Wert und seine Herkunft zu sehen. | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractsPage.neue_instanz_e3e518 | Vertrag und Vorlage | Neuer Vertrag | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractsPage.contract_instanzen_1a0c12 | Vertrag und Vorlage | Verträge | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractsPage.filter_638e24 | Vertrag und Vorlage | Filter | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractsPage.contracts_suchen_453163 | Vertrag und Vorlage | Verträge suchen | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractsPage.aktivierung_90ba1a | Vertrag und Vorlage | Eingeschaltet oder ausgeschaltet | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractsPage.alle_3801a3 | Vertrag und Vorlage | Alle | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractsPage.jede_gesundheit_b848a7 | Vertrag und Vorlage | Jeder Zustand | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractsPage.noch_keine_contract_instanzen_c7f1ae | Vertrag und Vorlage | Noch keine Verträge | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractsPage.keine_treffer_6df7e9 | Vertrag und Vorlage | Keine Treffer | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractsPage.filter_oder_suche_anpassen_3493b0 | Vertrag und Vorlage | Filter oder Suche anpassen. | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractsPage.live_zustand_moglicherweise_veraltet_57c06a | Vertrag und Vorlage | Aktueller Zustand möglicherweise veraltet ( | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionDetailPage.definition_v0_v1_nicht_gefunden_d09de5 | Vertrag und Vorlage | Vorlage „{v0}@{v1}“ nicht gefunden | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionDetailPage.sie_existiert_im_geoffneten_draft_nicht_0632aa | Vertrag und Vorlage | Sie existiert im geöffneten Entwurf nicht. | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionDetailPage.sie_existiert_in_der_aktiven_registry_nicht_8e5152 | Vertrag und Vorlage | Sie existiert in der aktiven Konfiguration nicht. | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionDetailPage.v0_version_v1_1d1973 | Vertrag und Vorlage | {v0} · Version {v1} | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionDetailPage.v_4c9448 | Vertrag und Vorlage | v | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionDetailPage.entwurf_2ba46e | Vertrag und Vorlage | Entwurf | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionDetailPage.neue_version_e81cfe | Vertrag und Vorlage | Neue Version | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionDetailPage.entfernen_382837 | Vertrag und Vorlage | Entfernen | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionDetailPage.definition_9813fa | Vertrag und Vorlage | Vorlage | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionDetailPage.definitionseditor_c9b1ee | Vertrag und Vorlage | Vorlageneditor | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionDetailPage.schreibgeschutzte_ansicht_der_aktiven_registry_10e355 | Vertrag und Vorlage | Schreibgeschützte Ansicht der aktiven Konfiguration. | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionDetailPage.verwendung_947c0a | Vertrag und Vorlage | Verwendung | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionDetailPage.verwendet_von_f83bfe | Vertrag und Vorlage | Verwendet von  | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionDetailPage.neue_version_von_v0_8ee68e | Vertrag und Vorlage | Neue Version von {v0} | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionDetailPage.es_wird_v_v0_als_kopie_von_v_v1_angelegt_die_bis_cdd655 | Vertrag und Vorlage | Es wird v{v0} als Kopie von v{v1} angelegt. Die bisherige Version bleibt unverändert; Verträge verweisen weiter auf sie, bis sie umgestellt werden. | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionDetailPage.abbrechen_f7ff11 | Vertrag und Vorlage | Abbrechen | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionDetailPage.version_anlegen_3d33f7 | Vertrag und Vorlage | Version anlegen | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionDetailPage.instanzen_gleich_auf_die_neue_version_umstellen__a98ead | Vertrag und Vorlage | Verträge gleich auf die neue Version umstellen? Das ändert ihre Berechnungsgrundlage. Gespeicherte Zeitregeln können dadurch neu beginnen. Die Prüfung zeigt dir die Auswirkungen. | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionDetailPage.keine_instanz_verwendet_diese_version_2f0d3f | Vertrag und Vorlage | Kein Vertrag verwendet diese Version. | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionDetailPage.definition_entfernen_2fb8aa | Vertrag und Vorlage | Vorlage entfernen? | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionDetailPage.wird_aus_dem_draft_entfernt_2fe205 | Vertrag und Vorlage | wird aus dem Entwurf entfernt. | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionDetailPage.noch_verwendet_von_cd365f | Vertrag und Vorlage | Noch verwendet von:  | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionDetailPage.diese_version_war_bereits_aktiv_sie_kann_spater__eb414d | Vertrag und Vorlage | Diese Version war bereits aktiv. Für eine andere Berechnung brauchst du eine neue Vorlagenversion. | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionDetailPage.alle_definitionen_bd3333 | Vertrag und Vorlage | Alle Vorlagen | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionsPage.version_dd1679 | Vertrag und Vorlage | Version | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionsPage.v_4c9448 | Vertrag und Vorlage | v | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionsPage.name_dcd1d5 | Vertrag und Vorlage | Name | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionsPage.eingange_53fb39 | Vertrag und Vorlage | Eingänge | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionsPage.ausgaben_44e52a | Vertrag und Vorlage | Ausgaben | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionsPage.machine_8f1cc4 | Vertrag und Vorlage | Ablauf | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionsPage.ja_3702fc | Vertrag und Vorlage | ja | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionsPage.instanzen_a94c7e | Vertrag und Vorlage | Verträge | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionsPage.status_920e41 | Vertrag und Vorlage | Status | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionsPage.entwurf_2ba46e | Vertrag und Vorlage | Entwurf | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionsPage.fehler_f6cc01 | Vertrag und Vorlage | Fehler | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionsPage.neue_definition_fcff16 | Vertrag und Vorlage | Neue Vorlage | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionsPage.definitionen_871a91 | Vertrag und Vorlage | Vorlagen | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionsPage.noch_keine_definitionen_57fe40 | Vertrag und Vorlage | Noch keine Vorlagen | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionsPage.beginnt_mit_einem_eingang_und_einem_ausgabefeld__b84536 | Vertrag und Vorlage | Beginnt mit einem Eingang und einem Ausgabefeld. Alles Weitere – Eingänge, Regeln, Zusammenführung, Zeitregel, Ablauf – wird im Editor ergänzt. | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionsPage.abbrechen_f7ff11 | Vertrag und Vorlage | Abbrechen | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionsPage.anlegen_d34c0e | Vertrag und Vorlage | Anlegen | wie bisher | Geprüft; beibehalten. |
| features.contracts.DefinitionsPage.diese_typ_id_existiert_bereits_fur_anderungen_ei_01c137 | Vertrag und Vorlage | Diese Typ-ID existiert bereits. Für Änderungen eine neue Version anlegen. | wie bisher | Geprüft; beibehalten. |
| features.diagnostics.CommandsPanel.abgelehnt_34b49d | Erweitert / Nachweise | Abgelehnt. | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.CommandsPanel.abgelaufen_die_gultigkeit_endete_vor_der_verarbe_7e9bc2 | Erweitert / Nachweise | Abgelaufen: die Gültigkeit endete vor der Verarbeitung. | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.CommandsPanel.nicht_unterstutzt_der_contract_kennt_diesen_befe_51e577 | Erweitert / Nachweise | Nicht unterstützt: der Vertrag kennt diesen Befehl nicht. | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.CommandsPanel.kein_gespeichertes_ergebnis_v0_f20069 | Erweitert / Nachweise | Kein gespeichertes Ergebnis: {v0} | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.CommandsPanel.keine_commands_verfugbar_7e30a7 | Erweitert / Nachweise | Keine Befehle verfügbar | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.CommandsPanel.commands_gibt_es_nur_fur_aktivierte_contracts_de_eced61 | Erweitert / Nachweise | Befehle gibt es nur für aktivierte Verträge, deren Typ Befehle deklariert (z. B. ein Ablauf mit Befehlen). | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.CommandsPanel.command_713166 | Erweitert / Nachweise | Befehle | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.CommandsPanel.contract_a6f5b0 | Erweitert / Nachweise | Vertrag | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.CommandsPanel.wahlen_602246 | Erweitert / Nachweise | — wählen — | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.CommandsPanel.befehl_c8505b | Erweitert / Nachweise | Befehl | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.CommandsPanel.argumente_typisiert_b6a75c | Erweitert / Nachweise | Argumente (typisiert) | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.CommandsPanel.v0_v1_63ec26 | Erweitert / Nachweise | {v0}{v1} | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.CommandsPanel.dieser_befehl_hat_keine_argumente_cc8092 | Erweitert / Nachweise | Dieser Befehl hat keine Argumente. | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.CommandsPanel.ergebnis_cd8e22 | Erweitert / Nachweise | Ergebnis | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.CommandsPanel.warte_auf_die_antwort_5e512a | Erweitert / Nachweise | Warte auf die Antwort … | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.CommandsPanel.antwort_unbekannt_e79d9d | Erweitert / Nachweise | Antwort unbekannt | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.CommandsPanel.gespeichertes_ergebnis_abfragen_f219ee | Erweitert / Nachweise | Gespeichertes Ergebnis abfragen | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.CommandsPanel.wird_an_bc6f65 | Erweitert / Nachweise | “ wird an  | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.CommandsPanel.gesendet_das_ist_eine_aktion_am_laufenden_system_55df5a | Erweitert / Nachweise | gesendet. Das ist eine Aktion am laufenden System: Wenn die Bedingung es erlaubt, wechselt der Ablauf seinen Zustand. | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.CommandsPanel.senden_079bef | Erweitert / Nachweise | Senden | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.erststart_c02a0d | Erweitert / Nachweise | Erststart | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.der_contract_war_noch_nie_aktiv_es_gibt_nichts_w_98f097 | Erweitert / Nachweise | Der Vertrag war noch nie aktiv; es gibt nichts wiederherzustellen. | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.wiederherstellung_gultig_749640 | Erweitert / Nachweise | Wiederherstellung gültig | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.gespeicherter_kontext_passt_zum_aktuellen_finger_d896af | Erweitert / Nachweise | Die gespeicherten Zeitregeln passen zur aktuellen Berechnungsgrundlage. Bestehende Fristen bleiben erhalten. | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.veraltet_d9075b | Erweitert / Nachweise | Veraltet | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.inkompatibel_815c9f | Erweitert / Nachweise | Inkompatibel | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.der_fingerprint_hat_sich_geandert_kontext_wurde__e8791d | Erweitert / Nachweise → Erweitert | Die Berechnungsgrundlage hat sich geändert. Gespeicherte Zeitregeln konnten deshalb nicht wiederhergestellt werden. | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.unvollstandig_dc0649 | Erweitert / Nachweise | Unvollständig | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.keine_diagnose_verfugbar_5e4723 | Erweitert / Nachweise | Keine Diagnose verfügbar | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.der_contract_existiert_in_der_aktiven_registry_n_e38687 | Erweitert / Nachweise | Der Vertrag existiert in der aktiven Konfiguration nicht oder ist nicht konfiguriert. | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.wiederherstellung_066f4c | Erweitert / Nachweise | Wiederherstellung | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.identitat_wiederherstellung_c1cd99 | Erweitert / Nachweise | Identität &amp; Wiederherstellung | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.startfall_21a6b9 | Erweitert / Nachweise | Startfall | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.nachste_falligkeit_8bdf5b | Erweitert / Nachweise | Nächste Fälligkeit | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.gespeicherter_fingerprint_0c9622 | Erweitert / Nachweise → Erweitert | Gespeicherte Berechnungsgrundlage | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.erwarteter_fingerprint_78ff3b | Erweitert / Nachweise → Erweitert | Erwartete Berechnungsgrundlage | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.temporal_840fec | Erweitert / Nachweise | Zeitregel | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.nur_zeit_und_identitatsfelder_vorherige_rohwerte_e154ad | Erweitert / Nachweise | Nur Zeit- und Identitätsfelder; vorherige Rohwerte werden nicht ausgegeben. | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.knoten_abcd86 | Erweitert / Nachweise | Knoten | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.seit_b00312 | Erweitert / Nachweise | Seit | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.grace_bis_1a1c13 | Erweitert / Nachweise | Haltefrist bis | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.grace_aktiv_c2d892 | Erweitert / Nachweise | Haltefrist aktiv | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.lucke_079b36 | Erweitert / Nachweise | Lücke | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.restore_a76e13 | Erweitert / Nachweise | Wiederherstellung | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.ausstehend_345f38 | Erweitert / Nachweise | ausstehend | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.state_machine_801376 | Erweitert / Nachweise | Ablauf | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.keine_state_machine_6f3191 | Erweitert / Nachweise | Kein Ablauf | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.dieser_contract_verwendet_keine_state_machine_a52923 | Erweitert / Nachweise | Dieser Vertrag verwendet keinen Ablauf. | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.zustande_f5ef55 | Erweitert / Nachweise | Zustände | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.deadline_6fcb38 | Erweitert / Nachweise | Frist | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.sessions_6fa3cb | Erweitert / Nachweise | Sitzungen | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.befehle_23a3b7 | Erweitert / Nachweise | Befehle | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.aktueller_zustand_c391dc | Erweitert / Nachweise | Aktueller Zustand | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.vorheriger_zustand_bbe7d8 | Erweitert / Nachweise | Vorheriger Zustand | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.grund_ausloser_50d333 | Erweitert / Nachweise | Grund / Auslöser | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.session_6959b4 | Erweitert / Nachweise | Sitzung | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.herkunft_514fce | Erweitert / Nachweise | Herkunft | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.transitionen_41ef48 | Erweitert / Nachweise | Übergänge | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.von_640e86 | Erweitert / Nachweise | Von | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.nach_0ea777 | Erweitert / Nachweise | Nach | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.ereignis_af9e77 | Erweitert / Nachweise | Ereignis | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.grund_b45f40 | Erweitert / Nachweise | Grund | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.explain_3b61e4 | Erweitert / Nachweise | Erklärung | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.DiagnosticsPage.contract_a6f5b0 | Erweitert / Nachweise | Vertrag | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.DiagnosticsPage.wahlen_602246 | Erweitert / Nachweise | — wählen — | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.DiagnosticsPage.es_wurde_noch_kein_snapshot_empfangen_ec5820 | Erweitert / Nachweise | Es wurde noch kein vollständiger Stand empfangen ( | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.DiagnosticsPage.keine_aktiven_contracts_ec85c7 | Erweitert / Nachweise | Keine aktiven Verträge | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.DiagnosticsPage.die_aktive_registry_enthalt_keine_aktivierten_co_ee9568 | Erweitert / Nachweise | Die aktive Konfiguration enthält keine aktivierten Verträge oder es ist keine Konfiguration aktiv. | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.DiagnosticsPage.contract_wahlen_um_felder_quality_reasons_und_ev_31617c | Erweitert / Nachweise | Vertrag wählen, um Felder, Qualität, Gründe und Nachweis zu sehen. | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.DiagnosticsPage.bestatigt_61794f | Erweitert / Nachweise | Bestätigt | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.DiagnosticsPage.nein_4d03db | Erweitert / Nachweise | nein | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.DiagnosticsPage.epochen_570ce9 | Erweitert / Nachweise → Erweitert | Epochen | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.DiagnosticsPage.keine_epochen_in_den_geladenen_zeilen_2208ad | Erweitert / Nachweise → Erweitert | Keine Epochen in den geladenen Zeilen. | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.DiagnosticsPage.max_seq_384fa8 | Erweitert / Nachweise | max. Seq  | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.DiagnosticsPage.lucken_3bdb09 | Erweitert / Nachweise | Lücken | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.DiagnosticsPage.lucken_history_gaps_6d2e41 | Erweitert / Nachweise | Lücken im Verlauf | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.DiagnosticsPage.aktuelle_diagnose_meldet_fa6c61 | Erweitert / Nachweise | Aktuelle Diagnose meldet  | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.DiagnosticsPage.seq_43ac26 | Erweitert / Nachweise | Seq | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.DiagnosticsPage.gesundheit_1c7f2f | Erweitert / Nachweise | Gesundheit | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.DiagnosticsPage.live_zustand_39e6cc | Erweitert / Nachweise | Aktueller Zustand | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.DiagnosticsPage.contract_wahlen_fur_explain_temporal_restore_und_bc22e6 | Erweitert / Nachweise | Vertrag wählen für Erklärung, Zeitregel, Wiederherstellung und Ablauf. | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.DiagnosticsPage.evidence_03867a | Erweitert / Nachweise | Nachweis | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.DiagnosticsPage.commands_b269dc | Erweitert / Nachweise | Befehle | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.EvidenceLookup.keine_aufgezeichnete_evidenz_b25154 | Erweitert / Nachweise | Kein gespeicherter Nachweis | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.EvidenceLookup.evidenz_nicht_lesbar_f315c2 | Erweitert / Nachweise | Nachweis nicht lesbar | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.EvidenceLookup.zu_dieser_referenz_liegt_keine_beobachtung_vor_z_825a45 | Erweitert / Nachweise | Zu dieser Referenz liegt keine Beobachtung vor (z. B. von einer älteren Laufzeit nicht aufgezeichnet). Es wird nichts rekonstruiert. | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.EvidenceLookup.evidenz_88ffe3 | Erweitert / Nachweise | Nachweis | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.EvidenceLookup.auflosen_6413ae | Erweitert / Nachweise | Auflösen | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.EvidenceLookup.nicht_lesbar_05abf0 | Erweitert / Nachweise | Nicht lesbar | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.EvidenceLookup.keine_aktuelle_beobachtung_4e0775 | Erweitert / Nachweise | Keine aktuelle Beobachtung | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.erster_treffer_e8c4e8 | Erweitert / Nachweise | Erster Treffer | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.state_machine_801376 | Erweitert / Nachweise | Ablauf | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.nicht_anwendbar_af8969 | Erweitert / Nachweise | Nicht anwendbar | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.kein_explain_trace_vorhanden_e15923 | Erweitert / Nachweise | Noch kein Erklärungsverlauf vorhanden | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.explain_trace_c40389 | Erweitert / Nachweise | Warum entsteht dieser Wert? | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.gekurzt_1_024_eintrage_429de4 | Erweitert / Nachweise | gekürzt (1 024 Einträge) | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.zeitpunkt_606cdc | Erweitert / Nachweise | Zeitpunkt:  | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.ausloser_4716db | Erweitert / Nachweise | Auslöser:  | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.revision_5fdcbb | Erweitert / Nachweise | Version:  | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.aufwand_a56513 | Erweitert / Nachweise | Aufwand:  | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.schritte_4ca538 | Erweitert / Nachweise | Schritte | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.bezug_e6d683 | Erweitert / Nachweise | Bezug | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.status_920e41 | Erweitert / Nachweise | Status | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.grunde_auswahl_e1f635 | Erweitert / Nachweise | Gründe / Auswahl | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.evidence_03867a | Erweitert / Nachweise | Nachweis | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.auswahl_nicht_aufgezeichnet_092f1a | Erweitert / Nachweise | Auswahl nicht aufgezeichnet | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.qualitat_nicht_aufgezeichnet_70a777 | Erweitert / Nachweise | Qualität nicht aufgezeichnet | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.gewahlt_3dbfa8 | Erweitert / Nachweise | Gewählt:  | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.nicht_aufgezeichnet_716a55 | Erweitert / Nachweise | nicht aufgezeichnet | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.kandidaten_021e5b | Erweitert / Nachweise | · Kandidaten:  | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.ref_817996 | Erweitert / Nachweise | Ref. | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.der_trace_enthalt_keine_schritte_95fc29 | Erweitert / Nachweise | Der Erklärungsverlauf enthält keine Schritte. | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.HistoryTab.beobachtungen_0b2f38 | Erweitert / Nachweise | Beobachtungen | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.HistoryTab.deadlines_6aff5f | Erweitert / Nachweise | Fristen | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.HistoryTab.commands_b269dc | Erweitert / Nachweise | Befehle | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.HistoryTab.diagnose_audit_ereignisse_46bb26 | Erweitert / Nachweise | Diagnose- &amp; Protokoll-Ereignisse | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.HistoryTab.aktivierungen_070c5d | Erweitert / Nachweise | Übernahmen | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.HistoryTab.historie_nicht_lesbar_7856db | Erweitert / Nachweise | Historie nicht lesbar | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.HistoryTab.keine_eintrage_35719c | Erweitert / Nachweise | Keine Einträge | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.HistoryTab.fur_diese_auswahl_liegen_keine_eintrage_vor_d256a2 | Erweitert / Nachweise | Für diese Auswahl liegen keine Einträge vor. | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.HistoryTab.zeit_74f249 | Erweitert / Nachweise | Zeit | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.HistoryTab.inhalt_3cc465 | Erweitert / Nachweise | Inhalt | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.HistoryTab.details_ausblenden_034376 | Erweitert / Nachweise | Details ausblenden | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.HistoryTab.details_anzeigen_cf5436 | Erweitert / Nachweise | Details anzeigen | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.HistoryTab.geladen_neueste_zuerst_6e064a | Erweitert / Nachweise | geladen · neueste zuerst | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.HistoryTab.ladt_c8ebc9 | Erweitert / Nachweise | Lädt … | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.HistoryTab.altere_eintrage_laden_f8e8e1 | Erweitert / Nachweise | Ältere Einträge laden | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.HistoryTab.ende_der_historie_e37499 | Erweitert / Nachweise | Ende der Historie | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.HistoryTab.historienfilter_862931 | Erweitert / Nachweise | Historienfilter | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.HistoryTab.art_75df35 | Erweitert / Nachweise | Art | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.HistoryTab.von_lokal_61799d | Erweitert / Nachweise | Von (lokal) | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.HistoryTab.beginn_liegt_nach_dem_ende_ff3c71 | Erweitert / Nachweise | Beginn liegt nach dem Ende. | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.HistoryTab.bis_lokal_4d9697 | Erweitert / Nachweise | Bis (lokal) | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.HistoryTab.filter_anwenden_2ed52c | Erweitert / Nachweise | Filter anwenden | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.HistoryTab.zurucksetzen_1ba046 | Erweitert / Nachweise | Zurücksetzen | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.HistoryTab.historienzeilen_ee988b | Erweitert / Nachweise | Historienzeilen | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.graph.buildGraph.ergebnis_von_v0_b655b9 | Zusammenhänge | Ergebnis von {v0} | wie bisher | Geprüft; beibehalten. |
| features.graph.buildGraph.liveness_3f256d | Zusammenhänge | Erreichbarkeit | wie bisher | Geprüft; beibehalten. |
| features.graph.buildGraph.dependency_711595 | Zusammenhänge | Abhängigkeit | wie bisher | Geprüft; beibehalten. |
| features.graph.GraphPage.aus_2337c3 | Zusammenhänge | aus | wie bisher | Geprüft; beibehalten. |
| features.graph.GraphPage.abhangigkeitsgraph_52b36e | Zusammenhänge | Abhängigkeitsgraph | wie bisher | Geprüft; beibehalten. |
| features.graph.GraphPage.abgeleitetes_ergebnis_1c7c27 | Zusammenhänge | Abgeleitetes Ergebnis | wie bisher | Geprüft; beibehalten. |
| features.graph.GraphPage.details_45989d | Zusammenhänge | Details | wie bisher | Geprüft; beibehalten. |
| features.graph.GraphPage.status_920e41 | Zusammenhänge | Status | wie bisher | Geprüft; beibehalten. |
| features.graph.GraphPage.verfugbar_e5a644 | Zusammenhänge | verfügbar | wie bisher | Geprüft; beibehalten. |
| features.graph.GraphPage.nicht_verfugbar_9a98b3 | Zusammenhänge | nicht verfügbar | wie bisher | Geprüft; beibehalten. |
| features.graph.GraphPage.kein_live_zustand_deaktiviert_nur_im_draft_oder__f8cc5d | Zusammenhänge | Kein aktueller Zustand: Der Vertrag ist ausgeschaltet oder wurde noch nicht übernommen. | wie bisher | Geprüft; beibehalten. |
| features.graph.GraphPage.hangt_ab_von_e6eb2f | Zusammenhänge | Hängt ab von ( | wie bisher | Geprüft; beibehalten. |
| features.graph.GraphPage.wird_verwendet_von_f076e4 | Zusammenhänge | Wird verwendet von ( | wie bisher | Geprüft; beibehalten. |
| features.graph.GraphPage.detailansicht_9d72e5 | Zusammenhänge | Detailansicht | wie bisher | Geprüft; beibehalten. |
| features.graph.GraphPage.diagnose_64dd65 | Zusammenhänge | Diagnose | wie bisher | Geprüft; beibehalten. |
| features.graph.GraphPage.contract_offnen_019eff | Zusammenhänge | Vertrag öffnen | wie bisher | Geprüft; beibehalten. |
| features.graph.GraphPage.quelle_offnen_16c604 | Zusammenhänge | Quelle öffnen | wie bisher | Geprüft; beibehalten. |
| features.graph.GraphPage.graph_32ab01 | Zusammenhänge | Zusammenhänge | wie bisher | Geprüft; beibehalten. |
| features.graph.GraphPage.knoten_suchen_5bcf84 | Zusammenhänge | Knoten suchen | wie bisher | Geprüft; beibehalten. |
| features.graph.GraphPage.knoten_suchen_64e35f | Zusammenhänge | Knoten suchen … | wie bisher | Geprüft; beibehalten. |
| features.graph.GraphPage.auswahlen_0bf1ed | Zusammenhänge | Auswählen | wie bisher | Geprüft; beibehalten. |
| features.graph.GraphPage.nachbarschaft_d49e47 | Zusammenhänge | Nachbarschaft | wie bisher | Geprüft; beibehalten. |
| features.graph.GraphPage.nachbarschaft_1_schritt_6ed35c | Zusammenhänge | Nachbarschaft: 1 Schritt | wie bisher | Geprüft; beibehalten. |
| features.graph.GraphPage.nachbarschaft_2_schritte_edd4a3 | Zusammenhänge | Nachbarschaft: 2 Schritte | wie bisher | Geprüft; beibehalten. |
| features.graph.GraphPage.nachbarschaft_3_schritte_0df84f | Zusammenhänge | Nachbarschaft: 3 Schritte | wie bisher | Geprüft; beibehalten. |
| features.graph.GraphPage.liveness_dependencies_4224a7 | Zusammenhänge | Erreichbarkeit &amp; Abhängigkeiten | wie bisher | Geprüft; beibehalten. |
| features.graph.GraphPage.quelle_037889 | Zusammenhänge | Quelle | wie bisher | Geprüft; beibehalten. |
| features.graph.GraphPage.contract_gesund_0a175e | Zusammenhänge | Vertrag gesund | wie bisher | Geprüft; beibehalten. |
| features.graph.GraphPage.eingeschrankt_7c77f8 | Zusammenhänge | eingeschränkt | wie bisher | Geprüft; beibehalten. |
| features.graph.GraphPage.ergebnis_cd8e22 | Zusammenhänge | Ergebnis | wie bisher | Geprüft; beibehalten. |
| features.graph.GraphPage.zustandsfarben_letzter_bekannter_stand_live_verb_243a87 | Zusammenhänge | Zustandsfarben: letzter bekannter Stand, Verbindung zur App nicht aktuell. | wie bisher | Geprüft; beibehalten. |
| features.graph.GraphPage.noch_nichts_darzustellen_acbf63 | Zusammenhänge | Noch nichts darzustellen | wie bisher | Geprüft; beibehalten. |
| features.graph.GraphPage.knotendetails_1af0bd | Zusammenhänge | Knotendetails | wie bisher | Geprüft; beibehalten. |
| features.graph.GraphPage.knoten_wahlen_b5df2f | Zusammenhänge | Knoten wählen | wie bisher | Geprüft; beibehalten. |
| features.graph.GraphPage.klicken_sie_einen_knoten_an_um_zustand_abhangigk_356431 | Zusammenhänge | Klicke einen Knoten an, um Zustand, Abhängigkeiten und Sprungziele zu sehen. | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.die_aktive_revision_hat_sich_wahrend_der_prufung_38126e | Entwürfe und Konfigurationen | Die aktive Version hat sich während der Prüfung geändert. Erneut prüfen. | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.die_aktive_revision_ist_inzwischen_v0_gepruft_ge_481253 | Entwürfe und Konfigurationen | Die aktive Version ist inzwischen {v0} (geprüft gegen {v1}). | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.konflikt_nichts_wurde_aktiviert_8709dc | Entwürfe und Konfigurationen | Konflikt – nichts wurde übernommen | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.stand_neu_laden_und_erneut_prufen_346ba0 | Entwürfe und Konfigurationen | Stand neu laden und erneut prüfen | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.der_server_hat_die_aktivierung_abgelehnt_9260c9 | Entwürfe und Konfigurationen | Die App hat die Übernahme abgelehnt | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.aktion_fehlgeschlagen_3a20cc | Entwürfe und Konfigurationen | Aktion fehlgeschlagen | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.prufergebnis_veraltet_ed4995 | Entwürfe und Konfigurationen | Prüfergebnis veraltet | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.erneut_prufen_7da626 | Entwürfe und Konfigurationen | Erneut prüfen | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.der_draft_wurde_zwischenzeitlich_auf_v_v0_geande_f36298 | Entwürfe und Konfigurationen | Der Entwurf wurde zwischenzeitlich auf v{v0} geändert (geöffnet: v{v1}). Neu laden und erneut prüfen. | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.der_draft_hat_sich_wahrend_der_prufung_geandert__832d36 | Entwürfe und Konfigurationen | Der Entwurf hat sich während der Prüfung geändert. Neu laden und erneut prüfen. | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.registry_aktivieren_8c0eff | Entwürfe und Konfigurationen | Konfiguration übernehmen | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.schlie_en_b808f6 | Entwürfe und Konfigurationen | Schließen | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.ich_habe_die_auswirkungen_gepruft_und_aktiviere__007da8 | Entwürfe und Konfigurationen | Ich habe die Auswirkungen geprüft und übernehme diesen Stand als Version  | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.zum_ubernehmen_zuerst_die_auswirkungen_prufen_un_5ce543 | Entwürfe und Konfigurationen | Zum Übernehmen zuerst die Auswirkungen prüfen und bestätigen. | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.abbrechen_f7ff11 | Entwürfe und Konfigurationen | Abbrechen | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.jetzt_aktivieren_957b0a | Entwürfe und Konfigurationen | Jetzt übernehmen | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.aktivierung_andert_den_aktiven_zustand_5e5312 | Entwürfe und Konfigurationen | Übernahme ändert den aktiven Zustand | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.drafts_sind_bis_zu_diesem_schritt_wirkungslos_di_60155e | Entwürfe und Konfigurationen | Entwürfe sind bis zu diesem Schritt wirkungslos. Die Übernahme ersetzt die aktive Konfiguration (aktuell Version  | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.atomar_und_mit_versionsprufung_rucknahme_geht_nu_906a06 | Entwürfe und Konfigurationen | ). Frühere Versionen bleiben erhalten. Du kannst später auf eine frühere Version zurücksetzen. | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.server_pruft_den_gespeicherten_draft_afe932 | Entwürfe und Konfigurationen | App prüft den gespeicherten Entwurf … | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.prufung_nicht_moglich_9c9bd1 | Entwürfe und Konfigurationen | Prüfung nicht möglich | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.der_gespeicherte_draft_ist_nicht_gultig_99bc6f | Entwürfe und Konfigurationen | Der gespeicherte Entwurf ist nicht gültig | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.aktivieren_ist_erst_nach_korrektur_und_erneutem__0d3dee | Entwürfe und Konfigurationen | Übernehmen ist erst nach Korrektur und erneutem Speichern möglich. | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.der_historische_stand_wird_als_neue_revision_akt_62c809 | Entwürfe und Konfigurationen | Der frühere Stand wird als neue Version übernommen. Die bisherigen Versionen bleiben erhalten. | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.ich_mochte_revision_5d682d | Entwürfe und Konfigurationen | Ich möchte Version  | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.als_neue_revision_9a365f | Entwürfe und Konfigurationen | als neue Version  | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.aktivieren_fdb22a | Entwürfe und Konfigurationen | übernehmen. | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.zum_zurucksetzen_zuerst_die_auswirkungen_prufen__6e723c | Entwürfe und Konfigurationen | Zum Zurücksetzen zuerst die Auswirkungen prüfen und bestätigen. | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.zuruckrollen_1c5e6f | Entwürfe und Konfigurationen | Zurücksetzen | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.neue_revision_1e5cad | Entwürfe und Konfigurationen | Neue Version  | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.aktiv_3139fc | Entwürfe und Konfigurationen | aktiv | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.inhalt_entspricht_revision_3fded2 | Entwürfe und Konfigurationen | Inhalt entspricht Version  | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.gehaltene_zeitkontexte_konnen_bei_geanderten_fin_7ae16f | Entwürfe und Konfigurationen | . Wenn sich Berechnungsregeln geändert haben, können betroffene Abläufe neu beginnen. | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.rollback_andert_den_aktiven_zustand_975420 | Entwürfe und Konfigurationen | Zurücksetzen ändert den aktiven Zustand | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.auswirkungen_gegenuber_der_aktuell_aktiven_revis_056129 | Entwürfe und Konfigurationen | Auswirkungen gegenüber der aktuell aktiven Version  | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.server_analysiert_den_historischen_stand_7fcf03 | Entwürfe und Konfigurationen | App analysiert den historischen Stand … | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.analyse_nicht_moglich_e876eb | Entwürfe und Konfigurationen | Analyse nicht möglich | wie bisher | Geprüft; beibehalten. |
| features.registry.ActivationDialogs.er_kann_nicht_zuruckgerollt_werden_a731a6 | Entwürfe und Konfigurationen | Er kann nicht zurückgesetzt werden. | wie bisher | Geprüft; beibehalten. |
| features.registry.DiffView.dependencies_2e41b1 | Entwürfe und Konfigurationen | Abhängigkeiten | wie bisher | Geprüft; beibehalten. |
| features.registry.DiffView.sources_caf85b | Entwürfe und Konfigurationen | Quellen | wie bisher | Geprüft; beibehalten. |
| features.registry.DiffView.bindings_7697ab | Entwürfe und Konfigurationen | Verknüpfungen | wie bisher | Geprüft; beibehalten. |
| features.registry.DiffView.kataloge_daf282 | Entwürfe und Konfigurationen | Wertelisten | wie bisher | Geprüft; beibehalten. |
| features.registry.DiffView.contracts_0488ac | Entwürfe und Konfigurationen | Verträge | wie bisher | Geprüft; beibehalten. |
| features.registry.DiffView.definitionen_871a91 | Entwürfe und Konfigurationen | Vorlagen | wie bisher | Geprüft; beibehalten. |
| features.registry.DiffView.keine_anderung_gegenuber_der_aktiven_revision_b4a476 | Entwürfe und Konfigurationen | Keine Änderung gegenüber der aktiven Version | wie bisher | Geprüft; beibehalten. |
| features.registry.DiffView.contracts_hinzugefugt_aa1b10 | Entwürfe und Konfigurationen | Verträge hinzugefügt | wie bisher | Geprüft; beibehalten. |
| features.registry.DiffView.contracts_entfernt_5c5965 | Entwürfe und Konfigurationen | Verträge entfernt | wie bisher | Geprüft; beibehalten. |
| features.registry.DiffView.contracts_geandert_59d44d | Entwürfe und Konfigurationen | Verträge geändert | wie bisher | Geprüft; beibehalten. |
| features.registry.DiffView.direkt_betroffen_832e51 | Entwürfe und Konfigurationen | Direkt betroffen | wie bisher | Geprüft; beibehalten. |
| features.registry.DiffView.transitiv_betroffen_ef01a8 | Entwürfe und Konfigurationen | Indirekt betroffen | wie bisher | Geprüft; beibehalten. |
| features.registry.DiffView.identitatswechsel_quellen_9211e3 | Entwürfe und Konfigurationen | Identitätswechsel Quellen | wie bisher | Geprüft; beibehalten. |
| features.registry.DiffView.identitatswechsel_bindings_3f8a12 | Entwürfe und Konfigurationen | Identitätswechsel Verknüpfungen | wie bisher | Geprüft; beibehalten. |
| features.registry.DiffView.fristen_bleiben_erhalten_bcbfe1 | Entwürfe und Konfigurationen | Fristen bleiben erhalten | wie bisher | Geprüft; beibehalten. |
| features.registry.DiffView.ja_bei_kompatiblem_fingerprint_219c13 | Entwürfe und Konfigurationen → Erweitert | Ja, wenn die Prüfsumme übereinstimmt | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.registry.DiffView.unverandert_85e10f | Entwürfe und Konfigurationen | unverändert | wie bisher | Geprüft; beibehalten. |
| features.registry.DiffView.v0_v1_neu_v2_geandert_v3_entfernt_80a78f | Entwürfe und Konfigurationen | {v0}: {v1} neu · {v2} geändert · {v3} entfernt | wie bisher | Geprüft; beibehalten. |
| features.registry.DiffView.hinzugefugt_1625f5 | Entwürfe und Konfigurationen | Hinzugefügt | wie bisher | Geprüft; beibehalten. |
| features.registry.DiffView.entfernt_d0124f | Entwürfe und Konfigurationen | Entfernt | wie bisher | Geprüft; beibehalten. |
| features.registry.DiffView.geandert_d63c93 | Entwürfe und Konfigurationen | Geändert | wie bisher | Geprüft; beibehalten. |
| features.registry.DiffView.felder_ad2dff | Entwürfe und Konfigurationen | Felder:  | wie bisher | Geprüft; beibehalten. |
| features.registry.DiffView.pfadliste_gekurzt_server_limit_1_024_344b24 | Entwürfe und Konfigurationen | Pfadliste gekürzt (App-Limit 1 024). | wie bisher | Geprüft; beibehalten. |
| features.registry.DiffView.betroffene_ausgabefelder_konservativ_1da6f9 | Entwürfe und Konfigurationen | Möglicherweise betroffene Werte | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.dependencies_2e41b1 | Entwürfe und Konfigurationen | Abhängigkeiten | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.sources_caf85b | Entwürfe und Konfigurationen | Quellen | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.bindings_7697ab | Entwürfe und Konfigurationen | Verknüpfungen | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.kataloge_daf282 | Entwürfe und Konfigurationen | Wertelisten | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.definitionen_871a91 | Entwürfe und Konfigurationen | Vorlagen | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.contracts_0488ac | Entwürfe und Konfigurationen | Verträge | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.registry_json_dceba9 | Entwürfe und Konfigurationen | Konfiguration-JSON | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.ubernehmen_936378 | Entwürfe und Konfigurationen | Übernehmen | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.zurucksetzen_1ba046 | Entwürfe und Konfigurationen | Zurücksetzen | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.draft_v0_nicht_gefunden_ea702b | Entwürfe und Konfigurationen | Entwurf „{v0}“ nicht gefunden | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.er_wurde_geloscht_oder_hat_nie_existiert_0556f2 | Entwürfe und Konfigurationen | Er wurde gelöscht oder hat nie existiert. | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.ein_anderer_draft_hat_ungespeicherte_anderungen_261d0b | Entwürfe und Konfigurationen | Ein anderer Entwurf hat ungespeicherte Änderungen | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.geoffnet_ist_e6c05b | Entwürfe und Konfigurationen | Geöffnet ist „ | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.speichern_sie_ihn_zuerst_oder_verwerfen_sie_die__baa37d | Entwürfe und Konfigurationen | “. Speichere ihn zuerst oder verwirf die Änderungen, um diesen Entwurf zu öffnen. | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.zum_geoffneten_draft_855199 | Entwürfe und Konfigurationen | Zum geöffneten Entwurf | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.verwerfen_und_wechseln_88c2d1 | Entwürfe und Konfigurationen | Verwerfen und wechseln | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.anderungen_verwerfen_d16767 | Entwürfe und Konfigurationen | Änderungen verwerfen? | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.verwerfen_594ca8 | Entwürfe und Konfigurationen | Verwerfen | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.draft_wird_geoffnet_7f5df8 | Entwürfe und Konfigurationen | Entwurf wird geöffnet … | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.export_366489 | Entwürfe und Konfigurationen | Speichern als Datei | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.validierung_d4bf21 | Entwürfe und Konfigurationen | Prüfergebnis | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.der_server_pruft_den_bearbeiteten_auch_ungespeic_ebe4cd | Entwürfe und Konfigurationen | Die App prüft den bearbeiteten (auch ungespeicherten) Stand – ohne ihn zu übernehmen. | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.automatisch_f0b793 | Entwürfe und Konfigurationen | automatisch | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.prufung_nicht_moglich_9c9bd1 | Entwürfe und Konfigurationen | Prüfung nicht möglich | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.keine_fehler_gefunden_0d9c76 | Entwürfe und Konfigurationen | Keine Fehler gefunden | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.der_stand_ist_strukturell_und_semantisch_gultig_a85b70 | Entwürfe und Konfigurationen | Der Entwurf ist vollständig und fehlerfrei. | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.v0_fehler_v1_bffe5e | Entwürfe und Konfigurationen | {v0} Fehler{v1} | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.diff_auswirkungen_b6da5d | Entwürfe und Konfigurationen | Was sich ändert | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.gegenuber_der_aktiven_revision_nur_sichtbar_wenn_b51778 | Entwürfe und Konfigurationen | Gegenüber der aktiven Version – nur sichtbar, wenn der Stand gültig ist. | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.die_aktive_revision_ccaa57 | Entwürfe und Konfigurationen | die aktive Version | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.erst_nach_korrektur_der_fehler_verfugbar_bd3e1e | Entwürfe und Konfigurationen | Erst nach Korrektur der Fehler verfügbar. | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.wird_nach_der_validierung_angezeigt_0f660e | Entwürfe und Konfigurationen | Wird nach der Prüfung angezeigt. | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.json_experte_7a839f | Entwürfe und Konfigurationen | JSON-Experte | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.name_dcd1d5 | Entwürfe und Konfigurationen | Name | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.name_des_drafts_2ca771 | Entwürfe und Konfigurationen | Name des Entwurfs | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.aktivierung_90ba1a | Entwürfe und Konfigurationen | Übernahme | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.gespeichert_5e2338 | Entwürfe und Konfigurationen | Gespeichert | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.aktuell_gultig_2034ba | Entwürfe und Konfigurationen | Aktuell gültig | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.inhalt_3cc465 | Entwürfe und Konfigurationen | Inhalt | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.registry_studio_995ef2 | Entwürfe und Konfigurationen | Konfiguration | wie bisher | Geprüft; beibehalten. |
| features.registry.IssueList.validierungsfehler_2901a7 | Entwürfe und Konfigurationen | Fehler im Entwurf | wie bisher | Geprüft; beibehalten. |
| features.registry.RegistryPage.es_sind_bereits_100_entwurfe_vorhanden_zuerst_ei_f0bbd8 | Entwürfe und Konfigurationen | Es sind bereits 100 Entwürfe vorhanden. Zuerst einen Entwurf entfernen. | wie bisher | Geprüft; beibehalten. |
| features.registry.RegistryPage.neuer_draft_610fb2 | Entwürfe und Konfigurationen | Neuer Entwurf | wie bisher | Geprüft; beibehalten. |
| features.registry.RegistryPage.aktion_fehlgeschlagen_3a20cc | Entwürfe und Konfigurationen | Aktion fehlgeschlagen | wie bisher | Geprüft; beibehalten. |
| features.registry.RegistryPage.noch_keine_drafts_a1dbb9 | Entwürfe und Konfigurationen | Noch keine Entwürfe | wie bisher | Geprüft; beibehalten. |
| features.registry.RegistryPage.ersten_draft_anlegen_8191b5 | Entwürfe und Konfigurationen | Ersten Entwurf anlegen | wie bisher | Geprüft; beibehalten. |
| features.registry.RegistryPage.geoffnet_ungespeichert_62ba6c | Entwürfe und Konfigurationen | geöffnet · ungespeichert | wie bisher | Geprüft; beibehalten. |
| features.registry.RegistryPage.geoffnet_ec5e95 | Entwürfe und Konfigurationen | geöffnet | wie bisher | Geprüft; beibehalten. |
| features.registry.RegistryPage.v_4c9448 | Entwürfe und Konfigurationen | Stand  | wie bisher | Geprüft; beibehalten. |
| features.registry.RegistryPage.basis_revision_690542 | Entwürfe und Konfigurationen | · auf Grundlage von Version  | wie bisher | Geprüft; beibehalten. |
| features.registry.RegistryPage.erstellt_555e13 | Entwürfe und Konfigurationen | · erstellt  | wie bisher | Geprüft; beibehalten. |
| features.registry.RegistryPage.geandert_4147a3 | Entwürfe und Konfigurationen | · geändert  | wie bisher | Geprüft; beibehalten. |
| features.registry.RegistryPage.bearbeiten_84e45e | Entwürfe und Konfigurationen | Bearbeiten | wie bisher | Geprüft; beibehalten. |
| features.registry.RegistryPage.duplizieren_9d400c | Entwürfe und Konfigurationen | Duplizieren | wie bisher | Geprüft; beibehalten. |
| features.registry.RegistryPage.export_366489 | Entwürfe und Konfigurationen | Speichern als Datei | wie bisher | Geprüft; beibehalten. |
| features.registry.RegistryPage.loschen_6c2d35 | Entwürfe und Konfigurationen | Löschen | wie bisher | Geprüft; beibehalten. |
| features.registry.RegistryPage.draft_loschen_4ca056 | Entwürfe und Konfigurationen | Entwurf löschen? | wie bisher | Geprüft; beibehalten. |
| features.registry.RegistryPage.wird_endgultig_geloscht_version_v_5065b7 | Entwürfe und Konfigurationen | “ wird endgültig gelöscht (Version v | wie bisher | Geprüft; beibehalten. |
| features.registry.RegistryPage.die_aktive_registry_bleibt_unberuhrt_cf60a6 | Entwürfe und Konfigurationen | ). Die aktive Konfiguration bleibt unberührt. | wie bisher | Geprüft; beibehalten. |
| features.registry.RegistryPage.endgultig_loschen_6c1fd3 | Entwürfe und Konfigurationen | Endgültig löschen | wie bisher | Geprüft; beibehalten. |
| features.registry.RegistryPage.revisionen_sind_unveranderlich_aktivierung_und_r_45199a | Entwürfe und Konfigurationen | Versionen sind unveränderlich. Übernahme und Zurücksetzen erzeugen immer eine neue Version. | wie bisher | Geprüft; beibehalten. |
| features.registry.RegistryPage.zwei_revisionen_vergleichen_ebd968 | Entwürfe und Konfigurationen | Zwei Versionen vergleichen ( | wie bisher | Geprüft; beibehalten. |
| features.registry.RegistryPage.noch_keine_revision_bf7c3f | Entwürfe und Konfigurationen | Noch keine Version | wie bisher | Geprüft; beibehalten. |
| features.registry.RegistryPage.es_wurde_noch_nie_eine_registry_aktiviert_66d0b4 | Entwürfe und Konfigurationen | Es wurde noch keine Konfiguration übernommen. | wie bisher | Geprüft; beibehalten. |
| features.registry.RegistryPage.revision_v0_zum_vergleich_wahlen_d77c8e | Entwürfe und Konfigurationen | Version {v0} zum Vergleich wählen | wie bisher | Geprüft; beibehalten. |
| features.registry.RegistryPage.revision_e330d8 | Entwürfe und Konfigurationen | Version  | wie bisher | Geprüft; beibehalten. |
| features.registry.RegistryPage.aktiv_3139fc | Entwürfe und Konfigurationen | aktiv | wie bisher | Geprüft; beibehalten. |
| features.registry.RegistryPage.ansehen_8e3136 | Entwürfe und Konfigurationen | Ansehen | wie bisher | Geprüft; beibehalten. |
| features.registry.RegistryPage.als_draft_051157 | Entwürfe und Konfigurationen | Als Entwurf | wie bisher | Geprüft; beibehalten. |
| features.registry.RegistryPage.zuruckrollen_1c5e6f | Entwürfe und Konfigurationen | Auf diese Version zurücksetzen | wie bisher | Geprüft; beibehalten. |
| features.registry.RegistryPage.revision_v0_v1_1a2b5a | Entwürfe und Konfigurationen | Version {v0} ↔ {v1} | wie bisher | Geprüft; beibehalten. |
| features.registry.RegistryPage.strukturelle_differenz_der_konfigurationsdokumen_aee6e2 | Entwürfe und Konfigurationen | Hier siehst du, welche Einträge sich zwischen den beiden Versionen unterscheiden. Die Auswirkungen prüft die App vor dem Übernehmen oder Zurücksetzen. | wie bisher | Geprüft; beibehalten. |
| features.registry.RegistryPage.inhaltlich_identisch_8109af | Entwürfe und Konfigurationen | Inhaltlich identisch | wie bisher | Geprüft; beibehalten. |
| features.sources.SourcesPage.v0_hinzufugen_198d5a | Quellen und Verknüpfungen | {v0} hinzufügen | wie bisher | Geprüft; beibehalten. |
| features.sources.SourcesPage.v0_wahlen_24a7a9 | Quellen und Verknüpfungen | {v0} wählen | wie bisher | Geprüft; beibehalten. |
| features.sources.SourcesPage.wahlen_sie_links_einen_eintrag_oder_legen_sie_mi_17add4 | Quellen und Verknüpfungen | Wähle links einen Eintrag oder füge oben einen neuen hinzu. | wie bisher | Geprüft; beibehalten. |
| features.sources.SourcesPage.wahlen_sie_links_einen_eintrag_zur_ansicht_257139 | Quellen und Verknüpfungen | Wähle links einen Eintrag zur Ansicht. | wie bisher | Geprüft; beibehalten. |
| features.sources.SourcesPage.duplizieren_9d400c | Quellen und Verknüpfungen | Duplizieren | wie bisher | Geprüft; beibehalten. |
| features.sources.SourcesPage.entfernen_382837 | Quellen und Verknüpfungen | Entfernen | wie bisher | Geprüft; beibehalten. |
| features.sources.SourcesPage.v0_entfernen_f1cd8a | Quellen und Verknüpfungen | {v0} entfernen? | wie bisher | Geprüft; beibehalten. |
| features.sources.SourcesPage.sources_bindings_613cff | Quellen und Verknüpfungen | Quellen &amp; Verknüpfungen | wie bisher | Geprüft; beibehalten. |
| features.sources.SourcesPage.sources_caf85b | Quellen und Verknüpfungen | Quellen | wie bisher | Geprüft; beibehalten. |
| features.sources.SourcesPage.source_0e570c | Quellen und Verknüpfungen | Quelle | wie bisher | Geprüft; beibehalten. |
| features.sources.SourcesPage.liveness_fur_09aba4 | Quellen und Verknüpfungen | Erreichbarkeit für | wie bisher | Geprüft; beibehalten. |
| features.sources.SourcesPage.bindings_7697ab | Quellen und Verknüpfungen | Verknüpfungen | wie bisher | Geprüft; beibehalten. |
| features.sources.SourcesPage.binding_164c69 | Quellen und Verknüpfungen | Verknüpfung | wie bisher | Geprüft; beibehalten. |
| features.sources.SourcesPage.contracts_uber_diese_quelle_22a5c9 | Quellen und Verknüpfungen | Verträge über diese Quelle | wie bisher | Geprüft; beibehalten. |
| features.sources.SourcesPage.kataloge_daf282 | Quellen und Verknüpfungen | Wertelisten | wie bisher | Geprüft; beibehalten. |
| features.sources.SourcesPage.katalog_1c58e0 | Quellen und Verknüpfungen | Werteliste | wie bisher | Geprüft; beibehalten. |
| features.sources.SourcesPage.v_v0_v1_eintrage_a26921 | Quellen und Verknüpfungen | v{v0} · {v1} Einträge | wie bisher | Geprüft; beibehalten. |
| features.sources.SourcesPage.verwendet_von_bindings_6b4d50 | Quellen und Verknüpfungen | Verwendet von Verknüpfungen | wie bisher | Geprüft; beibehalten. |
| features.sources.SourcesPage.dependencies_2e41b1 | Quellen und Verknüpfungen | Abhängigkeiten | wie bisher | Geprüft; beibehalten. |
| features.sources.SourcesPage.dependency_711595 | Quellen und Verknüpfungen | Abhängigkeit | wie bisher | Geprüft; beibehalten. |
| lib.api.der_dienst_ist_nicht_erreichbar_793240 | Gemeinsame Oberfläche / Wertanzeige | Der Dienst ist nicht erreichbar. | wie bisher | Geprüft; beibehalten. |
| lib.api.es_sind_bereits_100_entwurfe_vorhanden_entfernen_f89be6 | Gemeinsame Oberfläche / Wertanzeige | Es sind bereits 100 Entwürfe vorhanden. Entferne zuerst einen nicht mehr benötigten Entwurf. | wie bisher | Geprüft; beibehalten. |
| lib.api.diese_entwurfs_id_ist_bereits_vergeben_2355ad | Gemeinsame Oberfläche / Wertanzeige | Diese Entwurfs-ID ist bereits vergeben. | wie bisher | Geprüft; beibehalten. |
| lib.api.geheimnisse_sind_in_der_konfiguration_nicht_erla_dfcfff | Gemeinsame Oberfläche / Wertanzeige | Geheimnisse sind in der Konfiguration nicht erlaubt. Entferne geheime Schlüssel und Zugangsdaten vor dem Einlesen. | wie bisher | Geprüft; beibehalten. |
| lib.api.der_draft_wurde_zwischenzeitlich_geandert_neu_la_8afab3 | Gemeinsame Oberfläche / Wertanzeige | Der Entwurf wurde zwischenzeitlich geändert. Neu laden und Änderungen zusammenführen. | wie bisher | Geprüft; beibehalten. |
| lib.api.die_aktive_revision_hat_sich_geandert_stand_neu__b101a1 | Gemeinsame Oberfläche / Wertanzeige | Die aktive Version hat sich geändert. Stand neu laden und erneut prüfen. | wie bisher | Geprüft; beibehalten. |
| lib.api.es_ist_noch_keine_registry_aktiv_2f47c4 | Gemeinsame Oberfläche / Wertanzeige | Es ist noch keine Konfiguration aktiv. | wie bisher | Geprüft; beibehalten. |
| lib.api.home_assistant_entitatsliste_derzeit_nicht_verfu_4a74b1 | Gemeinsame Oberfläche / Wertanzeige | Home-Assistant-Entitätsliste derzeit nicht verfügbar. | wie bisher | Geprüft; beibehalten. |
| lib.api.der_contract_ist_deaktiviert_225806 | Gemeinsame Oberfläche / Wertanzeige | Der Vertrag ist ausgeschaltet. | wie bisher | Geprüft; beibehalten. |
| lib.api.diese_revision_existiert_nicht_011869 | Gemeinsame Oberfläche / Wertanzeige | Diese Version existiert nicht. | wie bisher | Geprüft; beibehalten. |
| lib.api.die_anfrage_ist_ungultig_85729c | Gemeinsame Oberfläche / Wertanzeige | Die Anfrage ist ungültig. | wie bisher | Geprüft; beibehalten. |
| lib.api.zu_viele_anfragen_weitere_anfragen_warten_diese__545695 | Gemeinsame Oberfläche / Wertanzeige | Zu viele Anfragen. Weitere Anfragen warten; diese Aktion wurde nicht automatisch wiederholt. | wie bisher | Geprüft; beibehalten. |
| lib.api.keine_berechtigung_fur_diese_aktion_a1a527 | Gemeinsame Oberfläche / Wertanzeige | Keine Berechtigung für diese Aktion. | wie bisher | Geprüft; beibehalten. |
| lib.identifiers.hochstens_128_zeichen_a_z_oder_a_z_zuerst_nur_di_f5ba89 | Gemeinsame Oberfläche / Wertanzeige | Höchstens 128 Zeichen; A–Z oder a–z zuerst. Nur diese Buchstaben, Ziffern, Punkt, Unterstrich und Bindestrich; kein Punkt am Ende. | wie bisher | Geprüft; beibehalten. |
| lib.status.gultig_87b71a | Gemeinsame Oberfläche / Wertanzeige | gültig | wie bisher | Geprüft; beibehalten. |
| lib.status.wert_ist_aktuell_und_belegt_40eba5 | Gemeinsame Oberfläche / Wertanzeige | Wert ist aktuell und belegt. | wie bisher | Geprüft; beibehalten. |
| lib.status.gehalten_9ce589 | Gemeinsame Oberfläche / Wertanzeige | gehalten | wie bisher | Geprüft; beibehalten. |
| lib.status.unbekannt_a418e6 | Gemeinsame Oberfläche / Wertanzeige | unbekannt | wie bisher | Geprüft; beibehalten. |
| lib.status.kein_verwendbarer_wert_das_ist_weder_aus_noch_fa_23fda0 | Gemeinsame Oberfläche / Wertanzeige | Kein verwendbarer Wert. Das ist weder „aus“ noch „falsch“. | wie bisher | Geprüft; beibehalten. |
| lib.status.ungelost_1a4c83 | Gemeinsame Oberfläche / Wertanzeige | ungelöst | wie bisher | Geprüft; beibehalten. |
| lib.status.der_wert_konnte_nicht_eindeutig_bestimmt_werden_508be4 | Gemeinsame Oberfläche / Wertanzeige | Der Wert konnte nicht eindeutig bestimmt werden. | wie bisher | Geprüft; beibehalten. |
| lib.status.nicht_anwendbar_d9b971 | Gemeinsame Oberfläche / Wertanzeige | nicht anwendbar | wie bisher | Geprüft; beibehalten. |
| lib.status.gesund_35c867 | Gemeinsame Oberfläche / Wertanzeige | gesund | wie bisher | Geprüft; beibehalten. |
| lib.status.eingeschrankt_7c77f8 | Gemeinsame Oberfläche / Wertanzeige | eingeschränkt | wie bisher | Geprüft; beibehalten. |
| lib.status.einrichtung_unvollstandig_ab8de5 | Gemeinsame Oberfläche / Wertanzeige | Einrichtung unvollständig | wie bisher | Geprüft; beibehalten. |
| lib.status.die_app_optionen_sind_ungultig_im_supervisor_kor_b69b18 | Gemeinsame Oberfläche / Wertanzeige | Die App-Optionen sind ungültig. Im Supervisor korrigieren; der Einrichtungsassistent ändert sie nicht. | wie bisher | Geprüft; beibehalten. |
| lib.status.die_datenbank_ist_nicht_erreichbar_zustande_werd_8902d8 | Gemeinsame Oberfläche / Wertanzeige | Die Datenbank ist nicht erreichbar. Zustände werden nicht bestätigt; Änderungen sind abgelehnt. | wie bisher | Geprüft; beibehalten. |
| lib.status.leere_konfiguration_e2bdda | Gemeinsame Oberfläche / Wertanzeige | Leere Konfiguration | wie bisher | Geprüft; beibehalten. |
| lib.status.es_ist_noch_keine_registry_aktiv_das_ist_ein_gul_4a298e | Gemeinsame Oberfläche / Wertanzeige | Es ist noch keine Konfiguration aktiv. Das ist ein gültiger Anfangszustand, keine Störung. | wie bisher | Geprüft; beibehalten. |
| lib.status.bereitschaft_ausstehend_3353d4 | Gemeinsame Oberfläche / Wertanzeige | Bereitschaft ausstehend | wie bisher | Geprüft; beibehalten. |
| lib.status.eingeschrankte_quelle_333805 | Gemeinsame Oberfläche / Wertanzeige | Eingeschränkte Quelle | wie bisher | Geprüft; beibehalten. |
| lib.status.v0_contracts_konnen_unbekannt_oder_eingeschrankt_0d697c | Gemeinsame Oberfläche / Wertanzeige | {v0}. Verträge können unbekannt oder eingeschränkt sein; das System selbst läuft. | wie bisher | Geprüft; beibehalten. |
| lib.status.letzter_stand_unbestatigt_7c2d6f | Gemeinsame Oberfläche / Wertanzeige | Letzter Stand unbestätigt | wie bisher | Geprüft; beibehalten. |
| lib.status.offline_a17947 | Gemeinsame Oberfläche / Wertanzeige | Ohne Verbindung | wie bisher | Geprüft; beibehalten. |
| lib.status.verbindungsabbruch_b5a0d4 | Gemeinsame Oberfläche / Wertanzeige | Verbindungsabbruch | wie bisher | Geprüft; beibehalten. |
| lib.status.die_live_verbindung_ist_unterbrochen_gezeigt_wir_355e23 | Gemeinsame Oberfläche / Wertanzeige | Die Verbindung zur App ist unterbrochen. Gezeigt wird der letzte bekannte Stand; er kann veraltet sein. | wie bisher | Geprüft; beibehalten. |
| lib.status.systemstorung_43a12a | Gemeinsame Oberfläche / Wertanzeige | Systemstörung | wie bisher | Geprüft; beibehalten. |
| lib.status.storung_8f18d2 | Gemeinsame Oberfläche / Wertanzeige | Störung | wie bisher | Geprüft; beibehalten. |
| lib.status.nicht_bereit_11f40b | Gemeinsame Oberfläche / Wertanzeige | Nicht bereit | wie bisher | Geprüft; beibehalten. |
| lib.status.eingeschrankt_55b605 | Gemeinsame Oberfläche / Wertanzeige | Eingeschränkt | wie bisher | Geprüft; beibehalten. |
| lib.status.ladt_9dd9e4 | Gemeinsame Oberfläche / Wertanzeige | Lädt | wie bisher | Geprüft; beibehalten. |
| lib.status.leer_f4e0ac | Gemeinsame Oberfläche / Wertanzeige | Leer | wie bisher | Geprüft; beibehalten. |
| lib.status.bereit_8d4d48 | Gemeinsame Oberfläche / Wertanzeige | Bereit | wie bisher | Geprüft; beibehalten. |
| lib.status.ungultige_app_optionen_0faff6 | Gemeinsame Oberfläche / Wertanzeige | Ungültige App-Optionen | wie bisher | Geprüft; beibehalten. |
| lib.status.keine_aktive_registry_f699ee | Gemeinsame Oberfläche / Wertanzeige | Keine aktive Konfiguration | wie bisher | Geprüft; beibehalten. |
| setup.setup.datenbankeinrichtung_noch_nicht_abgeschlossen_78e93d | Ersteinrichtung | Datenbankeinrichtung noch nicht abgeschlossen. | wie bisher | Geprüft; beibehalten. |
| setup.setup.ha_verbindung_nicht_verfugbar_keine_bridge_konfi_e25bc0 | Ersteinrichtung | HA-Verbindung nicht verfügbar. Keine HA-Anbindung-Konfiguration übernommen. | wie bisher | Geprüft; beibehalten. |
| setup.setup.ha_verbindung_fehlgeschlagen_erreichbarkeit_und__783d6b | Ersteinrichtung | HA-Verbindung fehlgeschlagen. Erreichbarkeit und Berechtigung prüfen. | wie bisher | Geprüft; beibehalten. |
| setup.setup.bridge_noch_nicht_erkannt_hacs_installation_und__6d0651 | Ersteinrichtung | HA-Anbindung noch nicht erkannt. HACS-Installation und bestätigten HA-Neustart prüfen. | wie bisher | Geprüft; beibehalten. |
| setup.setup.bridge_konfiguration_nicht_bestatigt_zustand_in__27f18b | Ersteinrichtung | HA-Anbindung-Konfiguration nicht bestätigt. Zustand in HA prüfen; nicht blind wiederholen. | wie bisher | Geprüft; beibehalten. |
| setup.setup.postgresql_nicht_erreichbar_oder_anmeldung_tls_f_4d0581 | Ersteinrichtung | PostgreSQL nicht erreichbar oder Anmeldung/TLS fehlgeschlagen. Host, Zugangsdaten und Zertifikat prüfen. | wie bisher | Geprüft; beibehalten. |
| setup.setup.postgresql_14_oder_neuer_ist_erforderlich_85b1b5 | Ersteinrichtung | PostgreSQL 14 oder neuer ist erforderlich. | wie bisher | Geprüft; beibehalten. |
| setup.setup.die_anwendungsrolle_besitzt_administratorrechte_9d1faf | Ersteinrichtung | Die Anwendungsrolle besitzt Administratorrechte. | wie bisher | Geprüft; beibehalten. |
| setup.setup.die_datenbank_enthalt_fremde_daten_eine_eigene_l_0c9df2 | Ersteinrichtung | Die Datenbank enthält fremde Daten. Eine eigene leere Datenbank verwenden. | wie bisher | Geprüft; beibehalten. |
| setup.setup.installations_id_passt_nicht_zu_dieser_app_keine_f2dbbb | Ersteinrichtung | Installations-ID passt nicht zu dieser App. Keine Änderung übernommen. | wie bisher | Geprüft; beibehalten. |
| setup.setup.vorhandene_datenbank_nur_mit_ihrer_ausdrucklich__4ba1fc | Ersteinrichtung | Vorhandene Datenbank nur mit ihrer ausdrücklich bestätigten Installations-ID übernehmen. | wie bisher | Geprüft; beibehalten. |
| setup.setup.initialisierung_der_eigenen_leeren_datenbank_aus_edb871 | Ersteinrichtung | Initialisierung der eigenen leeren Datenbank ausdrücklich bestätigen. | wie bisher | Geprüft; beibehalten. |
| setup.setup.den_eingeschrankten_tls_schutz_ausdrucklich_best_604357 | Ersteinrichtung | Den eingeschränkten TLS-Schutz ausdrücklich bestätigen. | wie bisher | Geprüft; beibehalten. |
| setup.setup.ubernahme_der_verbindung_ausdrucklich_bestatigen_e1e494 | Ersteinrichtung | Übernahme der Verbindung ausdrücklich bestätigen. | wie bisher | Geprüft; beibehalten. |
| setup.setup.der_importcode_gehort_nicht_zu_diesem_einrichtun_ad0620 | Ersteinrichtung | Der Einlesencode gehört nicht zu diesem Einrichtungsskript. | wie bisher | Geprüft; beibehalten. |
| setup.setup.eingaben_oder_importcode_ungultig_bitte_prufen_4d9ba1 | Ersteinrichtung | Eingaben oder Einlesencode ungültig. Bitte prüfen. | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.willkommen_c4dc12 | Ersteinrichtung | Willkommen | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.bridge_einrichten_325458 | Ersteinrichtung | HA-Anbindung einrichten | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.abschluss_e47280 | Ersteinrichtung | Abschluss | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.bridge_erkannt_konfigurationseintrag_fehlt_41dc32 | Ersteinrichtung | HA-Anbindung erkannt, Konfigurationseintrag fehlt | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.bridge_nicht_erkannt_fehlt_oder_ha_neustart_steh_d102c5 | Ersteinrichtung | HA-Anbindung nicht erkannt: fehlt oder HA-Neustart steht aus | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.ha_verbindung_derzeit_nicht_erreichbar_d0026e | Ersteinrichtung | HA-Verbindung derzeit nicht erreichbar | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.ha_zugriff_nicht_autorisiert_0a376b | Ersteinrichtung | HA-Zugriff nicht autorisiert | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.bridge_wird_gepruft_35a305 | Ersteinrichtung | HA-Anbindung wird geprüft | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.postgresql_nicht_erreichbar_oder_anmeldung_tls_f_968aed | Ersteinrichtung | PostgreSQL nicht erreichbar oder Anmeldung/TLS fehlgeschlagen. Verbindung und Zertifikat prüfen; Einrichtung bleibt offen. | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.identitat_oder_schema_abgewiesen_verbindung_pruf_0debd0 | Ersteinrichtung | Identität oder Schema abgewiesen. Verbindung prüfen; keine automatische Neuinitialisierung. | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.einrichtung_fehlgeschlagen_959a79 | Ersteinrichtung | Einrichtung fehlgeschlagen. | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.ersteinrichtung_84c9bd | Ersteinrichtung | Ersteinrichtung | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.core_contracts_einrichten_c89657 | Ersteinrichtung | Mimir | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.schritt_c0f684 | Ersteinrichtung | Schritt  | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.von_16b4d3 | Ersteinrichtung | von  | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.einrichtungsfortschritt_b753dc | Ersteinrichtung | Einrichtungsfortschritt | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.der_datenbankstart_bleibt_gesperrt_identitat_und_1b065e | Ersteinrichtung | Der Datenbankstart bleibt gesperrt. Identität und Daten werden nicht verändert. | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.noch_nicht_konfiguriert_24db6c | Ersteinrichtung | Noch nicht konfiguriert | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.datenbank_eingerichtet_installations_id_a2ec23 | Ersteinrichtung | Datenbank eingerichtet. Installations-ID:  | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.bestehende_identitat_wird_beibehalten_697e3e | Ersteinrichtung | . Bestehende Identität wird beibehalten. | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.datenbankschritte_uberspringen_d4f0ab | Ersteinrichtung | Datenbankschritte überspringen | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.vorhandene_verbindung_wird_gepruft_oberflache_bl_32f31b | Ersteinrichtung | Vorhandene Verbindung wird geprüft. Oberfläche bleibt auch bei DB-Ausfall erreichbar. | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.verbindung_8ec4b6 | Ersteinrichtung | Verbindung  | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.ausdrucklich_neu_konfigurieren_8d323e | Ersteinrichtung | ausdrücklich neu konfigurieren | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.einrichtungsweg_d2aab1 | Ersteinrichtung | Einrichtungsweg | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.vorhandene_verbindung_verwenden_4ba967 | Ersteinrichtung | Vorhandene Verbindung verwenden | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.port_72e9a5 | Ersteinrichtung | Port | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.datenbank_4cc807 | Ersteinrichtung | Datenbank | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.passwort_a36c10 | Ersteinrichtung | Passwort | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.ssl_postgres_ca_pem_72603c | Ersteinrichtung | /ssl/postgres-ca.pem | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.version_wird_nach_authentifizierter_verbindung_g_bcfd63 | Ersteinrichtung | Version wird nach authentifizierter Verbindung geprüft; ohne Zugangsdaten nicht zuverlässig ermittelbar. | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.postgresql_erreichbar_tls_v0_version_und_zertifi_e4a728 | Ersteinrichtung | PostgreSQL erreichbar. TLS {v0}; Version und Zertifikat folgen bei Anmeldung. | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.erreichbarkeit_ohne_zugangsdaten_prufen_ab97c1 | Ersteinrichtung | Erreichbarkeit ohne Zugangsdaten prüfen | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.weiter_1e14bd | Ersteinrichtung | Weiter | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.host_port_namen_und_gegebenenfalls_passwort_pruf_df6e6a | Ersteinrichtung | Host, Port, Namen und gegebenenfalls Passwort prüfen. Namen: Kleinbuchstaben, Ziffern, Unterstrich. | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.verbindung_ubernehmen_0d954e | Ersteinrichtung | Verbindung übernehmen | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.skript_prufen_und_vollstandig_einmal_in_ein_priv_163953 | Ersteinrichtung | Skript prüfen und vollständig einmal in ein privates Terminal des PostgreSQL-LXC einfügen. Es läuft lokal als postgres; keine Datei und kein Verzeichnis müssen manuell angelegt werden. Linux, Python ab 3.10, psql und sudo erforderlich. Fremde Datenbanken/Rollen werden abgewiesen. | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.skript_8c598d | Ersteinrichtung | Skript | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.postgresql_einrichtungsskript_7896f8 | Ersteinrichtung | PostgreSQL-Einrichtungsskript | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.skript_kopieren_20d48d | Ersteinrichtung | Skript kopieren | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.geheimer_importcode_3f5e14 | Ersteinrichtung | Geheimer Einlesencode | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.importcode_kopieren_geheim_ea96b8 | Ersteinrichtung | Einlesencode kopieren (geheim) | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.eigene_leere_datenbank_ausdrucklich_initialisier_780b2a | Ersteinrichtung | Eigene leere Datenbank ausdrücklich initialisieren | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.bei_wiederherstellung_vorhandene_datenbank_id_au_a247ee | Ersteinrichtung | Bei Wiederherstellung: vorhandene Datenbank-ID ausdrücklich übernehmen | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.vorhandene_uuid_sonst_leer_479fff | Ersteinrichtung | Vorhandene UUID; sonst leer | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.eingeschrankten_tls_schutz_ausdrucklich_akzeptie_6c5204 | Ersteinrichtung | Eingeschränkten TLS-Schutz ausdrücklich akzeptieren | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.verbindung_prufen_und_als_alleinige_db_konfigura_7c2dc2 | Ersteinrichtung | Verbindung prüfen und als alleinige DB-Konfigurationsquelle der App speichern. Bei laufender Installation erst nach eigenem App-Neustart wirksam. | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.prufen_und_ubernehmen_6d85d6 | Ersteinrichtung | Prüfen und übernehmen | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.bridge_zustand_unbekannt_5482dd | Ersteinrichtung | HA-Anbindung-Zustand unbekannt | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.in_hacs_d237bf | Ersteinrichtung | In HACS  | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.levtos_core_contract_app_991b3f | Ersteinrichtung | Levtos/mimir | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.bifrost_694370 | Ersteinrichtung | bifrost | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.legacy_integration_nicht_auswahlen_3a1ea1 | Ersteinrichtung | ; Legacy-Integration nicht auswählen. | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.bridge_konfiguration_in_ha_offnen_473fc7 | Ersteinrichtung | HA-Anbindung-Konfiguration in HA öffnen | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.bridge_erneut_prufen_78c8e3 | Ersteinrichtung | HA-Anbindung erneut prüfen | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.weiter_ergebnisse_ansehen_a99408 | Ersteinrichtung | Weiter · Ergebnisse ansehen | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.genau_einen_bifrost_eintrag_in_ha__95dd29 | Ersteinrichtung | Genau einen Mimir HA-Anbindung-Eintrag in HA anlegen? Die Legacy-Integration wird nicht geändert. | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.bridge_konfigurationseintrag_anlegen_8c6e61 | Ersteinrichtung | HA-Anbindung-Konfigurationseintrag anlegen | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.ergebnis_cd8e22 | Ersteinrichtung | Ergebnis | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.datenbank_6fda4b | Ersteinrichtung | Datenbank:  | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.initialisierung_noch_ausstehend_e337ae | Ersteinrichtung | Initialisierung noch ausstehend | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.bridge_d2884b | Ersteinrichtung | . HA-Anbindung:  | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.neue_verbindung_gespeichert_eigener_app_neustart_286a9f | Ersteinrichtung | Neue Verbindung gespeichert. Eigener App-Neustart erforderlich. Vorher Backup und Ziel prüfen. | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.konfiguration_version_v0_ist_aktiv_3f9131 | Ersteinrichtung | Konfiguration: Version {v0} ist aktiv. | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.es_ist_noch_keine_konfiguration_ubernommen_45abe2 | Ersteinrichtung | Es ist noch keine Konfiguration übernommen. | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.der_aktive_konfigurationsstand_ist_noch_nicht_be_8968d0 | Ersteinrichtung | Der aktive Konfigurationsstand ist noch nicht bekannt. | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.der_assistent_selbst_ubernimmt_keine_konfigurati_867ac0 | Ersteinrichtung | Der Assistent selbst übernimmt keine Konfiguration. | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.einrichtung_abschlie_en_und_oberflache_offnen_ba08e2 | Ersteinrichtung | Einrichtung abschließen und Oberfläche öffnen | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.zuruck_548611 | Ersteinrichtung | Zurück | wie bisher | Geprüft; beibehalten. |
| components.ContractLiveState.v0_8b43bb | Gemeinsame Oberfläche / Wertanzeige |  · {v0} | wie bisher | Geprüft; beibehalten. |
| editors.common.fehler_f6cc01 | Formular für Vorlage / Quelle / Vertrag | Fehler | wie bisher | Geprüft; beibehalten. |
| editors.MachineEditor.befehl_v0_fc4317 | Formular für Vorlage / Quelle / Vertrag | Befehl: {v0} | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.typumwandlung_8e7b19 | Formular für Vorlage / Quelle / Vertrag; Quellen und Verknüpfungen | Typumwandlung | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.katalog_zuordnung_b96c20 | Formular für Vorlage / Quelle / Vertrag; Quellen und Verknüpfungen | Wertelisten-Zuordnung | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.draft_definition_fd7330 | Formular für Vorlage / Quelle / Vertrag |  (Entwurf-Vorlage) | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.definition_96ce96 | Formular für Vorlage / Quelle / Vertrag |  (Vorlage) | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.paket_92cb87 | Formular für Vorlage / Quelle / Vertrag |  (Paket) | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.pflicht_6a047f | Formular für Vorlage / Quelle / Vertrag | Pflicht | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.optional_ec91fd | Formular für Vorlage / Quelle / Vertrag | freiwillig | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.v0_8b43bb | Formular für Vorlage / Quelle / Vertrag |  · {v0} | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.bereit_7f2ffe | Einstellungen | bereit | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.verbergen_a710cb | Einstellungen | Verbergen | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.anzeigen_ccb27f | Einstellungen | Anzeigen | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.kopiert_c2756e | Einstellungen | Kopiert | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.kopieren_472050 | Einstellungen | Kopieren | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractDetailPage.aktiviert_acb27b | Vertrag und Vorlage | eingeschaltet | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractDetailPage.deaktiviert_10f33e | Vertrag und Vorlage | ausgeschaltet | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractDetailPage.quelle_037889 | Vertrag und Vorlage | Quelle | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractDetailPage.contract_a6f5b0 | Vertrag und Vorlage | Vertrag | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractDetailPage.unbekannt_a418e6 | Vertrag und Vorlage | unbekannt | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractsPage.definition_393327 | Vertrag und Vorlage | (Vorlage) | wie bisher | Geprüft; beibehalten. |
| features.contracts.ContractsPage.paket_d2cfa9 | Vertrag und Vorlage | (Paket) | wie bisher | Geprüft; beibehalten. |
| features.diagnostics.ContractDiagnosis.ja_3702fc | Erweitert / Nachweise | Ja | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.nein_4d03db | Erweitert / Nachweise | Nein | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.initial_cc8413 | Erweitert / Nachweise |  (Startzustand) | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.erlaubt_cee957 | Erweitert / Nachweise | erlaubt | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.abgelehnt_e31099 | Erweitert / Nachweise | abgelehnt | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.unentschieden_ad663a | Erweitert / Nachweise | unentschieden | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.strategie_definiert_879b24 | Erweitert / Nachweise | durch das Verfahren bestimmt | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.v0_bea408 | Erweitert / Nachweise | [{v0}] | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.registry.DiffView.nein_4d03db | Entwürfe und Konfigurationen | nein | wie bisher | Geprüft; beibehalten. |
| features.registry.RegistryPage.rollback_c591f5 | Entwürfe und Konfigurationen | Zurücksetzen | wie bisher | Geprüft; beibehalten. |
| features.registry.RegistryPage.aktivierung_90ba1a | Entwürfe und Konfigurationen | Übernahme | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.einrichten_f456a9 | Ersteinrichtung | einrichten | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.nicht_angeboten_4730a6 | Ersteinrichtung | nicht angeboten | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.eingerichtet_68b238 | Ersteinrichtung | eingerichtet | wie bisher | Geprüft; beibehalten. |
| codes.valid | Wert-/Ursachenanzeige, dynamisch | gültig | wie bisher | Geprüft; beibehalten. |
| codes.held | Wert-/Ursachenanzeige, dynamisch | gehalten | wie bisher | Geprüft; beibehalten. |
| codes.unknown | Wert-/Ursachenanzeige, dynamisch | unbekannt | wie bisher | Geprüft; beibehalten. |
| codes.unresolved | Wert-/Ursachenanzeige, dynamisch | ungelöst | wie bisher | Geprüft; beibehalten. |
| codes.not_applicable | Wert-/Ursachenanzeige, dynamisch | nicht anwendbar | wie bisher | Geprüft; beibehalten. |
| codes.healthy | Wert-/Ursachenanzeige, dynamisch | gesund | wie bisher | Geprüft; beibehalten. |
| codes.degraded | Wert-/Ursachenanzeige, dynamisch | eingeschränkt | wie bisher | Geprüft; beibehalten. |
| codes.available | Wert-/Ursachenanzeige, dynamisch | verfügbar | wie bisher | Geprüft; beibehalten. |
| codes.unavailable | Wert-/Ursachenanzeige, dynamisch | nicht verfügbar | wie bisher | Geprüft; beibehalten. |
| codes.absent | Wert-/Ursachenanzeige, dynamisch | fehlt | wie bisher | Geprüft; beibehalten. |
| codes.fresh | Wert-/Ursachenanzeige, dynamisch | aktuell | wie bisher | Geprüft; beibehalten. |
| codes.stale | Wert-/Ursachenanzeige, dynamisch | veraltet | wie bisher | Geprüft; beibehalten. |
| codes.invalid | Wert-/Ursachenanzeige, dynamisch | ungültig | wie bisher | Geprüft; beibehalten. |
| codes.connected | Wert-/Ursachenanzeige, dynamisch | verbunden | wie bisher | Geprüft; beibehalten. |
| codes.disconnected | Wert-/Ursachenanzeige, dynamisch | getrennt | wie bisher | Geprüft; beibehalten. |
| codes.disabled | Wert-/Ursachenanzeige, dynamisch | ausgeschaltet | wie bisher | Geprüft; beibehalten. |
| codes.not_needed | Wert-/Ursachenanzeige, dynamisch | wird nicht gebraucht | wie bisher | Geprüft; beibehalten. |
| codes.connecting | Wert-/Ursachenanzeige, dynamisch | Verbindung wird aufgebaut | wie bisher | Geprüft; beibehalten. |
| codes.open | Wert-/Ursachenanzeige, dynamisch | verbunden | wie bisher | Geprüft; beibehalten. |
| codes.reconnecting | Wert-/Ursachenanzeige, dynamisch | Verbindung wird wiederhergestellt | wie bisher | Geprüft; beibehalten. |
| codes.resyncing | Wert-/Ursachenanzeige, dynamisch | Stand wird abgeglichen | wie bisher | Geprüft; beibehalten. |
| codes.offline | Wert-/Ursachenanzeige, dynamisch | ohne Verbindung | wie bisher | Geprüft; beibehalten. |
| codes.stopped | Wert-/Ursachenanzeige, dynamisch | angehalten | wie bisher | Geprüft; beibehalten. |
| codes.mismatch | Wert-/Ursachenanzeige, dynamisch | Installation stimmt nicht überein | wie bisher | Geprüft; beibehalten. |
| codes.bool | Wert-/Ursachenanzeige, dynamisch | Ja/Nein | wie bisher | Geprüft; beibehalten. |
| codes.boolean | Wert-/Ursachenanzeige, dynamisch | Ja/Nein | wie bisher | Geprüft; beibehalten. |
| codes.number | Wert-/Ursachenanzeige, dynamisch | Zahl | wie bisher | Geprüft; beibehalten. |
| codes.numeric | Wert-/Ursachenanzeige, dynamisch | Zahl | wie bisher | Geprüft; beibehalten. |
| codes.text | Wert-/Ursachenanzeige, dynamisch | Text | wie bisher | Geprüft; beibehalten. |
| codes.string | Wert-/Ursachenanzeige, dynamisch | Text | wie bisher | Geprüft; beibehalten. |
| codes.integer | Wert-/Ursachenanzeige, dynamisch | ganze Zahl | wie bisher | Geprüft; beibehalten. |
| codes.enum | Wert-/Ursachenanzeige, dynamisch | Auswahl | wie bisher | Geprüft; beibehalten. |
| codes.timestamp | Wert-/Ursachenanzeige, dynamisch | Zeitpunkt | wie bisher | Geprüft; beibehalten. |
| codes.array | Wert-/Ursachenanzeige, dynamisch | Liste | wie bisher | Geprüft; beibehalten. |
| codes.null | Wert-/Ursachenanzeige, dynamisch | leer | wie bisher | Geprüft; beibehalten. |
| codes.state | Wert-/Ursachenanzeige, dynamisch | Zustand | wie bisher | Geprüft; beibehalten. |
| codes.attribute | Wert-/Ursachenanzeige, dynamisch | Attribut | wie bisher | Geprüft; beibehalten. |
| codes.event | Wert-/Ursachenanzeige, dynamisch | Ereignis | wie bisher | Geprüft; beibehalten. |
| codes.local | Wert-/Ursachenanzeige, dynamisch | diese Installation | wie bisher | Geprüft; beibehalten. |
| codes.ha | Übersicht | Home Assistant | wie bisher | Geprüft; beibehalten. |
| codes.mqtt | Wert-/Ursachenanzeige, dynamisch | MQTT | wie bisher | Geprüft; beibehalten. |
| codes.other | Wert-/Ursachenanzeige, dynamisch | andere Verbindung | wie bisher | Geprüft; beibehalten. |
| codes.internal | Wert-/Ursachenanzeige, dynamisch | durch die App | wie bisher | Geprüft; beibehalten. |
| codes.source | Wert-/Ursachenanzeige, dynamisch | durch eine Quelle | wie bisher | Geprüft; beibehalten. |
| codes.ha_state | Wert-/Ursachenanzeige, dynamisch | Home-Assistant-Zustand | wie bisher | Geprüft; beibehalten. |
| codes.ha_attribute | Wert-/Ursachenanzeige, dynamisch | Home-Assistant-Attribut | wie bisher | Geprüft; beibehalten. |
| codes.scheduler | Wert-/Ursachenanzeige, dynamisch | Zeitplanung | wie bisher | Geprüft; beibehalten. |
| codes.command | Wert-/Ursachenanzeige, dynamisch | Befehl | wie bisher | Geprüft; beibehalten. |
| codes.report_heartbeat | Wert-/Ursachenanzeige, dynamisch | regelmäßige Meldung | wie bisher | Geprüft; beibehalten. |
| codes.liveness_source | Wert-/Ursachenanzeige, dynamisch | Erreichbarkeitsquelle | wie bisher | Geprüft; beibehalten. |
| codes.periodic_ttl | Wert-/Ursachenanzeige, dynamisch | zeitlich begrenzt | wie bisher | Geprüft; beibehalten. |
| codes.event_stateful | Wert-/Ursachenanzeige, dynamisch | bis zur nächsten Änderung | wie bisher | Geprüft; beibehalten. |
| codes.type_cast | Wert-/Ursachenanzeige, dynamisch | Typumwandlung | wie bisher | Geprüft; beibehalten. |
| codes.unit_scale | Wert-/Ursachenanzeige, dynamisch | Einheit skalieren | wie bisher | Geprüft; beibehalten. |
| codes.map_ref | Wert-/Ursachenanzeige, dynamisch | Wertzuordnung | wie bisher | Geprüft; beibehalten. |
| codes.map | Wert-/Ursachenanzeige, dynamisch | Wertzuordnung | wie bisher | Geprüft; beibehalten. |
| codes.accepted | Wert-/Ursachenanzeige, dynamisch | angenommen | wie bisher | Geprüft; beibehalten. |
| codes.rejected | Wert-/Ursachenanzeige, dynamisch | abgelehnt | wie bisher | Geprüft; beibehalten. |
| codes.expired | Wert-/Ursachenanzeige, dynamisch | abgelaufen | wie bisher | Geprüft; beibehalten. |
| codes.not_supported | Wert-/Ursachenanzeige, dynamisch | nicht unterstützt | wie bisher | Geprüft; beibehalten. |
| codes.command_id_conflict | Wert-/Ursachenanzeige, dynamisch | Befehls-ID bereits anders verwendet | wie bisher | Geprüft; beibehalten. |
| codes.active_revision_conflict | Wert-/Ursachenanzeige, dynamisch | Aktive Version wurde geändert | wie bisher | Geprüft; beibehalten. |
| codes.invalid_value | Wert-/Ursachenanzeige, dynamisch | Wert passt nicht zum vereinbarten Typ | wie bisher | Geprüft; beibehalten. |
| codes.guard_rejected | Wert-/Ursachenanzeige, dynamisch | Bedingung ist nicht erfüllt | wie bisher | Geprüft; beibehalten. |
| codes.guard_unknown | Wert-/Ursachenanzeige, dynamisch | Bedingung kann nicht geprüft werden | wie bisher | Geprüft; beibehalten. |
| codes.state_unknown | Wert-/Ursachenanzeige, dynamisch | Der Ablauf hat keinen gültigen Zustand. Er wartet auf die Neustart-Bedingung und gültige Nachweise. | wie bisher | Geprüft; beibehalten. |
| codes.input_unavailable | Wert-/Ursachenanzeige, dynamisch | Quelle ist nicht verfügbar | wie bisher | Geprüft; beibehalten. |
| codes.input_unknown | Wert-/Ursachenanzeige, dynamisch | Quelle meldet einen unbekannten Wert | wie bisher | Geprüft; beibehalten. |
| codes.input_stale | Wert-/Ursachenanzeige, dynamisch | Nachweis ist veraltet | wie bisher | Geprüft; beibehalten. |
| codes.input_restored | Wert-/Ursachenanzeige, dynamisch | Wiederhergestellter Wert ist noch nicht neu bestätigt | wie bisher | Geprüft; beibehalten. |
| codes.input_absent | Wert-/Ursachenanzeige, dynamisch | Eingang fehlt | wie bisher | Geprüft; beibehalten. |
| codes.unmapped_value | Wert-/Ursachenanzeige, dynamisch | Für diesen Wert fehlt eine Zuordnung | wie bisher | Geprüft; beibehalten. |
| codes.no_match | Wert-/Ursachenanzeige, dynamisch | Keine Regel trifft zu | wie bisher | Geprüft; beibehalten. |
| codes.conflict | Wert-/Ursachenanzeige, dynamisch | Nachweise widersprechen sich | wie bisher | Geprüft; beibehalten. |
| codes.partial_evidence | Wert-/Ursachenanzeige, dynamisch | Nur ein Teil der Nachweise ist verwendbar | wie bisher | Geprüft; beibehalten. |
| codes.source_transition_grace | Wert-/Ursachenanzeige, dynamisch | Letzter gültiger Wert wird innerhalb der Haltefrist verwendet | wie bisher | Geprüft; beibehalten. |
| codes.selection_blocked | Wert-/Ursachenanzeige, dynamisch | Ein unbekannter Eingang verhindert die Auswahl | wie bisher | Geprüft; beibehalten. |
| codes.dependency_unavailable | Wert-/Ursachenanzeige, dynamisch | Benötigte Verbindung oder Quelle ist nicht verfügbar | wie bisher | Geprüft; beibehalten. |
| codes.config_incomplete | Wert-/Ursachenanzeige, dynamisch | Konfiguration ist unvollständig | wie bisher | Geprüft; beibehalten. |
| codes.evaluation_error | Wert-/Ursachenanzeige, dynamisch | Berechnung konnte nicht abgeschlossen werden | wie bisher | Geprüft; beibehalten. |
| codes.restore_context_missing | Wert-/Ursachenanzeige, dynamisch | Gespeicherter Ablaufzustand fehlt. Gültige Nachweise für die Neustart-Bedingung werden benötigt. | wie bisher | Geprüft; beibehalten. |
| codes.restore_context_incompatible | Wert-/Ursachenanzeige, dynamisch | Die Bedeutung wurde geändert. Der Ablauf wartet auf gültige Nachweise für seine Neustart-Bedingung. | wie bisher | Geprüft; beibehalten. |
| codes.restore_context_stale | Wert-/Ursachenanzeige, dynamisch | Gespeicherter Zustand ist veraltet und muss neu belegt werden | wie bisher | Geprüft; beibehalten. |
| codes.history_gap | Wert-/Ursachenanzeige, dynamisch | Für diesen Zeitraum fehlen Nachweise | wie bisher | Geprüft; beibehalten. |
| codes.deadline_overdue_unprocessed | Wert-/Ursachenanzeige, dynamisch | Fällige Frist kann noch nicht mit gültigen Nachweisen verarbeitet werden | wie bisher | Geprüft; beibehalten. |
| codes.automatic | Wert-/Ursachenanzeige, dynamisch | automatisch | wie bisher | Geprüft; beibehalten. |
| codes.manual | Wert-/Ursachenanzeige, dynamisch | manuell | wie bisher | Geprüft; beibehalten. |
| codes.restore | Wert-/Ursachenanzeige, dynamisch | wiederhergestellt | wie bisher | Geprüft; beibehalten. |
| codes.input | Wert-/Ursachenanzeige, dynamisch | Eingang | wie bisher | Geprüft; beibehalten. |
| codes.first_start | Wert-/Ursachenanzeige, dynamisch | Erststart | wie bisher | Geprüft; beibehalten. |
| codes.initial | Wert-/Ursachenanzeige, dynamisch | Startzustand | wie bisher | Geprüft; beibehalten. |
| codes.reinitialize_when | Wert-/Ursachenanzeige, dynamisch | Neustart-Bedingung erfüllt | wie bisher | Geprüft; beibehalten. |
| codes.deadline | Wert-/Ursachenanzeige, dynamisch | Frist abgelaufen | wie bisher | Geprüft; beibehalten. |
| codes.process_restart | Wert-/Ursachenanzeige, dynamisch | App wurde neu gestartet | wie bisher | Geprüft; beibehalten. |
| codes.database_rollback | Wert-/Ursachenanzeige, dynamisch | Datenbankstand wurde zurückgesetzt | wie bisher | Geprüft; beibehalten. |
| codes.db_outage | Wert-/Ursachenanzeige, dynamisch | Datenbank war nicht verfügbar | wie bisher | Geprüft; beibehalten. |
| codes.ha_disconnect | Wert-/Ursachenanzeige, dynamisch | Home-Assistant-Verbindung wurde unterbrochen | wie bisher | Geprüft; beibehalten. |
| codes.mqtt_disconnect | Wert-/Ursachenanzeige, dynamisch | MQTT-Verbindung wurde unterbrochen | wie bisher | Geprüft; beibehalten. |
| codes.source_change | Wert-/Ursachenanzeige, dynamisch | Quelle geändert | wie bisher | Geprüft; beibehalten. |
| codes.snapshot | Wert-/Ursachenanzeige, dynamisch | vollständiger aktueller Stand | wie bisher | Geprüft; beibehalten. |
| codes.live_change | Wert-/Ursachenanzeige, dynamisch | neue Änderung | wie bisher | Geprüft; beibehalten. |
| codes.report | Wert-/Ursachenanzeige, dynamisch | neue Meldung | wie bisher | Geprüft; beibehalten. |
| codes.administrative | Wert-/Ursachenanzeige, dynamisch | Verwaltung | wie bisher | Geprüft; beibehalten. |
| codes.draft_create | Wert-/Ursachenanzeige, dynamisch | Entwurf angelegt | wie bisher | Geprüft; beibehalten. |
| codes.draft_update | Wert-/Ursachenanzeige, dynamisch | Entwurf gespeichert | wie bisher | Geprüft; beibehalten. |
| codes.draft_delete | Wert-/Ursachenanzeige, dynamisch | Entwurf entfernt | wie bisher | Geprüft; beibehalten. |
| codes.activate | Wert-/Ursachenanzeige, dynamisch | Konfiguration übernommen | wie bisher | Geprüft; beibehalten. |
| codes.rollback | Wert-/Ursachenanzeige, dynamisch | Konfiguration zurückgesetzt | wie bisher | Geprüft; beibehalten. |
| codes.registry_activated | Wert-/Ursachenanzeige, dynamisch | Konfiguration übernommen | wie bisher | Geprüft; beibehalten. |
| codes.registry_rollback | Wert-/Ursachenanzeige, dynamisch | Konfiguration zurückgesetzt | wie bisher | Geprüft; beibehalten. |
| codes.token_rotate | Wert-/Ursachenanzeige, dynamisch | Zugangsschlüssel erneuert | wie bisher | Geprüft; beibehalten. |
| codes.token_rotation_intent | Wert-/Ursachenanzeige, dynamisch | Erneuerung eines Zugangsschlüssels angefordert | wie bisher | Geprüft; beibehalten. |
| codes.token_rotation_complete | Wert-/Ursachenanzeige, dynamisch | Zugangsschlüssel erneuert | wie bisher | Geprüft; beibehalten. |
| codes.token_rotation_ack | Wert-/Ursachenanzeige, dynamisch | Erneuerung eines Zugangsschlüssels bestätigt | wie bisher | Geprüft; beibehalten. |
| codes.complete | Wert-/Ursachenanzeige, dynamisch | abgeschlossen | wie bisher | Geprüft; beibehalten. |
| codes.completion_unconfirmed | Wert-/Ursachenanzeige, dynamisch | Abschluss noch nicht bestätigt | wie bisher | Geprüft; beibehalten. |
| codes.rotated | Wert-/Ursachenanzeige, dynamisch | erneuert | wie bisher | Geprüft; beibehalten. |
| codes.intent | Wert-/Ursachenanzeige, dynamisch | angefordert | wie bisher | Geprüft; beibehalten. |
| codes.admin | Wert-/Ursachenanzeige, dynamisch | Administrator | wie bisher | Geprüft; beibehalten. |
| codes.consumer | Wert-/Ursachenanzeige, dynamisch | lesender Zugriff | wie bisher | Geprüft; beibehalten. |
| codes.ingress | Wert-/Ursachenanzeige, dynamisch | Home-Assistant-Zugriff | wie bisher | Geprüft; beibehalten. |
| codes.token | Wert-/Ursachenanzeige, dynamisch | Zugangsschlüssel | wie bisher | Geprüft; beibehalten. |
| codes.system | Wert-/Ursachenanzeige, dynamisch | App | wie bisher | Geprüft; beibehalten. |
| codes.first_healthy | Wert-/Ursachenanzeige, dynamisch | erster verwendbarer Wert | wie bisher | Geprüft; beibehalten. |
| codes.latest | Wert-/Ursachenanzeige, dynamisch | zuletzt gemessener Wert | wie bisher | Geprüft; beibehalten. |
| codes.any_true | Wert-/Ursachenanzeige, dynamisch | mindestens ein Ja | wie bisher | Geprüft; beibehalten. |
| codes.all_true | Wert-/Ursachenanzeige, dynamisch | alle Ja | wie bisher | Geprüft; beibehalten. |
| codes.first_match | Wert-/Ursachenanzeige, dynamisch | erster Treffer | wie bisher | Geprüft; beibehalten. |
| codes.stable_for | Wert-/Ursachenanzeige, dynamisch | Lange genug Ja | wie bisher | Geprüft; beibehalten. |
| codes.dwell | Wert-/Ursachenanzeige, dynamisch | Wartezeit bei Ja | wie bisher | Geprüft; beibehalten. |
| codes.grace | Wert-/Ursachenanzeige, dynamisch | Haltefrist | wie bisher | Geprüft; beibehalten. |
| codes.edge | Wert-/Ursachenanzeige, dynamisch | Wechsel erkannt | wie bisher | Geprüft; beibehalten. |
| codes.delta | Wert-/Ursachenanzeige, dynamisch | Differenz | wie bisher | Geprüft; beibehalten. |
| codes.age | Wert-/Ursachenanzeige, dynamisch | Alter der Messung | wie bisher | Geprüft; beibehalten. |
| codes.priority | Wert-/Ursachenanzeige, dynamisch | Reihenfolge | wie bisher | Geprüft; beibehalten. |
| codes.latest_measurement | Wert-/Ursachenanzeige, dynamisch | Messzeit | wie bisher | Geprüft; beibehalten. |
| codes.independent | Wert-/Ursachenanzeige, dynamisch | unabhängig | wie bisher | Geprüft; beibehalten. |
| codes.package | Wert-/Ursachenanzeige, dynamisch | eingebaute Vorlage | wie bisher | Geprüft; beibehalten. |
| codes.active-definition | Wert-/Ursachenanzeige, dynamisch | übernommene Vorlage | wie bisher | Geprüft; beibehalten. |
| codes.draft-definition | Wert-/Ursachenanzeige, dynamisch | Vorlage im Entwurf | wie bisher | Geprüft; beibehalten. |
| codes.state_machine | Wert-/Ursachenanzeige, dynamisch | Ablauf | wie bisher | Geprüft; beibehalten. |
| codes.resolver | Wert-/Ursachenanzeige, dynamisch | Berechnung | wie bisher | Geprüft; beibehalten. |
| codes.fusion | Wert-/Ursachenanzeige, dynamisch | Zusammenführung | wie bisher | Geprüft; beibehalten. |
| codes.temporal | Wert-/Ursachenanzeige, dynamisch | Zeitregel | wie bisher | Geprüft; beibehalten. |
| codes.reference | Wert-/Ursachenanzeige, dynamisch | Verweis | wie bisher | Geprüft; beibehalten. |
| codes.literal | Wert-/Ursachenanzeige, dynamisch | Konstante | wie bisher | Geprüft; beibehalten. |
| codes.and | Wert-/Ursachenanzeige, dynamisch | UND | wie bisher | Geprüft; beibehalten. |
| codes.or | Wert-/Ursachenanzeige, dynamisch | ODER | wie bisher | Geprüft; beibehalten. |
| codes.not | Wert-/Ursachenanzeige, dynamisch | NICHT | wie bisher | Geprüft; beibehalten. |
| codes.compare | Wert-/Ursachenanzeige, dynamisch | Vergleich | wie bisher | Geprüft; beibehalten. |
| codes.formula | Wert-/Ursachenanzeige, dynamisch | Formel | wie bisher | Geprüft; beibehalten. |
| codes.true | Wert-/Ursachenanzeige, dynamisch | Ja | wie bisher | Geprüft; beibehalten. |
| codes.false | Wert-/Ursachenanzeige, dynamisch | Nein | wie bisher | Geprüft; beibehalten. |
| codes.on | Wert-/Ursachenanzeige, dynamisch | Ein | wie bisher | Geprüft; beibehalten. |
| codes.off | Wert-/Ursachenanzeige, dynamisch | Aus | wie bisher | Geprüft; beibehalten. |
| codes.required | Wert-/Ursachenanzeige, dynamisch | Pflicht | wie bisher | Geprüft; beibehalten. |
| codes.optional | Wert-/Ursachenanzeige, dynamisch | freiwillig | wie bisher | Geprüft; beibehalten. |
| codes.internal_cycle | Wert-/Ursachenanzeige, dynamisch | Regeln verweisen im Kreis | wie bisher | Geprüft; beibehalten. |
| codes.protected | Wert-/Ursachenanzeige, dynamisch | geschützt | wie bisher | Geprüft; beibehalten. |
| codes.rejected_reason | Wert-/Ursachenanzeige, dynamisch | Ablehnungsgrund | wie bisher | Geprüft; beibehalten. |
| codes.none | Wert-/Ursachenanzeige, dynamisch | keine | wie bisher | Geprüft; beibehalten. |
| codes.public | Wert-/Ursachenanzeige, dynamisch | öffentlich | wie bisher | Geprüft; beibehalten. |
| codes.server_utc | Wert-/Ursachenanzeige, dynamisch | Zeitpunkt der App | wie bisher | Geprüft; beibehalten. |
| codes.time_desc_key_desc | Wert-/Ursachenanzeige, dynamisch | neueste zuerst | wie bisher | Geprüft; beibehalten. |
| codes.automatic_init | Wert-/Ursachenanzeige, dynamisch | automatischer Erststart | wie bisher | Geprüft; beibehalten. |
| codes.incomplete | Wert-/Ursachenanzeige, dynamisch | unvollständig | wie bisher | Geprüft; beibehalten. |
| fields.contract_id | Dynamische Formularbeschriftung | Vertrags-ID | wie bisher | Geprüft; beibehalten. |
| fields.source_id | Dynamische Formularbeschriftung | Quellen-ID | wie bisher | Geprüft; beibehalten. |
| fields.binding_id | Dynamische Formularbeschriftung | Verknüpfungs-ID | wie bisher | Geprüft; beibehalten. |
| fields.dependency_id | Dynamische Formularbeschriftung | Verbindungs-ID | wie bisher | Geprüft; beibehalten. |
| fields.type_id | Dynamische Formularbeschriftung | Vorlagen-ID | wie bisher | Geprüft; beibehalten. |
| fields.type_version | Dynamische Formularbeschriftung | Vorlagen-Version | wie bisher | Geprüft; beibehalten. |
| fields.display_name | Dynamische Formularbeschriftung | Anzeigename | wie bisher | Geprüft; beibehalten. |
| fields.description | Dynamische Formularbeschriftung | Beschreibung | wie bisher | Geprüft; beibehalten. |
| fields.value | Entwurf und Bearbeitung; Vertrag und Vorlage | Wert | wie bisher | Geprüft; beibehalten. |
| fields.status | Dynamische Formularbeschriftung | Zustand | wie bisher | Geprüft; beibehalten. |
| fields.quality | Dynamische Formularbeschriftung | Qualität | wie bisher | Geprüft; beibehalten. |
| fields.reasons | Dynamische Formularbeschriftung | Gründe | wie bisher | Geprüft; beibehalten. |
| fields.evidence | Dynamische Formularbeschriftung | Nachweise | wie bisher | Geprüft; beibehalten. |
| fields.freshness | Dynamische Formularbeschriftung | Aktualität | wie bisher | Geprüft; beibehalten. |
| fields.mode | Dynamische Formularbeschriftung | Modus | wie bisher | Geprüft; beibehalten. |
| fields.unit | Dynamische Formularbeschriftung | Einheit | wie bisher | Geprüft; beibehalten. |
| fields.value_catalog | Dynamische Formularbeschriftung | Werteliste | wie bisher | Geprüft; beibehalten. |
| fields.source_type | Dynamische Formularbeschriftung | Quellenart | wie bisher | Geprüft; beibehalten. |
| fields.source_origin | Dynamische Formularbeschriftung | Herkunft der Quelle | wie bisher | Geprüft; beibehalten. |
| fields.physical_source_key | Dynamische Formularbeschriftung | Schlüssel der Messung | wie bisher | Geprüft; beibehalten. |
| fields.interval_s | Dynamische Formularbeschriftung | Abstand der Aufbewahrungsschritte in Sekunden | wie bisher | Geprüft; beibehalten. |
| fields.future_tolerance_s | Dynamische Formularbeschriftung | Zukunftstoleranz in Sekunden | wie bisher | Geprüft; beibehalten. |
| fields.liveness_source | Dynamische Formularbeschriftung | Erreichbarkeitsquelle | wie bisher | Geprüft; beibehalten. |
| fields.enabled | Dynamische Formularbeschriftung | eingeschaltet | wie bisher | Geprüft; beibehalten. |
| fields.inputs | Dynamische Formularbeschriftung | Eingänge | wie bisher | Geprüft; beibehalten. |
| fields.fields | Dynamische Formularbeschriftung | Felder | wie bisher | Geprüft; beibehalten. |
| fields.output | Dynamische Formularbeschriftung | Ausgabe | wie bisher | Geprüft; beibehalten. |
| fields.outputs | Dynamische Formularbeschriftung | Ausgaben | wie bisher | Geprüft; beibehalten. |
| fields.rules | Dynamische Formularbeschriftung | Regeln | wie bisher | Geprüft; beibehalten. |
| fields.machine | Dynamische Formularbeschriftung | Ablauf | wie bisher | Geprüft; beibehalten. |
| fields.required | Dynamische Formularbeschriftung | Pflichtwert | wie bisher | Geprüft; beibehalten. |
| fields.physical_state | Dynamische Formularbeschriftung | physischer Zustand | wie bisher | Geprüft; beibehalten. |
| fields.grace_capable | Dynamische Formularbeschriftung | Haltefrist erlaubt | wie bisher | Geprüft; beibehalten. |
| fields.grace_parameter | Dynamische Formularbeschriftung | Parameter der Haltefrist | wie bisher | Geprüft; beibehalten. |
| fields.available_projection | Dynamische Formularbeschriftung | Verfügbarkeitsfelder | wie bisher | Geprüft; beibehalten. |
| fields.adapter | Dynamische Formularbeschriftung | Anbindung | wie bisher | Geprüft; beibehalten. |
| fields.kind | Dynamische Formularbeschriftung | Art | wie bisher | Geprüft; beibehalten. |
| fields.target | Dynamische Formularbeschriftung | Ziel | wie bisher | Geprüft; beibehalten. |
| fields.source | Dynamische Formularbeschriftung | Quelle | wie bisher | Geprüft; beibehalten. |
| fields.ref | Dynamische Formularbeschriftung | Verweis | wie bisher | Geprüft; beibehalten. |
| fields.name | Dynamische Formularbeschriftung | Name | wie bisher | Geprüft; beibehalten. |
| fields.id | Dynamische Formularbeschriftung | ID | wie bisher | Geprüft; beibehalten. |
| fields.initial | Dynamische Formularbeschriftung | Startzustand | wie bisher | Geprüft; beibehalten. |
| fields.state | Dynamische Formularbeschriftung | Zustand | wie bisher | Geprüft; beibehalten. |
| fields.states | Dynamische Formularbeschriftung | Zustände | wie bisher | Geprüft; beibehalten. |
| fields.commands | Dynamische Formularbeschriftung | Befehle | wie bisher | Geprüft; beibehalten. |
| fields.arguments | Dynamische Formularbeschriftung | Argumente | wie bisher | Geprüft; beibehalten. |
| fields.argument_equals | Dynamische Formularbeschriftung | Bedingung für Argumente | wie bisher | Geprüft; beibehalten. |
| fields.guard | Dynamische Formularbeschriftung | Bedingung | wie bisher | Geprüft; beibehalten. |
| fields.transitions | Dynamische Formularbeschriftung | Übergänge | wie bisher | Geprüft; beibehalten. |
| fields.event | Dynamische Formularbeschriftung | Ereignis | wie bisher | Geprüft; beibehalten. |
| fields.reason | Dynamische Formularbeschriftung | Grund | wie bisher | Geprüft; beibehalten. |
| fields.trigger | Dynamische Formularbeschriftung | Auslöser | wie bisher | Geprüft; beibehalten. |
| fields.origin | Dynamische Formularbeschriftung | Herkunft | wie bisher | Geprüft; beibehalten. |
| fields.sessions | Dynamische Formularbeschriftung | Sitzungen | wie bisher | Geprüft; beibehalten. |
| fields.deadline_s | Dynamische Formularbeschriftung | Frist in Sekunden | wie bisher | Geprüft; beibehalten. |
| fields.reinitialize_when | Dynamische Formularbeschriftung | Neustart-Bedingung | wie bisher | Geprüft; beibehalten. |
| fields.new_episode | Dynamische Formularbeschriftung | neue Episode | wie bisher | Geprüft; beibehalten. |
| fields.ends_episode | Dynamische Formularbeschriftung | Episode beenden | wie bisher | Geprüft; beibehalten. |
| fields.args | Dynamische Formularbeschriftung | Argumente | wie bisher | Geprüft; beibehalten. |
| fields.arg | Dynamische Formularbeschriftung | Argument | wie bisher | Geprüft; beibehalten. |
| fields.op | Dynamische Formularbeschriftung | Berechnung | wie bisher | Geprüft; beibehalten. |
| fields.factor | Dynamische Formularbeschriftung | Faktor | wie bisher | Geprüft; beibehalten. |
| fields.offset | Dynamische Formularbeschriftung | Verschiebung | wie bisher | Geprüft; beibehalten. |
| fields.operation | Dynamische Formularbeschriftung | Aktion | wie bisher | Geprüft; beibehalten. |
| fields.duration_s | Dynamische Formularbeschriftung | Dauer in Sekunden | wie bisher | Geprüft; beibehalten. |
| fields.accepts_held | Dynamische Formularbeschriftung | gehaltene Werte zulassen | wie bisher | Geprüft; beibehalten. |
| fields.version | Dynamische Formularbeschriftung | Version | wie bisher | Geprüft; beibehalten. |
| fields.entries | Dynamische Formularbeschriftung | Zuordnungen | wie bisher | Geprüft; beibehalten. |
| fields.strategy | Dynamische Formularbeschriftung | Verfahren | wie bisher | Geprüft; beibehalten. |
| fields.comparison | Dynamische Formularbeschriftung | Vergleich | wie bisher | Geprüft; beibehalten. |
| fields.left | Dynamische Formularbeschriftung | linke Seite | wie bisher | Geprüft; beibehalten. |
| fields.right | Dynamische Formularbeschriftung | rechte Seite | wie bisher | Geprüft; beibehalten. |
| fields.lower | Dynamische Formularbeschriftung | untere Grenze | wie bisher | Geprüft; beibehalten. |
| fields.upper | Dynamische Formularbeschriftung | obere Grenze | wie bisher | Geprüft; beibehalten. |
| fields.received_at | Dynamische Formularbeschriftung | Empfangen | wie bisher | Geprüft; beibehalten. |
| fields.measured_at | Dynamische Formularbeschriftung | Gemessen | wie bisher | Geprüft; beibehalten. |
| fields.since_at | Dynamische Formularbeschriftung | Seit | wie bisher | Geprüft; beibehalten. |
| fields.computed_at | Dynamische Formularbeschriftung | Berechnet | wie bisher | Geprüft; beibehalten. |
| fields.at | Dynamische Formularbeschriftung | Zeitpunkt | wie bisher | Geprüft; beibehalten. |
| fields.created_at | Dynamische Formularbeschriftung | Angelegt | wie bisher | Geprüft; beibehalten. |
| fields.updated_at | Dynamische Formularbeschriftung | Gespeichert | wie bisher | Geprüft; beibehalten. |
| fields.registry_revision | Dynamische Formularbeschriftung | Konfigurationsversion | wie bisher | Geprüft; beibehalten. |
| fields.epoch_id | Dynamische Formularbeschriftung → Erweitert | Laufzeitabschnitt | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| fields.session_id | Dynamische Formularbeschriftung | Sitzung | wie bisher | Geprüft; beibehalten. |
| fields.contract_health | Dynamische Formularbeschriftung | Vertragsqualität | wie bisher | Geprüft; beibehalten. |
| fields.observation_kind | Dynamische Formularbeschriftung | Art des Nachweises | wie bisher | Geprüft; beibehalten. |
| fields.previous_state | Dynamische Formularbeschriftung | Vorheriger Zustand | wie bisher | Geprüft; beibehalten. |
| fields.transition_reason | Dynamische Formularbeschriftung | Übergangsgrund | wie bisher | Geprüft; beibehalten. |
| fields.evidence_refs | Dynamische Formularbeschriftung | Nachweise | wie bisher | Geprüft; beibehalten. |
| fields.deadline | Dynamische Formularbeschriftung | Frist | wie bisher | Geprüft; beibehalten. |
| fields.confirm | Dynamische Formularbeschriftung | Bestätigung | wie bisher | Geprüft; beibehalten. |
| fields.deadline_seconds | Dynamische Formularbeschriftung | Frist in Sekunden | wie bisher | Geprüft; beibehalten. |
| fields.expected_registry_revision | Dynamische Formularbeschriftung | Erwartete Konfigurationsversion | wie bisher | Geprüft; beibehalten. |
| fields.issued_at | Dynamische Formularbeschriftung | Angefordert | wie bisher | Geprüft; beibehalten. |
| fields.valid_until | Dynamische Formularbeschriftung | Gültig bis | wie bisher | Geprüft; beibehalten. |
| fields.actor | Dynamische Formularbeschriftung | Ausgelöst von | wie bisher | Geprüft; beibehalten. |
| fields.client_name | Dynamische Formularbeschriftung | Anwendung | wie bisher | Geprüft; beibehalten. |
| fields.command_id | Dynamische Formularbeschriftung | Befehls-ID | wie bisher | Geprüft; beibehalten. |
| fields.config_schema_version | Dynamische Formularbeschriftung | Konfigurationsschema | wie bisher | Geprüft; beibehalten. |
| fields.checksum | Dynamische Formularbeschriftung | Prüfsumme | wie bisher | Geprüft; beibehalten. |
| fields.monitor | Dynamische Formularbeschriftung | Überwachung | wie bisher | Geprüft; beibehalten. |
| fields.ha_entity_id | Dynamische Formularbeschriftung | Home-Assistant-Gerät | wie bisher | Geprüft; beibehalten. |
| fields.ha_attribute | Dynamische Formularbeschriftung | Home-Assistant-Attribut | wie bisher | Geprüft; beibehalten. |
| fields.ha_time_attribute | Dynamische Formularbeschriftung | Attribut für die Messzeit | wie bisher | Geprüft; beibehalten. |
| fields.mqtt_topic | Dynamische Formularbeschriftung | MQTT-Kanal | wie bisher | Geprüft; beibehalten. |
| fields.mqtt_value_path | Dynamische Formularbeschriftung | MQTT-Wertpfad | wie bisher | Geprüft; beibehalten. |
| fields.mqtt_time_path | Dynamische Formularbeschriftung | MQTT-Zeitpfad | wie bisher | Geprüft; beibehalten. |
| fields.transform | Dynamische Formularbeschriftung | Umwandlung | wie bisher | Geprüft; beibehalten. |
| fields.config | Dynamische Formularbeschriftung | Konfiguration | wie bisher | Geprüft; beibehalten. |
| common.unknownCode | Gemeinsame Oberfläche / Wertanzeige | unbekannt | wie bisher | Geprüft; beibehalten. |
| common.requestFailed | Gemeinsame Oberfläche / Wertanzeige | Die Anfrage konnte nicht abgeschlossen werden. Prüfe die Verbindung und die betroffenen Felder. | wie bisher | Geprüft; beibehalten. |
| common.invalidJson | Formular für Vorlage / Quelle / Vertrag; Entwurf und Bearbeitung | Der JSON-Text ist ungültig. Prüfe Klammern, Anführungszeichen und Kommas. | wie bisher | Geprüft; beibehalten. |
| validation.unknown | Gemeinsame Oberfläche / Wertanzeige | Dieses Feld ist ungültig. Prüfe die Eingabe und ihre Verweise. | wie bisher | Geprüft; beibehalten. |
| validation.schema.missing | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Dieses Pflichtfeld fehlt. | wie bisher | Geprüft; beibehalten. |
| validation.schema.string_pattern_mismatch | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Die ID enthält unzulässige Zeichen oder hat nicht den erforderlichen Namensraum. | wie bisher | Geprüft; beibehalten. |
| validation.schema.string_too_long | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Der Text ist zu lang. | wie bisher | Geprüft; beibehalten. |
| validation.schema.literal_error | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Wähle einen der erlaubten Werte. | wie bisher | Geprüft; beibehalten. |
| validation.schema.extra_forbidden | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Dieses Feld ist hier nicht erlaubt. | wie bisher | Geprüft; beibehalten. |
| validation.identity_invalid | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Eine ID hat höchstens 128 Zeichen, beginnt mit A–Z oder a–z und enthält nur diese Buchstaben, Ziffern, Punkt, Unterstrich und Bindestrich; kein Punkt am Ende. | wie bisher | Geprüft; beibehalten. |
| validation.immutable_source_type | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Diese Quelle wurde bereits übernommen. Typ und Einheit sind gesperrt; für einen Typwechsel ist eine neue Quelle nötig. | wie bisher | Geprüft; beibehalten. |
| validation.immutable_source_catalog | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Diese Quelle wurde bereits übernommen. Ihre Werteliste darf nur ergänzt werden; bestehende Werte bleiben erhalten. | wie bisher | Geprüft; beibehalten. |
| validation.binding_cast_required | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Quelle {source} liefert Home-Assistant-Text. Ergänze die zum Quellentyp passende Umwandlung. | wie bisher | Geprüft; beibehalten. |
| validation.binding_type_mismatch | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Quelle {source} erwartet {expected}; die Umwandlung liefert {actual}. Wähle eine passende Umwandlung. | wie bisher | Geprüft; beibehalten. |
| validation.source_type_mismatch | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Quellenart und Wertschema haben verschiedene Typen. | wie bisher | Geprüft; beibehalten. |
| validation.input_type_mismatch | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Quelle {source} liefert {actual} ({actualUnit}); Eingang {input} erwartet {expected} ({expectedUnit}). | wie bisher | Geprüft; beibehalten. |
| validation.contract_cycle | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Verträge verweisen im Kreis aufeinander: {cycle} | wie bisher | Geprüft; beibehalten. |
| validation.machine_never_recovers | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Dieser Ablauf kann sich nach einer Änderung nie selbst erholen. | wie bisher | Geprüft; beibehalten. |
| common.noUnit | Gemeinsame Oberfläche / Wertanzeige | keine Einheit | wie bisher | Geprüft; beibehalten. |
| components.PanelLayout.v0_position_v1_von_v2_528978 | Anordnung der Seitenbereiche | {v0}: Position {v1} von {v2}. | wie bisher | Geprüft; beibehalten. |
| editors.SchemaForm.variante_v0_78b949 | Formular für Vorlage / Quelle / Vertrag | Variante {v0} | wie bisher | Geprüft; beibehalten. |
| features.diagnostics.ExplainPanel.eingang_d8af5e | Erweitert / Nachweise | Eingang | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.konstante_2e2736 | Erweitert / Nachweise | Konstante | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.und_fd2908 | Erweitert / Nachweise | UND | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.oder_43e406 | Erweitert / Nachweise | ODER | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.nicht_774d65 | Erweitert / Nachweise | NICHT | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.vergleich_79a63c | Erweitert / Nachweise | Vergleich | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.zuordnung_750995 | Erweitert / Nachweise | Zuordnung | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.formel_244289 | Erweitert / Nachweise | Formel | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.fusion_09d751 | Erweitert / Nachweise | Zusammenführung | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.fusion_auswahl_3a43a6 | Erweitert / Nachweise | Zusammenführung – Auswahl | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.temporal_840fec | Erweitert / Nachweise | Zeitregel | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ExplainPanel.guard_c8d3fc | Erweitert / Nachweise | Bedingung | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| common.validationError | Formular für Vorlage / Quelle / Vertrag; Entwürfe und Konfigurationen | Prüffehler | wie bisher | Geprüft; beibehalten. |
| system.haConnection | Gemeinsame Oberfläche / Wertanzeige | Home Assistant: {state} | wie bisher | Geprüft; beibehalten. |
| system.bridgeConnection | Gemeinsame Oberfläche / Wertanzeige | HA-Anbindung: {state} | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.api_v0_bridge_v1_schema_v2_feaecd | Einstellungen | API {v0} · HA-Anbindung {v1} · Schema {v2} | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.keine_db028e | Einstellungen | keine | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.verfugbar_e5a644 | Einstellungen | verfügbar | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.nicht_erreichbar_b129fa | Einstellungen | nicht erreichbar | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.bestatigt_26bfc3 | Einstellungen | bestätigt | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.unbestatigt_40dee0 | Einstellungen | unbestätigt | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.v0_s_30054e | Einstellungen | {v0} s | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.wird_gepruft_3242b4 | Einstellungen | wird geprüft … | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.nicht_lesbar_0bfbf9 | Einstellungen | nicht lesbar | wie bisher | Geprüft; beibehalten. |
| features.admin.AdminPage.v0_460783 | Einstellungen | {v0}× | wie bisher | Geprüft; beibehalten. |
| features.diagnostics.ContractDiagnosis.keine_db028e | Erweitert / Nachweise | keine | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.v0_s_30054e | Erweitert / Nachweise | {v0} s | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.v0_v1_585a47 | Erweitert / Nachweise | {v0} / {v1} | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.ContractDiagnosis.v0_seit_v1_v2_8d5ea5 | Erweitert / Nachweise | {v0} (seit {v1}){v2} | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.DiagnosticsPage.ja_3702fc | Erweitert / Nachweise | ja | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.diagnostics.DiagnosticsPage.v0_460783 | Erweitert / Nachweise | {v0}× | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.graph.GraphPage.deaktiviert_10f33e | Zusammenhänge | ausgeschaltet | wie bisher | Geprüft; beibehalten. |
| features.graph.GraphPage.aktiviert_acb27b | Zusammenhänge | eingeschaltet | wie bisher | Geprüft; beibehalten. |
| lib.status.ja_cde9e5 | Gemeinsame Oberfläche / Wertanzeige; Vertrag und Vorlage; Erweitert / Nachweise | Ja | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| lib.status.nein_90ebc1 | Gemeinsame Oberfläche / Wertanzeige; Vertrag und Vorlage; Erweitert / Nachweise | Nein | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| product.name | Gemeinsame Oberfläche / Wertanzeige | Mimir | wie bisher | Geprüft; beibehalten. |
| codes.token_rotation_requested | Wert-/Ursachenanzeige, dynamisch | Erneuerung eines Zugangsschlüssels angefordert | wie bisher | Geprüft; beibehalten. |
| codes.token_rotated | Wert-/Ursachenanzeige, dynamisch | Zugangsschlüssel erneuert | wie bisher | Geprüft; beibehalten. |
| duration.seconds | Gemeinsame Oberfläche / Wertanzeige | {value} s | wie bisher | Geprüft; beibehalten. |
| duration.minutes | Gemeinsame Oberfläche / Wertanzeige | {value} min | wie bisher | Geprüft; beibehalten. |
| duration.hours | Gemeinsame Oberfläche / Wertanzeige | {value} h | wie bisher | Geprüft; beibehalten. |
| duration.days | Gemeinsame Oberfläche / Wertanzeige | {value} Tage | wie bisher | Geprüft; beibehalten. |
| features.diagnostics.ContractDiagnosis.beendet_v0_58bce5 | Erweitert / Nachweise |  · beendet {v0} | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| features.sources.SourcesPage.neu_391955 | Quellen und Verknüpfungen | (neu) | wie bisher | Geprüft; beibehalten. |
| draft.copyName | Entwurf und Bearbeitung | {name} (Kopie) | wie bisher | Geprüft; beibehalten. |
| editors.RegistryObjects.leer_ac5c66 | Formular für Vorlage / Quelle / Vertrag | (leer) | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.v0_37b56e | Formular für Vorlage / Quelle / Vertrag |  ({v0}) | wie bisher | Geprüft; beibehalten. |
| editors.RuleEditor.v0_8b43bb | Formular für Vorlage / Quelle / Vertrag |  · {v0} | wie bisher | Geprüft; beibehalten. |
| editors.ValueEditor.leer_ac5c66 | Formular für Vorlage / Quelle / Vertrag | (leer) | wie bisher | Geprüft; beibehalten. |
| features.authoring.locate.v0_cdb96d | Entwurf und Bearbeitung | #{v0} | wie bisher | Geprüft; beibehalten. |
| features.registry.DraftPage.veraltet_14c672 | Entwürfe und Konfigurationen |  (veraltet) | wie bisher | Geprüft; beibehalten. |
| setup.SetupWizard.angeboten_b7e201 | Ersteinrichtung | angeboten | wie bisher | Geprüft; beibehalten. |
| fields.value_raw | Dynamische Formularbeschriftung | Ursprünglicher Wert | wie bisher | Geprüft; beibehalten. |
| fields.value_normalized | Dynamische Formularbeschriftung | Umgewandelter Wert | wie bisher | Geprüft; beibehalten. |
| fields.normalized | Dynamische Formularbeschriftung | Wert umgewandelt | wie bisher | Geprüft; beibehalten. |
| fields.device_time | Dynamische Formularbeschriftung | Messzeit vom Gerät | wie bisher | Geprüft; beibehalten. |
| fields.ha_last_changed | Dynamische Formularbeschriftung | Home Assistant: Zustand geändert | wie bisher | Geprüft; beibehalten. |
| fields.ha_last_updated | Dynamische Formularbeschriftung | Home Assistant: Eintrag aktualisiert | wie bisher | Geprüft; beibehalten. |
| fields.ha_last_reported | Dynamische Formularbeschriftung | Home Assistant: Zustand gemeldet | wie bisher | Geprüft; beibehalten. |
| fields.ha_time_fired | Dynamische Formularbeschriftung | Home Assistant: Ereigniszeit | wie bisher | Geprüft; beibehalten. |
| fields.ha_context_id | Dynamische Formularbeschriftung → Erweitert | Home Assistant: Zusammenhangskennung | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| fields.ha_restored | Dynamische Formularbeschriftung | Home Assistant: wiederhergestellter Wert | wie bisher | Geprüft; beibehalten. |
| fields.mqtt_retained | Dynamische Formularbeschriftung | Gespeicherte MQTT-Meldung | wie bisher | Geprüft; beibehalten. |
| fields.mqtt_qos | Dynamische Formularbeschriftung | MQTT-Zustellstufe | wie bisher | Geprüft; beibehalten. |
| fields.assumed_state | Dynamische Formularbeschriftung | Nur angenommener Zustand | wie bisher | Geprüft; beibehalten. |
| fields.invalid_timestamp | Dynamische Formularbeschriftung | Ungültige Zeitangabe | wie bisher | Geprüft; beibehalten. |
| fields.transform_error | Dynamische Formularbeschriftung | Fehler bei der Umwandlung | wie bisher | Geprüft; beibehalten. |
| fields.ingest_seq | Dynamische Formularbeschriftung | Eingangsnummer | wie bisher | Geprüft; beibehalten. |
| fields.reference_version | Dynamische Formularbeschriftung | Nachweisformat | wie bisher | Geprüft; beibehalten. |
| fields.availability | Dynamische Formularbeschriftung | Verfügbarkeit | wie bisher | Geprüft; beibehalten. |
| alpha7.copy.structuredValue | Formular für Vorlage / Quelle / Vertrag | Zusammengesetzter Wert | wie bisher | Geprüft; beibehalten. |
| alpha7.copy.noValue | Formular für Vorlage / Quelle / Vertrag | Kein Wert | wie bisher | Geprüft; beibehalten. |
| alpha7.copy.oneArgument | Formular für Vorlage / Quelle / Vertrag | 1 Eingangswert | wie bisher | Geprüft; beibehalten. |
| alpha7.copy.arguments | Formular für Vorlage / Quelle / Vertrag | {n} Eingangswerte | wie bisher | Geprüft; beibehalten. |
| alpha7.copy.argument | Formular für Vorlage / Quelle / Vertrag | Eingangswert | wie bisher | Geprüft; beibehalten. |
| alpha7.copy.current | Formular für Vorlage / Quelle / Vertrag | Aktuell | wie bisher | Geprüft; beibehalten. |
| alpha7.copy.comparison | Formular für Vorlage / Quelle / Vertrag | Vergleich | wie bisher | Geprüft; beibehalten. |
| alpha7.copy.unknownCalculation | Formular für Vorlage / Quelle / Vertrag | Unbekannte Berechnung | wie bisher | Geprüft; beibehalten. |
| alpha7.copy.unchanged | Entwürfe und Konfigurationen | Es gibt noch keine Änderung an diesem Text. | wie bisher | Geprüft; beibehalten. |
| alpha7.copy.firstRow | Anordnung der Seitenbereiche | Bereits an erster Stelle | wie bisher | Geprüft; beibehalten. |
| alpha7.copy.lastRow | Anordnung der Seitenbereiche | Bereits an letzter Stelle | wie bisher | Geprüft; beibehalten. |
| alpha7.copy.requiredRow | Formular für Vorlage / Quelle / Vertrag | Mindestens ein Eintrag muss bleiben. | wie bisher | Geprüft; beibehalten. |
| alpha7.copy.inProgress | Formular für Vorlage / Quelle / Vertrag; Ersteinrichtung; Einstellungen; Entwurf und Bearbeitung; Vertrag und Vorlage; Erweitert / Nachweise; Quellen und Verknüpfungen | Die Aktion läuft. Bitte warte auf das Ergebnis. | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| alpha7.copy.validationRunning | Entwurf und Bearbeitung | Die Prüfung läuft. Bitte warte auf das Ergebnis. | wie bisher | Geprüft; beibehalten. |
| alpha7.copy.copyNeedsValue | Formular für Vorlage / Quelle / Vertrag | Gib zuerst einen neuen, noch nicht vorhandenen Wert ein. | wie bisher | Geprüft; beibehalten. |
| alpha7.copy.liveReadOnly | Entwurf und Bearbeitung | Du siehst die laufende Konfiguration. Wähle oben Bearbeiten, um Änderungen zu sammeln. | wie bisher | Geprüft; beibehalten. |
| alpha7.copy.advancedLocation | Entwürfe und Konfigurationen | Erweitert: Fundstelle | wie bisher | Geprüft; beibehalten. |
| fields.AdapterConfig | Dynamische Formularbeschriftung | Anbindung | wie bisher | Geprüft; beibehalten. |
| fields.Binding | Dynamische Formularbeschriftung | Verknüpfung | wie bisher | Geprüft; beibehalten. |
| fields.BooleanRule | Dynamische Formularbeschriftung | Logische Regel | wie bisher | Geprüft; beibehalten. |
| fields.BucketRule | Dynamische Formularbeschriftung | Schaltschwellen | wie bisher | Geprüft; beibehalten. |
| fields.Case | Dynamische Formularbeschriftung | Fall | wie bisher | Geprüft; beibehalten. |
| fields.Catalog | Dynamische Formularbeschriftung | Werteliste | wie bisher | Geprüft; beibehalten. |
| fields.CommandDefinition | Dynamische Formularbeschriftung | Befehl | wie bisher | Geprüft; beibehalten. |
| fields.CompareRule | Dynamische Formularbeschriftung | Vergleich | wie bisher | Geprüft; beibehalten. |
| fields.Contract | Dynamische Formularbeschriftung | Vertrag | wie bisher | Geprüft; beibehalten. |
| fields.DeclarativeDefinition | Dynamische Formularbeschriftung | Eigene Vorlage | wie bisher | Geprüft; beibehalten. |
| fields.Dependency | Dynamische Formularbeschriftung | Abhängigkeit | wie bisher | Geprüft; beibehalten. |
| fields.FieldSchema | Dynamische Formularbeschriftung | Werteart | wie bisher | Geprüft; beibehalten. |
| fields.FirstMatchRule | Dynamische Formularbeschriftung | Erster Treffer | wie bisher | Geprüft; beibehalten. |
| fields.FormulaRule | Dynamische Formularbeschriftung | Formel | wie bisher | Geprüft; beibehalten. |
| fields.FusionRule | Dynamische Formularbeschriftung | Zusammenführung | wie bisher | Geprüft; beibehalten. |
| fields.HistoryQuery | Dynamische Formularbeschriftung | Verlaufsabfrage | wie bisher | Geprüft; beibehalten. |
| fields.InputRule | Dynamische Formularbeschriftung | Eingang | wie bisher | Geprüft; beibehalten. |
| fields.LiteralRule | Dynamische Formularbeschriftung | Konstante | wie bisher | Geprüft; beibehalten. |
| fields.MachineDefinition | Dynamische Formularbeschriftung | Ablauf | wie bisher | Geprüft; beibehalten. |
| fields.MachineRule | Dynamische Formularbeschriftung | Ablaufzustand | wie bisher | Geprüft; beibehalten. |
| fields.MapRule | Dynamische Formularbeschriftung | Zuordnung | wie bisher | Geprüft; beibehalten. |
| fields.NotApplicableRule | Dynamische Formularbeschriftung | Bedingung trifft nicht zu | wie bisher | Geprüft; beibehalten. |
| fields.RegistryConfig | Dynamische Formularbeschriftung | Konfiguration | wie bisher | Geprüft; beibehalten. |
| fields.TemporalRule | Dynamische Formularbeschriftung | Zeitregel | wie bisher | Geprüft; beibehalten. |
| fields.TransitionDefinition | Dynamische Formularbeschriftung | Zustandswechsel | wie bisher | Geprüft; beibehalten. |
| fields.TypedInput | Dynamische Formularbeschriftung | Eingang mit Werteart | wie bisher | Geprüft; beibehalten. |
| fields.allow_manual_restart | Dynamische Formularbeschriftung | Manuellen Neustart erlauben | wie bisher | Geprüft; beibehalten. |
| fields.bindings | Dynamische Formularbeschriftung | Verknüpfungen | wie bisher | Geprüft; beibehalten. |
| fields.cases | Dynamische Formularbeschriftung | Fälle | wie bisher | Geprüft; beibehalten. |
| fields.catalogs | Dynamische Formularbeschriftung | Wertelisten | wie bisher | Geprüft; beibehalten. |
| fields.contracts | Dynamische Formularbeschriftung | Verträge | wie bisher | Geprüft; beibehalten. |
| fields.cursor | Dynamische Formularbeschriftung | Fortsetzung der Abfrage | wie bisher | Geprüft; beibehalten. |
| fields.definitions | Dynamische Formularbeschriftung | Vorlagen | wie bisher | Geprüft; beibehalten. |
| fields.dependencies | Dynamische Formularbeschriftung | Abhängigkeiten | wie bisher | Geprüft; beibehalten. |
| fields.fixture | Dynamische Formularbeschriftung | Testbeispiel | wie bisher | Geprüft; beibehalten. |
| fields.limit | Dynamische Formularbeschriftung | Höchste Anzahl | wie bisher | Geprüft; beibehalten. |
| fields.refresh_inputs | Dynamische Formularbeschriftung | Eingänge erneut lesen | wie bisher | Geprüft; beibehalten. |
| fields.schema | Dynamische Formularbeschriftung | Werteart | wie bisher | Geprüft; beibehalten. |
| fields.since | Dynamische Formularbeschriftung | Von | wie bisher | Geprüft; beibehalten. |
| fields.sources | Dynamische Formularbeschriftung | Quellen | wie bisher | Geprüft; beibehalten. |
| fields.then | Dynamische Formularbeschriftung | Dann | wie bisher | Geprüft; beibehalten. |
| fields.type | Dynamische Formularbeschriftung | Typ | wie bisher | Geprüft; beibehalten. |
| fields.until | Dynamische Formularbeschriftung | Bis | wie bisher | Geprüft; beibehalten. |
| fields.value_schema | Dynamische Formularbeschriftung | Werteart der Quelle | wie bisher | Geprüft; beibehalten. |
| fields.when | Dynamische Formularbeschriftung | Wenn | wie bisher | Geprüft; beibehalten. |
| codes.eq | Wert-/Ursachenanzeige, dynamisch | gleich | wie bisher | Geprüft; beibehalten. |
| codes.ne | Wert-/Ursachenanzeige, dynamisch | ungleich | wie bisher | Geprüft; beibehalten. |
| codes.lt | Wert-/Ursachenanzeige, dynamisch | kleiner | wie bisher | Geprüft; beibehalten. |
| codes.le | Wert-/Ursachenanzeige, dynamisch | höchstens | wie bisher | Geprüft; beibehalten. |
| codes.gt | Wert-/Ursachenanzeige, dynamisch | größer | wie bisher | Geprüft; beibehalten. |
| codes.ge | Wert-/Ursachenanzeige, dynamisch | mindestens | wie bisher | Geprüft; beibehalten. |
| codes.test.sum | Wert-/Ursachenanzeige, dynamisch | Summe der Zahlen | wie bisher | Geprüft; beibehalten. |
| codes.test_agreement | Wert-/Ursachenanzeige, dynamisch | Übereinstimmung im Test | wie bisher | Geprüft; beibehalten. |
| alpha7.draft.unnamed | Entwurf und Bearbeitung; Entwürfe und Konfigurationen | Entwurf ohne Namen | wie bisher | Geprüft; beibehalten. |
| alpha7.draft.advanced | Entwürfe und Konfigurationen | Erweitert | wie bisher | Geprüft; beibehalten. |
| alpha7.draft.identifier | Entwürfe und Konfigurationen | Entwurfskennung | wie bisher | Geprüft; beibehalten. |
| alpha7.diff.comparison | Entwürfe und Konfigurationen | Der Vergleich bezieht sich auf {against}. | wie bisher | Geprüft; beibehalten. |
| alpha7.diff.reinitialize | Entwürfe und Konfigurationen | Bestehende Abläufe beginnen neu | wie bisher | Geprüft; beibehalten. |
| alpha7.diff.reinitializeHelp | Entwürfe und Konfigurationen | Die Berechnungsregeln haben sich geändert. Betroffene Abläufe beginnen nach dem Übernehmen neu. | wie bisher | Geprüft; beibehalten. |
| alpha8.parameters.title | Formular für Vorlage / Quelle / Vertrag | Einstellungen für diesen Vertrag | wie bisher | Geprüft; beibehalten. |
| alpha8.parameters.draftHint | Formular für Vorlage / Quelle / Vertrag | Deine Änderung gilt erst, wenn du den Entwurf übernimmst. | wie bisher | Geprüft; beibehalten. |
| alpha8.ha.disconnected | Übersicht | Home Assistant getrennt seit {since} – {count} Werte ohne Frist gelten unverändert weiter | wie bisher | Geprüft; beibehalten. |
| alpha8.configuration.title | Vertrag und Vorlage; Übersicht | Konfiguration unvollständig | wie bisher | Geprüft; beibehalten. |
| alpha8.configuration.signal | Übersicht | Signal gestört | wie bisher | Geprüft; beibehalten. |
| alpha8.configuration.unassigned | Vertrag und Vorlage; Übersicht | Noch nicht zugeordnet | wie bisher | Geprüft; beibehalten. |
| codes.parameter | Wert-/Ursachenanzeige, dynamisch | Einstellung am Vertrag | wie bisher | Geprüft; beibehalten. |
| codes.time_reached | Wert-/Ursachenanzeige, dynamisch | Zeitpunkt erreicht | wie bisher | Geprüft; beibehalten. |
| codes.lower | Wert-/Ursachenanzeige, dynamisch | Kleinschreibung | wie bisher | Geprüft; beibehalten. |
| codes.strip | Wert-/Ursachenanzeige, dynamisch | Leerzeichen am Rand entfernen | wie bisher | Geprüft; beibehalten. |
| codes.normalize_key | Wert-/Ursachenanzeige, dynamisch | Schreibweise und Trennzeichen vereinheitlichen | wie bisher | Geprüft; beibehalten. |
| codes.matches | Wert-/Ursachenanzeige, dynamisch | Passt zum Muster | wie bisher | Geprüft; beibehalten. |
| codes.contains | Wert-/Ursachenanzeige, dynamisch | Enthält | wie bisher | Geprüft; beibehalten. |
| codes.configuration_hint | Wert-/Ursachenanzeige, dynamisch | Hinweis zur Vollständigkeit | wie bisher | Geprüft; beibehalten. |
| codes.retired | Wert-/Ursachenanzeige, dynamisch | Zurückgezogen | wie bisher | Geprüft; beibehalten. |
| codes.deprecated | Wert-/Ursachenanzeige, dynamisch | Läuft aus | wie bisher | Geprüft; beibehalten. |
| codes.clock | Wert-/Ursachenanzeige, dynamisch | Uhr und Kalender | wie bisher | Geprüft; beibehalten. |
| codes.connectivity | Wert-/Ursachenanzeige, dynamisch | Verbindung zu Home Assistant | wie bisher | Geprüft; beibehalten. |
| fields.lifecycle | Dynamische Formularbeschriftung | Verfügbarkeit dieser Version | wie bisher | Geprüft; beibehalten. |
| fields.reactivation_note | Dynamische Formularbeschriftung | Begründung für die Wiederfreigabe | wie bisher | Geprüft; beibehalten. |
| fields.parameter_schema | Dynamische Formularbeschriftung | Einstellungen der Vorlage | wie bisher | Geprüft; beibehalten. |
| fields.parameter_relations | Dynamische Formularbeschriftung | Zusammenhang zwischen Einstellungen | wie bisher | Geprüft; beibehalten. |
| validation.version_retired | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Diese Version wurde zurückgezogen. Bestehende Verträge dürfen sie weiter verwenden; wähle für die neue Bindung eine freigegebene Version. | wie bisher | Geprüft; beibehalten. |
| validation.parameter.value_error | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Die Einstellungen passen nicht zusammen. Prüfe ihre Werte und Beziehungen. | wie bisher | Geprüft; beibehalten. |
| validation.parameter.invalid_slot | Dynamische Beschriftung; Namensraum im Quellcode erhalten | Eine Dauer muss positiv sein und innerhalb der erlaubten Grenzen liegen. | wie bisher | Geprüft; beibehalten. |
| alpha8.lifecycle.title | Formular für Vorlage / Quelle / Vertrag | Verfügbarkeit der Vorlage | wie bisher | Geprüft; beibehalten. |
| alpha8.lifecycle.note | Formular für Vorlage / Quelle / Vertrag | Begründung für die Wiederfreigabe | wie bisher | Geprüft; beibehalten. |
| alpha8.lifecycle.noteHint | Formular für Vorlage / Quelle / Vertrag | Wenn du eine auslaufende oder zurückgezogene Version wieder freigibst, begründe diese Entscheidung. | wie bisher | Geprüft; beibehalten. |
| alpha8.bucket.multiclass | Formular für Vorlage / Quelle / Vertrag | Mehrere Klassen verwenden | wie bisher | Geprüft; beibehalten. |
| codes.active | Wert-/Ursachenanzeige, dynamisch | Freigegeben | wie bisher | Geprüft; beibehalten. |
| fields.minute_of_day | Dynamische Formularbeschriftung | Minute des Tages | wie bisher | Geprüft; beibehalten. |
| fields.day_of_year | Dynamische Formularbeschriftung | Tag des Jahres | wie bisher | Geprüft; beibehalten. |
| fields.boundaries | Dynamische Formularbeschriftung | Klassengrenzen | wie bisher | Geprüft; beibehalten. |
| fields.classes | Dynamische Formularbeschriftung | Klassen | wie bisher | Geprüft; beibehalten. |
| fields.hysteresis | Dynamische Formularbeschriftung | Umschaltbereich | wie bisher | Geprüft; beibehalten. |
| fields.class | Dynamische Formularbeschriftung | Klasse | wie bisher | Geprüft; beibehalten. |
| fields.unknown | Dynamische Formularbeschriftung | Noch unbekannt | wie bisher | Geprüft; beibehalten. |
| fields.minimum | Dynamische Formularbeschriftung | Kleinster erlaubter Wert | wie bisher | Geprüft; beibehalten. |
| fields.maximum | Dynamische Formularbeschriftung | Größter erlaubter Wert | wie bisher | Geprüft; beibehalten. |
| fields.label | Dynamische Formularbeschriftung | Bezeichnung | wie bisher | Geprüft; beibehalten. |
| fields.calendar | Dynamische Formularbeschriftung | Lokale Zeit und Kalender | wie bisher | Geprüft; beibehalten. |
| fields.projection | Dynamische Formularbeschriftung | Benötigter Zeitwert | wie bisher | Geprüft; beibehalten. |
| fields.resolution | Dynamische Formularbeschriftung | Genauigkeit | wie bisher | Geprüft; beibehalten. |
| fields.timezone | Dynamische Formularbeschriftung | Zeitzone | wie bisher | Geprüft; beibehalten. |
| fields.history_retention | Dynamische Formularbeschriftung | Aufbewahrung der Messwerte | wie bisher | Geprüft; beibehalten. |
| fields.batch_size | Dynamische Formularbeschriftung | Messwerte je Aufbewahrungsschritt | wie bisher | Geprüft; beibehalten. |
| alpha8.lifecycle.existing | Formular für Vorlage / Quelle / Vertrag | Bestehende Verträge behalten diese Version. Für neue Verträge wählst du eine freigegebene Vorlage. | wie bisher | Geprüft; beibehalten. |
| alpha8.parameters.deadlineName | Formular für Vorlage / Quelle / Vertrag | Einstellung für die Frist | wie bisher | Geprüft; beibehalten. |
| alpha8.retention.required | Gemeinsame Oberfläche / Wertanzeige | Aufbewahrung der Messwerte fehlt | wie bisher | Geprüft; beibehalten. |
| alpha8.retention.evidenceTitle | Erweitert / Nachweise | Außerhalb der Aufbewahrungsfrist | wie bisher | Geprüft; beibehalten. Nur Erweitert. |
| alpha8.retention.evidenceGone | Gemeinsame Oberfläche / Wertanzeige | Dieser einzelne Nachweis liegt außerhalb des noch aufbewahrten Verlaufs. Seine ursprüngliche Beobachtung wird nicht nachgebildet; verfügbare Stundenwerte sind eine Zusammenfassung und kein neuer Messwert. | wie bisher | Geprüft; beibehalten. |
| fields.seasons | Dynamische Formularbeschriftung | Jahreszeiten und ihre Anfangstage | wie bisher | Geprüft; beibehalten. |
| fields.month_day | Dynamische Formularbeschriftung | Monat und Tag (MM-TT) | wie bisher | Geprüft; beibehalten. |
| fields.leap_day | Dynamische Formularbeschriftung | Jahrestag in Jahren ohne 29. Februar | wie bisher | Geprüft; beibehalten. |
| fields.start | Dynamische Formularbeschriftung | Anfangstag (MM-TT) | wie bisher | Geprüft; beibehalten. |
| fields.code | Dynamische Formularbeschriftung | Hinweiskennung | wie bisher | Geprüft; beibehalten. |
| fields.message | Dynamische Formularbeschriftung | Hinweistext | wie bisher | Geprüft; beibehalten. |
| fields.delimiters | Dynamische Formularbeschriftung | Zu vereinheitlichende Trennzeichen | wie bisher | Geprüft; beibehalten. |
| fields.separator | Dynamische Formularbeschriftung | Gemeinsames Trennzeichen | wie bisher | Geprüft; beibehalten. |
| fields.calendar_input | Dynamische Formularbeschriftung | Lokaler Zeitwert | wie bisher | Geprüft; beibehalten. |
| fields.bucket_initial | Dynamische Formularbeschriftung | Anfangsklasse oder noch unbekannt | wie bisher | Geprüft; beibehalten. |
| fields.bucket_boundary | Dynamische Formularbeschriftung | Klassengrenze | wie bisher | Geprüft; beibehalten. |
| fields.parameter_definition | Dynamische Formularbeschriftung | Einstellung der Vorlage | wie bisher | Geprüft; beibehalten. |
| fields.parameter_relation | Dynamische Formularbeschriftung | Zusammenhang zwischen Einstellungen | wie bisher | Geprüft; beibehalten. |
| fields.retention_policy | Dynamische Formularbeschriftung | Aufbewahrung der Messwerte | wie bisher | Geprüft; beibehalten. |
| codes.date | Wert-/Ursachenanzeige, dynamisch | Lokales Datum | wie bisher | Geprüft; beibehalten. |
| codes.time | Wert-/Ursachenanzeige, dynamisch | Lokale Uhrzeit als Text | wie bisher | Geprüft; beibehalten. |
| codes.weekday | Wert-/Ursachenanzeige, dynamisch | Wochentag (Montag = 1) | wie bisher | Geprüft; beibehalten. |
| codes.minute_of_day | Wert-/Ursachenanzeige, dynamisch | Minute des Tages (0–1439) | wie bisher | Geprüft; beibehalten. |
| codes.day_of_year | Wert-/Ursachenanzeige, dynamisch | Tag des Jahres (1–366) | wie bisher | Geprüft; beibehalten. |
| codes.season | Wert-/Ursachenanzeige, dynamisch | Jahreszeit | wie bisher | Geprüft; beibehalten. |
| codes.minute | Wert-/Ursachenanzeige, dynamisch | Minutengenau | wie bisher | Geprüft; beibehalten. |
| codes.second | Wert-/Ursachenanzeige, dynamisch | Sekundengenau (nur bei ausdrücklichem Bedarf) | wie bisher | Geprüft; beibehalten. |
| codes.skip | Wert-/Ursachenanzeige, dynamisch | Bis zum nächsten Schaltjahr auslassen | wie bisher | Geprüft; beibehalten. |
| codes.feb28 | Wert-/Ursachenanzeige, dynamisch | Am 28. Februar | wie bisher | Geprüft; beibehalten. |
| codes.mar01 | Wert-/Ursachenanzeige, dynamisch | Am 1. März | wie bisher | Geprüft; beibehalten. |
| alpha8.parameters.unitHint | Entwurf und Bearbeitung | {description} ({unit}) | wie bisher | Geprüft; beibehalten. |
| alpha8.formula.inputLabel | Formular für Vorlage / Quelle / Vertrag | {name}{unit} | wie bisher | Geprüft; beibehalten. |
| alpha8.formula.unit | Formular für Vorlage / Quelle / Vertrag |  ({unit}) | wie bisher | Geprüft; beibehalten. |
| alpha8.formula.addInput | Formular für Vorlage / Quelle / Vertrag | Eingang {name} hinzufügen | wie bisher | Geprüft; beibehalten. |
| alpha8.formula.removeInput | Formular für Vorlage / Quelle / Vertrag | Optionalen Eingang {name} entfernen | wie bisher | Geprüft; beibehalten. |

## Ergänzungen beim A2-Bau

Die freigegebene Herkunftsregistrierung braucht zusätzliche Feldnamen im Bereich
Einstellungen → HA-Anbindung → Erweitert. Dafür gelten dieselben deutschen
Bezeichnungen für die beiden getrennten Rollen; keine Policy-/Apply-Ausführung.

| Schlüssel | Ort | alt | neu | Grund |
|---|---|---|---|---|
| `fields.producer_id` | HA-Anbindung → Erweitert | — | Kennung des Dienstes | Typisiertes Formular ohne JSON; technische Kennungen bleiben unter Erweitert. |
| `fields.context_producers` | HA-Anbindung → Erweitert | — | Bekannte Automatikdienste | Typisiertes Formular ohne JSON; technische Kennungen bleiben unter Erweitert. |
| `codes.policy` | HA-Anbindung → Erweitert | — | Entscheidender Dienst | Typisiertes Formular ohne JSON; technische Kennungen bleiben unter Erweitert. |
| `codes.apply` | HA-Anbindung → Erweitert | — | Ausführender Dienst | Typisiertes Formular ohne JSON; technische Kennungen bleiben unter Erweitert. |

Für das freigegebene Abfrageverfahren und die notwendige Standortbestätigung
braucht das konkrete Formular folgende ergänzende Beschriftungen:

| Schlüssel | Ort | alt | neu | Grund |
|---|---|---|---|---|
| `alpha9.refresh.method` | Verknüpfung / Vertrag → Quellen erneut abfragen | — | So wird die Quelle erneut abgefragt | Feste Verfahren, ausdrückliche Voraussetzung, Zeitfelder mit Minutenhilfe. |
| `alpha9.refresh.poll` | Verknüpfung / Vertrag → Quellen erneut abfragen | — | Wert vom Gerät neu lesen | Feste Verfahren, ausdrückliche Voraussetzung, Zeitfelder mit Minutenhilfe. |
| `alpha9.refresh.companion` | Verknüpfung / Vertrag → Quellen erneut abfragen | — | Standort vom Handy neu anfragen | Feste Verfahren, ausdrückliche Voraussetzung, Zeitfelder mit Minutenhilfe. |
| `alpha9.refresh.permission` | Verknüpfung / Vertrag → Quellen erneut abfragen | — | Ich habe geprüft, dass das Handy Standortabfragen im Hintergrund erlaubt. | Feste Verfahren, ausdrückliche Voraussetzung, Zeitfelder mit Minutenhilfe. |
| `alpha9.refresh.offset` | Verknüpfung / Vertrag → Quellen erneut abfragen | — | Wartezeit seit Beginn (Sekunden) | Feste Verfahren, ausdrückliche Voraussetzung, Zeitfelder mit Minutenhilfe. |
| `alpha9.refresh.stop` | Verknüpfung / Vertrag → Quellen erneut abfragen | — | Beenden, sobald dieser Vertrag Ja meldet | Feste Verfahren, ausdrückliche Voraussetzung, Zeitfelder mit Minutenhilfe. |

### Formularbeschriftungen A2: Fristen

| Schlüssel | Ort | alt | neu | Grund |
|---|---|---|---|---|
| alpha9.deadline.stateDuration | Vorlage → Ablauf | — | Zeit bis zum nächsten Schritt in „{state}“ | Auswahl im freigegebenen Fristenformular. |
| alpha9.deadline.fixed | Vorlage → Ablauf | — | Feste Dauer | Auswahl im freigegebenen Fristenformular. |
| alpha9.deadline.target | Vorlage → Ablauf | — | Danach zu diesem Schritt | Auswahl im freigegebenen Fristenformular. |
| alpha9.deadline.from | Vorlage → Ablauf | — | Gilt im Schritt „{state}“ | Auswahl im freigegebenen Fristenformular. |
| alpha9.deadline.priority | Vorlage → Ablauf | — | Bei gleichem Zeitpunkt zuerst | Auswahl im freigegebenen Fristenformular. |
| alpha9.deadline.action | Vorlage → Ablauf | — | Was passiert mit der Frist? | Auswahl im freigegebenen Fristenformular. |
| alpha9.deadline.keep | Vorlage → Ablauf | — | Frist beibehalten | Auswahl im freigegebenen Fristenformular. |
| alpha9.deadline.clear | Vorlage → Ablauf | — | Frist beenden | Auswahl im freigegebenen Fristenformular. |

### Formularbeschriftungen A2: manuelle Angaben

| Schlüssel | Ort | alt | neu | Grund |
|---|---|---|---|---|
| codes.manual | Manuelle Quelle | — | Manuell eingegeben | Bedienung, Gültigkeit und Ergebnisabfrage ohne JSON. |
| codes.input_not_yet_valid | Manuelle Quelle | — | Diese Angabe gilt noch nicht. | Bedienung, Gültigkeit und Ergebnisabfrage ohne JSON. |
| alpha9.manual.future | Manuelle Quelle | — | Angaben mit einem späteren Beginn zulassen | Bedienung, Gültigkeit und Ergebnisabfrage ohne JSON. |
| alpha9.manual.affected | Manuelle Quelle | — | Diese Verträge verwenden deine Angabe: {names} | Bedienung, Gültigkeit und Ergebnisabfrage ohne JSON. |
| alpha9.manual.inactive | Manuelle Quelle | — | Verknüpfe diese Quelle zuerst mit einem eingeschalteten Vertrag. | Bedienung, Gültigkeit und Ergebnisabfrage ohne JSON. |
| alpha9.manual.failed | Manuelle Quelle | — | Die Angabe wurde nicht übernommen. Prüfe die Gültigkeit und lade die aktuelle Konfiguration neu. | Bedienung, Gültigkeit und Ergebnisabfrage ohne JSON. |
| alpha9.manual.checkResult | Manuelle Quelle | — | Gespeichertes Ergebnis abfragen | Bedienung, Gültigkeit und Ergebnisabfrage ohne JSON. |
| alpha9.manual.unit | Manuelle Quelle | — | Einheit | Bedienung, Gültigkeit und Ergebnisabfrage ohne JSON. |
| alpha9.manual.minimum | Manuelle Quelle | — | Kleinster erlaubter Wert | Bedienung, Gültigkeit und Ergebnisabfrage ohne JSON. |
| alpha9.manual.maximum | Manuelle Quelle | — | Größter erlaubter Wert | Bedienung, Gültigkeit und Ergebnisabfrage ohne JSON. |

### Formularbeschriftungen A2: Sensorprüfung und Herkunft

| Schlüssel | Ort | alt | neu | Grund |
|---|---|---|---|---|
| alpha9.sensor.choose | Quelle und Vertrag | — | Ausgewählte Sensorprüfung | Formulare und getrennte Herkunftsangabe ohne JSON. |
| alpha9.sensor.defaultName | Quelle und Vertrag | — | Eigene Sensorprüfung | Formulare und getrennte Herkunftsangabe ohne JSON. |
| alpha9.sensor.referenceDelta | Quelle und Vertrag | — | Mindestens diese Änderung bei der Vergleichsquelle | Formulare und getrennte Herkunftsangabe ohne JSON. |
| alpha9.sensor.profileVersion | Quelle und Vertrag | — | Version der Sensorprüfung | Formulare und getrennte Herkunftsangabe ohne JSON. |
| alpha9.valueOrigin.provider | Quelle und Vertrag | — | Anbieter oder Berechnung | Formulare und getrennte Herkunftsangabe ohne JSON. |
| alpha9.valueOrigin.issued_at | Quelle und Vertrag | — | Erstellt am | Formulare und getrennte Herkunftsangabe ohne JSON. |
| alpha9.valueOrigin.valid_from | Quelle und Vertrag | — | Gültig von | Formulare und getrennte Herkunftsangabe ohne JSON. |
| alpha9.valueOrigin.valid_until | Quelle und Vertrag | — | Gültig bis | Formulare und getrennte Herkunftsangabe ohne JSON. |
| alpha9.valueOrigin.output | Quelle und Vertrag | — | Art des Ergebnisses „{name}“ | Formulare und getrennte Herkunftsangabe ohne JSON. |
| alpha9.valueOrigin.inputs | Quelle und Vertrag | — | Verwendete Eingänge: {kinds} | Formulare und getrennte Herkunftsangabe ohne JSON. |
| alpha9.valueOrigin.point | Quelle und Vertrag | — | Vorhersage {number} | Formulare und getrennte Herkunftsangabe ohne JSON. |
| alpha9.valueOrigin.addPoint | Quelle und Vertrag | — | Zeitraum hinzufügen | Formulare und getrennte Herkunftsangabe ohne JSON. |
| alpha9.valueOrigin.series | Quelle und Vertrag | — | {count} Zeiträume eingetragen | Formulare und getrennte Herkunftsangabe ohne JSON. |
| codes.sensor_stuck_suspected | Quelle und Vertrag | — | Wert seit ungewöhnlich langer Zeit unverändert | Formulare und getrennte Herkunftsangabe ohne JSON. |
| codes.value_validity_gap | Quelle und Vertrag | — | Für diesen Zeitpunkt ist kein Wert gültig. | Formulare und getrennte Herkunftsangabe ohne JSON. |
| fields.value_origin_path | Quelle und Vertrag | — | Herkunftsangabe im gelieferten Datensatz | Formulare und getrennte Herkunftsangabe ohne JSON. |
