"""Arma la carpeta Bajo_el_Arbol lista para Cowork."""
import os
import shutil
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/user/bajo-el-arbol/redes-sociales"
UPL = "/root/.claude/uploads/f8889f2a-7da1-5d79-9967-f6747953b760"
DEST = os.path.join(AQUI, "Bajo_el_Arbol")

sys.path.insert(0, AQUI)
from datos import SEMANAS, CAL  # noqa: E402

if os.path.exists(DEST):
    shutil.rmtree(DEST)


def carpeta(*partes):
    p = os.path.join(DEST, *partes)
    os.makedirs(p, exist_ok=True)
    return p


def texto(ruta, contenido):
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(contenido.strip() + "\n")


def copiar(origen, *destino):
    d = os.path.join(DEST, *destino)
    os.makedirs(os.path.dirname(d), exist_ok=True)
    shutil.copy(origen, d)


WA = "223 143 0025"

# ------------------------------------------------------------------ 01 Contrato y plan
copiar(f"{UPL}/fd993e4d-Plan_de_Trabajo_Bajo_el_Arbol.pdf", "01_Contrato_y_plan", "Plan_de_Trabajo_Bajo_el_Arbol.pdf")
copiar(f"{UPL}/9a7ddf2e-Calendario_Navideno_Bajo_el_Arbol.pdf", "01_Contrato_y_plan", "Calendario_Navideno_Bajo_el_Arbol.pdf")
texto(os.path.join(carpeta("01_Contrato_y_plan"), "_LEEME.txt"), """
Aquí van los documentos firmados y los acuerdos con el cliente.
- Plan_de_Trabajo_Bajo_el_Arbol.pdf: método, servicio incluido, inversión, indicadores y condiciones.
- Calendario_Navideno_Bajo_el_Arbol.pdf: publicaciones del 10 nov al 31 dic y datos que debe entregar el negocio.
Cuando el cliente firme el acuerdo, guarde aquí la foto o el PDF firmado con el nombre:
  Acuerdo_firmado_AAAA-MM-DD.pdf
""")

# ------------------------------------------------------------------ 02 Marca
img = f"{REPO}/fuente/img"
copiar(f"{img}/logo.webp", "02_Marca", "Logo", "logo_bajo_el_arbol.webp")
for f in sorted(os.listdir(img)):
    if f in ("logo.webp", "qr-grupo.webp", "hojas.webp"):
        continue
    copiar(os.path.join(img, f), "02_Marca", "Fotos_del_sitio_web", f)
copiar(f"{img}/qr-grupo.webp", "02_Marca", "Logo", "qr_grupo_whatsapp.webp")
copiar(f"{img}/hojas.webp", "02_Marca", "Logo", "decoracion_hojas.webp")
texto(os.path.join(carpeta("02_Marca"), "Identidad_de_marca.txt"), """
IDENTIDAD DE MARCA · BAJO EL ÁRBOL, PANADERÍA Y CAFÉ

Colores
- Verde bosque (fondo oscuro): #0F1F14
- Verde: #1D3F26
- Dorado: #C8A25E (dorado claro #E6CD97)
- Crema (fondo claro): #FBF3E4
- Café (precios en fondo claro): #3F2412
- Verde WhatsApp (botones): #14783C

Tipografías (Google Fonts, gratuitas)
- Títulos: Playfair Display (normal 700 e itálica 500)
- Etiquetas y botones: Barlow Condensed (600, en mayúsculas con espaciado)
- Textos: Barlow (400 y 600)
- Frases manuscritas: Allura

Datos fijos
- Dirección: Camelia local C, INFONAVIT San José Xilotzingo, 72593, Puebla, Pue.
- Horario: 7:00 AM a 9:00 PM (confirmar días y horarios especiales con el dueño)
- WhatsApp de pedidos: 223 143 0025 · enlace: https://wa.me/522231430025
- Grupo de WhatsApp: https://chat.whatsapp.com/GNZ0RQuA6ud8ayOPIg0raE
- Opinión en Google: 5.0 · "Que café más rico y muy bonito lugar"

Tono
- Cálido, cercano y sencillo; se habla de "tú".
- Siempre cerrar con una invitación: pedir por WhatsApp, visitar o comentar.
- Hashtags base: #BajoElArbol #CafeteriaPuebla #CafePuebla #Xilotzingo #DesayunosPuebla

Formatos
- Feed (Facebook e Instagram): 1080 × 1350 px (4:5)
- Historias y Reels: 1080 × 1920 px (9:16); dejar libres 250 px arriba y abajo
""")

# ------------------------------------------------------------------ 03 Publicaciones
pub = f"{REPO}/publicaciones"
his = f"{REPO}/historias"
nav = f"{REPO}/temporada-navidad"
for f in sorted(os.listdir(pub)):
    copiar(os.path.join(pub, f), "03_Publicaciones", "00_Banco_de_respaldo", "Feed", f)
for f in sorted(os.listdir(his)):
    copiar(os.path.join(his, f), "03_Publicaciones", "00_Banco_de_respaldo", "Historias", f)
texto(os.path.join(carpeta("03_Publicaciones", "00_Banco_de_respaldo"), "_LEEME.txt"), """
Piezas aprobables que no dependen de datos pendientes.
Úselas como respaldo si un dato del cliente no llega a tiempo, o como anuncios.
- 02-desayunos y 05-chilaquiles: dos versiones del anuncio de mensajes por WhatsApp (16 al 22 nov).
- 03-cafe-y-pan, 06-frappes, 08-opinion: respaldo para cualquier día.
Los textos para publicarlas están en Textos_banco.txt.
""")
texto(os.path.join(DEST, "03_Publicaciones", "00_Banco_de_respaldo", "Textos_banco.txt"), f"""
03-cafe-y-pan.png
La pausa perfecta: café + pan dulce por $20. ☕🥐
Tu café de siempre y una concha, bajo el árbol.
📍 Camelia local C, INFONAVIT San José Xilotzingo · 📲 {WA}
#BajoElArbol #PanDulce #CafeYPan #CafePuebla #Xilotzingo

05-chilaquiles.png
El favorito del desayuno: chilaquiles. 🔥
🍳 Con huevo o pollo deshebrado — $49
🥩 Con bisteck o pechuga asada — $59
Y tú, ¿con qué los pides? Cuéntanos. 👇
📲 Pide por WhatsApp: {WA} · 🕖 Desde las 7:00 AM
#BajoElArbol #Chilaquiles #DesayunosPuebla #Xilotzingo

06-frappes.png
¿Cuál es tu favorito? 🥤
☕ Frappé Café $65 · 🍫 Frappé Moka $75 · 🍪 Frappé Oreo $80
Comenta Café, Moka u Oreo y etiqueta a quien te invitaría uno. 👇
📲 {WA}
#BajoElArbol #Frappe #CafePuebla #Xilotzingo

08-opinion.png
"Que café más rico y muy bonito lugar." ⭐⭐⭐⭐⭐
Gracias por sus palabras en Google. Comentarios así nos motivan a preparar cada taza con el mismo cariño. 💚
¿Ya nos visitaste? Déjanos tu opinión en Google Maps.
#BajoElArbol #ClientesFelices #CafePuebla #Xilotzingo
""")

NOMBRES = {1: "Semana_1_10-15nov", 2: "Semana_2_16-22nov", 3: "Semana_3_23-29nov", 4: "Semana_4_30nov-6dic",
           5: "Semana_5_7-13dic", 6: "Semana_6_14-20dic", 7: "Semana_7_21-27dic", 8: "Semana_8_28-31dic"}

# Semana 1
s1 = ("03_Publicaciones", NOMBRES[1])
for i, f in enumerate(["01-bienvenida.png", "04-nuestros-cafes.png", "02-desayunos.png", "07-como-pedir.png", "09-visitanos.png"], 1):
    copiar(os.path.join(pub, f), *s1, "P1_Carrusel_Conoce_12nov", f"{i}_{f[3:]}")
copiar(f"{nav}/2026-11-13-fin-de-semana-largo.png", *s1, "P2_Fin_de_semana_largo_13nov", "fin-de-semana-largo.png")
for i, f in enumerate(["03-ya-abrimos.png", "01-grupo-whatsapp.png", "02-encuesta.png"], 1):
    copiar(os.path.join(his, f), *s1, "P3_Historias", f"{i}_{f[3:]}")
texto(os.path.join(DEST, *s1, "Textos_para_publicar.txt"), f"""
SEMANA 1 · 10 al 15 de noviembre · Arranque y fin de semana largo

=== P1 · Jueves 12 nov · Carrusel "Conoce Bajo el Árbol" (5 imágenes, en el orden de la carpeta) ===
Un lugar para disfrutar, compartir y crear momentos inolvidables. 🌳☕

Somos Bajo el Árbol, panadería y café en INFONAVIT San José Xilotzingo. Desliza y conoce nuestros cafés, desayunos y cómo pedir. 👉

📍 Camelia local C, INFONAVIT San José Xilotzingo, Puebla
🕖 7:00 AM a 9:00 PM
📲 Pide por WhatsApp al {WA} o visítanos.

#BajoElArbol #CafeteriaPuebla #CafePuebla #Xilotzingo #PanaderiaPuebla #DesayunosPuebla

=== P2 · Viernes 13 nov · Fin de semana largo ===
¡Llegó el fin de semana largo! ☕🥐

Del viernes 13 al martes 17 de noviembre: [PRODUCTO Y PRECIO DE LA PROMOCIÓN — PENDIENTE DEL CLIENTE].

Ven a disfrutarlo bajo el árbol o pídelo por WhatsApp al {WA}.

📍 Camelia local C, INFONAVIT San José Xilotzingo
🕖 7:00 AM a 9:00 PM

#BajoElArbol #FinDeSemanaLargo #CafeYPan #CafePuebla #Xilotzingo
(No usar el nombre "El Buen Fin": solo pueden usarlo los comercios registrados.)

=== P3 · Historias (jueves, viernes y sábado) ===
1_ya-abrimos: agregar sticker de ENLACE a https://wa.me/522231430025 con el texto "Pedir ahora", sobre el botón verde.
2_grupo-whatsapp: agregar sticker de ENLACE a https://chat.whatsapp.com/GNZ0RQuA6ud8ayOPIg0raE con el texto "Unirme al grupo", debajo del QR.
3_encuesta: agregar sticker de ENCUESTA "Calientito ☕ / Frappé 🥤" en el espacio libre bajo las bebidas.
""")

# Semana 2
s2 = ("03_Publicaciones", NOMBRES[2])
copiar(f"{nav}/2026-11-16-lunes-festivo.png", *s2, "P4_Desayuno_de_puente_16nov", "desayuno-de-puente.png")
for i in range(1, 6):
    copiar(f"{nav}/2026-11-20-carrusel-desayunos-{i}.png", *s2, "P6_Carrusel_Desayunos_20nov", f"{i}_carrusel-desayunos.png")
carpeta(*s2, "P5_Video_pan_18nov")
texto(os.path.join(DEST, *s2, "P5_Video_pan_18nov", "Guion.txt"), f"""
VIDEO CORTO · Miércoles 18 nov · "Detrás de cámaras: así se prepara el pan"
Duración: 15 a 25 s · vertical 9:16 · luz natural

1 (0-3 s)   Manos amasando o formando conchas · texto: "¿Alguna vez viste cómo nace tu pan?"
2 (3-8 s)   Charola entrando al horno · texto: "Todo empieza muy temprano"
3 (8-14 s)  Pan saliendo del horno, con vapor
4 (14-20 s) Pan en la vitrina junto a una taza de café · texto: "Bajo el Árbol · Panadería y café"
5 (20-23 s) Logotipo o fachada · texto: "Síguenos para más"

Texto: Así empieza el día en Bajo el Árbol. 🥐 Síguenos para ver más de lo que pasa detrás del mostrador. 📲 {WA}
Guarde aquí los clips grabados y el video terminado.
""")
for i, f in enumerate(["06-frappes.png", "08-opinion.png"], 1):
    copiar(os.path.join(pub, f), *s2, "P7_Historias", f"{i}_{f[3:]}")
texto(os.path.join(DEST, *s2, "Textos_para_publicar.txt"), f"""
SEMANA 2 · 16 al 22 de noviembre · Desayunos

=== P4 · Lunes 16 nov (día festivo) · Desayuno de puente ===
(Confirmar con el cliente que abren y en qué horario.)
Lunes de puente = desayuno sin prisas. 🍳☕

Hoy también te esperamos de 7:00 AM a 9:00 PM. Desayunos desde $39: huevos al gusto, chilaquiles, enchiladas, arrachera y más.

📲 Pide por WhatsApp al {WA} y pasa por él, o desayuna con nosotros.

#BajoElArbol #DesayunosPuebla #DiaFestivo #Xilotzingo #CafeteriaPuebla

=== P5 · Miércoles 18 nov · Video del pan ===
Ver P5_Video_pan_18nov/Guion.txt

=== P6 · Viernes 20 nov · Carrusel "Desayunos Bajo el Árbol" (5 imágenes) ===
Desayunos hechos con amor, para empezar tu día perfecto. 🍳

Desliza y elige el tuyo 👉
01 Huevos al gusto — $39
02 Bisteck o pechuga asada — $49
03 Chilaquiles — $49 / $59
04 Enchiladas (5) — $49
05 Pechuga empanizada — $49
06 Tacos dorados (5) — $49
07 Arrachera — $69
08 Sopes (5) — $49 / $69
09 Enfrijoladas con pollo (5) — $49

☕ Café + pan dulce: $20
🥡 Para llevar: +$5 por contenedor

📲 Reserva o pide por WhatsApp: {WA}
🕖 Desde las 7:00 AM

Guarda esta publicación para tu próximo desayuno. 📌

#BajoElArbol #DesayunosPuebla #Chilaquiles #Xilotzingo #ComidaMexicana

=== P7 · Historias ===
1_frappes: compartir con sticker de ENCUESTA "¿Moka u Oreo?".
2_opinion: compartir tal cual.
3: un clip corto del video del pan (P5).
""")

# Semana 3
s3 = ("03_Publicaciones", NOMBRES[3])
texto(os.path.join(carpeta(*s3, "P8_Cajas_de_regalo_23nov"), "_PENDIENTE.txt"), """
PREVENTA DE CAJAS DE REGALO · Lunes 23 nov
Pendiente del cliente (antes del 20 nov): contenido de cada caja, precio, foto y días de anticipación para apartar.
Cuando llegue, pida a Claude: "Diseña la publicación P8 de cajas de regalo con estos datos".
""")
texto(os.path.join(carpeta(*s3, "P9_Video_capuchino_25nov"), "Guion.txt"), f"""
VIDEO CORTO · Miércoles 25 nov · "Así preparamos tu capuchino"
1 (0-3 s)   Granos cayendo al molino · "Del grano…"
2 (3-7 s)   Molienda y preparación del espresso · "…recién molido"
3 (7-12 s)  Vaporizado de la leche
4 (12-18 s) Arte latte en la taza, plano cenital · "…a tu taza"
5 (18-22 s) Taza servida bajo el árbol · "Capuchino desde $40 · Ven por el tuyo"
Texto: Del grano a la taza: así preparamos tu capuchino. ☕ Mediano $40 · Grande $50. Ven por el tuyo o pídelo al {WA}.
""")
texto(os.path.join(carpeta(*s3, "P10_Navidad_en_el_local_27nov"), "Guion.txt"), """
PUBLICACIÓN Y VIDEO · Viernes 27 nov · "Llegó la Navidad al local"
1 (0-4 s)   Paneo del árbol y la terraza con luces, al atardecer · "Llegó la Navidad bajo el árbol"
2 (4-10 s)  Detalles de la decoración: luces, adornos, mesas
3 (10-16 s) Chocolate caliente en una mesa decorada · "Ven a tomarte la foto"
4 (16-20 s) Fachada · "Camelia local C · Xilotzingo · 7:00 AM a 9:00 PM"
Texto: La Navidad ya llegó a Bajo el Árbol. 🎄✨ Ven a tomarte la foto con nuestras luces y acompáñala con un café.
📍 Camelia local C, INFONAVIT San José Xilotzingo.
Tome además 3 o 4 fotos fijas para la publicación y las historias.
Este video se usa también en el anuncio de reconocimiento.
""")

# Semanas 4 a 8: plan de la semana
for n, rango, tema in SEMANAS:
    if n <= 3:
        continue
    lineas = [f"SEMANA {n} · {rango} · {tema}", "", "Publicaciones del calendario:"]
    for (fe, sem, formato, pilar, pubn, cta, _c, _d, nota) in CAL:
        if sem == n:
            dia = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"][fe.weekday()]
            lineas.append(f"- {dia} {fe.day:02d}/{fe.month:02d} · {formato} · {pubn} · CTA: {cta}" + (f" · NOTA: {nota}" if nota else ""))
    lineas += ["- 3 historias: encuestas, detrás de cámaras o fotos de clientes (con permiso).", "",
               "Para prepararla, pida a Claude en Cowork:",
               f'"Prepara la semana {n} según CONTROL_DE_TAREAS.xlsx y el calendario navideño."']
    texto(os.path.join(carpeta("03_Publicaciones", NOMBRES[n]), "_PLAN_DE_LA_SEMANA.txt"), "\n".join(lineas))

# ------------------------------------------------------------------ 04 Revisión del cliente
copiar(f"{REPO}/para-cliente/Revision_contenido_Bajo_el_Arbol.pdf", "04_Revision_cliente", "Semanas_1-3_por_enviar", "Revision_contenido_Bajo_el_Arbol.pdf")
copiar(f"{REPO}/para-cliente/mensaje_whatsapp.txt", "04_Revision_cliente", "Semanas_1-3_por_enviar", "mensaje_whatsapp.txt")
texto(os.path.join(carpeta("04_Revision_cliente"), "_LEEME.txt"), """
Una carpeta por envío al cliente.
1. Mientras no se envía: Semanas_X-Y_por_enviar
2. Al enviarlo: cambie el nombre a Semanas_X-Y_enviado_AAAA-MM-DD
3. Guarde dentro las respuestas del cliente (capturas de WhatsApp o el PDF firmado) en una subcarpeta Respuestas.
4. Actualice la columna "Aprobado" de la pestaña Calendario en CONTROL_DE_TAREAS.xlsx.
""")

# ------------------------------------------------------------------ 05 Anuncios
texto(os.path.join(carpeta("05_Anuncios"), "Pauta_temporada.txt"), """
PUBLICIDAD PAGADA · Temporada navideña 2026 (Plan de trabajo y Calendario, p. 4)

Presupuesto: $1,000 MXN al mes, pagado a Meta con la tarjeta del negocio (≈ $33.33 al día)

Campaña 1 · Mensajes por WhatsApp · 70 % = $700 (≈ $23.33 al día)
- 16-22 nov: anuncios 02-desayunos y 05-chilaquiles (dos versiones; dejar la de menor costo por mensaje)
- 23 nov-18 dic: cajas de regalo y pan para posadas
- 19-31 dic: café y pan para el recalentado y fin de año

Campaña 2 · Reconocimiento en la zona · 30 % = $300 (= $10.00 al día)
- Carrusel "Conoce Bajo el Árbol" (12 nov) y, desde el 27 nov, video del local con luces navideñas

Segmentación de ambas: radio de 2 a 3 km alrededor del local; mayores de 18 años; feed e historias de Facebook e Instagram.
Regla semanal: costo por mensaje = inversión en anuncios ÷ mensajes recibidos; concentrar el presupuesto en el anuncio con menor costo.
Promoción exclusiva de los anuncios: PENDIENTE de definir con el dueño (agregarla al texto de los anuncios).
""")

# ------------------------------------------------------------------ 06 Reportes
texto(os.path.join(carpeta("06_Reportes"), "_LEEME.txt"), """
Guarde aquí:
- Captura de los números del punto de partida (antes de empezar).
- Cada reporte semanal enviado por WhatsApp: Reporte_semana_N_AAAA-MM-DD.pdf o .txt
- El reporte final del mes de prueba.
Los números se capturan en CONTROL_DE_TAREAS.xlsx (pestañas Punto de partida, Reporte semanal e Indicadores del mes).
""")
texto(os.path.join(DEST, "06_Reportes", "Plantilla_reporte_WhatsApp.txt"), """
Reporte semanal · Bajo el Árbol · [fechas]
💰 Gasto en anuncios: $___ (mensajes $___ · reconocimiento $___)
👥 Personas alcanzadas: ___
💬 Mensajes recibidos desde anuncios: ___ → costo por mensaje: $___
🎟️ Promociones del anuncio usadas: ___
📈 Lo que mejor funcionó: ___
🔧 Ajuste para la próxima semana: ___
""")

# ------------------------------------------------------------------ 07 Material del local
texto(os.path.join(carpeta("07_Material_del_local"), "_LEEME.txt"), """
Fotos y videos originales tomados en cada visita al local, sin editar.
Cree una subcarpeta por visita: Visita_AAAA-MM-DD
Nombre sugerido de archivos: tema_numero (ej. pan_horno_01.jpg, capuchino_arte_03.mp4).
""")

# ------------------------------------------------------------------ 08 Plantillas técnicas
for f in ("publicaciones.html", "fuentes.css", "exportar.js"):
    copiar(f"{REPO}/fuente/{f}", "08_Plantillas_tecnicas", f)
for f in sorted(os.listdir(img)):
    copiar(os.path.join(img, f), "08_Plantillas_tecnicas", "img", f)
texto(os.path.join(carpeta("08_Plantillas_tecnicas"), "_LEEME.txt"), """
Plantillas con las que se generaron las imágenes (HTML + script de exportación).
Úselas con Claude Code cuando quiera regenerar muchas piezas iguales (por ejemplo, si cambia un precio).
Para la operación diaria NO es necesario tocar esta carpeta.
Copia maestra: repositorio splua1312-blip/bajo-el-arbol, carpeta redes-sociales/.
""")

print("ok", DEST)
