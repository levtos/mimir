import { useState } from 'react';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, expect, it } from 'vitest';
import { CalendarFields, calendarDefaults, planCalendar, validCalendarSettings } from './CalendarSourceDialog';

describe('calendar source form', () => {
  it('creates a typed calendar source and matching freshness in a schema-2 draft', () => {
    const original = { config_schema_version: 1, sources: [], bindings: [], dependencies: [], contracts: [], catalogs: [] };
    const result = planCalendar(original, 'calendar.familie', 'Familie', calendarDefaults);
    expect(original.sources).toEqual([]);
    expect(result.config.config_schema_version).toBe(2);
    expect(result.config.sources[0]).toMatchObject({ display_name: 'Familie', source_origin: 'local', value_schema: { type: 'object' }, freshness: { mode: 'periodic_ttl', interval_s: 3600 } });
    expect(result.config.bindings[0]).toMatchObject({ adapter: { kind: 'ha_calendar', ha_entity_id: 'calendar.familie', refresh_s: 900, max_age_s: 3600 } });
    expect(() => planCalendar(result.config, 'calendar.familie', 'Familie', calendarDefaults)).toThrow();
  });

  it('edits day windows and minute durations without a JSON input', async () => {
    function Harness() {
      const [value, setValue] = useState(calendarDefaults);
      return <><CalendarFields value={value} onChange={setValue} /><button disabled={!validCalendarSettings(value)}>Speichern</button></>;
    }
    const user = userEvent.setup(); render(<Harness />);
    const validity = screen.getByLabelText('Ohne neue Antwort gültig für (Minuten)');
    await user.clear(validity); await user.type(validity, '5');
    expect(screen.getByRole('button', { name: 'Speichern' })).toBeDisabled();
    await user.clear(validity); await user.type(validity, '30');
    expect(screen.getByRole('button', { name: 'Speichern' })).toBeEnabled();
    expect(screen.queryByRole('textbox')).not.toBeInTheDocument();
  });
});
