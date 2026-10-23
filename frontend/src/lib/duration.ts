/** Exact decimal authoring at the scheduler's microsecond resolution. */
import { t } from '@/i18n';
export type DurationUnit = 'minutes' | 'hours';
export function durationSeconds(text: string, unit: DurationUnit): number | null {
  if (text.length > 64 || !/^\d+(?:[.,]\d+)?$/.test(text.trim())) return null;
  const [whole, fraction = ''] = text.trim().replace(',', '.').split('.');
  if (fraction.length > 18) return null;
  const scale = 10n ** BigInt(fraction.length);
  const micros = BigInt(`${whole}${fraction}`) * BigInt(unit === 'hours' ? 3600 : 60) * 1000000n;
  if (micros % scale !== 0n || micros / scale > BigInt(Number.MAX_SAFE_INTEGER)) return null;
  return Number(micros / scale) / 1000000;
}
export function durationText(seconds: number): string {
  if (!Number.isFinite(seconds)) return '–';
  if (seconds === 0) return '0 Minuten';
  if (seconds < 60) return t('b4.time.short');
  const number = (value: number) => new Intl.NumberFormat('de-DE', { maximumFractionDigits: 12, useGrouping: false }).format(value);
  if (seconds % 3600 === 0) return `${number(seconds / 3600)} ${seconds === 3600 ? 'Stunde' : 'Stunden'}`;
  return `${number(seconds / 60)} ${seconds === 60 ? 'Minute' : 'Minuten'}`;
}
