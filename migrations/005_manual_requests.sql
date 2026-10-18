-- Repeat-safe manual input results are append-only, not a growing runtime cache.
CREATE TABLE manual_request (key text PRIMARY KEY, payload jsonb NOT NULL);
