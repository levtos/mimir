import { useState } from 'react';
import { useQuery, useQueryClient } from '@tanstack/react-query';
import { t } from '@/i18n';
import { api, describeError } from '@/lib/api';
import { useActiveRevision, useCapabilities } from '@/lib/queries';
import { asArray } from '@/features/authoring/model';
import { isObject } from '@/lib/json';
import { useAuthoringSource } from '@/features/authoring/useAuthoringSource';
import { useWorkingDocument } from '@/features/authoring/WorkingDocument';
import { useHaCatalog } from '@/features/sources/useHaCatalog';
import { Button } from '@/components/ui/button';
import { Field, Input, Select } from '@/components/ui/form';
import { MdiIcon } from '@/components/MdiIcon';
import { CATEGORIES, NO_ROOM, areaRoom, categoryIcons, categoryKeys, findMetadata, objectKey, roomKey, safeIcon, suggestedRoom, type Category, type EditorialResponse, type EditorialRow, type ObjectRef, type Room } from './model';

export function useEditorial() {
  const doc = useWorkingDocument();
  const draftId = doc.editing ? doc.draft?.draft_id : undefined;
  const query = useQuery({ queryKey: ['editorial', draftId ?? 'active'], queryFn: () => api<EditorialResponse>(`editorial${draftId ? `?draft_id=${encodeURIComponent(draftId)}` : ''}`), retry: false });
  return { ...query, item: (object: ObjectRef) => findMetadata(query.data, object) };
}
export function CategoryBadge({ category }: { category: Category }) {
  return <span className="inline-flex items-center gap-2 text-sm"><MdiIcon name={categoryIcons[category]} />{t(`alpha9.category.${categoryKeys[category]}`)}</span>;
}
export function RoomBadge({ room }: { room: Room }) {
  return <span className="inline-flex items-center gap-2 text-sm"><MdiIcon name={room.icon} />{room.mode === 'none' ? t('alpha9.room.none') : room.name}</span>;
}
export function CategorySelect({ value, onChange, all = false }: { value: Category | ''; onChange: (value: Category | '') => void; all?: boolean }) {
  return <Field label={t('alpha9.category.label')}>{props => <Select {...props} value={value} onChange={event => onChange(event.target.value as Category | '')}>{all && <option value="">{t('alpha9.category.all')}</option>}{CATEGORIES.map(category => <option key={category} value={category}>{t(`alpha9.category.${categoryKeys[category]}`)}</option>)}</Select>}</Field>;
}
export function EditorialPanel({ object }: { object: ObjectRef }) {
  const [open, setOpen] = useState(false);
  const metadata = useEditorial();
  const src = useAuthoringSource();
  const row = metadata.item(object);
  return <section className="mb-4 rounded-lg border border-line p-4">
    <div className="flex flex-wrap items-center gap-5"><CategoryBadge category={row.category} />{object.kind === 'contract' && <RoomBadge room={row.room} />}</div>
    {row.room.missing && <p className="mt-2 text-sm text-warn">{t('alpha9.room.missing')}</p>}
    {metadata.isError && <p role="alert" className="mt-2 text-sm text-bad">{t('alpha9.editorial.loadFailed')}</p>}
    <details className="mt-2" onToggle={event => setOpen(event.currentTarget.open)}><summary className="cursor-pointer text-sm text-muted">{t(object.kind === 'contract' ? 'alpha9.editorial.change' : 'alpha9.editorial.changeCategory')}</summary>
      {open && (metadata.isPending ? <p className="mt-3 text-sm text-muted">{t('alpha9.editorial.loading')}</p> : !metadata.isError && <EditorialForm key={`${objectKey(object)}:${row.editorial_version}:${src.source}`} row={row} />)}
    </details>
  </section>;
}
function EditorialForm({ row }: { row: EditorialRow }) {
  const doc = useWorkingDocument(); const src = useAuthoringSource(); const active = useActiveRevision(); const caps = useCapabilities();
  const client = useQueryClient(); const ha = useHaCatalog(row.object.kind === 'contract', true);
  const [category, setCategory] = useState(row.category); const [room, setRoom] = useState(row.room);
  const [busy, setBusy] = useState(false); const [error, setError] = useState(''); const [saved, setSaved] = useState(false);
  const contract = asArray(src.config?.contracts).filter(isObject).find(item => item.contract_id === row.object.id);
  const suggestion = suggestedRoom(src.config, contract, ha.entities);
  const areas = ha.areas?.map(area => ({ mode: 'manual' as const, area_id: area.area_id, name: area.area_name, icon: safeIcon(area.area_icon), missing: false })) ?? [...new Map(ha.entities.flatMap(entity => { const room = areaRoom(entity); return room ? [[room.area_id!, room] as const] : []; })).values()];
  const existing = row.object.kind === 'contract' ? asArray(active.data?.config?.contracts).filter(isObject).some(item => item.contract_id === row.object.id) : asArray(active.data?.config?.definitions).filter(isObject).some(item => item.type_id === row.object.id) || !!caps.data?.types.some(item => !item.definition && item.type_id === row.object.id);
  const valid = room.mode === 'none' || !!room.name.trim();
  const save = async () => {
    setBusy(true); setError(''); setSaved(false);
    try {
      const draft = existing ? null : await doc.prepareActivation();
      await api('editorial', { method: 'PUT', body: { object: row.object, expected_editorial_version: row.editorial_version, category, room: { ...room, name: room.name.trim() }, ...(draft ? { draft_id: draft.draft_id, draft_version: draft.draft_version } : {}) } });
      setSaved(true); await client.invalidateQueries({ queryKey: ['editorial'] });
    } catch (failure) { setError(describeError(failure)); }
    finally { setBusy(false); }
  };
  return <div className="mt-4 space-y-4">
    <p className="text-sm text-muted">{t(existing ? 'alpha9.editorial.immediate' : 'alpha9.editorial.draft')}</p>
    <fieldset disabled={busy} className="grid max-w-2xl gap-4 sm:grid-cols-2">
      <CategorySelect value={category} onChange={value => setCategory(value || 'other')} />
      {row.object.kind === 'contract' && <>
        <Field label={t('alpha9.room.label')}>{props => <Select {...props} value={room.mode === 'none' ? 'none' : room.mode === 'manual' && !room.area_id ? 'custom' : `area:${room.area_id}`} onChange={event => { const area = areas.find(item => `area:${item.area_id}` === event.target.value); setRoom(event.target.value === 'none' ? NO_ROOM : event.target.value === 'custom' ? { ...NO_ROOM, mode: 'manual' } : area ? { ...area, mode: 'manual' } : room); setSaved(false); }}><option value="none">{t('alpha9.room.none')}</option><option value="custom">{t('alpha9.room.custom')}</option>{room.area_id && !areas.some(item => item.area_id === room.area_id) && <option value={`area:${room.area_id}`}>{room.name}</option>}{areas.map(area => <option key={area.area_id} value={`area:${area.area_id}`}>{area.name}</option>)}</Select>}</Field>
        {room.mode === 'manual' && !room.area_id && <Field label={t('alpha9.room.custom')}>{props => <Input {...props} value={room.name} maxLength={128} onChange={event => { setRoom({ ...room, name: event.target.value }); setSaved(false); }} />}</Field>}
      </>}
    </fieldset>
    {row.object.kind === 'contract' && <>
      {ha.isError && <p className="text-sm text-muted">{t('alpha9.editorial.haUnavailable')}</p>}
      {suggestion.multiple && <p className="text-sm text-muted">{t('alpha9.room.multiple')}</p>}
      {suggestion.room && <div className="flex flex-wrap items-center gap-3"><p className="text-sm text-muted">{t('alpha9.room.suggestion', { room: suggestion.room.name })}</p><Button disabled={busy} onClick={() => { setRoom(suggestion.room!); setSaved(false); }}>{t('alpha9.room.accept')}</Button></div>}
      <RoomBadge room={room} />
    </>}
    {error && <p role="alert" className="text-sm text-bad">{error}</p>}{saved && <p role="status" className="text-sm text-ok">{t('alpha9.editorial.saved')}</p>}
    <Button disabled={busy || !valid || active.isPending || caps.isPending || (!existing && !doc.editing)} onClick={() => void save()}>{t('alpha9.editorial.save')}</Button>
  </div>;
}
export { roomKey };
