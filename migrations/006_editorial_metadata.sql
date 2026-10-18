-- Organization is independent of all historical contract configurations.
CREATE TABLE editorial_current (key text PRIMARY KEY, payload jsonb NOT NULL);
CREATE TABLE editorial_draft (key text PRIMARY KEY, payload jsonb NOT NULL);
