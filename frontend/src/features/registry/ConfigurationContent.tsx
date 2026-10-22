import { t } from '@/i18n';
import { fieldLabel, codeLabel } from '@/i18n/codes';
import { Collapsible } from '@/components/ui/controls';
import type { Json, JsonObject } from '@/lib/json';

/** Readable historical content; protocol representation stays in technical details. */
function Content({ value, field = '' }: { value: Json; field?: string }) {
  if (value === null) return <span>—</span>;
  if (Array.isArray(value)) return <ul className="space-y-3">{value.map((item, index) => <li key={index} className="border-l border-line pl-3"><Content value={item} field={field} /></li>)}</ul>;
  if (typeof value === 'object') return <dl className="space-y-2">{Object.entries(value).map(([key, item]) => <div key={key} className="min-w-0"><dt className="font-medium">{fieldLabel(key)}</dt><dd className="break-words pl-3"><Content value={item} field={key} /></dd></div>)}</dl>;
  return <span>{typeof value === 'boolean' ? t(value ? 'lib.status.ja_cde9e5' : 'lib.status.nein_90ebc1') : typeof value === 'number' ? value.toLocaleString('de-DE') : ['mode', 'source_type', 'kind', 'target', 'monitor'].includes(field) ? codeLabel(value) : value}</span>;
}

export function ConfigurationContent({ config }: { config: JsonObject }) {
  return <div className="space-y-3">{Object.entries(config).map(([key, value]) => <Collapsible key={key} title={fieldLabel(key)}><Content value={value} field={key} /></Collapsible>)}</div>;
}
