const path=require('path');const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+path.join(__dirname,'guia.html'));await p.evaluate(()=>document.fonts.ready);
await p.pdf({path:path.join(__dirname,'Bajo_el_Arbol','00_GUIA_DE_TRABAJO.pdf'),format:'Letter',printBackground:true,preferCSSPageSize:true,displayHeaderFooter:true,headerTemplate:'<span></span>',
footerTemplate:'<div style="width:100%;font:8px Arial;color:#777;padding:0 15mm;display:flex;justify-content:space-between"><span>Guía de trabajo · Bajo el Árbol</span><span>Página <span class="pageNumber"></span> de <span class="totalPages"></span></span></div>'});
await b.close();console.log('ok');})();
