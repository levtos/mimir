import { useState } from 'react';
import { t } from '@/i18n';
import { Button } from '@/components/ui/button';
import { Field, Input } from '@/components/ui/form';
import { Switch } from '@/components/ui/controls';
import { PageHeader, Panel, PanelHeader } from '@/components/ui/layout';
import { CreateDraftDialog } from '@/features/authoring/CreateDraftDialog';
import { SecondsField } from '@/components/SecondsField';
import { useWorkingDocument } from '@/features/authoring/WorkingDocument';
import { useAuthoringSource } from '@/features/authoring/useAuthoringSource';
import { asObject } from '@/features/authoring/model';
import { describeError } from '@/lib/api';
import type { JsonObject } from '@/lib/json';

export function noticeSettings(config: JsonObject | null) {
  const notices = asObject(config?.notifications);
  return { ...notices, signal: { enabled: true, debounce_s: 30, clear_after_s: 10, min_update_s: 300, ...asObject(notices.signal) },
    configuration: { enabled: false, debounce_s: 60, clear_after_s: 10, min_update_s: 300, ...asObject(notices.configuration) }, max_items: notices.max_items ?? 10 };
}
export default function NotificationsPage() {
  const doc = useWorkingDocument(); const source = useAuthoringSource();
  const [creating, setCreating] = useState(false);
  const [busy, setBusy] = useState(false); const [error, setError] = useState('');
  const settings = noticeSettings(source.config);
  const change = (value: JsonObject) => doc.edit(current => ({ ...current, config_schema_version: Math.max(2, Number(current.config_schema_version ?? 1)), notifications: value }));
  const save = async () => {
    if (!source.editable) { if (doc.draft) doc.setEditing(true); else setCreating(true); return; }
    setBusy(true); setError('');
    try {
      await doc.editAndSave(current => ({ ...current, config_schema_version: Math.max(2, Number(current.config_schema_version ?? 1)), notifications: noticeSettings(current) }));
    } catch (failure) { setError(describeError(failure)); } finally { setBusy(false); }
  };
  return <>
    <PageHeader title={t('alpha9.notifications.title')} description={t('alpha9.notifications.description')} actions={<Button variant="primary" disabled={busy || source.loading || doc.saving} onClick={() => void save()}>{t('alpha9.actions.saveDraft')}</Button>} />
    <fieldset disabled={!source.editable || busy || doc.saving} className="space-y-4">
      {(['signal', 'configuration'] as const).map(axis => <Panel key={axis}><PanelHeader title={t(`alpha9.notifications.${axis}`)} /><div className="space-y-4 p-4">
        <Switch label={t(`alpha9.notifications.${axis}`)} checked={Boolean(settings[axis].enabled)} disabled={!source.editable || busy} onCheckedChange={enabled => change({ ...settings, [axis]: { ...settings[axis], enabled } })} />
        {axis === 'configuration' && <p className="text-sm text-muted">{t('alpha9.notifications.configurationHelp')}</p>}
        <div className="grid gap-4 sm:grid-cols-3">{([
          ['debounce_s', 'delay'], ['clear_after_s', 'clearDelay'], ['min_update_s', 'updateDelay'],
        ] as const).map(([key, label]) => <SecondsField key={key} label={t(`alpha9.notifications.${label}`)} value={Number(settings[axis][key])} onChange={value => change({ ...settings, [axis]: { ...settings[axis], [key]: value } })} />)}</div>
      </div></Panel>)}
      <Field label={t('alpha9.notifications.maxItems')}>{props => <Input {...props} type="number" min={1} max={10} step={1} value={Number(settings.max_items)} onChange={event => change({ ...settings, max_items: event.target.value === '' ? 0 : event.target.valueAsNumber })} />}</Field>
    </fieldset>
    <p className="mt-4 text-sm text-muted">{t('alpha8.parameters.draftHint')}</p>
    <Panel className="mt-4"><PanelHeader title={t('alpha9.notifications.preview')} /><div className="space-y-3 p-4 text-sm"><p>{t('alpha9.notifications.signalTitle')}</p><p>{t('alpha9.notifications.signalSummary', { count: 3 })}</p><p>{t('alpha9.notifications.configTitle')}</p><p>{t('alpha9.notifications.configSummary', { count: 2 })}</p></div></Panel>
    {error && <p role="alert" className="mt-4 text-bad">{error}</p>}
    <CreateDraftDialog open={creating} onOpenChange={setCreating} />
  </>;
}
