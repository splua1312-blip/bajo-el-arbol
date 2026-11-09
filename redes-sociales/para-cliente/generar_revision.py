"""Genera el documento de revisión para el cliente (HTML -> PDF).

Uso, desde la raíz del repositorio:
    python3 redes-sociales/para-cliente/generar_revision.py
    node redes-sociales/para-cliente/imprimir_pdf.js

Crea vistas JPEG comprimidas en para-cliente/.vistas/ y el archivo
para-cliente/revision.html, que imprimir_pdf.js convierte en PDF.
"""
import html
import os
from PIL import Image

BASE = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(BASE)  # redes-sociales/
VISTAS = os.path.join(BASE, ".vistas")
os.makedirs(VISTAS, exist_ok=True)


def vista(ruta):
    """Devuelve la ruta relativa de una vista JPEG de la pieza (la crea si no existe)."""
    origen = os.path.join(RAIZ, ruta)
    nombre = ruta.replace("/", "__").replace(".png", ".jpg")
    destino = os.path.join(VISTAS, nombre)
    if not os.path.exists(destino) or os.path.getmtime(destino) < os.path.getmtime(origen):
        im = Image.open(origen).convert("RGB")
        im.thumbnail((720, 1280))
        im.save(destino, quality=84, optimize=True)
    return ".vistas/" + nombre


WA = "223 143 0025"

# ------------------------------------------------------------------ contenido
SEMANAS = [
    {
        "titulo": "Semana 1 · 10 al 15 de noviembre",
        "tema": "Arranque y fin de semana largo",
        "limite": "Responder a más tardar el miércoles 11 de noviembre",
        "piezas": [
            {
                "id": "P1", "fecha": "Jueves 12 de noviembre", "formato": "Carrusel de 5 imágenes",
                "nombre": "Conoce Bajo el Árbol",
                "imgs": ["publicaciones/01-bienvenida.png", "publicaciones/04-nuestros-cafes.png",
                         "publicaciones/02-desayunos.png", "publicaciones/07-como-pedir.png",
                         "publicaciones/09-visitanos.png"],
                "texto": "Un lugar para disfrutar, compartir y crear momentos inolvidables. 🌳☕\n\n"
                         "Somos Bajo el Árbol, panadería y café en INFONAVIT San José Xilotzingo. Desliza y conoce "
                         "nuestros cafés, desayunos y cómo pedir. 👉\n\n"
                         "📍 Camelia local C, INFONAVIT San José Xilotzingo, Puebla\n🕖 7:00 AM a 9:00 PM\n"
                         f"📲 Pide por WhatsApp al {WA} o visítanos.\n\n"
                         "#BajoElArbol #CafeteriaPuebla #CafePuebla #Xilotzingo #PanaderiaPuebla #DesayunosPuebla",
                "confirmar": ["Que los precios de cafés y desayunos sigan vigentes.",
                              "Que el horario de 7:00 AM a 9:00 PM aplique todos los días que abren."],
                "nota": "Este carrusel también se usará en el anuncio para darse a conocer en la zona.",
            },
            {
                "id": "P2", "fecha": "Viernes 13 de noviembre", "formato": "Publicación",
                "nombre": "Fin de semana largo",
                "imgs": ["temporada-navidad/2026-11-13-fin-de-semana-largo.png"],
                "texto": "¡Llegó el fin de semana largo! ☕🥐\n\n"
                         "Del viernes 13 al martes 17 de noviembre: [PRODUCTO Y PRECIO DE LA PROMOCIÓN].\n\n"
                         f"Ven a disfrutarlo bajo el árbol o pídelo por WhatsApp al {WA}.\n\n"
                         "📍 Camelia local C, INFONAVIT San José Xilotzingo\n🕖 7:00 AM a 9:00 PM\n\n"
                         "#BajoElArbol #FinDeSemanaLargo #CafeYPan #CafePuebla #Xilotzingo",
                "confirmar": ["¿Qué incluye la promoción de café con pan y cuál es su precio?"],
                "nota": "El precio va solo en el texto, por eso la imagen no cambia. No se usa el nombre "
                        "\"El Buen Fin\", porque solo pueden usarlo los comercios registrados.",
            },
            {
                "id": "P3", "fecha": "Jueves 12 al sábado 14 de noviembre", "formato": "3 historias",
                "nombre": "Historias de la semana",
                "imgs": ["historias/03-ya-abrimos.png", "historias/01-grupo-whatsapp.png",
                         "historias/02-encuesta.png"],
                "texto": "Jueves: \"Ya estamos tomando pedidos\", con botón para escribir por WhatsApp.\n"
                         "Viernes: invitación al grupo de WhatsApp, con el código QR y un botón para unirse.\n"
                         "Sábado: encuesta \"¿Calientito o frappé?\".",
                "confirmar": ["Que el código QR y el enlace del grupo de WhatsApp sigan funcionando."],
                "nota": None,
            },
        ],
    },
    {
        "titulo": "Semana 2 · 16 al 22 de noviembre",
        "tema": "Desayunos",
        "limite": "Responder a más tardar el viernes 13 de noviembre",
        "piezas": [
            {
                "id": "P4", "fecha": "Lunes 16 de noviembre (día festivo)", "formato": "Publicación",
                "nombre": "Desayuno de puente",
                "imgs": ["temporada-navidad/2026-11-16-lunes-festivo.png"],
                "texto": "Lunes de puente = desayuno sin prisas. 🍳☕\n\n"
                         "Hoy también te esperamos de 7:00 AM a 9:00 PM. Desayunos desde $39: huevos al gusto, "
                         "chilaquiles, enchiladas, arrachera y más.\n\n"
                         f"📲 Pide por WhatsApp al {WA} y pasa por él, o desayuna con nosotros.\n\n"
                         "#BajoElArbol #DesayunosPuebla #DiaFestivo #Xilotzingo #CafeteriaPuebla",
                "confirmar": ["¿Abren el lunes 16? ¿En el horario de siempre, de 7:00 AM a 9:00 PM?"],
                "nota": None,
            },
            {
                "id": "P5", "fecha": "Miércoles 18 de noviembre", "formato": "Video corto (15 a 25 s)",
                "nombre": "Detrás de cámaras: así se prepara el pan",
                "imgs": [],
                "guion": ["Manos amasando o formando conchas · texto: \"¿Alguna vez viste cómo nace tu pan?\"",
                          "Charola entrando al horno · texto: \"Todo empieza muy temprano\"",
                          "Pan saliendo del horno, con vapor",
                          "Pan en la vitrina junto a una taza de café",
                          "Logotipo o fachada · texto: \"Síguenos para más\""],
                "texto": "Así empieza el día en Bajo el Árbol. 🥐 Síguenos para ver más de lo que pasa detrás "
                         f"del mostrador. 📲 {WA}",
                "confirmar": ["Día y hora en que se hornea el pan, para grabar durante la visita al local."],
                "nota": "Se aprueba la idea; el video terminado se le enviará antes de publicarlo.",
            },
            {
                "id": "P6", "fecha": "Viernes 20 de noviembre", "formato": "Carrusel de 5 imágenes",
                "nombre": "Desayunos Bajo el Árbol",
                "imgs": [f"temporada-navidad/2026-11-20-carrusel-desayunos-{i}.png" for i in range(1, 6)],
                "texto": "Desayunos hechos con amor, para empezar tu día perfecto. 🍳\n\nDesliza y elige el tuyo 👉\n"
                         "01 Huevos al gusto — $39\n02 Bisteck o pechuga asada — $49\n03 Chilaquiles — $49 / $59\n"
                         "04 Enchiladas (5) — $49\n05 Pechuga empanizada — $49\n06 Tacos dorados (5) — $49\n"
                         "07 Arrachera — $69\n08 Sopes (5) — $49 / $69\n09 Enfrijoladas con pollo (5) — $49\n\n"
                         "☕ Café + pan dulce: $20\n🥡 Para llevar: +$5 por contenedor\n\n"
                         f"📲 Reserva o pide por WhatsApp: {WA}\n🕖 Desde las 7:00 AM\n\n"
                         "#BajoElArbol #DesayunosPuebla #Chilaquiles #Xilotzingo #ComidaMexicana",
                "confirmar": ["Que los 9 platillos y sus precios estén vigentes."],
                "nota": None,
            },
            {
                "id": "P7", "fecha": "Durante la semana 2", "formato": "3 historias",
                "nombre": "Historias de la semana",
                "imgs": ["publicaciones/06-frappes.png", "publicaciones/08-opinion.png"],
                "texto": "1) Frappés con encuesta \"¿Moka u Oreo?\".\n"
                         "2) Opinión de un cliente en Google (sin mostrar su nombre).\n"
                         "3) Un clip corto del video del pan (P5).",
                "confirmar": None,
                "nota": None,
            },
        ],
    },
    {
        "titulo": "Semana 3 · 23 al 29 de noviembre",
        "tema": "Arranque navideño",
        "limite": "Responder a más tardar el viernes 20 de noviembre",
        "piezas": [
            {
                "id": "P8", "fecha": "Lunes 23 de noviembre", "formato": "Publicación",
                "nombre": "Regalos Bajo el Árbol: preventa de cajas de pan",
                "imgs": [],
                "texto": "La pieza se diseña en cuanto se reciba la información de las cajas.",
                "confirmar": ["¿Qué contiene cada caja de regalo y cuál es su precio?",
                              "Una foto de la caja (o la tomamos en la visita al local).",
                              "¿Con cuántos días de anticipación deben apartarse?"],
                "nota": None,
            },
            {
                "id": "P9", "fecha": "Miércoles 25 de noviembre", "formato": "Video corto (15 a 25 s)",
                "nombre": "Así preparamos tu capuchino",
                "imgs": [],
                "guion": ["Granos cayendo al molino · texto: \"Del grano…\"",
                          "Molienda y preparación del espresso · texto: \"…recién molido\"",
                          "Vaporizado de la leche",
                          "Arte latte en la taza · texto: \"…a tu taza\"",
                          "Taza servida bajo el árbol · texto: \"Capuchino desde $40 · Ven por el tuyo\""],
                "texto": "Del grano a la taza: así preparamos tu capuchino. ☕ Mediano $40 · Grande $50. "
                         f"Ven por el tuyo o pídelo al {WA}.",
                "confirmar": None,
                "nota": "Se aprueba la idea; el video terminado se le enviará antes de publicarlo.",
            },
            {
                "id": "P10", "fecha": "Viernes 27 de noviembre", "formato": "Publicación y video",
                "nombre": "Llegó la Navidad al local",
                "imgs": [],
                "guion": ["Paneo del árbol y la terraza con luces, al atardecer · \"Llegó la Navidad bajo el árbol\"",
                          "Detalles de la decoración: luces, adornos, mesas",
                          "Chocolate caliente sobre una mesa decorada · \"Ven a tomarte la foto\"",
                          "Fachada con dirección y horario"],
                "texto": "La Navidad ya llegó a Bajo el Árbol. 🎄✨ Ven a tomarte la foto con nuestras luces y "
                         "acompáñala con un café. 📍 Camelia local C, INFONAVIT San José Xilotzingo.",
                "confirmar": ["¿Qué día estará decorado el local, para tomar las fotos y el video?"],
                "nota": "Este video se usará también en el anuncio para darse a conocer en la zona.",
            },
        ],
    },
]

RESPALDO = {
    "id": "P11", "nombre": "Piezas de respaldo y anuncios",
    "imgs": ["publicaciones/02-desayunos.png", "publicaciones/05-chilaquiles.png",
             "publicaciones/03-cafe-y-pan.png", "publicaciones/06-frappes.png", "publicaciones/08-opinion.png"],
    "texto": "Desayunos y Chilaquiles son las dos versiones del anuncio de mensajes por WhatsApp del 16 al 22 de "
             "noviembre; después se deja activa la que consiga mensajes a menor costo. Café + pan, Frappés y "
             "Opinión se publican si algún dato pendiente no llega a tiempo, para no dejar días vacíos.",
}

PENDIENTES = [
    ("Producto y precio de la promoción de fin de semana largo", "P2", "11 nov"),
    ("¿Abren el lunes 16 de noviembre? ¿En qué horario?", "P4", "11 nov"),
    ("Promoción exclusiva de los anuncios (por ejemplo: menciona el anuncio y llévate un pan de regalo con tu café)",
     "Anuncios", "11 nov"),
    ("Acceso de administrador en Meta Business Suite y tarjeta registrada en la cuenta publicitaria",
     "Anuncios", "11 nov"),
    ("Confirmar precios del menú de cafés y desayunos", "P1, P6", "13 nov"),
    ("Fecha para la visita al local (fotos y videos)", "P5, P9", "13 nov"),
    ("Contenido, precio y foto de las cajas de regalo", "P8", "20 nov"),
    ("Día en que el local estará decorado", "P10", "20 nov"),
]

# ------------------------------------------------------------------ plantilla
e = html.escape


def bloque_pieza(p):
    imgs = p.get("imgs") or []
    if len(imgs) == 1:
        galeria = f'<div class="galeria una"><img src="{vista(imgs[0])}"></div>'
    elif imgs:
        clase = "historias" if all(i.startswith("historias/") for i in imgs) else "varias"
        celdas = "".join(f'<figure><img src="{vista(i)}"><figcaption>{n}</figcaption></figure>'
                         for n, i in enumerate(imgs, 1))
        galeria = f'<div class="galeria {clase}">{celdas}</div>'
    else:
        galeria = ""
    guion = ""
    if p.get("guion"):
        guion = '<div class="guion"><h4>Tomas del video</h4><ol>' + \
                "".join(f"<li>{e(t)}</li>" for t in p["guion"]) + "</ol></div>"
    confirmar = ""
    if p.get("confirmar"):
        confirmar = '<div class="confirmar"><h4>Necesitamos que nos confirme</h4><ul>' + \
                    "".join(f"<li>{e(c)}</li>" for c in p["confirmar"]) + "</ul></div>"
    nota = f'<p class="nota">{e(p["nota"])}</p>' if p.get("nota") else ""
    texto = e(p["texto"]).replace("[PRODUCTO Y PRECIO DE LA PROMOCIÓN]",
                                  '<mark>[PRODUCTO Y PRECIO DE LA PROMOCIÓN]</mark>')
    sin_imagen = "" if imgs else " sin-imagen"
    lado = len(imgs) == 1
    clase = sin_imagen + (" lado" if lado else "")
    izq = f'<div class="col-img">{galeria}</div><div class="col-txt">' if lado else galeria
    cierre = "</div>" if lado else ""
    return f"""
<article class="pieza{clase}">
  <header>
    <span class="id">{p['id']}</span>
    <div><h3>{e(p['nombre'])}</h3><p>{e(p['fecha'])} · {e(p['formato'])}</p></div>
  </header>
  <div class="cuerpo">{izq}
  {guion}
  <div class="texto"><h4>Texto de la publicación</h4><pre>{texto}</pre></div>
  {confirmar}
  {nota}
  <div class="decision">
    <span><i></i>Aprobado</span><span><i></i>Aprobado con cambios</span><span><i></i>No publicar</span>
    <div class="cambios">Cambios o comentarios:</div>
  </div>{cierre}</div>
</article>"""


def semana(s):
    piezas = "".join(bloque_pieza(p) for p in s["piezas"])
    return f"""
<section class="semana">
  <div class="cab-semana"><div><h2>{e(s['titulo'])}</h2><p>{e(s['tema'])}</p></div>
  <span class="limite">{e(s['limite'])}</span></div>
  {piezas}
</section>"""


filas_resumen = "".join(
    f"<tr><td>{p['id']}</td><td>{e(p['fecha'])}</td><td>{e(p['nombre'])}</td><td>{e(p['formato'])}</td></tr>"
    for s in SEMANAS for p in s["piezas"])
filas_pend = "".join(
    f"<tr><td>{n}</td><td>{e(d)}</td><td>{e(para)}</td><td>{e(f)}</td></tr>"
    for n, (d, para, f) in enumerate(PENDIENTES, 1))
filas_firma = "".join(
    f"<tr><td>{p['id']}</td><td>{e(p['nombre'])}</td><td></td><td></td></tr>"
    for s in SEMANAS for p in s["piezas"]) + \
    f"<tr><td>{RESPALDO['id']}</td><td>{e(RESPALDO['nombre'])}</td><td></td><td></td></tr>"

respaldo_celdas = "".join(f'<figure><img src="{vista(i)}"></figure>' for i in RESPALDO["imgs"])

DOC = f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<title>Revisión de contenido · Bajo el Árbol</title>
<link rel="stylesheet" href="../fuente/fuentes.css">
<style>
@page {{ size: Letter; margin: 14mm 14mm 16mm; }}
:root{{--verde:#1d3f26;--bosque:#0f1f14;--oro:#b48a45;--crema:#fbf3e4;--papel:#f4ead8;--tinta:#1c2a1e;--cafe:#3f2412;--linea:#e2d3b5}}
*{{box-sizing:border-box}}
body{{margin:0;font:400 10.5pt/1.45 "Barlow",Arial,sans-serif;color:var(--tinta)}}
h1,h2,h3,h4{{margin:0;font-family:"Playfair Display",Georgia,serif;color:var(--verde)}}
p{{margin:0}}
.portada{{height:248mm;display:flex;flex-direction:column;justify-content:center;page-break-after:always;position:relative}}
.portada .franja{{position:absolute;top:0;left:0;right:0;height:6mm;background:var(--verde);border-bottom:2mm solid var(--oro)}}
.portada img.logo{{width:42mm;margin-bottom:10mm}}
.portada .eti{{font:600 10pt/1 "Barlow Condensed",sans-serif;letter-spacing:.2em;text-transform:uppercase;color:var(--oro)}}
.portada h1{{font-size:34pt;line-height:1.05;margin-top:4mm}}
.portada .sub{{font-size:13pt;margin-top:4mm;color:#4a4a4a}}
.portada table{{margin-top:14mm}}
.intro{{margin-top:12mm;font-size:11pt;max-width:165mm}}
table{{border-collapse:collapse;width:100%}}
th,td{{text-align:left;padding:2.2mm 3mm;border-bottom:.3mm solid var(--linea);vertical-align:top}}
th{{background:var(--verde);color:#fff;font:600 9.5pt/1.2 "Barlow",sans-serif}}
tr:nth-child(even) td{{background:#faf5ea}}
.datos td:first-child{{font-weight:600;color:var(--verde);width:42mm}}
.datos td{{background:none!important}}
h2.sec{{font-size:18pt;margin:0 0 4mm}}
.pasos{{counter-reset:p;margin:0 0 6mm;padding:0;list-style:none}}
.pasos li{{counter-increment:p;position:relative;padding:2mm 0 2mm 11mm}}
.pasos li::before{{content:counter(p);position:absolute;left:0;top:1.4mm;width:7mm;height:7mm;border-radius:50%;background:var(--oro);color:#fff;font:700 10pt/7mm "Barlow",sans-serif;text-align:center}}
.bloque{{page-break-after:always}}
.semana{{page-break-before:always}}
.cab-semana{{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:.8mm solid var(--oro);padding-bottom:3mm;margin-bottom:5mm}}
.cab-semana h2{{font-size:20pt}}
.cab-semana p{{color:#6b5a3e;font-size:11pt}}
.limite{{background:#fff4d6;border:.3mm solid #e8c97a;color:#7a5410;border-radius:2mm;padding:1.5mm 3mm;font:600 9pt/1.2 "Barlow",sans-serif}}
.pieza{{border:.3mm solid var(--linea);border-radius:3mm;padding:4mm 5mm;margin-bottom:4mm;page-break-inside:avoid;background:#fff}}
.pieza header{{display:flex;gap:4mm;align-items:center;margin-bottom:4mm}}
.pieza .id{{flex:none;background:var(--verde);color:#fff;border-radius:2mm;padding:1.5mm 3mm;font:700 11pt/1 "Barlow",sans-serif}}
.pieza h3{{font-size:14pt}}
.pieza header p{{color:#6b5a3e;font-size:9.5pt}}
.galeria{{display:flex;gap:3mm;margin-bottom:4mm;justify-content:center}}
.galeria img{{display:block;width:100%;border-radius:1.5mm;border:.3mm solid var(--linea)}}
.galeria.una img{{width:78mm}}
.pieza.lado .cuerpo{{display:grid;grid-template-columns:50mm 1fr;gap:5mm;align-items:start}}
.pieza.lado .galeria{{margin:0}}
.pieza.lado .galeria.una img{{width:50mm}}
.grupo{{break-inside:avoid;page-break-inside:avoid}}
.galeria.varias figure{{margin:0;flex:1}}
.galeria.historias figure{{margin:0;width:29mm}}
.galeria figcaption{{text-align:center;font:600 8pt/1 "Barlow",sans-serif;color:#8a7650;margin-top:1.2mm}}
h4{{font:600 8.5pt/1 "Barlow Condensed",sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--oro);margin-bottom:1.5mm}}
.texto pre{{white-space:pre-wrap;font:400 9pt/1.4 "Barlow",sans-serif;background:var(--papel);border-radius:2mm;padding:3mm 4mm;margin:0}}
mark{{background:#ffe08a;padding:0 1mm}}
.guion ol{{margin:0 0 4mm;padding-left:5mm;font-size:9.5pt}}
.confirmar{{margin-top:3mm;background:#fff7e0;border-left:1.2mm solid #e0a92e;border-radius:1.5mm;padding:2.5mm 4mm}}
.confirmar ul{{margin:0;padding-left:5mm;font-size:9.5pt}}
.nota{{margin-top:3mm;font-size:9pt;color:#5d5d5d;font-style:italic}}
.decision{{margin-top:4mm;border-top:.3mm dashed #cbb88f;padding-top:3mm;display:flex;flex-wrap:wrap;gap:3mm 8mm;font:600 9.5pt/1 "Barlow",sans-serif;color:var(--verde)}}
.decision span{{display:flex;align-items:center;gap:2mm}}
.decision i{{width:4.5mm;height:4.5mm;border:.4mm solid var(--verde);border-radius:1mm;display:inline-block}}
.decision .cambios{{flex-basis:100%;font-weight:400;color:#6b6b6b;border-bottom:.3mm solid #d9cdb4;padding-bottom:6mm}}
.respaldo .galeria figure{{margin:0;flex:1}}
.firma td{{height:9mm}}
.firma td:nth-child(3),.firma td:nth-child(4){{width:30mm}}
.lineas{{display:grid;grid-template-columns:1fr 1fr;gap:10mm;margin-top:12mm}}
.lineas div{{border-top:.3mm solid #555;padding-top:2mm;font-size:9.5pt;color:#555}}
.pie-doc{{margin-top:8mm;font-size:9pt;color:#6b6b6b}}
</style></head><body>

<section class="portada">
  <div class="franja"></div>
  <img class="logo" src="../fuente/img/logo.webp">
  <div class="eti">Revisión y autorización de contenido</div>
  <h1>Publicaciones para Facebook<br>e Instagram</h1>
  <p class="sub">Panadería y Cafetería <b>Bajo el Árbol</b> · Temporada navideña 2026 · Semanas 1 a 3 (12 al 27 de noviembre)</p>
  <table class="datos">
    <tr><td>Preparado por</td><td>Santiago Raúl Cortés Cortés</td></tr>
    <tr><td>Contacto</td><td>WhatsApp 222 954 9368</td></tr>
    <tr><td>Fecha</td><td>9 de noviembre de 2026</td></tr>
    <tr><td>Referencia</td><td>Plan de trabajo y calendario de contenido navideño</td></tr>
  </table>
  <p class="intro">Como acordamos en el plan de trabajo, ninguna publicación sale sin su autorización. En este documento
  encontrará cada imagen, la fecha en que se publicaría, el texto que la acompaña y los datos que necesitamos que nos confirme.</p>
</section>

<section class="bloque">
  <h2 class="sec">Cómo revisar este documento</h2>
  <ol class="pasos">
    <li>Revise cada pieza (P1 a P11): la imagen, el texto y los datos marcados en amarillo.</li>
    <li>Marque en cada una <b>Aprobado</b>, <b>Aprobado con cambios</b> o <b>No publicar</b>, y anote los cambios que quiera.</li>
    <li>Respóndanos por WhatsApp. Basta un mensaje como <i>"Apruebo P1, P3 y P6. En P2 la promoción es café americano + concha a $35"</i>, o una foto de la última página firmada.</li>
    <li>Envíe los datos pendientes de la tabla de abajo. Las piezas que dependen de un dato no se publican hasta tenerlo.</li>
  </ol>
  <h2 class="sec">Resumen de publicaciones</h2>
  <table><tr><th>Pieza</th><th>Fecha</th><th>Publicación</th><th>Formato</th></tr>{filas_resumen}
  <tr><td>P11</td><td>Según se necesite</td><td>{e(RESPALDO['nombre'])}</td><td>5 imágenes</td></tr></table>
  <div class="grupo"><h2 class="sec" style="margin-top:8mm">Datos que necesitamos de usted</h2>
  <table><tr><th>#</th><th>Dato</th><th>Para</th><th>Antes del</th></tr>{filas_pend}</table></div>
</section>

{''.join(semana(s) for s in SEMANAS)}

<section class="semana respaldo">
  <div class="cab-semana"><div><h2>Piezas de respaldo y anuncios</h2><p>Se usan cuando se necesitan</p></div></div>
  <article class="pieza">
    <header><span class="id">{RESPALDO['id']}</span><div><h3>{e(RESPALDO['nombre'])}</h3><p>Desayunos · Chilaquiles · Café + pan · Frappés · Opinión</p></div></header>
    <div class="galeria varias">{respaldo_celdas}</div>
    <p style="font-size:9.5pt">{e(RESPALDO['texto'])}</p>
    <div class="decision"><span><i></i>Aprobado</span><span><i></i>Aprobado con cambios</span><span><i></i>No publicar</span>
    <div class="cambios">Cambios o comentarios:</div></div>
  </article>
  <h2 class="sec" style="margin-top:6mm">Anuncios pagados</h2>
  <p style="font-size:10pt">Presupuesto de <b>$1,000 MXN al mes</b>, pagado directamente a Meta con la tarjeta del negocio:
  <b>$700</b> para que los clientes escriban por WhatsApp y <b>$300</b> para darse a conocer entre los vecinos en un radio de
  <b>2 a 3 km</b>. Cada semana le enviaremos por WhatsApp el gasto, las personas alcanzadas, los mensajes recibidos y las promociones usadas.</p>
</section>

<section class="semana">
  <div class="cab-semana"><div><h2>Autorización</h2><p>Marque cada pieza y firme</p></div></div>
  <table class="firma"><tr><th>Pieza</th><th>Publicación</th><th>Aprobada (sí / no)</th><th>Iniciales</th></tr>{filas_firma}</table>
  <p class="pie-doc">Al firmar, el cliente autoriza la publicación de las piezas marcadas como aprobadas, con los cambios anotados.
  Las piezas que dependen de un dato pendiente se publicarán una vez recibido ese dato.</p>
  <div class="lineas"><div>Nombre y firma del cliente</div><div>Fecha</div></div>
</section>
</body></html>"""

with open(os.path.join(BASE, "revision.html"), "w", encoding="utf-8") as f:
    f.write(DOC)
print("ok revision.html")
