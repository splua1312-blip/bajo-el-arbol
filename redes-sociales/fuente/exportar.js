// Exporta cada pieza de publicaciones.html a PNG (la ruta de salida está en data-archivo).
// Uso (desde la raíz del repositorio):
//   node redes-sociales/fuente/exportar.js            -> exporta todas las piezas
//   node redes-sociales/fuente/exportar.js navidad    -> solo las que contienen "navidad" en su ruta
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const filtro = process.argv[2] || '';

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 2000 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.join(__dirname, 'publicaciones.html'));
  await page.evaluate(() => document.fonts.ready);
  for (const el of await page.$$('section.pieza')) {
    const archivo = await el.getAttribute('data-archivo');
    if (!archivo.includes(filtro)) continue;
    const destino = path.join(__dirname, '..', archivo);
    fs.mkdirSync(path.dirname(destino), { recursive: true });
    await el.screenshot({ path: destino });
    console.log('ok', archivo);
  }
  await browser.close();
})();
