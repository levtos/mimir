import { t } from '@/i18n';
import { Link } from 'react-router';
import { DurationField } from '@/components/SecondsField';
import { asArray, asObject, str } from '@/features/authoring/model';
import { isObject, type JsonObject } from '@/lib/json';
import { effectiveRule, freshnessLabel } from '@/features/sources/freshness';

/** Edit the existing source slot; never create a contract parameter copy. */
export function OpeningHeartbeatSettings({ config, contract, onChange }: {
  config: JsonObject; contract: JsonObject; onChange: (index: number, interval: number) => void;
}) {
  if (!['opening.dual_contact', 'opening.single_contact'].includes(str(contract.type_id))) return null;
  const refs = new Set(asArray(contract.inputs).filter(isObject).map(input => str(input.ref)));
  return <section className="mt-4 space-y-3">
    <h3 className="text-sm font-semibold">{t('beta1.heartbeat.title')}</h3>
    <p className="text-xs text-muted">{t('beta1.heartbeat.help')}</p>
    {asArray(config.sources).map((source, index) => {
      if (!isObject(source) || !refs.has(str(source.source_id))) return null;
      const freshness = effectiveRule(config, source);
      const interval = freshness.interval_s;
      const consumers = asArray(config.contracts).filter(isObject).filter(item => asArray(item.inputs).filter(isObject).some(input => input.ref === source.source_id)).length;
      const valid = typeof interval === 'number' && Number.isFinite(interval) && interval > 0;
      return <div key={str(source.source_id)}>
        {asObject(source.freshness_selection).kind === 'shared' ? <><p>{freshnessLabel(config, source)}</p><Link className="inline-flex min-h-11 items-center underline" to="/sources/freshness">{t('b4.templateChange')}</Link><Link className="inline-flex min-h-11 items-center underline" to={`/sources/devices?item=${index}`}>{t('b4.own')}</Link></> : <DurationField label={t('beta1.heartbeat.label', { name: str(source.display_name) || str(source.source_id) })} min={0.000001} value={typeof interval === 'number' ? interval : 0} onChange={value => onChange(index, value)} />}
        <p className="text-xs text-muted">{t('beta1.heartbeat.shared', { count: consumers })}</p>
        {!valid && <p role="alert" className="text-sm text-bad">{t('beta1.heartbeat.invalid')}</p>}
      </div>;
    })}
  </section>;
}
