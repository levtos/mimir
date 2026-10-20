-- Historical decisions are append-only; heads and sightings are projections.
CREATE TABLE catalog_content_revision (key text PRIMARY KEY, payload jsonb NOT NULL);
CREATE UNIQUE INDEX catalog_revision_identity ON catalog_content_revision ((payload->>'catalog'), (payload->>'revision'));
CREATE TABLE catalog_entry_revision (key text PRIMARY KEY, payload jsonb NOT NULL);
CREATE UNIQUE INDEX catalog_entry_identity ON catalog_entry_revision ((payload->>'catalog'), (payload->>'revision'), (payload->>'identity'));
CREATE TABLE catalog_head (key text PRIMARY KEY, payload jsonb NOT NULL);
CREATE TABLE catalog_sighting (key text PRIMARY KEY, payload jsonb NOT NULL);
CREATE TABLE catalog_request (key text PRIMARY KEY, payload jsonb NOT NULL);
CREATE TABLE catalog_import (key text PRIMARY KEY, payload jsonb NOT NULL);
