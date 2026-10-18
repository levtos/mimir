import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, expect, it, vi } from 'vitest';
import type { JsonObject } from '@/lib/json';
import NotificationsPage from './NotificationsPage';

const mocks = vi.hoisted(() => ({ edit: vi.fn(), editAndSave: vi.fn().mockResolvedValue(undefined) }));
vi.mock('@/features/authoring/WorkingDocument', () => ({ useWorkingDocument: () => ({ ...mocks, saving: false }) }));
vi.mock('@/features/authoring/useAuthoringSource', () => ({ useAuthoringSource: () => ({ editable: true, loading: false, config: { config_schema_version: 1, sources: [], contracts: [] } }) }));

describe('notification settings', () => {
  it('shows separate axes, minute hints and a preview; edits only the working draft', async () => {
    const user = userEvent.setup(); render(<QueryClientProvider client={new QueryClient()}><NotificationsPage /></QueryClientProvider>);
    expect(screen.getByRole('heading', { level: 1, name: 'Benachrichtigungen' })).toBeInTheDocument();
    expect(screen.getAllByText('= 5 Minuten')).toHaveLength(2);
    expect(screen.getByText('So sieht der Hinweis aus. Es wird keine Nachricht gesendet.')).toBeInTheDocument();
    const delay = screen.getAllByLabelText('Erst melden, wenn das Problem so lange besteht (Sekunden)')[0]!;
    await user.clear(delay); await user.type(delay, '120');
    const update = mocks.edit.mock.lastCall![0] as (config: JsonObject) => JsonObject;
    expect(update({ config_schema_version: 1 })).toMatchObject({ config_schema_version: 2, notifications: { configuration: { enabled: false } } });
    await user.click(screen.getByRole('button', { name: 'Im Entwurf speichern' }));
    expect(mocks.editAndSave).toHaveBeenCalledOnce();
  });
});
