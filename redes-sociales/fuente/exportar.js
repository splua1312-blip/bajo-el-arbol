// Exporta cada pieza de publicaciones.html a PNG en ../publicaciones y ../historias
// Uso (desde la raíz del repositorio): node redes-sociales/fuente/exportar.js
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 2000 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.join(__dirname, 'publicaciones.html'));
  await page.evaluate(() => document.fonts.ready);
  for (const el of await page.$$('section.pieza')) {
    const archivo = await el.getAttribute('data-archivo');
    await el.screenshot({ path: path.join(__dirname, '..', archivo) });
    console.log('ok', archivo);
  }
  await browser.close();
})();
