import { t } from '@/i18n';
import { Link } from 'react-router';
import { Button } from '@/components/ui/button';
import { Switch, Checkbox } from '@/components/ui/controls';
import { Field, Select } from '@/components/ui/form';
import { SecondsField } from '@/components/SecondsField';
import type { RefOption } from '@/features/authoring/catalog';
import { asArray, asObject, str } from '@/features/authoring/model';
import type { JsonObject } from '@/lib/json';

export interface RefreshSource { id: string; name: string; profile?: string; bindingIndex?: number }
export function RefreshPlanEditor({ value, onChange, references, sources }: { value: JsonObject | null; onChange: (value: JsonObject | undefined) => void; references: RefOption[]; sources: RefreshSource[] }) {
  const refs = references.filter(reference => reference.kind === 'contract' && reference.schema?.type === 'bool');
  const plan = value ?? { trigger_ref: refs[0]?.value ?? '', targets: [], attempt_offsets_s: [0, 10, 30], window_s: 60, cooldown_s: 120 };
  const targets = asArray(plan.targets).map(String); const offsets = asArray(plan.attempt_offsets_s).map(Number);
  const minimum = sources.some(item => targets.includes(item.id) && item.profile === 'companion_location') ? 60 : 10;
  const chooseTarget = (source: RefreshSource, enabled: boolean) => {
    const nextTargets = enabled ? [...targets, source.id] : targets.filter(id => id !== source.id);
    const minimum = sources.some(item => nextTargets.includes(item.id) && item.profile === 'companion_location') ? 60 : 10;
    const nextOffsets = offsets.map((offset, index) => index === 0 ? 0 : Math.max(offset, index*minimum));
    const window = Math.min(300, Math.max(Number(plan.window_s), (nextOffsets.at(-1) ?? 0)+minimum));
    onChange({ ...plan, targets: nextTargets, attempt_offsets_s: nextOffsets, window_s: window, cooldown_s: Math.max(Number(plan.cooldown_s), window) });
  };
  const chooseRef = (label: string, selected: string, onSelected: (value: string) => void) => <Field label={label}>{props => <Select {...props} value={selected} onChange={event => onSelected(event.target.value)}><option value="">{t('alpha7.device.choose')}</option>{selected && !refs.some(ref => ref.value === selected) && <option value={selected}>{selected}</option>}{refs.map(ref => <option key={ref.value} value={ref.value}>{ref.label}</option>)}</Select>}</Field>;
  return <section className="space-y-3 border-t border-line pt-4">
    <Switch checked={value !== null} label={t('alpha9.refresh.title')} onCheckedChange={enabled => onChange(enabled ? plan : undefined)} />
    <p className="text-xs text-muted">{t('alpha9.refresh.help')}</p>
    {value && <>
      {chooseRef(t('alpha9.refresh.trigger'), str(plan.trigger_ref), trigger_ref => onChange({ ...plan, trigger_ref }))}
      <div className="space-y-2"><h3 className="text-sm font-medium">{t('alpha9.refresh.targets')}</h3>{sources.map(source => <div key={source.id} className="flex flex-wrap items-center gap-2"><Checkbox checked={targets.includes(source.id)} disabled={!source.profile} label={source.name} onCheckedChange={enabled => chooseTarget(source, enabled)} />{!source.profile && <span className="text-xs text-muted">{t('alpha9.refresh.unsupported')} {source.bindingIndex !== undefined && <Link className="underline" to={`/sources/bindings?item=${source.bindingIndex}`}>{t('alpha7.nav.bindings')}</Link>}</span>}</div>)}</div>
      <h3 className="text-sm font-medium">{t('alpha9.refresh.attempts')}</h3>
      <div className="space-y-2">{offsets.map((offset, index) => <div key={index} className="flex items-center gap-3"><SecondsField disabled={index === 0} label={t('alpha9.refresh.offset')} value={offset} max={299} onChange={next => onChange({ ...plan, attempt_offsets_s: offsets.map((item, position) => position === index ? next : item) })} />{index > 0 && <Button onClick={() => onChange({ ...plan, attempt_offsets_s: offsets.filter((_, position) => position !== index) })}>{t('editors.common.entfernen_382837')}</Button>}</div>)}</div>
      <Button disabled={offsets.length >= 5 || (offsets.at(-1) ?? 0)+minimum >= 300} onClick={() => {
        const next = (offsets.at(-1) ?? 0)+minimum; const window = Math.min(300, Math.max(Number(plan.window_s), next+minimum));
        onChange({ ...plan, attempt_offsets_s: [...offsets, next], window_s: window, cooldown_s: Math.max(Number(plan.cooldown_s), window) });
      }}>{t('editors.common.hinzufugen_cbb95c')}</Button>
      <div className="grid gap-3 sm:grid-cols-2"><SecondsField label={t('alpha9.refresh.window')} value={Number(plan.window_s)} min={1} max={300} onChange={window_s => onChange({ ...plan, window_s })} /><SecondsField label={t('alpha9.refresh.cooldown')} value={Number(plan.cooldown_s)} min={1} onChange={cooldown_s => onChange({ ...plan, cooldown_s })} /></div>
      {chooseRef(t('alpha9.refresh.stop'), str(asObject(plan.stop_when).ref)+(asObject(plan.stop_when).field ? `.${str(asObject(plan.stop_when).field)}` : ''), ref => {
        const next = { ...plan }; if (ref) next.stop_when = { ref }; else delete next.stop_when; onChange(next);
      })}
    </>}
  </section>;
}
