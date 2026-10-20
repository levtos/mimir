import { cn } from '@/lib/utils';

const base = import.meta.env.BASE_URL;
export function HerdFigure({ name = 'wuschel', className }: { name?: 'wuschel' | 'traber'; className?: string }) {
  return <img data-herd-figure={name} src={base + `herde/${name}-figur-512.webp`} srcSet={base + `herde/${name}-figur-512.webp 512w, ` + base + `herde/${name}-figur-1024.webp 1024w`} sizes="(min-width: 768px) 80px, 64px" width={80} height={120} alt="" loading="eager" decoding="async" className={cn('h-28 w-auto shrink-0 object-contain', className)} />;
}
export function HerdIcon({ name = 'wuschel', className }: { name?: 'wuschel' | 'traber'; className?: string }) {
  return <img src={base + `herde/${name}-icon-32.png`} srcSet={base + `herde/${name}-icon-64.png 2x`} width={32} height={32} alt="" className={cn('size-8 shrink-0', className)} />;
}
