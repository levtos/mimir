CREATE TABLE activation_receipt (key text PRIMARY KEY, payload jsonb NOT NULL);
CREATE TABLE draft_continuation (key text PRIMARY KEY, payload jsonb NOT NULL);
CREATE TABLE registry_draft_version (key text PRIMARY KEY, payload jsonb NOT NULL);
