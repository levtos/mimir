import { useState } from 'react';
import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router';
import userEvent from '@testing-library/user-event';
import { expect, it } from 'vitest';
import type { JsonObject } from '@/lib/json';
import { RefreshPlanEditor } from './RefreshPlanEditor';

it('chooses a canonical trigger and supported sources with bounded times and minute hints', async () => {
  let current: JsonObject | null = null;
  function Harness() {
    const [value, setValue] = useState<JsonObject | null>(null);
    return <RefreshPlanEditor value={value} onChange={next => { current = next ?? null; setValue(current); }} references={[{ value: 'example.trigger.value', kind: 'contract', label: 'Abfrage gewünscht', schema: { type: 'bool', required: true, physical_state: false } }]} sources={[{ id: 'source.phone', name: 'Handy', profile: 'companion_location' }, { id: 'source.unsupported', name: 'Andere Quelle' }]} />;
  }
  const user = userEvent.setup(); render(<MemoryRouter><Harness /></MemoryRouter>);
  await user.click(screen.getByRole('switch', { name: 'Quellen erneut abfragen' }));
  expect(current).toMatchObject({ trigger_ref: 'example.trigger.value', attempt_offsets_s: [0, 10, 30] });
  expect(screen.getByRole('checkbox', { name: 'Andere Quelle' })).toHaveAttribute('aria-disabled', 'true');
  await user.click(screen.getByRole('checkbox', { name: 'Andere Quelle' }));
  expect(current).toMatchObject({ targets: [] });
  await user.click(screen.getByRole('checkbox', { name: 'Handy' }));
  expect(current).toMatchObject({ targets: ['source.phone'], attempt_offsets_s: [0, 60, 120], window_s: 180 });
  expect(screen.getAllByText('= 1 Minute').length).toBeGreaterThan(0);
  expect(screen.queryByRole('textbox')).not.toBeInTheDocument();
  expect(screen.getAllByRole('spinbutton')[0]).toBeDisabled();
  await user.click(screen.getByRole('switch', { name: 'Quellen erneut abfragen' }));
  expect(current).toBeNull();
});
