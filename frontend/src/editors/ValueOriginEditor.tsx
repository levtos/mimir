import { t } from '@/i18n';
import { Field, Input, Select } from '@/components/ui/form';
import { Button } from '@/components/ui/button';
import { asArray, asObject, str, type FieldSchema } from '@/features/authoring/model';
import type { Json, JsonObject } from '@/lib/json';
import { isoToLocalInput, TypedValueEditor } from './common';

export function OriginIntervalFields({ value, onChange }: { value: JsonObject; onChange: (next: JsonObject) => void }) {
  return <div className="grid gap-3 sm:grid-cols-3">{(['issued_at', 'valid_from', 'valid_until'] as const).map(key => <Field key={key} label={t(`alpha9.valueOrigin.${key}`)}>{props => <Input {...props} type="datetime-local" step={1} value={isoToLocalInput(str(value[key]))} onChange={event => { const next = { ...value }; if (event.target.value) next[key] = new Date(event.target.value).toISOString(); else delete next[key]; onChange(next); }} />}</Field>)}</div>;
}

export function newForecastPoint(schema: FieldSchema, origin: JsonObject, now = Date.now()): JsonObject {
  const start = new Date(now).toISOString(); const end = new Date(now+3600000).toISOString();
  return { value: schema.type === 'number' ? 0 : schema.type === 'bool' ? false : schema.type === 'object' ? {} : '', value_origin: { ...origin, kind: 'forecast', issued_at: new Date().toISOString(), valid_from: start, valid_until: end } };
}

export function ForecastValuesEditor({ value, schema, origin, onChange }: { value: Json; schema: FieldSchema; origin: JsonObject; onChange: (next: Json) => void }) {
  const points = asArray(value).map(asObject);
  return <div className="space-y-4">{points.map((point, index) => <fieldset key={index} className="space-y-3 rounded border border-line p-3">
    <legend className="px-2 text-sm">{t('alpha9.valueOrigin.point', { number: index+1 })}</legend>
    <TypedValueEditor label={t('alpha9.manual.value')} pointer={`/forecast/${index}/value`} value={point.value ?? null} schema={schema} onChange={next => onChange(points.map((item, at) => at === index ? { ...item, value: next } : item))} />
    <OriginIntervalFields value={asObject(point.value_origin)} onChange={next => onChange(points.map((item, at) => at === index ? { ...item, value_origin: next } : item))} />
    <Button onClick={() => onChange(points.filter((_, at) => at !== index))}>{t('features.sources.SourcesPage.entfernen_382837')}</Button>
  </fieldset>)}<Button disabled={points.length >= 512} onClick={() => { const latest = points.at(-1); const begin = Date.parse(str(asObject(latest?.value_origin).valid_until)); onChange([...points, newForecastPoint(schema, origin, Number.isFinite(begin) ? begin : Date.now())]); }}>{t('alpha9.valueOrigin.addPoint')}</Button></div>;
}

export function OutputOriginsEditor({ value, onChange }: { value: JsonObject; onChange: (next: JsonObject) => void }) {
  const origins = asObject(value.output_origins);
  return <div className="space-y-3">{Object.keys(asObject(value.outputs)).map(name => { const origin = asObject(origins[name]); return <Field key={name} label={t('alpha9.valueOrigin.output', { name })}>{props => <Select {...props} value={str(origin.kind)} onChange={event => { const next = { ...origins }; if (event.target.value) next[name] = { kind: event.target.value }; else delete next[name]; onChange({ ...value, output_origins: next }); }}><option value="">{t('alpha9.valueOrigin.unknown')}</option><option value="model">{t('alpha9.valueOrigin.model')}</option><option value="replacement">{t('alpha9.valueOrigin.replacement')}</option></Select>}</Field>; })}</div>;
}
