# Namen und Zuständigkeiten

| Name | Aufgabe |
|---|---|
| Wuschel | Core Contracts, eigenständige App, Slug wuschel |
| Traber | HA-Integration, Domain traber; die Funktion heißt „HA-Anbindung“ |
| Schnüffel | Anwesenheit, spätere Vorlage |
| Kuschel | Klima, spätere Vorlage |
| Funkel | Licht, spätere Vorlage |
| Blinzel | Rollos, spätere Vorlage |
| Schlummer | Schlaf/Wecken, spätere Vorlage |
| Träller | Medien, spätere Vorlage |
| Pförtchen | Tür, spätere Vorlage |

Die [Herde](https://github.com/Levtos/control/issues/60) legt Figuren, Farben
und Symbole fest. Weitere Module werden hier nicht implementiert.
Images ghcr.io/levtos/{arch}-wuschel. Hauptdistribution und CLI: wuschel.
Python-Import core_contracts und SDK core_contracts_client/CoreContractsClient
bleiben technische Schnittstellen. Traber spricht traber/* mit Protokoll 2.
Fachliche IDs, /api/v1 und gespeicherte Dokumente werden nicht umbenannt.

Wuschel ersetzt den Produktnamen Mimir, Traber den Namen Bifröst. Historische
Tags/Belege und installierte alte Apps bleiben unverändert. core_contracts/
bleibt bytegleich als Terra-Store-Eintrag. Keine automatische Übernahme alter
DBs, UUIDs, /data-Ablagen oder HA-Einträge. Siehe
[ADR 0022](adr/0022-wuschel-traber-naming.md) und [Betrieb](operations.md).
Producer liefern Evidence; Policies entscheiden Handlungen; Apply führt sie aus.
