import { useState } from 'react';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { expect, it } from 'vitest';
import { t } from '@/i18n';
import { SourceQualityEditor } from './SourceQualityEditor';
import { ForecastValuesEditor, newForecastPoint } from './ValueOriginEditor';
import { asArray, newFieldSchema } from '@/features/authoring/model';
import type { Json, JsonObject } from '@/lib/json';

it('enables numeric checking explicitly and edits instance thresholds without a new profile version', async () => {
  function Harness() {
    const [value, setValue] = useState<JsonObject>({ source_id: 'source.example', value_schema: { type: 'number', unit: '°C' } });
    return <><SourceQualityEditor value={value} onChange={setValue} /><output data-testid="source">{JSON.stringify(value)}</output></>;
  }
  render(<Harness />); const user = userEvent.setup();
  await user.click(screen.getByRole('checkbox', { name: t('alpha9.sensor.profile') }));
  const input = screen.getByLabelText(t('alpha9.sensor.minReports'));
  await user.clear(input); await user.type(input, '12');
  const source = JSON.parse(screen.getByTestId('source').textContent!);
  expect(source.sensor_parameters.min_reports).toBe(12);
  expect(source.sensor_profile.version).toBe(1);
  expect(source.sensor_profile.stuck.min_reports).toEqual({ op: 'parameter', name: 'min_reports' });
});

it('does not suggest a constant-value defect for contacts', () => {
  render(<SourceQualityEditor value={{ source_type: 'boolean', value_schema: { type: 'bool' } }} onChange={() => {}} />);
  expect(screen.queryByRole('checkbox', { name: t('alpha9.sensor.profile') })).not.toBeInTheDocument();
});

it('edits forecast values and validity with ordinary fields', async () => {
  const schema = newFieldSchema('number'); const origin = { kind: 'forecast', provider: 'example' };
  function Harness() {
    const [value, setValue] = useState<Json>([newForecastPoint(schema, origin)]);
    return <><ForecastValuesEditor schema={schema} origin={origin} value={value} onChange={setValue} /><output data-testid="points">{JSON.stringify(value)}</output></>;
  }
  render(<Harness />); const user = userEvent.setup();
  expect(screen.getByLabelText(t('alpha9.valueOrigin.valid_from'))).toHaveAttribute('type', 'datetime-local');
  await user.click(screen.getByRole('button', { name: t('alpha9.valueOrigin.addPoint') }));
  const points = asArray(JSON.parse(screen.getByTestId('points').textContent!));
  expect(points).toHaveLength(2);
  expect(screen.getAllByLabelText(t('alpha9.valueOrigin.valid_until'))).toHaveLength(2);
});
