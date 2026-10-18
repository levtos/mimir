import { t } from '@/i18n';
import { Button } from '@/components/ui/button';
import { PageHeader, Spinner } from '@/components/ui/layout';

/** A page keeps its heading and action while its data or module is unavailable. */
export function PageLoading({ title = t('App.terra_workbench_7ad523'), description = t('alpha9.pages.app'), loading = true }: { title?: string; description?: string; loading?: boolean }) {
  return <div data-page-loading>
    <PageHeader title={title} description={description} actions={<Button variant="primary" disabled={loading} disabledReason={t('alpha7.copy.inProgress')} onClick={() => location.reload()}>{t('components.RouteError.seite_neu_laden_61e2c2')}</Button>} />
    {loading && <Spinner />}
  </div>;
}
