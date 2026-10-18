import { useState } from 'react';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { expect, it } from 'vitest';
import { MachineDeadlinesEditor } from './MachineDeadlinesEditor';
import { withMinimumLanguage } from '@/features/authoring/model';
import { t } from '@/i18n';
import type { JsonObject } from '@/lib/json';

it('edits state durations and a typed absolute input without rewriting old definitions on load', async () => {
  const old = { language_version: 2, machine: { deadline_s: 120 } };
  expect(withMinimumLanguage(old)).toBe(old);
  function Harness() {
    const [value, setValue] = useState<JsonObject>({ states: ['a', 'b'], deadline_s: 120 });
    return <><MachineDeadlinesEditor value={value} onChange={setValue} definition={{ inputs: [{ name: 'planned', schema: { type: 'timestamp' } }], parameter_schema: { wait_s: { schema: { type: 'number' } } } }} /><output data-testid="machine">{JSON.stringify(value)}</output></>;
  }
  render(<Harness />);
  const user = userEvent.setup();
  await user.click(screen.getByRole('checkbox', { name: t('alpha9.deadline.unknown') }));
  expect(screen.getAllByText('= 2 Minuten')).toHaveLength(2);
  await user.selectOptions(screen.getByLabelText(t('alpha9.deadline.absolute')), 'planned');
  const machine = JSON.parse(screen.getByTestId('machine').textContent!);
  expect(machine.deadline_by_state.a.duration).toBe(120);
  expect(machine.absolute_transition).toEqual({ states: ['a'], target: 'b', at_input: 'planned', priority: 'absolute' });
  expect(withMinimumLanguage({ ...old, machine }).language_version).toBe(3);
});
