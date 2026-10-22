import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { MemoryRouter, Route, Routes } from 'react-router';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { WorkingDocumentProvider } from '@/features/authoring/WorkingDocument';
import { ContinuationDialog } from '@/features/registry/ContinuationDialog';
import { CONTINUE, activateWithReceipt, currentDraft, draftState, type ActivationPreview } from '@/features/registry/authoring';
import { LiveProvider } from '@/lib/live-context';
import { countSentence, valueText } from '@/lib/valueText';
import type { FieldSchema } from '@/features/authoring/model';
import type { Draft } from '@/lib/types';
import DraftPage from '@/features/registry/DraftPage';
import { ActivateDialog } from '@/features/registry/ActivationDialogs';
import { t } from '@/i18n';
import { idleLive } from '../test/harness';
import { installFakeApi, makeDraft, reply, sampleConfig } from '../test/fakeApi';

function mount(ui: React.ReactNode) {
  return render(<QueryClientProvider client={new QueryClient({ defaultOptions: { queries: { retry: false } } })}><MemoryRouter initialEntries={['/changes/drafts/d1']}><LiveProvider store={idleLive()}><WorkingDocumentProvider validateDebounceMs={5}>{ui}</WorkingDocumentProvider></LiveProvider></MemoryRouter></QueryClientProvider>);
}

beforeEach(() => sessionStorage.clear());

describe('b3 UX-1, UX-2 and UX-5-09..12', () => {
  it('UX-1-04/06 shows a completed draft read-only and a stale draft with both bases', async () => {
    const draft = makeDraft('d1', sampleConfig(), { lifecycle: 'completed' });
    const fake = installFakeApi({ drafts: [draft] });
    fake.touchDraft('d1', { ...draft, completed_revision: 2 } as Partial<typeof draft>);
    mount(<Routes><Route path="/changes/drafts/:draftId" element={<DraftPage />} /></Routes>);
    expect(await screen.findByText('Erledigt · als Konfiguration 2 übernommen')).toBeVisible();
    expect(screen.queryByRole('textbox')).toBeNull();
    expect(screen.getByRole('button', { name: 'Konfiguration ansehen' })).toBeVisible();
    expect(sessionStorage.getItem('terra.workingDraft')).toBeNull();
    expect(draftState({ ...draft, lifecycle: 'open', base_revision: 1 }, 2)).toContain('Veraltet · Grundlage: Konfiguration 1 · Aktiv: Konfiguration 2');
    expect(currentDraft({ ...draft, lifecycle: 'open', base_status: 'needs_review' }, 0)).toBe(false);
  });

  it('UX-2-01 presents the exact continuation action without allowing old-content edits', async () => {
    const draft = makeDraft('d1', sampleConfig(), { base_revision: 1 });
    installFakeApi({ drafts: [draft], revisions: [{ revision: 2, config: sampleConfig(), checksum: 'sum', created_at: '2026-01-01T12:00:00Z' }] });
    mount(<Routes><Route path="/changes/drafts/:draftId" element={<DraftPage />} /></Routes>);
    expect(await screen.findByRole('button', { name: CONTINUE })).toBeVisible();
    expect(screen.getByLabelText('Name des Entwurfs')).toBeDisabled();
    expect(screen.queryByRole('button', { name: 'Übernehmen' })).toBeNull();
  });

  it('UX-2-05 no conflict choice is preselected; decisions bind all three digests', async () => {
    const user = userEvent.setup(); const draft = makeDraft('d1', sampleConfig());
    const fake = installFakeApi({ drafts: [draft] });
    const conflict = { path: '/sources/source.a/display_name', kind: 'property', base: 'Vorher', draft: 'Entwurf', current: 'Aktuell', digests: ['b', 'd', 'c'] };
    const session = { session_id: 'session', session_version: 1, expected_active_revision: 2, status: 'open', conflicts: [conflict], decisions: {} };
    fake.routes.push({ match: /\/continuations$/, respond: () => reply(200, session) });
    fake.routes.push({ match: /continuations\/session\/decisions$/, respond: () => reply(200, { ...session, session_version: 2, conflicts: [] }) });
    mount(<ContinuationDialog draft={draft as Draft} onClose={() => {}} />);
    const radios = await screen.findAllByRole('radio');
    expect(radios.every(r => !(r as HTMLInputElement).checked)).toBe(true);
    expect(screen.getByRole('button', { name: 'Auswahl bestätigen' })).toBeDisabled();
    await user.click(radios[0]!); await user.click(screen.getByRole('button', { name: 'Auswahl bestätigen' }));
    await screen.findByRole('button', { name: 'Entwurf fertigstellen' });
    expect(fake.calls.find(c => c.path.endsWith('/decisions'))?.body).toEqual({ session_version: 1, decisions: { [conflict.path]: { digests: ['b', 'd', 'c'], choice: 'draft' } } });
    expect(fake.activations).toHaveLength(0);
  });

  it('UX-1-09 resolves response loss from the exact request receipt', async () => {
    const fake = installFakeApi({ drafts: [makeDraft('d1', sampleConfig())] });
    const handle = fake.fetch.getMockImplementation() as (url: string, init?: RequestInit) => Promise<Response>;
    fake.fetch.mockImplementation(async (url: string, init?: RequestInit) => {
      const result = await handle(url, init);
      if (url.endsWith('/activate')) throw new TypeError('synthetic response loss');
      return result;
    });
    const uncertain = vi.fn();
    const preview: ActivationPreview = { expected_active_revision: 0, comparison_digest: 'd1:1:0', no_effect: false, required_confirmations: ['impact'], retention: { before: null, after: null, changed: false, shortening: [] } };
    const result = await activateWithReceipt(makeDraft('d1', sampleConfig()), preview, crypto.randomUUID(), '', false, uncertain);
    expect(result.revision).toBe(1); expect(uncertain).toHaveBeenCalledOnce(); expect(fake.activations).toHaveLength(1);
    expect(fake.calls.filter(c => c.path.endsWith('/activate'))).toHaveLength(1);
    await waitFor(() => expect(sessionStorage.getItem('wuschel.activation.d1')).toBeNull());
  });

  it('UX-5-12 translates declared states consistently while preserving free text and 0/1/n', () => {
    const schema = { type: 'enum', required: true, physical_state: true } as FieldSchema;
    expect(['closed', 'tilted', 'open', 'ready', 'starting', 'unavailable', 'unknown'].map(value => valueText(value, schema))).toEqual(['zu', 'gekippt', 'offen', 'bereit', 'startet', 'nicht erreichbar', 'unbekannt']);
    expect(valueText('open', { ...schema, type: 'text' })).toBe('open');
    expect(valueText('new_state', schema)).toBe('Unbekannter Zustand');
    expect(valueText('bereit', { ...schema, value_catalog: ['bereit', 'fertig'] })).toBe('bereit');
    expect([0, 1, 3].map(n => countSentence(n, 'changes'))).toEqual(['Keine Änderungen', 'Eine Änderung', '3 Änderungen']);
  });

  it('UX-2-09 keeps a recomparison session open even though it also contains a draft ID and candidate config', async () => {
    const user = userEvent.setup(); const draft = makeDraft('d1', sampleConfig());
    const fake = installFakeApi({ drafts: [draft] }); const close = vi.fn();
    const session = { session_id: 'synthetic-session', session_version: 1, draft_id: 'd1', config: draft.config, status: 'open', conflicts: [], decisions: {}, expected_active_revision: 2 };
    fake.routes.push({ match: /\/continuations$/, respond: () => reply(200, session) });
    fake.routes.push({ match: /\/finish$/, respond: () => reply(200, { ...session, session_version: 2, conflicts: [{ path: '/sources/source.a/display_name', base: 'B', draft: 'D', current: 'C', digests: ['b', 'd', 'c'], kind: 'property' }] }) });
    mount(<ContinuationDialog draft={draft} onClose={close} />);
    const finish = await screen.findByRole('button', { name: 'Entwurf fertigstellen' });
    await waitFor(() => expect(finish).toBeEnabled()); await user.click(finish);
    expect(await screen.findAllByRole('radio')).toHaveLength(2);
    expect(close).not.toHaveBeenCalled();
    expect(sessionStorage.getItem('wuschel.continuation.d1')).toBe('synthetic-session');
  });

  it('UX-2-10 cancels the server session explicitly while later-resume keeps it', async () => {
    const user = userEvent.setup(); const draft = makeDraft('d1', sampleConfig());
    const fake = installFakeApi({ drafts: [draft] }); const close = vi.fn();
    const session = { session_id: 'synthetic-session', session_version: 1, status: 'open', conflicts: [], decisions: {}, expected_active_revision: 0 };
    fake.routes.push({ match: /\/continuations$/, respond: () => reply(200, session) });
    fake.routes.push({ match: /\/cancel$/, respond: () => reply(200, { ...session, status: 'cancelled' }) });
    mount(<ContinuationDialog draft={draft} onClose={close} />);
    await waitFor(() => expect(screen.getByRole('button', { name: 'Entwurf fertigstellen' })).toBeEnabled());
    await user.click(screen.getByRole('button', { name: 'Abbrechen' }));
    await waitFor(() => expect(close).toHaveBeenCalledOnce());
    expect(fake.calls.find(c => c.path.endsWith('/cancel'))?.body).toEqual({ session_version: 1 });
    expect(fake.activations).toEqual([]);
    expect(sessionStorage.getItem('wuschel.continuation.d1')).toBeNull();
  });

  it('UX-1-09/2-10 resumes the original finished result after response loss', async () => {
    const draft = makeDraft('d1', sampleConfig()); const result = makeDraft('continued', sampleConfig());
    const fake = installFakeApi({ drafts: [draft, result] }); const close = vi.fn();
    sessionStorage.setItem('wuschel.continuation.d1', 'finished');
    fake.routes.push({ match: /continuations\/finished$/, respond: () => reply(200, { session_id: 'finished', status: 'completed', result }) });
    mount(<ContinuationDialog draft={draft} onClose={close} />);
    await waitFor(() => expect(close).toHaveBeenCalledOnce());
    expect(sessionStorage.getItem('wuschel.continuation.d1')).toBeNull();
    expect(sessionStorage.getItem('terra.workingDraft')).toBe('continued');
    expect(fake.calls.some(c => c.path.endsWith('/finish'))).toBe(false);
  });

  it.each([
    ['same', false, [], { raw_days: 30, rollup_days: 365 }, { raw_days: 30, rollup_days: 365 }],
    ['longer', true, [], { raw_days: 30, rollup_days: 365 }, { raw_days: 60, rollup_days: 365 }],
    ['shorter', true, ['raw_days'], { raw_days: 30, rollup_days: 365 }, { raw_days: 7, rollup_days: 365 }],
    ['mixed', true, ['raw_days'], { raw_days: 30, rollup_days: 365 }, { raw_days: 7, rollup_days: 730 }],
    ['operation', true, [], { raw_days: 30, rollup_days: 365, batch_size: 100 }, { raw_days: 30, rollup_days: 365, batch_size: 200 }],
  ] as const)('UX-5-09/10 renders the server retention comparison: %s', async (_case, changed, shortening, before, after) => {
    const draft = makeDraft('d1', sampleConfig()); const fake = installFakeApi({ drafts: [draft] });
    fake.routes.push({ match: /\/activation-preview$/, respond: () => reply(200, { expected_active_revision: 0, comparison_digest: 'fixture', no_effect: false, required_confirmations: ['impact', ...(shortening.length ? ['retention'] : [])], retention: { before, after, changed, shortening } }) });
    mount(<ActivateDialog draft={draft} open onOpenChange={() => {}} />);
    await screen.findByRole('checkbox', { name: /Auswirkungen geprüft/ });
    expect(!!screen.queryByText(t('beta3.5c8fb977482e'))).toBe(changed);
    expect(!!screen.queryByRole('checkbox', { name: t('beta3.525da4f813eb') })).toBe(!!shortening.length);
    if (_case === 'operation') expect(screen.getByText(t('b3.retentionOperation'))).toBeVisible();
  });
});
