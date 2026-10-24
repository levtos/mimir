import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { act, render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { MemoryRouter } from 'react-router';
import { expect, it, vi } from 'vitest';
import { ReviewDraftButton } from '@/features/authoring/DraftBar';
import { WorkingDocumentProvider, useWorkingDocument } from '@/features/authoring/WorkingDocument';
import { installFakeApi, makeDraft, reply, sampleConfig } from '../../test/fakeApi';
import { clickReadyButton } from '../../test/gui';
import verdict from '../../test/fixtures/validate-ok.json';

it('retains the real review control across revalidation and clicks once only after it is ready', async () => {
  sessionStorage.clear(); localStorage.clear();
  const fake = installFakeApi({ drafts: [makeDraft('ready', sampleConfig())] });
  const user = userEvent.setup(); const reviewed = vi.fn();
  let validate!: () => Promise<void>;
  function Controls() {
    const doc = useWorkingDocument(); validate = doc.validateNow;
    return <><button onClick={() => doc.open(makeDraft('ready', sampleConfig()))}>Open</button><span>{doc.validation.state}</span><ReviewDraftButton onReview={reviewed} /></>;
  }
  render(<QueryClientProvider client={new QueryClient({ defaultOptions: { queries: { retry: false } } })}><MemoryRouter><WorkingDocumentProvider validateDebounceMs={5}><Controls /></WorkingDocumentProvider></MemoryRouter></QueryClientProvider>);
  await user.click(screen.getByRole('button', { name: 'Open' }));
  await screen.findByText('done');
  const found = await screen.findByRole('button', { name: 'Übernehmen' });
  let respond!: (response: Response) => void;
  fake.routes.push({ match: /^registry\/validate$/, respond: () => new Promise(resolve => { respond = resolve; }) });
  await act(async () => { void validate(); });
  await waitFor(() => expect(respond).toBeDefined());
  // This is the previous E2E's exact false assumption: a successful find does
  // not guarantee that the next label lookup will still match during checking.
  expect(() => screen.getByRole('button', { name: 'Übernehmen' })).toThrow();
  expect(screen.getByRole('button', { name: 'Wird geprüft …' })).toBe(found);
  expect(found).toBeDisabled();
  const click = clickReadyButton(user, found, 'Übernehmen');
  expect(reviewed).not.toHaveBeenCalled();
  await act(async () => { respond(reply(200, verdict)); });
  await click;
  await waitFor(() => expect(reviewed).toHaveBeenCalledExactlyOnceWith(expect.objectContaining({ draft_id: 'ready' })));
  expect(fake.calls.filter(call => call.method === 'GET' && call.path === 'registry/drafts/ready')).toHaveLength(1);
});
