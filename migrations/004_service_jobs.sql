-- Current bounded external work and calendar cache; time supplied by Clock.
CREATE TABLE service_job (key text PRIMARY KEY, payload jsonb NOT NULL);
CREATE TABLE service_state (key text PRIMARY KEY, payload jsonb NOT NULL);
