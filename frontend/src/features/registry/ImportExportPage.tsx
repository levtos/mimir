import { useState } from 'react';
import { useNavigate } from 'react-router';
import { useQueryClient } from '@tanstack/react-query';
import { t } from '@/i18n';
import { Button } from '@/components/ui/button';
import { Field, FileInput, Input, Select } from '@/components/ui/form';
import { Dialog } from '@/components/ui/dialog';
import { Notice, PageHeader, Panel, PanelHeader } from '@/components/ui/layout';
import { downloadText } from '@/features/authoring/importExport';
import { useWorkingDocument } from '@/features/authoring/WorkingDocument';
import { api, apiText, describeError } from '@/lib/api';
import { useActiveRevision } from '@/lib/queries';
import type { Draft } from '@/lib/types';
import type { Registry } from '@/lib/types';
import { FreshnessAssignment, type FreshnessChoices } from '@/features/sources/FreshnessAssignment';
import { asArray } from '@/features/authoring/model';
import { isObject } from '@/lib/json';
import { currentDraft } from './authoring';

interface Preview { config: Registry; freshness_changed_sources?: string[]; catalog_entries?: number; editorial_entries?: number; plan_digest: string; added: number; reused: number; conflicts: string[]; unresolved: string[]; editorial_versions: Record<string, number>; package: { config: Registry; editorial: { object: { kind: string; id: string }; category: string; room: { name: string } }[] } }
type Resolution = 'keep' | 'file' | { new_id: string };

export default function ImportExportPage() {
  const active = useActiveRevision(); const doc = useWorkingDocument(); const cache = useQueryClient(); const navigate = useNavigate();
  const [fileText, setFileText] = useState(''); const [filename, setFilename] = useState('');
  const [preview, setPreview] = useState<Preview | null>(null); const [resolutions, setResolutions] = useState<Record<string, Resolution>>({});
  const [editorialChoices, setEditorialChoices] = useState<Record<string, string>>({}); const [error, setError] = useState('');
  const [busy, setBusy] = useState(false); const [backingUp, setBackingUp] = useState(false); const [scope, setScope] = useState('active');
  const [requestId, setRequestId] = useState(''); const [stale, setStale] = useState(false);
  const [freshnessChoices, setFreshnessChoices] = useState<FreshnessChoices>({});
  const isContract = (() => { try { return JSON.parse(fileText).scope === 'contract'; } catch { return false; } })();
  const targetUnavailable = isContract && (!doc.draft || !currentDraft(doc.draft, active.data?.revision ?? 0) || doc.dirty);
  const body = () => ({ package_text: fileText, resolutions, editorial_choices: editorialChoices, freshness_choices: freshnessChoices, ...(isContract && doc.draft ? { target_draft_id: doc.draft.draft_id, target_draft_version: doc.draft.draft_version } : {}) });
  const check = async () => { setBusy(true); setError(''); try { setPreview(await api<Preview>('portable/preview', { method: 'POST', body: body() })); setRequestId(crypto.randomUUID()); setStale(false); } catch (failure) { setError(describeError(failure)); } finally { setBusy(false); } };
  const assignmentMissing = !!preview && asArray(preview.package.config?.sources).filter(isObject).some(source => source.origin !== 'manual' && !freshnessChoices[String(source.source_id)]);
  const save = async () => { if (!preview || assignmentMissing) return; setBusy(true); setError(''); try {
    const draft = await api<Draft>('portable/stage', { method: 'POST', body: { ...body(), plan_digest: preview.plan_digest, request_id: requestId } });
    await cache.invalidateQueries({ queryKey: ['registry', 'drafts'] }); if (draft.draft_id === doc.draft?.draft_id) doc.open(draft, { reload: true }); else doc.requestOpen(draft); navigate(`/changes/drafts/${encodeURIComponent(draft.draft_id)}`);
  } catch (failure) { setError(describeError(failure)); } finally { setBusy(false); } };
  const backup = async () => { setBusy(true); setError(''); try {
    const data = await apiText('portable/export', { method: 'POST', body: { expected_active_revision: active.data?.revision ?? 0,
      ...(scope === 'draft' && doc.draft ? { draft_id: doc.draft.draft_id, draft_version: doc.draft.draft_version } : {}) } });
    downloadText(`wuschel-${new Date().toISOString().slice(0, 10)}.json`, data); setBackingUp(false);
  } catch (failure) { setError(describeError(failure)); } finally { setBusy(false); } };
  return <>
    <PageHeader title={t('alpha10.transfer.title')} description={t('alpha10.transfer.description')} actions={<Button variant="primary" disabled={!active.data && !doc.draft} onClick={() => { setScope(active.data ? 'active' : 'draft'); setBackingUp(true); }}>{t('alpha9.actions.backup')}</Button>} />
    <Notice tone="info">{t('alpha10.transfer.history')}</Notice>
    <Panel className="mt-5"><PanelHeader title={t('alpha10.transfer.read')} /><div className="space-y-4 p-5">
      <Field label={t('alpha7.import.file')}>{p => <FileInput {...p} accept="application/json,.json" disabled={busy} onChange={async e => { const file = e.target.files?.[0]; if (!file) return; setPreview(null); setError(''); setResolutions({}); setEditorialChoices({}); setFreshnessChoices({}); setFilename(file.name); if (file.size > 50 * 1024 * 1024) { setError(t('alpha10.transfer.tooLarge')); setFileText(''); return; } setFileText(await file.text()); }} />}</Field>
      <p className="text-sm text-muted">{filename || t('alpha10.transfer.choose')}</p>
      <Button disabled={!fileText || busy || targetUnavailable} onClick={() => void check()}>{t('alpha10.transfer.preview')}</Button>
      {isContract && <Notice tone="info">{doc.draft ? t('alpha10.transfer.target', { name: doc.displayName || doc.draft.draft_id }) : t('alpha10.transfer.targetRequired')}{!doc.draft && <Button onClick={() => void doc.ensureDraft().catch(failure => setError(describeError(failure)))}>{t('alpha10.transfer.createTarget')}</Button>}{doc.dirty && <p>{t('alpha10.transfer.targetSave')}</p>}</Notice>}
      {error && <Notice tone="bad">{error}</Notice>}
      {preview && <section className="space-y-4" aria-live="polite">
        <h2>{t('b4.assignImport')}</h2><FreshnessAssignment config={preview.package.config} target={preview.config} choices={freshnessChoices} onChange={next => { setFreshnessChoices(next); setStale(true); }} />
        {!stale && preview.freshness_changed_sources && <p>{t(preview.freshness_changed_sources.length === 1 ? 'b4.fileChangeOne' : 'b4.fileChanges', { count: preview.freshness_changed_sources.length })}</p>}
        <p>{t('alpha10.transfer.counts', { added: preview.added, reused: preview.reused, conflicts: preview.conflicts.length })}</p>
        <p>{t('alpha10.transfer.contents', { n: preview.catalog_entries ?? 0, metadata: preview.editorial_entries ?? 0 })}</p>
        <Notice tone="warn">{t('alpha10.transfer.addresses')}</Notice>
        {preview.conflicts.map(key => <div key={key} className="space-y-2 rounded-lg border border-line p-3"><p className="break-all text-sm">{key}</p><Field label={t('alpha10.transfer.collision')}>{p => <Select {...p} value={resolutions[key] === 'keep' ? 'keep' : resolutions[key] === 'file' ? 'file' : typeof resolutions[key] === 'object' ? 'new' : ''} onChange={e => { setResolutions(previous => ({ ...previous, [key]: e.target.value === 'keep' ? 'keep' : e.target.value === 'file' ? 'file' : { new_id: '' } })); setStale(true); }}><option value="">{t('alpha10.transfer.decide')}</option><option value="keep">{t('alpha10.transfer.keep')}</option>{!isContract && key.startsWith('freshness_templates:') && <option value="file">{t('b4.fileTemplate')}</option>}{!key.startsWith('catalog-entry:') && <option value="new">{t('alpha10.transfer.new')}</option>}</Select>}</Field>{typeof resolutions[key] === 'object' && <Field label={t('alpha10.transfer.newId')}>{p => <Input {...p} value={(resolutions[key] as { new_id: string }).new_id} onChange={e => { setResolutions(previous => ({ ...previous, [key]: { new_id: e.target.value } })); setStale(true); }} />}</Field>}</div>)}
        {preview.package.editorial.map(row => { const key = `${row.object.kind}:${row.object.id}`; return <div key={key} className="rounded-lg border border-line p-3"><p>{row.object.id} · {row.category} · {row.room.name}</p>{preview.editorial_versions[key] ? <Field label={t('alpha10.transfer.metadata')}>{p => <Select {...p} value={editorialChoices[key] ?? 'keep'} onChange={e => { setEditorialChoices(previous => ({ ...previous, [key]: e.target.value })); setStale(true); }}><option value="keep">{t('alpha10.transfer.keepMetadata')}</option><option value="file">{t('alpha10.transfer.fileMetadata')}</option></Select>}</Field> : <p>{t('alpha10.transfer.newMetadata')}</p>}</div>; })}
        {(preview.package as { legacy?: boolean }).legacy && <Notice tone="info">{t('alpha10.transfer.legacy')}</Notice>}<p className="text-sm text-muted">{t('alpha10.transfer.draftHelp')}</p><Button disabled={busy || stale || assignmentMissing || targetUnavailable || preview.unresolved.length > 0} onClick={() => void save()}>{t('alpha10.transfer.stage')}</Button>
      </section>}
    </div></Panel>
    <Dialog open={backingUp} onOpenChange={setBackingUp} title={t('alpha9.actions.backup')} footer={<Button variant="primary" disabled={busy || (scope === 'draft' && !!doc.dirty)} onClick={() => void backup()}>{t('alpha9.export.saveFile')}</Button>}>
      <Field label={t('alpha9.export.scope')}>{p => <Select {...p} value={scope} onChange={e => setScope(e.target.value)}><option value="active" disabled={!active.data}>{t('alpha7.export.active')}</option><option value="draft" disabled={!doc.draft}>{t('alpha7.export.draft')}</option></Select>}</Field>
      <p className="mt-3 text-sm">{t('alpha10.transfer.savedOnly')}</p><p className="mt-3 text-sm">{t('alpha10.transfer.history')}</p>
    </Dialog>
  </>;
}
