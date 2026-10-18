import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { beforeEach, expect, it, vi } from 'vitest';
import { t } from '@/i18n';
import { newFieldSchema } from '@/features/authoring/model';
import { planManual } from './ManualSourceDialog';
import { ManualSourcePanel } from './ManualSourcePanel';

const mocks = vi.hoisted(() => ({ api: vi.fn() }));
vi.mock('@/lib/api', async importOriginal => ({ ...await importOriginal<typeof import('@/lib/api')>(), api: mocks.api }));
vi.mock('@/lib/queries', () => ({ useActiveRevision: () => ({ data: { revision: 9, config: { sources: [{ source_id: 'source.manual', origin: 'manual', value_schema: { type: 'bool' }, freshness: { mode: 'event_stateful' } }], contracts: [{ contract_id: 'example.use', enabled: true, inputs: [{ ref: 'source.manual' }] }] } } }) }));

beforeEach(() => { mocks.api.mockReset(); });

it('adds an explicit typed manual source and transport-free binding to the draft', () => {
  const original = { sources: [], bindings: [], dependencies: [] };
  const planned = planManual(original, 'Eigene Angabe', newFieldSchema('bool'), 300, false);
  expect(original.sources).toHaveLength(0);
  expect(planned.config.sources[0]).toMatchObject({ origin: 'manual', freshness: { mode: 'periodic_ttl', interval_s: 300 } });
  expect(planned.config.bindings[0]).toMatchObject({ adapter: { kind: 'manual' } });
  expect(planned.config.config_schema_version).toBe(2);
});

it('requires explicit unbounded confirmation and reads a lost reply before another input', async () => {
  mocks.api.mockImplementation(async (path: string, init?: { method: string }) => {
    if (path.startsWith('evidence/')) return [];
    if (init?.method === 'POST') throw new TypeError('lost reply');
    return { status: 'accepted' };
  });
  render(<QueryClientProvider client={new QueryClient({ defaultOptions: { queries: { retry: false } } })}><ManualSourcePanel sourceId="source.manual" /></QueryClientProvider>);
  const user = userEvent.setup();
  const button = await screen.findByRole('button', { name: t('alpha9.manual.enter') });
  expect(button).toBeDisabled();
  await user.click(screen.getByRole('checkbox', { name: t('alpha9.manual.unboundedConfirm') }));
  await user.selectOptions(screen.getByLabelText(t('alpha9.manual.value')), 'true');
  await user.click(button);
  expect(await screen.findByText(t('alpha9.manual.unknownResult'))).toBeInTheDocument();
  expect(button).toBeDisabled();
  const writes = mocks.api.mock.calls.filter(([, init]) => init?.method === 'POST');
  expect(writes).toHaveLength(1);
  expect(writes[0]![1].body).toMatchObject({ value: true, expected_active_revision: 9, confirm_unbounded: true });
  await user.click(screen.getByRole('button', { name: t('alpha9.manual.checkResult') }));
  expect(await screen.findByText(t('alpha9.manual.recorded'))).toBeInTheDocument();
  expect(mocks.api.mock.calls.filter(([, init]) => init?.method === 'POST')).toHaveLength(1);
});
