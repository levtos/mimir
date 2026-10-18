import { useState } from 'react';
import { t } from '@/i18n';
import { Checkbox } from '@/components/ui/controls';
import { Field, Select } from '@/components/ui/form';
import { asObject, str } from '@/features/authoring/model';
import type { JsonObject } from '@/lib/json';
import { useHaCatalog } from './useHaCatalog';

export function BindingRefreshEditor({ value, onChange }: { value: JsonObject; onChange: (value: JsonObject) => void }) {
  const [open, setOpen] = useState(false); const ha = useHaCatalog(open, true);
  const refresh = asObject(value.refresh); const adapter = asObject(value.adapter);
  const entity = ha.entities.find(item => item.entity_id === adapter.ha_entity_id);
  const profiles = entity?.refresh_profiles ?? [];
  const change = (next: JsonObject | undefined) => { const copy = { ...value }; if (next) copy.refresh = next; else delete copy.refresh; onChange(copy); };
  return <details onToggle={event => setOpen(event.currentTarget.open)} className="space-y-3 rounded border border-line p-3">
    <summary className="cursor-pointer text-sm font-medium">{t('alpha9.refresh.title')}</summary>
    <p className="my-3 text-xs text-muted">{t('alpha9.refresh.help')}</p>
    <Field label={t('alpha9.refresh.method')}>{props => <Select {...props} value={str(refresh.profile)} onChange={event => change(event.target.value ? { profile: event.target.value, permission_confirmed: false } : undefined)}><option value="">{t('editors.RegistryObjects.keine_db028e')}</option>{refresh.profile && !profiles.includes(str(refresh.profile)) && <option value={str(refresh.profile)}>{t(refresh.profile === 'companion_location' ? 'alpha9.refresh.companion' : 'alpha9.refresh.poll')}</option>}{profiles.map(profile => <option key={profile} value={profile}>{t(profile === 'companion_location' ? 'alpha9.refresh.companion' : 'alpha9.refresh.poll')}</option>)}</Select>}</Field>
    {refresh.profile === 'companion_location' && <div className="mt-3"><Checkbox checked={refresh.permission_confirmed === true} label={t('alpha9.refresh.permission')} onCheckedChange={permission_confirmed => change({ ...refresh, permission_confirmed })} /></div>}
    {open && (ha.isError ? <p className="mt-3 text-sm text-muted">{t('alpha7.device.unavailable')}</p> : !ha.isPending && !profiles.length && <p className="mt-3 text-sm text-muted">{t('alpha9.refresh.unsupported')}</p>)}
  </details>;
}
