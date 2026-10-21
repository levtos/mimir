import { t } from '@/i18n';
import { Field, Input } from '@/components/ui/form';
import { asArray, asObject, str } from '@/features/authoring/model';
import { isObject, type JsonObject } from '@/lib/json';

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
      const freshness = asObject(source.freshness);
      const interval = freshness.interval_s;
      const consumers = asArray(config.contracts).filter(isObject).filter(item => asArray(item.inputs).filter(isObject).some(input => input.ref === source.source_id)).length;
      const valid = typeof interval === 'number' && Number.isFinite(interval) && interval > 0;
      return <div key={str(source.source_id)}>
        <Field label={t('beta1.heartbeat.label', { name: str(source.display_name) || str(source.source_id) })} hint={t('beta1.heartbeat.shared', { count: consumers })}>{props => <Input {...props} type="number" min={1} step="any" value={typeof interval === 'number' ? interval : ''} aria-invalid={!valid} onChange={event => onChange(index, Number(event.target.value))} />}</Field>
        {!valid && <p role="alert" className="text-sm text-bad">{t('beta1.heartbeat.invalid')}</p>}
      </div>;
    })}
  </section>;
}
