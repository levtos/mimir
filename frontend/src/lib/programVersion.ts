import { t } from '@/i18n';

export function programVersion(version: string): string {
  const stage = version.match(/^\d+\.\d+\.\d+(a|b)(\d+)$/);
  const label = stage ? t(stage[1] === 'a' ? 'alpha9.system.alpha' : 'alpha9.system.beta', { count: Number(stage[2]) }) : '';
  return t('alpha9.system.programVersionValue', { version, stage: label ? ` (${label})` : '' });
}
