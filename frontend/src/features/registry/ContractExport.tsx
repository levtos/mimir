import { useState } from 'react';
import { t } from '@/i18n';
import { apiText, describeError } from '@/lib/api';
import { useActiveRevision } from '@/lib/queries';
import { useWorkingDocument } from '@/features/authoring/WorkingDocument';
import { downloadText } from '@/features/authoring/importExport';
import { Button } from '@/components/ui/button';
import { Dialog } from '@/components/ui/dialog';
import { Notice } from '@/components/ui/layout';

interface Package { config: Record<string, unknown>; manifest: { roots: string[] }; [key: string]: unknown }
export function ContractExport({ contractId, source }: { contractId: string; source: 'active' | 'draft' }) {
  const active = useActiveRevision(); const doc = useWorkingDocument();
  const [open, setOpen] = useState(false); const [data, setData] = useState<Package | null>(null); const [error, setError] = useState('');
  const [fileText, setFileText] = useState('');
  const load = async () => { setOpen(true); setData(null); setError(''); try {
    const text = await apiText('portable/export', { method: 'POST', body: { contract_id: contractId, expected_active_revision: active.data?.revision ?? 0,
      ...(source === 'draft' && doc.draft ? { draft_id: doc.draft.draft_id, draft_version: doc.draft.draft_version } : {}) } });
    setData(JSON.parse(text) as Package); setFileText(text);
  } catch (failure) { setError(describeError(failure)); } };
  return <>
    <Button size="sm" disabled={source === 'draft' && doc.dirty} disabledReason={t('alpha10.transfer.savedOnly')} onClick={() => void load()}>{t('alpha10.transfer.contractExport')}</Button>
    <Dialog open={open} onOpenChange={setOpen} title={t('alpha10.transfer.contractExport')} footer={<Button variant="primary" disabled={!data} onClick={() => { if (data) downloadText(`wuschel-${contractId}.json`, fileText); setOpen(false); }}>{t('alpha9.export.saveFile')}</Button>}>
      <p>{contractId} · {t(source === 'draft' ? 'alpha7.export.draft' : 'alpha7.export.active')}</p>
      {error && <Notice tone="bad">{error}</Notice>}
      {data && <ul className="my-4 space-y-1">{Object.entries(data.config).filter(([, value]) => Array.isArray(value)).map(([key, value]) => <li key={key}>{t(`alpha10.transfer.group.${key}`)}: {(value as unknown[]).length}</li>)}</ul>}
      <p>{t('alpha10.transfer.history')}</p>
    </Dialog>
  </>;
}
