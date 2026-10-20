# Alpha 10 — vollständiges Umbenennungsinventar der Basis

Basis `f039081a19896e0529d0f508725f7fda97485981`; alle getrackten Pfade und UTF-8-Inhalte geprüft.
Suchmuster (case-insensitive): `mimir|bifröst|bifrost|terra|core[-_ ]contracts`.
Zeilen beziehen sich auf die unveränderte Basis, nicht den späteren A2-Head.
Pfadtreffer ohne Texttreffer sind ausdrücklich enthalten; Binärbilder werden nicht als Text gelesen.
Keine Trefferzahl ist eine Aufforderung zur globalen Ersetzung. A2 ergänzt neue Fundstellen.

| Datei/Pfad | Basis-Zeilen | Behandlung |
|---|---|---|
| `.github/workflows/ci.yml` | 16,18,20,22,34,94,112,149,156,157,160,165,169 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `.github/workflows/publish-images.yml` | 57 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `AGENTS.md` | 1 | Kurze Governance-Brücke erhalten; keine globale Textersetzung |
| `CHANGELOG.md` | 3,5,10,23,58,63 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `README.md` | 1,3,5,7,8,15,16,21,38 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `client/core_contracts_client/__init__.py` | nur Pfad | SDK-Distribution/Importpfad/öffentliche Klasse erhalten |
| `client/pyproject.toml` | 2,12 | SDK-Distribution/Importpfad/öffentliche Klasse erhalten |
| `core_contracts/CHANGELOG.md` | 10,27,32 | Terra-Store bytegleich erhalten |
| `core_contracts/DOCS.md` | 1,30 | Terra-Store bytegleich erhalten |
| `core_contracts/Dockerfile` | 36 | Terra-Store bytegleich erhalten |
| `core_contracts/config.yaml` | 1,3,4,22,26,27 | Terra-Store bytegleich erhalten |
| `core_contracts/rootfs/entrypoint.sh` | 8 | Terra-Store bytegleich erhalten |
| `custom_components/bifrost/__init__.py` | 19 | Pfad nach traber; Domains/Endpunkte/Präfixe/Texte gezielt ersetzen |
| `custom_components/bifrost/config_flow.py` | 6,13 | Pfad nach traber; Domains/Endpunkte/Präfixe/Texte gezielt ersetzen |
| `custom_components/bifrost/manifest.json` | 2,3,6,7 | Pfad nach traber; Domains/Endpunkte/Präfixe/Texte gezielt ersetzen |
| `custom_components/bifrost/service_channel.py` | 47,118,119 | Pfad nach traber; Domains/Endpunkte/Präfixe/Texte gezielt ersetzen |
| `custom_components/bifrost/source_metadata.py` | nur Pfad | Pfad nach traber; Domains/Endpunkte/Präfixe/Texte gezielt ersetzen |
| `custom_components/bifrost/strings.json` | 1 | Pfad nach traber; Domains/Endpunkte/Präfixe/Texte gezielt ersetzen |
| `custom_components/bifrost/translations/de.json` | 1 | Pfad nach traber; Domains/Endpunkte/Präfixe/Texte gezielt ersetzen |
| `custom_components/bifrost/translations/en.json` | 1 | Pfad nach traber; Domains/Endpunkte/Präfixe/Texte gezielt ersetzen |
| `dev/alpha8_scale_probe.py` | 15,16,17 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `dev/compose.yaml` | 5,6,11 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `dev/container_smoke.py` | 11,29,104,116,163 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `dev/fake_ha.py` | 35,51,63,83 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `dev/image_package.py` | 18,24,27,79,89,153,154,173,231 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `dev/phase1a_acceptance.py` | 15,16,17,18,19,20,173,177 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `dev/resource_probe.py` | 11,12,13,14,15 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `dev/review_probe.py` | 21,22,23,24,25,26,27,28 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `dev/stage_app.py` | 11,14,23,24 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `dev/version_gate.py` | 96,102 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `dev/workbench_alpha8.py` | 8,9,160 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `dev/workbench_alpha9.py` | 6 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `dev/workbench_demo.py` | 1,33,34,35,36,37,38,39,40,41,114,119 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `dev/workbench_devices.py` | 7 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `dev/workbench_post1.py` | 5,6 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `docs/README.md` | 7,11,13,29,32,33 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `docs/adr/0002-phase1a-producer-and-ownership.md` | 6 | Entscheidung historisch erhalten; gezielten Fortschreibungslink setzen |
| `docs/adr/0004-manual-machine-restart.md` | 23 | Entscheidung historisch erhalten; gezielten Fortschreibungslink setzen |
| `docs/adr/0008-mimir-naming-installation.md` | 1,11,13,14,15,16,17,18,19,20,21,22,24,27,30,38,43,45,46,50,51,52,55,58,60,62,70,72 | Entscheidung historisch erhalten; gezielten Fortschreibungslink setzen |
| `docs/adr/0009-prerelease-version-gate.md` | 3,15,37,43,58 | Entscheidung historisch erhalten; gezielten Fortschreibungslink setzen |
| `docs/adr/0012-bifrost-service-channel.md` | 1,4,10,11,12,13,16,18,21,22,26,33,52 | Entscheidung historisch erhalten; gezielten Fortschreibungslink setzen |
| `docs/adr/0013-calendar-cache.md` | 1,5 | Entscheidung historisch erhalten; gezielten Fortschreibungslink setzen |
| `docs/adr/0014-problem-notifications.md` | 5,9,40,41,48 | Entscheidung historisch erhalten; gezielten Fortschreibungslink setzen |
| `docs/adr/0016-manual-source.md` | 10 | Entscheidung historisch erhalten; gezielten Fortschreibungslink setzen |
| `docs/adr/0017-ha-context-origin.md` | 4,8,76,79 | Entscheidung historisch erhalten; gezielten Fortschreibungslink setzen |
| `docs/adr/0018-reconciliation-refresh.md` | 5,86 | Entscheidung historisch erhalten; gezielten Fortschreibungslink setzen |
| `docs/adr/0020-category-room-metadata.md` | 64,95,110 | Entscheidung historisch erhalten; gezielten Fortschreibungslink setzen |
| `docs/adr/0021-plain-ui-retention-readiness.md` | 68,69 | Entscheidung historisch erhalten; gezielten Fortschreibungslink setzen |
| `docs/alpha8/ABNAHME.md` | 3,11,32,43,67,77,79,83,85,86 | Historischen Beleg einschließlich Dateiname erhalten |
| `docs/alpha8/README.md` | 1,3,4,20,24,35,37,38,39 | Historischen Beleg einschließlich Dateiname erhalten |
| `docs/alpha8/retention-scaling.md` | 56,57 | Historischen Beleg einschließlich Dateiname erhalten |
| `docs/alpha8/screenshots/01-mimir-kopf.png` | nur Pfad | Historischen Beleg einschließlich Dateiname erhalten |
| `docs/alpha9/ABNAHME.md` | 4,12,35,63 | Historischen Beleg einschließlich Dateiname erhalten |
| `docs/alpha9/README.md` | 4,7,17,25,44,67,82,96,101 | Historischen Beleg einschließlich Dateiname erhalten |
| `docs/alpha9/TEXTE.md` | 51,57,59,88,89,91,92,94,95,96,97,116,117,161,170,172,173,176,179,185,186,190,204,208,211,231,234,260,268,271,303,328,329,330,338,342,384,401,411,429,455,461,487,490,494,495,499,500,501,503,504,515,516,517,519,552,563,564,590,594,626,635,636,751,756,791,801,818,854,988,996,997,1037,1077,1078,1918,1956,1957,1962,2344,2690,2699,2700,2828,2829,2831,2835,2857,2858,2859,2891,2892,2894,2895,2897,2930,2931,2935,2987 | Historischen Beleg einschließlich Dateiname erhalten |
| `docs/alpha9/versionsgate.json` | 3,19,20,27,28,35,36,43,44,51,52,59,60,67,68 | Historischen Beleg einschließlich Dateiname erhalten |
| `docs/api.md` | 32 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `docs/audits/akte-gap-2026-10.md` | 4,11,15,17,34,48,52,58,59,60,61,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,81,82,84,85,86,87,89,90,91,92,93,94,96,97,98,99,100,101,102,103,109,110,111,112,113,114,115,116,117,118,128,132,140,141,142,143,144,145,146,147,148,200,219,221,227 | Historischen Beleg einschließlich Dateiname erhalten |
| `docs/audits/profile-delta-audit-2026-10-07.md` | 1 | Historischen Beleg einschließlich Dateiname erhalten |
| `docs/audits/technical-baseline-check-2026-10-07.md` | 1 | Historischen Beleg einschließlich Dateiname erhalten |
| `docs/first-run.md` | 3,4,5,6,43,96,102,107,110 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `docs/naming.md` | 5,6,9,18,22,23,24,25,27 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `docs/operations.md` | 1,4,27,31,184 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `docs/operations/mimir-new-database.md` | 1,4,8,14,15,19,24,34,37,38,39,40,41,43,44,55,57,59,65,70,71,72,73,77,91,98,100,101,116,118 | Altes Runbook erhalten; durch neuen Runbook-Einstieg ablösen |
| `docs/platform-alpha1/build-specification.md` | 1,4,23,32,42,43,137,156,243,505,511,512,540,541,543,544,545,554,565,739,901,902,904,905,913 | Historische Basis erhalten; relevante Spezifikation per A2-Nachtrag fortschreiben |
| `docs/platform-alpha1/codex-build-prompt.md` | 1,3,19,21,22,38,76,82,107,112 | Historische Basis erhalten; relevante Spezifikation per A2-Nachtrag fortschreiben |
| `docs/platform-alpha1/completion-report.md` | 73,138 | Historische Basis erhalten; relevante Spezifikation per A2-Nachtrag fortschreiben |
| `docs/platform-alpha1/delta-remediation.md` | 79 | Historische Basis erhalten; relevante Spezifikation per A2-Nachtrag fortschreiben |
| `docs/platform-alpha1/live-acceptance.md` | 25,61 | Historische Basis erhalten; relevante Spezifikation per A2-Nachtrag fortschreiben |
| `docs/platform-alpha1/opus-pre-install-review.md` | 12,103,104,121,123,124,125,126,137,152,156,157,159,191,209,211,351,352,353,409,441,442,477,478,513,514,544,565,566,583,603,604,628,647,666,667,685,686,709,726,741,757,758,772,799,813,820,826,832,839,853,858,866,867,871,877,882,896,897,992,1066,1067,1068,1069,1070,1071,1072 | Historische Basis erhalten; relevante Spezifikation per A2-Nachtrag fortschreiben |
| `docs/platform-alpha1/opus-remediation.md` | 37,65,77,150 | Historische Basis erhalten; relevante Spezifikation per A2-Nachtrag fortschreiben |
| `docs/platform-alpha1/reuse-analysis.md` | 4,6 | Historische Basis erhalten; relevante Spezifikation per A2-Nachtrag fortschreiben |
| `docs/publishing.md` | 3,5,9,10,12,33,34,59,60,64,72,96 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `docs/releases/1.0.0a2.md` | 17,18,34,42,84 | Historischen Beleg einschließlich Dateiname erhalten |
| `docs/releases/1.0.0a3.md` | 48,49 | Historischen Beleg einschließlich Dateiname erhalten |
| `docs/releases/1.0.0a4.md` | 93,94 | Historischen Beleg einschließlich Dateiname erhalten |
| `docs/releases/1.0.0a5.md` | 1,18,41,42 | Historischen Beleg einschließlich Dateiname erhalten |
| `docs/releases/1.0.0a6.md` | 20 | Historischen Beleg einschließlich Dateiname erhalten |
| `docs/releases/1.0.0a7.md` | 1,53,95 | Historischen Beleg einschließlich Dateiname erhalten |
| `docs/releases/1.0.0a7.post1.md` | 30,44 | Historischen Beleg einschließlich Dateiname erhalten |
| `docs/releases/1.0.0a8.md` | 1,6,7,28,29,30,31 | Historischen Beleg einschließlich Dateiname erhalten |
| `docs/releases/alpha6-reset-runbook.md` | 6 | Historischen Beleg einschließlich Dateiname erhalten |
| `docs/workbench/README.md` | 1,141 | Historischen Beleg einschließlich Dateiname erhalten |
| `docs/workbench/alpha7-post1/KORREKTUR.md` | 18 | Historischen Beleg einschließlich Dateiname erhalten |
| `docs/workbench/alpha7/ABLAUF-NEUSTART.md` | 73 | Historischen Beleg einschließlich Dateiname erhalten |
| `docs/workbench/alpha7/ABNAHME.md` | 94,108 | Historischen Beleg einschließlich Dateiname erhalten |
| `docs/workbench/alpha7/QUELLENUMZUG.md` | 20 | Historischen Beleg einschließlich Dateiname erhalten |
| `docs/workbench/review-resolution.md` | 1,48 | Historischen Beleg einschließlich Dateiname erhalten |
| `frontend/index.html` | 8 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `frontend/package-lock.json` | 2,8 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `frontend/package.json` | 2 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `frontend/scripts/capture-alpha8.mjs` | 6,18 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `frontend/scripts/capture-alpha9.mjs` | 7,68 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `frontend/src/alpha7/manualRestart.test.tsx` | 46 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `frontend/src/alpha7/readiness.test.tsx` | 10,25,29 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `frontend/src/alpha9-pages.test.tsx` | 53 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `frontend/src/alpha9/retention-readiness.test.tsx` | 46,47,48,49,71 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `frontend/src/assets/mdi/02.json` | 1 | Gepinntes fremdes MDI-Vokabular erhalten (Substring-Treffer) |
| `frontend/src/assets/mdi/23.json` | 1 | Gepinntes fremdes MDI-Vokabular erhalten (Substring-Treffer) |
| `frontend/src/components/PageLoading.tsx` | 6 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `frontend/src/components/PanelLayout.tsx` | 11 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `frontend/src/components/RouteError.tsx` | 13 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `frontend/src/components/Shell.tsx` | 62,63 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `frontend/src/e2e.test.tsx` | 24,27,29,335 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `frontend/src/editors/valueEditor.test.tsx` | 34,48 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `frontend/src/features/authoring/WorkingDocument.tsx` | 76 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `frontend/src/features/diagnostics/CommandsPanel.tsx` | 93 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `frontend/src/features/diagnostics/diagnostics.test.tsx` | 177 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `frontend/src/features/graph/GraphPage.tsx` | 45,70,85 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `frontend/src/features/registry/ImportExportPage.tsx` | 71,73,75 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `frontend/src/features/sources/useSourceSelection.ts` | 14,16 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `frontend/src/i18n/de.json` | 55,78,83,120,131,143,151,184,185,191,193,239,275,276,338,346,347,348,400,402,411,420,452,453,486,499,598,614,625,709,808,811,812,827,835,985,1062,1101,1166,1255,1311,1490,1499,1515,1528,1537,1541,1547,1549,1550,1592,1594,1596,1597,1599,1600,1605,2003,2176,2216,2225,2226,2354,2355,2357,2361,2383,2384,2385,2417,2418,2420,2421,2423,2456,2457,2461 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `frontend/src/index.css` | 6 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `frontend/src/lib/request-budget.ts` | 11 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `frontend/src/lib/status.test.ts` | 35 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `frontend/src/setup/SetupWizard.tsx` | 61,280,283,295 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `frontend/src/setup/wizard.test.tsx` | 53,62,63,64,78,90,121,122 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `hacs.json` | 1 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `mimir/CHANGELOG.md` | 3,5,10,23,58,63 | Apppfad nach wuschel; Namen/Distribution/Metadaten nach ADR 0022 |
| `mimir/DOCS.md` | 1,6,12,30,32 | Apppfad nach wuschel; Namen/Distribution/Metadaten nach ADR 0022 |
| `mimir/Dockerfile` | 25,36 | Apppfad nach wuschel; Namen/Distribution/Metadaten nach ADR 0022 |
| `mimir/config.yaml` | 1,3,4,5,22,26,27 | Apppfad nach wuschel; Namen/Distribution/Metadaten nach ADR 0022 |
| `mimir/rootfs/entrypoint.sh` | 8 | Apppfad nach wuschel; Namen/Distribution/Metadaten nach ADR 0022 |
| `pyproject.toml` | 2,8,15,29,52,56 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `repository.yaml` | 1,2 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |
| `src/core_contracts/__init__.py` | 1 | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/adapters/__init__.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/adapters/ha.py` | 149,168,450,479,487,534 | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/adapters/mqtt.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/api.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/app.py` | 262,390 | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/calendar_cache.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/calendar_inputs.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/capabilities.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/clock.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/declarative.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/declarative_models.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/editorial.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/engines.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/evidence.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/fusion.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/ha_context.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/history.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/identity.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/instance_parameters.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/lifecycle.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/manual_restart.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/manual_source.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/model.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/multibucket.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/notifications.py` | 131,148 | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/persistence.py` | 272 | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/producer.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/provision.py` | 84,108 | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/quality.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/refresh_plan.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/registry.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/resolver.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/resources/de.json` | 214,223,224 | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/retention.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/runtime.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/schema.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/security.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/sensor_profile.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/service_jobs.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/setup.py` | 79,80,96,102,105,113,126,214,222,245,355,357 | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/statemachine.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/temporal.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/testing/__init__.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/testing/contract_types/__init__.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/testing/contract_types/evaluate.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/text_rules.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/user_text.py` | 14 | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/validation.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `src/core_contracts/value_origin.py` | nur Pfad | Importpfad erhalten; Produkttexte/Domain/Distribution/IDs gezielt ersetzen |
| `tests/conftest.py` | 5,6,7,8 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_alpha4_acceptance.py` | 8,10,11,12,13,14 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_alpha4_delta2.py` | 10,11,12,13,14,15,16,17 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_alpha4_review.py` | 12,13,14,15,16,17,18,19,20,21,22,23 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_alpha6.py` | 7,8,92,100,114,115,124,125,198 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_alpha6_ux12.py` | 8 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_alpha7_discovery.py` | 8,78 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_alpha7_manual_restart.py` | 9,10,11,12 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_alpha7_post1.py` | 7,21 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_alpha7_source_migration.py` | 7 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_alpha8_platform.py` | 1,2 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_alpha9_calendar.py` | 5,6,7 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_alpha9_context.py` | 7,8,9,10,11,12,13,14,15 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_alpha9_deadlines.py` | 8,9,10,11,12,13 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_alpha9_editorial.py` | 5,6 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_alpha9_manual_source.py` | 7 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_alpha9_notifications.py` | 4,5,6,71,73,75,81 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_alpha9_refresh.py` | 5 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_alpha9_sensor_origin.py` | 6,7,8,9,10,285,286 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_alpha9_service_channel.py` | 11,12,152,164 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_backup.py` | 8,9,10,11 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_bootstrap.py` | 1,5,12 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_bridge_kernel.py` | 18,19,20,69,100 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_calendar_inputs.py` | 5,6,7,8,9 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_configuration_completeness.py` | 1,2,3 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_core.py` | 6,7,8,9,10,11,12 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_declarative.py` | 8,9,10,11,12,13,71,94,217,218,219,249,250,361,447,628 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_delta_review.py` | 11,12,13,14,15 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_image_distribution.py` | 45,57,58,60,62,115,127,130 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_instance_parameters.py` | 5,6,7,8 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_measurement_ordering.py` | 7,8 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_mqtt_integration.py` | 14,15,16,17,18 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_multibucket.py` | 5,6,7,91 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_named_formulas.py` | 5,6,7,14 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_partial_evaluation.py` | 3,4 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_phase1a.py` | 13,15,16,17,18,19,20,21,22,23,24,25,26,729,772,828 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_postgres.py` | 13,14,15,16,136,306,307 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_provision.py` | 7,26 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_remediation.py` | 14,16,17,18,19,20,21,22,23,24,25,26,417,420,538,673,674,722 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_restore.py` | 5,6,7,8 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_retention.py` | 5,6 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_retention_postgres.py` | 5,6,7,8,9,10 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_runtime.py` | 7,8,9,10,11 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_scope_packaging.py` | 8,9,65,103,109,111,112,117,124,130 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_setup.py` | 10,11,12,13,14,266,332,333,342,343,359,388,389,396,405 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_setup_postgres.py` | 13,14,15,16 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_startup_lifecycle.py` | 14,15,45,136 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_text_rules.py` | 3,4 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_transports.py` | 8,10,11,12,13,14,176,177,181,291 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_version_lifecycle.py` | 5 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_version_lines.py` | 32,33,34,39,44,45,46,51,53,54,55,58,61,63,64,65,66 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_workbench_api.py` | 10,11,12,13,14,15,16,315 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `tests/test_workbench_ci_lifecycle.py` | 49,65 | Technische Imports behalten; aktuelle Namens-/Pfad-Erwartungen anpassen |
| `uv.lock` | 236 | Aktive Produktnamen/Pfade/URLs gemäß ADR 0022; technische APIs erhalten |

## A2-Abschlusssuche

Aktuelle Produktionsquellen unter `src`, `custom_components/traber` und
`frontend/src` erneut nach `mimir|bifrost|bifröst|terra` (ohne Beachtung der
Großschreibung) durchsucht. Backend und Traber: keine Treffer. Im Frontend
verbleiben ausschließlich die unten erklärten technischen Kennungen,
Regressionsmuster und Teilwörter im eingebundenen MDI-Symbolkatalog.
Sichtbares deutsches Wörterbuch separat mit Regression geprüft; keine alten
Produktnamen. Befehlsherkunft heißt jetzt `wuschel-workbench`.
Historische Dokumente und der geschützte Terra-Store bleiben separat erhalten.

| Datei | Zeile am Prüfstand | Einordnung |
|---|---:|---|
| `frontend/src/alpha10.test.tsx` | 60 | Regression: alte Wörter ausdrücklich abweisen bzw. technische Bestandskennung prüfen |
| `frontend/src/alpha9/retention-readiness.test.tsx` | 71 | Regression: alte Wörter ausdrücklich abweisen bzw. technische Bestandskennung prüfen |
| `frontend/src/assets/mdi/02.json` | 1 | MDI-Symbolkatalog: Teilwörter wie Terrain, kein Produktname |
| `frontend/src/assets/mdi/23.json` | 1 | MDI-Symbolkatalog: Teilwörter wie Terrain, kein Produktname |
| `frontend/src/components/PageLoading.tsx` | 6 | Interner Übersetzungsschlüssel; sichtbarer Wert ist Wuschel |
| `frontend/src/components/PanelLayout.tsx` | 11 | Interner Graph-/Browser-Speicherschlüssel; kein sichtbarer Produktname |
| `frontend/src/components/RouteError.tsx` | 13 | Interner Übersetzungsschlüssel; sichtbarer Wert ist Wuschel |
| `frontend/src/components/Shell.tsx` | 63 | Interner Übersetzungsschlüssel; sichtbarer Wert ist Wuschel |
| `frontend/src/features/authoring/WorkingDocument.tsx` | 76 | Interner Graph-/Browser-Speicherschlüssel; kein sichtbarer Produktname |
| `frontend/src/features/graph/GraphPage.tsx` | 70 | Interner Graph-/Browser-Speicherschlüssel; kein sichtbarer Produktname |
| `frontend/src/features/graph/GraphPage.tsx` | 85 | Interner Graph-/Browser-Speicherschlüssel; kein sichtbarer Produktname |
| `frontend/src/features/sources/useSourceSelection.ts` | 14 | Interner Graph-/Browser-Speicherschlüssel; kein sichtbarer Produktname |
| `frontend/src/features/sources/useSourceSelection.ts` | 16 | Interner Graph-/Browser-Speicherschlüssel; kein sichtbarer Produktname |
| `frontend/src/i18n/de.json` | 400 | Interner Übersetzungsschlüssel; sichtbarer Wert ist Wuschel |
| `frontend/src/i18n/de.json` | 452 | Interner Übersetzungsschlüssel; sichtbarer Wert ist Wuschel |
| `frontend/src/lib/request-budget.ts` | 11 | Interner Graph-/Browser-Speicherschlüssel; kein sichtbarer Produktname |
