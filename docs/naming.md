# Namen und Zuständigkeiten

| Name | Aufgabe |
|---|---|
| Wuschel | Core Contracts, eigenständige App |
| Traber | HA-Bridge, reiner Transport, Domain `traber` |
| Yggdrasil | Proxmox-Anzeigename; Hostname `einhornstation` bleibt |
| Midgard | Home Assistant Benni |
| Vanaheim | Home Assistant Eltern, eigene Wuschel-Installation, eigene DB/Rolle/ID/Tokens |
| Heimdall | Anwesenheit |
| Frey | Klima |
| Sol | Licht und Rollos |
| Mani | Schlafen und Wecken |
| Bragi | Medien |
| Hugin, Munin, Sleipnir, Odin | Reserve |

Producer liefern Zustände und Evidence ein. Policies entscheiden Handlungen;
Apply führt sie aus. Diese Rollen bleiben getrennt. Wuschel hat keine Core-Profile
(APP-01 und [Profil-Delta-Audit](audits/profile-delta-audit-2026-10-07.md)).
Technische Python-Importnamen und Contract-IDs bleiben stabil.

Die neue App liegt unter `wuschel/`, Slug `wuschel`, Images
`ghcr.io/levtos/{arch}-wuschel`. `core_contracts/config.yaml` bleibt als unveränderter
Terra-App-Store-Eintrag erhalten; neue Builds und Veröffentlichungen betreffen Wuschel.
Terra, alte Bridge und Legacy bleiben bis zu Bennis Abnahme installiert.
Installation, Supervisor-Weiterleitung und gegebenenfalls Ergänzung der neuen
Repo-URL im Store werden erst in Teil B geprüft, ohne den Terra-Eintrag zu entfernen.
