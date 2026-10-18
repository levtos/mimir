import { useEffect, useState } from 'react';
import { t } from '@/i18n';
import { Button } from '@/components/ui/button';
import { Field, Input } from '@/components/ui/form';
import { Collapsible } from '@/components/ui/controls';
import { PageHeader, Panel, Spinner } from '@/components/ui/layout';
import { SecondsField } from '@/components/SecondsField';
import { CreateDraftDialog } from '@/features/authoring/CreateDraftDialog';
import { useWorkingDocument } from '@/features/authoring/WorkingDocument';
import { useAuthoringSource } from '@/features/authoring/useAuthoringSource';
import { asObject } from '@/features/authoring/model';
import { describeError } from '@/lib/api';

export default function RetentionPage() {
  const doc = useWorkingDocument(); const src = useAuthoringSource();
  const original = JSON.stringify(asObject(src.config?.history_retention));
  const [values, setValues] = useState({ raw_days: 7, rollup_days: 730, batch_size: 1000, interval_s: 3600 });
  const [busy, setBusy] = useState(false); const [error, setError] = useState(''); const [saved, setSaved] = useState(false); const [creating, setCreating] = useState(false);
  useEffect(() => {
    const policy = JSON.parse(original) as Partial<typeof values>;
    setValues({ raw_days: policy.raw_days ?? 7, rollup_days: policy.rollup_days ?? 730, batch_size: policy.batch_size ?? 1000, interval_s: policy.interval_s ?? 3600 });
    setError('');
  }, [original, doc.draft?.draft_id, src.source]);
  useEffect(() => { setSaved(false); }, [doc.draft?.draft_id, src.source]);
  const rawError = !Number.isInteger(values.raw_days) || values.raw_days < 1 || values.raw_days > 3650;
  const rollupError = !Number.isInteger(values.rollup_days) || values.rollup_days < 1 || values.rollup_days > 36500;
  const relationError = !rawError && !rollupError && values.rollup_days < values.raw_days;
  const advancedError = !Number.isInteger(values.batch_size) || values.batch_size < 1 || values.batch_size > 10000 || !Number.isInteger(values.interval_s) || values.interval_s < 60 || values.interval_s > 86400;
  const invalid = rawError || rollupError || relationError || advancedError;
  const save = async () => {
    if (!src.editable) {
      if (doc.draft) doc.setEditing(true); else setCreating(true);
      return;
    }
    setBusy(true); setError(''); setSaved(false);
    try { await doc.editAndSave(current => ({ ...current, history_retention: { ...asObject(current.history_retention), ...values } })); setSaved(true); }
    catch (failure) { setError(describeError(failure)); }
    finally { setBusy(false); }
  };
  const change = (key: keyof typeof values, value: number) => { setValues(current => ({ ...current, [key]: value })); setSaved(false); };
  return <>
    <PageHeader title={t('alpha9.retention.title')} description={t('alpha9.retention.description')} actions={<Button variant="primary" disabled={busy || src.loading || doc.saving || src.editable && invalid} onClick={() => void save()}>{t('alpha9.retention.save')}</Button>} />
    {src.loading ? <Spinner /> : <Panel className="max-w-4xl space-y-5 p-5">
      {!src.config?.history_retention && <p className="text-sm text-muted">{t('alpha9.retention.suggestion')}</p>}
      {!src.editable && <p className="text-sm text-muted">{t('alpha9.retention.startDraft')}</p>}
      <fieldset disabled={!src.editable || busy || doc.saving} className="space-y-5">
        <div className="grid gap-5 sm:grid-cols-2">
          <Field label={t('alpha9.retention.rawDays')} hint={t('alpha9.retention.rawHelp')} errors={rawError ? [{ code: 'range', message: t('alpha9.retention.rawRange') }] : []}>{props => <Input {...props} type="number" min={1} max={3650} step={1} value={values.raw_days} onChange={event => change('raw_days', event.target.value === '' ? 0 : event.target.valueAsNumber)} />}</Field>
          <Field label={t('alpha9.retention.rollupDays')} hint={t('alpha9.retention.rollupHelp')} errors={rollupError ? [{ code: 'range', message: t('alpha9.retention.rollupRange') }] : relationError ? [{ code: 'relation', message: t('alpha9.retention.relationError') }] : []}>{props => <Input {...props} type="number" min={1} max={36500} step={1} value={values.rollup_days} onChange={event => change('rollup_days', event.target.value === '' ? 0 : event.target.valueAsNumber)} />}</Field>
        </div>
        <Collapsible title={t('alpha7.contract.advanced')}><div className="grid gap-5 sm:grid-cols-2">
          <Field label={t('alpha9.retention.batch')}>{props => <Input {...props} type="number" min={1} max={10000} step={1} value={values.batch_size} onChange={event => change('batch_size', event.target.value === '' ? 0 : event.target.valueAsNumber)} />}</Field>
          <SecondsField label={t('alpha9.retention.interval')} min={60} max={86400} value={values.interval_s} onChange={value => change('interval_s', value)} />
        </div>{advancedError && <p role="alert" className="mt-3 text-sm text-bad">{t('alpha9.retention.advancedError')}</p>}</Collapsible>
      </fieldset>
      <p className="text-sm text-muted">{t('alpha9.retention.deleteEffect')}</p>
    </Panel>}
    {saved && <p role="status" className="mt-4 text-sm text-ok">{t('alpha9.retention.pending')}</p>}
    {error && <p role="alert" className="mt-4 text-sm text-bad">{error}</p>}
    <CreateDraftDialog open={creating} onOpenChange={setCreating} />
  </>;
}
