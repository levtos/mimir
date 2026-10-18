import { useEffect, useState } from 'react';
import small from '@/assets/mdi-categories.json';

const chunks = import.meta.glob<Record<string, string>>('../assets/mdi/[0-9a-f][0-9a-f].json', { import: 'default' });
const loaded = new Map<string, Promise<Record<string, string>>>();
export function mdiExportName(name: string): string | null {
  if (!/^mdi:[a-z0-9-]{1,64}$/.test(name)) return null;
  return 'mdi'+name.slice(4).split('-').map(part => part[0]?.toUpperCase()+part.slice(1)).join('');
}
export function mdiShard(name: string) { let hash = 0; for (const char of name) hash = (hash*31+char.charCodeAt(0)) >>> 0; return (hash%64).toString(16).padStart(2, '0'); }
export async function mdiPath(name: string) {
  if (name in small) return small[name as keyof typeof small];
  const exported = mdiExportName(name);
  if (!exported) return small['mdi:home'];
  const path = `../assets/mdi/${mdiShard(exported)}.json`;
  const loader = chunks[path];
  if (!loader) return small['mdi:home'];
  if (!loaded.has(path)) loaded.set(path, loader());
  return (await loaded.get(path))?.[exported] ?? small['mdi:home'];
}
export function MdiIcon({ name, className = 'h-5 w-5' }: { name: string; className?: string }) {
  const [path, setPath] = useState(name in small ? small[name as keyof typeof small] : small['mdi:home']);
  useEffect(() => { let current = true; void mdiPath(name).then(next => { if (current) setPath(next); }).catch(() => { if (current) setPath(small['mdi:home']); }); return () => { current = false; }; }, [name]);
  return <svg viewBox="0 0 24 24" aria-hidden="true" className={className} fill="currentColor"><path d={path} /></svg>;
}
