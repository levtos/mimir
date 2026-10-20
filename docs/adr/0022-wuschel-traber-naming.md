# ADR 0022 — Wuschel und Traber ersetzen Mimir und Bifröst

20.10.2026 · Produktnamen durch Benni beschlossen; technische Details **A1 / Review**.
Ersetzt [ADR 0008](0008-mimir-naming-installation.md) für neue Installationen ab
Alpha 10, einschließlich der damaligen Aussage „kein weiterer Slugwechsel“ und
der alten Modulnamenliste. Historische Installationen/Tags bleiben unverändert.
Bezug: [#24](https://github.com/Levtos/wuschel/issues/24),
[control#60](https://github.com/Levtos/control/issues/60), [ADR 0009](0009-prerelease-version-gate.md).

## Umbenennungsmatrix

| Stelle / Ausgangsidentität | Ziel / Behandlung in A2 |
|---|---|
| Repo `Levtos/mimir`, ältere Adresse `Levtos/core_contract_app` | `Levtos/wuschel`; Benni hat umbenannt. Redirects und Assets lesen/präsentieren prüfen; keine alten Releases neu publizieren |
| `mimir/` mit config, Dockerfile, rootfs, DOCS, CHANGELOG | `wuschel/`; altes `mimir/` nicht als veränderten Store-Eintrag behalten |
| `core_contracts/` (Terra-Store) | gesamter Verzeichnisinhalt bytegleich; keine Aktualisierung seines Manifests |
| App-Name, description, Browser-Titel, Shell, Setup, Diagnose, Fehler, aria-Texte | Wuschel; Feature bleibt „HA-Anbindung“, Integration heißt Traber |
| Slug / Default-DB / Default-Rolle | `wuschel` / `wuschel` / `wuschel_app`; eigene /data- und DB-Identität |
| Architekturimage/OCI source, description, title, package metadata | `ghcr.io/levtos/{amd64,aarch64}-wuschel`; Source `https://github.com/Levtos/wuschel` |
| `repository.yaml` Name/URL, App-URL | Wuschel / neue Repo-URL; Supervisor-Store-URL in B prüfen, alte URL nicht blind als ausreichenden Redirect annehmen |
| Hauptdistribution `core-contracts-platform`, CLI `core-contracts` | Distribution `wuschel`, CLI `wuschel`; pyproject, uv.lock, Docker, Metadatenabfragen und Packaging gemeinsam ändern |
| Python-Import `src/core_contracts`, SDK `core-contracts-client`, `core_contracts_client`, `CoreContractsClient` | technische Bibliotheks-/API-Namen bleiben: kein fachlicher API-Bruch durch Produktbranding; keine Anzeige als Produktname |
| Frontend `mimir-workbench` | `wuschel-workbench`, beide Lockfile-Metadaten, Downloadnamen `wuschel-…json`, document title |
| `custom_components/bifrost/` | `custom_components/traber/`; DOMAIN, config-flow domain/title, logger, Manifest, strings, de/en, HACS-Dokumentation, Config-Entry neu |
| `bifrost/info` | `traber/info` |
| `bifrost/negotiate` | `traber/negotiate` |
| `bifrost/subscribe` | `traber/subscribe` |
| `bifrost/service_call` | `traber/service_call` |
| `bifrost/source_metadata` | `traber/source_metadata` |
| feste Serviceoperationen | `calendar_events`, `problem_notice_put`, `problem_notice_remove`, `source_refresh` bleiben; HA-Zielaktionen unverändert |
| `mimir_<UUID>_signal/configuration` | `wuschel_<neue UUID>_signal/configuration`; Regex, Verbindungsbindung und App-Generator gemeinsam ändern |
| Hinweis-Titel/-Text/-Link „Mimir …“ | „Wuschel …“; Ingress-Ziel aus tatsächlichem Supervisor-Kontext, keine hart codierte Store-ID |
| Ereignisse, Capability-/Versionsantworten, Setup-Prüfung, Fake-HA, HA-Kernel-/Clienttests | neue Domain überall synchron; bestehende Nutzdaten-/Capabilities bleiben erhalten |
| CI / Release / Staging / Image-Smoke | neue App-/Integrationspfade und Distribution; beide Architektur-Belege, anonyme Pulls; keinen alten Imagepfad überschreiben |
| dev compose, Fixture-Runner, synthetische lokale Logs/Testtitel | aktuelle ausführbare Pfade und Namen umstellen; historische Abnahmebilder unverändert |
| aktive README, docs/naming.md, api.md, operations.md, publishing.md, first-run.md | neue Begriffe und Links; neue Aufräumanleitung, weitere Herdenmodule nur Namensvorlage |
| ADRs/Audits/Releasebelege/alte Abnahmebilder | historischen Inhalt erhalten, ersetzende ADR verlinken; keine globale Textersetzung |
| `/api/v1`, DB-Tabellen `cc_*`, Contract-/Source-/Type-IDs, Sprachversionen | erhalten; Produktname ist keine Vertragssemantik |

Die vollständige Dateiliste samt Fundzeilen und Behandlung steht im
[Inventar](../alpha10/rename-inventory.md). A2 wiederholt den Suchlauf auf seinem
finalen Head; neue Treffer dürfen weder ungeprüft ersetzt noch unbemerkt ignoriert
werden. Insbesondere wird die neue Hauptdistribution an allen
`importlib.metadata.version`-Stellen angepasst; SDK-Version 0.1.0 ist getrennt.

## Protokollentscheidung

**Protokoll 2 bleibt.** Neue Domain = ausdrücklich neue Integration, keine
transparente Weiterentwicklung der alten Endpunktadresse. Innerhalb von
`traber/*` bleiben Aushandlung, Adminpflicht, Payloads, Limits, Context,
Kalender-/Bereichsantworten und Operationen aus ADR 0012–0020 semantisch gleich.
Neue Hinweispräfixe gehören zur neu installierten Domain/UUID. Es gibt keine
falsche Zusage, dass eine alte Bifröst-App gegen Traber läuft.
Traber bewahrt die angebotene v1/v2-Aushandlung innerhalb seiner Domain;
Wuschel-Abnahme verlangt selected=2. Kein Fallback von Wuschel auf `bifrost/*`.
Sollte A2 weitere inkompatible Nutzdatenänderungen benötigen, ist diese Begründung
erneut zu reviewen statt still „2“ beizubehalten.

## Alte Frontend-Links

Hashrouter und Ingress bleiben. Bestehende `legacyTarget`-Abbildungen bleiben
funktional; `/contracts/import/json` und `/changes/transfer` leiten per replace
zu `/import-export` weiter. `/sources/catalogs` bleibt Wertelisten-Einstieg;
neue Katalogpflege unter `/catalogs/:catalogId`. Query-/Filterzustand erhalten,
encoded IDs genau einmal dekodieren, kein externes Redirect aus Queryparametern.
Alte Vertrags-/Vorlagen-/Entwurfslinks werden mit vorhandenen Aliasen getestet.
Keine Umleitung eines alten Supervisor-/Terra-/Mimir-App-Slugs: ein Bookmark
zu einer anderen installierten App lässt sich nicht durch Wuschels Router retten.
Benni aktualisiert diese Favoriten nach B; keine Änderung der HA-Konfiguration in A1/A2.

## Bennis Schritte: Bifröst sauber entfernen

Diese Schritte stehen später auch in operations.md. Durchführung erst in B
nach Sicherung und ausdrücklichem Go; Mimir bleibt installiert und unverändert.
Die Entfernung von Bifröst beendet bewusst seine HA-Anbindung.

1. Bifröst-Version und Config-Entry über reine Integrationsmetadaten erfassen;
   alte App-UUID aus ihrer bereits redigierten Installationsidentität notieren,
   keine App-Optionen öffnen/abfragen. HA-Sicherung bei Benni.
2. In Einstellungen → Geräte & Dienste den Bifröst-Eintrag löschen.
   Alle zugehörigen Einträge prüfen, nicht allein auf die Kachel vertrauen.
3. In HACS das bisherige Integrationspaket entfernen. HACS identifiziert das
   Paket nach Repository: das umbenannte Repo ist keine zweite Paketidentität.
   Erst altes Paket entfernen, dann neue Domain aus derselben Repo-URL laden.
4. Nach Entfernen des Eintrags das alte Verzeichnis
   `custom_components/bifrost` prüfen. Nur wenn tatsächlich übrig geblieben:
   Benni löscht genau dieses Verzeichnis; keine Handarbeit an `.storage`.
   Keine fremden custom_components oder die Legacy-Integration anfassen.
5. Konfigurationsprüfung, geplanter HA-Neustart im B-Ablauf; erst danach
   Traber installieren/neu einrichten oder bei gemeinsam vorbereitetem
   Installationsschritt beide Änderungen in demselben geplanten Neustart prüfen.
   B-Nachweis muss geladenes `traber` und fehlendes `bifrost` belegen.
6. Alte dauerhafte Hinweise separat bereinigen: Benni bestätigt genau
   `mimir_<alte UUID>_signal` und `mimir_<alte UUID>_configuration` und entfernt
   sie einzeln per HA-Oberfläche beziehungsweise `persistent_notification.dismiss`.
   Kein `dismiss_all`, keine Präfix-Wildcards, keine fremden UUIDs.

Traber bekommt **keine** Befugnis zum Entfernen alter `mimir_*`-Hinweise;
sein Kanal akzeptiert ausschließlich die zwei `wuschel_*`-IDs seiner
ausgehandelten UUID. Kein automatischer Abbau beim Config-Entry-Unload:
Benni muss die zwei alten Hinweise deshalb ausdrücklich prüfen.
Rückweg: Traber-Eintrag/Paket von Benni entfernen, alten geprüften Release
v1.0.0a9 über HACS wieder installieren und Bifröst neu einrichten; Mimir-DB
und /data bleiben unverändert. Alte Hinweise nicht blind neu erzeugen.

## Nachweise in A2/B

A2: Pfad-/Metadatenkonsistenz, Distribution/CLI im Paket, beide Architekturen,
vollständige Channel-Namensliste, fremde UUID/alter Präfix abgewiesen, neue
Integration/Config-Flow, alle Redirects mit Query/IDs, i18n inklusive Meldungen.
Terra-Verzeichnis bytegleich zur Basis. B: Repo-/Release-Weiterleitungen und
alte Image-Abrufbarkeit, Store-Repository, Traber geladen mit echter
Manifestversion/Protokoll 2, eigene neue UUID. Keine Live-Behauptung aus CI.
