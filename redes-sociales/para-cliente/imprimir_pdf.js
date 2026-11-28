// Convierte para-cliente/revision.html en PDF.
// Uso (desde la raíz del repositorio): node redes-sociales/para-cliente/imprimir_pdf.js
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.join(__dirname, 'revision.html'));
  await page.evaluate(() => document.fonts.ready);
  const salida = path.join(__dirname, 'Revision_contenido_Bajo_el_Arbol.pdf');
  await page.pdf({
    path: salida,
    format: 'Letter',
    printBackground: true,
    preferCSSPageSize: true,
    displayHeaderFooter: true,
    headerTemplate: '<span></span>',
    footerTemplate:
      '<div style="width:100%;font:8px Arial;color:#777;padding:0 14mm;display:flex;justify-content:space-between">' +
      '<span>Revisión de contenido · Bajo el Árbol</span>' +
      '<span>Página <span class="pageNumber"></span> de <span class="totalPages"></span></span></div>',
  });
  await browser.close();
  console.log('ok', salida);
})();
