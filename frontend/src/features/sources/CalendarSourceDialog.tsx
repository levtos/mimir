import { useState } from 'react';
import { t } from '@/i18n';
import { Button } from '@/components/ui/button';
import { Dialog } from '@/components/ui/dialog';
import { Field, Input, Select } from '@/components/ui/form';
import { useWorkingDocument } from '@/features/authoring/WorkingDocument';
import { asArray, asObject, str, uniqueName } from '@/features/authoring/model';
import { clone, isObject, type JsonObject } from '@/lib/json';
import { describeError } from '@/lib/api';
import { useHaCatalog } from './useHaCatalog';

export interface CalendarSettings { past: number; future: number; refreshMinutes: number; validMinutes: number }
export const calendarDefaults: CalendarSettings = { past: 1, future: 14, refreshMinutes: 15, validMinutes: 60 };
export function validCalendarSettings(value: CalendarSettings) {
  return Object.values(value).every(Number.isInteger) && value.past >= 0 && value.future >= 1 && value.past + value.future <= 31 && value.refreshMinutes >= 1 && value.refreshMinutes <= 1440 && value.validMinutes >= value.refreshMinutes && value.validMinutes <= 10080;
}
export function planCalendar(config: JsonObject, entity: string, name: string, settings: CalendarSettings) {
  if (!/^calendar\.[a-z0-9_]+$/.test(entity) || !validCalendarSettings(settings)) throw new Error(t('alpha9.form.unavailable'));
  for (const key of ['sources', 'bindings', 'dependencies']) if (config[key] !== undefined && (!Array.isArray(config[key]) || !asArray(config[key]).every(isObject))) throw new Error(t('alpha9.form.unavailable'));
  const next = clone(config);
  const sources = asArray(next.sources).filter(isObject); const bindings = asArray(next.bindings).filter(isObject); const dependencies = asArray(next.dependencies).filter(isObject);
  if (bindings.some(binding => asObject(binding.adapter).kind === 'ha_calendar' && asObject(binding.adapter).ha_entity_id === entity)) throw new Error(t('alpha7.device.reused'));
  let dependency = dependencies.find(item => item.kind === 'ha' && item.monitor === 'internal');
  if (!dependency) { dependency = { dependency_id: uniqueName('dep.ha', dependencies.map(item => str(item.dependency_id))), kind: 'ha', monitor: 'internal' }; dependencies.push(dependency); }
  const sourceId = uniqueName(`source.${entity.replace('.', '_')}`, sources.map(item => str(item.source_id)));
  sources.push({ source_id: sourceId, source_type: 'state', source_origin: 'local', display_name: name,
    dependency_id: dependency.dependency_id!, physical_source_key: uniqueName(`physical.${entity.replace('.', '_')}`, sources.map(item => str(item.physical_source_key))),
    value_schema: { type: 'object', required: true, physical_state: false },
    freshness: { mode: 'periodic_ttl', interval_s: settings.validMinutes*60, future_tolerance_s: 0 } });
  bindings.push({ binding_id: uniqueName(`binding.${entity.replace('.', '_')}`, bindings.map(item => str(item.binding_id))), source_id: sourceId,
    adapter: { kind: 'ha_calendar', ha_entity_id: entity, window: { timezone: 'Europe/Berlin', past_days: settings.past, future_days: settings.future }, refresh_s: settings.refreshMinutes*60, max_age_s: settings.validMinutes*60 } });
  return { config: { ...next, config_schema_version: 2, sources, bindings, dependencies }, sourceIndex: sources.length-1 };
}

export function CalendarFields({ value, onChange }: { value: CalendarSettings; onChange: (value: CalendarSettings) => void }) {
  return <div className="grid gap-3 sm:grid-cols-2">{([
    ['past', 'alpha9.calendar.windowPast', 0, 30], ['future', 'alpha9.calendar.windowFuture', 1, 31],
    ['refreshMinutes', 'alpha9.calendar.refresh', 1, 1440], ['validMinutes', 'alpha9.calendar.validFor', 1, 10080],
  ] as const).map(([key, label, min, max]) => <Field key={key} label={t(label)}>{props => <Input {...props} type="number" min={min} max={max} step={1} value={Number.isFinite(value[key]) ? value[key] : ''} onChange={event => onChange({ ...value, [key]: event.target.valueAsNumber })} />}</Field>)}</div>;
}

export function CalendarSourceDialog({ open, onOpenChange, onAdded }: { open: boolean; onOpenChange: (open: boolean) => void; onAdded: (index: number) => void }) {
  const doc = useWorkingDocument(); const ha = useHaCatalog(open, true);
  const [entity, setEntity] = useState(''); const [name, setName] = useState(''); const [settings, setSettings] = useState(calendarDefaults);
  const [error, setError] = useState(''); const [busy, setBusy] = useState(false);
  const selected = ha.entities.find(item => item.entity_id === entity);
  const add = async () => {
    if (busy || !selected || !validCalendarSettings(settings)) return;
    setBusy(true); setError('');
    try {
      const current = await doc.ensureDraft(); const result = planCalendar(current, entity, name || selected.display_name, settings);
      doc.replaceAll(result.config); onOpenChange(false); onAdded(result.sourceIndex);
    } catch (failure) { setError(describeError(failure)); } finally { setBusy(false); }
  };
  return <Dialog open={open} onOpenChange={value => !busy && onOpenChange(value)} title={t('alpha9.calendar.add')} description={t('alpha7.device.explanation')} footer={<><Button disabled={busy} onClick={() => onOpenChange(false)}>{t('alpha7.device.cancel')}</Button><Button variant="primary" disabled={busy || !selected || !validCalendarSettings(settings)} onClick={() => void add()}>{t('alpha7.device.add')}</Button></>}>
    <div className="space-y-4">
      <Field label={t('alpha9.calendar.add')}>{props => <Select {...props} value={entity} onChange={event => { setEntity(event.target.value); setName(ha.entities.find(item => item.entity_id === event.target.value)?.display_name ?? ''); }}><option value="">{t('alpha7.device.selectFirst')}</option>{ha.entities.filter(item => item.entity_id.startsWith('calendar.')).map(item => <option key={item.entity_id} value={item.entity_id}>{item.display_name}</option>)}</Select>}</Field>
      {ha.isError && <p role="alert">{t('alpha7.device.unavailable')}</p>}
      <Field label={t('alpha7.device.name')}>{props => <Input {...props} value={name} maxLength={128} onChange={event => setName(event.target.value)} />}</Field>
      <CalendarFields value={settings} onChange={setSettings} />
      <p className="text-sm text-muted">{t('alpha8.parameters.draftHint')}</p>
      {error && <p role="alert">{error}</p>}
    </div>
  </Dialog>;
}
