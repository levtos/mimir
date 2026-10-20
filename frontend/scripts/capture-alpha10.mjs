/** Firefox evidence against the isolated memory-store harness only. */
import { firefox } from '@playwright/test';
import { mkdir, writeFile } from 'node:fs/promises';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const base = process.env.WUSCHEL_REVIEW_URL ?? 'http://127.0.0.1:18099';
if (new URL(base).hostname !== '127.0.0.1') throw new Error('Isolated loopback only');
const output = fileURLToPath(new URL('../../docs/alpha10/bilder/', import.meta.url));
await mkdir(output, { recursive: true });
const browser = await firefox.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 1568, height: 710 }, deviceScaleFactor: 1, locale: 'de-DE', timezoneId: 'Europe/Berlin', reducedMotion: 'reduce' });
const page = await context.newPage();
const errors = []; const external = []; const shots = [];
page.on('pageerror', error => errors.push(error.message));
await page.route('**/*', async route => {
  if (new URL(route.request().url()).hostname !== '127.0.0.1') { external.push(route.request().url()); await route.abort(); }
  else await route.continue();
});
const go = async (path, heading) => {
  await page.goto(`${base}/#${path}`);
  await page.getByRole('heading', { name: heading, exact: true, level: 1 }).waitFor();
  await page.evaluate(async () => { await document.fonts.ready; await Promise.all([...document.images].map(image => image.decode().catch(() => {}))); });
};
const shot = async name => {
  await page.screenshot({ path: resolve(output, name), fullPage: false, animations: 'disabled' });
  shots.push({ file: name, browser: 'Firefox', version: browser.version(), viewport: [1568, 710] });
  console.log(name);
};
try {
  await go('/', 'Übersicht'); await shot('01-uebersicht.png');
  await go('/contracts/list/all', 'Meine Verträge');
  await page.getByText('Noch keine Verträge', { exact: true }).waitFor();
  await shot('02-leere-vertragsliste.png');
  await go('/catalog-care', 'Titelkatalog');
  await page.getByRole('combobox', { name: 'Ansicht', exact: true }).selectOption('all');
  await page.getByText('Synthetischer Beispieltitel', { exact: true }).waitFor();
  await shot('03-katalogpflege.png');
  await go('/import-export', 'Import & Export'); await shot('04-import-export.png');
  await go('/changes/versions', 'Konfigurationen');
  await page.getByRole('button', { name: 'Technische Details', exact: true }).first().click();
  await page.getByText('Die Prüfsumme ist ein Fingerabdruck dieses Stands. Damit lassen sich zwei Stände vergleichen. Sie ist keine Kennung.').first().waitFor();
  await shot('05-versionen.png');
  await go('/settings/connections', 'Verbindungen');
  await page.getByText(/^MQTT ist ausgeschaltet\. Du hast Verbindungsdaten/).waitFor();
  await shot('06-verbindungen-mqtt.png');
  if (errors.length || external.length) throw new Error(JSON.stringify({ errors, external }));
  await writeFile(resolve(output, 'nachweis.json'), JSON.stringify({ engine: 'isolated real API, memory store, synthetic data', errors, external, shots }, null, 2) + '\n');
} finally { await browser.close(); }
