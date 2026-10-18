import { t } from '@/i18n';
import { Field, Input } from '@/components/ui/form';
import { formatNumber } from '@/lib/format';

export function minuteHint(seconds: number) {
  return Number.isFinite(seconds) && seconds >= 0 ? t(seconds === 60 ? 'alpha7.freshness.oneMinute' : 'alpha7.freshness.minutes', { minutes: formatNumber(seconds/60, 2) }) : undefined;
}
export function SecondsField({ label, value, onChange, min = 0, max = 86400, disabled }: { label: string; value: number; onChange: (value: number) => void; min?: number; max?: number; disabled?: boolean }) {
  return <Field label={label} hint={minuteHint(value)}>{props => <Input {...props} type="number" disabled={disabled} min={min} max={max} step={1} value={Number.isFinite(value) ? value : ''} onChange={event => onChange(event.target.value === '' ? 0 : event.target.valueAsNumber)} />}</Field>;
}
