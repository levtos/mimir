/** Reproducible Firefox review against the isolated real engine, never a live HA. */
import { firefox } from '@playwright/test';
import { mkdir, writeFile } from 'node:fs/promises';
import { resolve } from 'node:path';
import de from '../src/i18n/de.json' with { type: 'json' };

const base = process.env.MIMIR_REVIEW_URL;
if (!base || new URL(base).hostname !== '127.0.0.1') throw new Error('Only the isolated loopback harness is allowed');
const output = resolve('../docs/alpha9/bilder');
await mkdir(output, { recursive: true });
const browser = await firefox.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 1568, height: 710 }, deviceScaleFactor: 1, locale: 'de-DE', timezoneId: 'Europe/Berlin', reducedMotion: 'reduce' });
const page = await context.newPage();
const errors = []; const external = []; const shots = [];
page.on('pageerror', error => errors.push(error.message));
await page.route('**/*', async route => {
  const url = new URL(route.request().url());
  if (url.hostname !== '127.0.0.1') { external.push(url.origin); await route.abort(); }
  else await route.continue();
});
const go = async (path, heading) => {
  await page.goto(`${base}/#${path}`);
  await page.getByRole('heading', { name: heading, exact: true, level: 1 }).waitFor();
  await page.locator('[data-page-header]').getByText(/^Hier kannst du /).waitFor();
  await page.evaluate(() => document.fonts.ready);
};
const shot = async (name, description) => {
  await page.screenshot({ path: resolve(output, name), fullPage: false, animations: 'disabled' });
  shots.push({ file: name, description, viewport: '1568×710', browser: 'Firefox', version: browser.version() });
  console.log('Firefox-Bild:', name);
};
try {
  await go('/contracts/list/all', 'Meine Verträge');
  await page.getByLabel(de['alpha9.editorial.group']).selectOption('category');
  await page.locator('span').getByText('Testzimmer', { exact: true }).first().waitFor();
  await shot('01-vertraege-kategorie-raum.png', 'Kategorien, Raum, Filter und Gruppierung der Verträge');

  await go('/contracts/view/test.temperaturbereich', 'Temperaturbereich im Testzimmer');
  await page.getByText('Testzimmer', { exact: true }).waitFor();
  await shot('02-vertrag-kategorie-raum.png', 'Kategorie und Raum am Vertrag; gespeicherter Wert');
  await page.getByText(de['alpha9.editorial.change'], { exact: true }).click();
  await page.getByLabel('Kategorie', { exact: true }).waitFor();
  await shot('03-vertrag-ordnung-aendern.png', 'Redaktionelles Ändern ohne Konfigurationswechsel');

  await go('/sources/devices?selected=source.angabe', 'Quellen');
  await page.getByText('Eigene Temperaturangabe im Testzimmer', { exact: true }).first().click();
  await page.getByRole('button', { name: de['alpha9.manual.enter'], exact: true }).waitFor();
  await page.getByRole('button', { name: de['alpha9.manual.enter'], exact: true }).scrollIntoViewIfNeeded();
  await shot('04-manuelle-quelle.png', 'Manuelle Eingabe, Herkunft und Gültigkeit');

  await go('/settings/notifications', 'Benachrichtigungen');
  await page.getByRole('button', { name: 'Im Entwurf speichern', exact: true }).click();
  const dialog = page.getByRole('dialog', { name: 'Neuer Entwurf', exact: true });
  if (await dialog.isVisible()) {
    await dialog.getByLabel(de['features.authoring.CreateDraftDialog.name_optional_e09b37'], { exact: true }).fill('Hinweise und Aufbewahrung prüfen');
    await dialog.getByRole('button', { name: 'Entwurf anlegen', exact: true }).click();
    await dialog.waitFor({ state: 'hidden' });
  }
  await page.getByText('= 5 Minuten', { exact: true }).first().waitFor();
  await shot('05-benachrichtigungen.png', 'Getrennte Signal- und Konfigurationshinweise mit Minutenhilfe');

  await go('/settings/retention', 'Aufbewahrung');
  // Fresh navigation keeps the proposal visible; no retention rule is saved or activated.
  await page.getByLabel('Einzelmessungen aufbewahren (Tage)', { exact: true }).waitFor();
  await shot('06-aufbewahrung.png', 'Aufbewahrung als Vorschlag 7 / 730 über Entwurf');

  await go('/settings/system', 'System');
  await page.getByText('Mimir 1.0.0a9 (Alpha 9)', { exact: true }).waitFor();
  await page.getByText('Aufbewahrung fehlt', { exact: true }).waitFor();
  await shot('07-systemstatus.png', 'Alle offenen Voraussetzungen und dynamische Programmversion');

  await go('/', 'Übersicht');
  await page.getByRole('button', { name: 'Nicht bereit', exact: false }).click();
  await page.getByText('Aufbewahrung fehlt', { exact: true }).waitFor();
  await shot('08-kopfleiste-bereitschaft.png', 'Konfiguration im Kopf und vollständige Bereitschaftsliste');
  await page.keyboard.press('Escape');
  await shot('09-uebersicht.png', 'Signal gestört und Konfiguration unvollständig als eigene Bereiche');
  await page.getByRole('heading', { name: 'Konfiguration unvollständig', exact: true }).scrollIntoViewIfNeeded();
  await shot('10-vollstaendigkeit.png', 'Eigener Bereich für verwendbare Werte mit fehlenden Angaben');
  if (errors.length || external.length) throw new Error(JSON.stringify({ errors, external }));
  await writeFile(resolve(output, 'nachweis.json'), JSON.stringify({ capturedAt: new Date().toISOString(), engine: 'isolated real API, memory store, synthetic data', errors, external, shots }, null, 2)+'\n');
} finally { await browser.close(); }
