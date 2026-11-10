# Bajo el Árbol · Material para Facebook e Instagram

**Cliente:** Panadería y Cafetería Bajo el Árbol — Camelia local C, INFONAVIT San José Xilotzingo, Puebla.
**Prestador del servicio:** Santiago Raúl Cortés Cortés.
**Documentos rectores:** *Plan de trabajo y acuerdo de servicio* (9 de noviembre de 2026) y *Calendario de contenido · Temporada navideña 2026* (10 de noviembre al 31 de diciembre de 2026).

Esta carpeta contiene las piezas gráficas, los textos y las guías de producción del **mes de prueba**, organizados según el calendario navideño. El objetivo es el del plan: que más vecinos conozcan Bajo el Árbol, escriban por WhatsApp (223 143 0025) y visiten el local, y comprobar con números si la publicidad funciona.

Los precios, el horario, la dirección y la opinión de Google se tomaron del sitio web del negocio (`index.html`). **Todo el contenido se envía al dueño para su aprobación antes de publicarse**, como establece el plan.

En esta guía, "dato N" se refiere al número de la tabla *Información que debe proporcionar el negocio* del calendario navideño (p. 5).

---

## 1. Contenido de la carpeta

| Carpeta | Contenido |
|---|---|
| `temporada-navidad/` | Piezas con fecha del calendario navideño (nombre del archivo = fecha de publicación). |
| `publicaciones/` | Banco de 9 piezas de feed (4:5) reutilizables: forman el carrusel del 12 de noviembre, sirven como anuncios y como respaldo. |
| `historias/` | 3 historias (9:16): grupo de WhatsApp, encuesta y "ya estamos tomando pedidos". |
| `fuente/` | Archivo editable `publicaciones.html`, imágenes y tipografías de la marca, y el script `exportar.js`. |

**Formatos.** Para anuncios de una sola imagen en el feed de Facebook, Meta recomienda la relación vertical 4:5 (Meta, s. f.-b), con una resolución de 1080 × 1350 px; para historias recomienda 9:16, a 1080 × 1920 px (Meta, s. f.-c). El feed de Instagram admite imágenes de hasta 9:16, pero las recorta automáticamente a 4:5 (Meta, s. f.-d), por lo que todas las piezas de feed se diseñaron en 4:5.

**Cómo editar.** Cambie el texto o el precio en `fuente/publicaciones.html` y ejecute desde la raíz del repositorio:

```bash
node redes-sociales/fuente/exportar.js
```

Para regenerar solo una parte, agregue una palabra de la ruta del archivo (por ejemplo, `navidad` o `desayunos`):

```bash
node redes-sociales/fuente/exportar.js navidad
```

---

## 2. Calendario de las semanas 1 a 3 con su material

Ritmo del plan: **3 publicaciones y 3 historias por semana**.

### Semana 1 · 10 al 15 de noviembre · Arranque y fin de semana largo

| Fecha | Formato | Material listo | Estado |
|---|---|---|---|
| Mar 10 nov | Tarea interna | Lista de verificación de la sección 6 | — |
| Jue 12 nov | Carrusel · *Conoce Bajo el Árbol* | Tarjetas en este orden: `publicaciones/01-bienvenida.png` → `04-nuestros-cafes.png` → `02-desayunos.png` → `07-como-pedir.png` → `09-visitanos.png` | Listo |
| Vie 13 nov | Publicación · *Fin de semana largo* | `temporada-navidad/2026-11-13-fin-de-semana-largo.png` | Falta el producto y el precio de la promoción (dato 4), que van solo en el texto |
| Historias | — | Jue: `historias/03-ya-abrimos.png` · Vie: `historias/01-grupo-whatsapp.png` · Sáb: `historias/02-encuesta.png` | Listo |

> La pieza del 13 de noviembre **no menciona "El Buen Fin"**, en línea con la nota del calendario: solo los comercios registrados pueden usar ese nombre y su logotipo. Se comunica como promoción de fin de semana largo.

### Semana 2 · 16 al 22 de noviembre · Desayunos

| Fecha | Formato | Material listo | Estado |
|---|---|---|---|
| Lun 16 nov | Publicación · *Día festivo* | `temporada-navidad/2026-11-16-lunes-festivo.png` | Confirmar que se abre el día festivo en horario normal (7:00 AM a 9:00 PM) |
| Mié 18 nov | Video corto · *Detrás de cámaras: el pan* | Guion 1 (sección 4) | Se graba en la visita al local |
| Vie 20 nov | Carrusel · *Desayunos Bajo el Árbol* | `temporada-navidad/2026-11-20-carrusel-desayunos-1.png` a `-5.png` | Precios tomados del sitio web; confirmar con el dueño (dato 5) |
| Historias | — | Compartir `publicaciones/06-frappes.png` con sticker de encuesta "¿Moka u Oreo?"; clip del detrás de cámaras; `publicaciones/08-opinion.png` | Listo / se graba |

### Semana 3 · 23 al 29 de noviembre · Arranque navideño

| Fecha | Formato | Material | Estado |
|---|---|---|---|
| Lun 23 nov | Publicación · *Regalos Bajo el Árbol* (preventa de cajas) | Se diseña al recibir el contenido, el precio y una foto de la caja (dato 6, antes del 20 de noviembre) | Pendiente del cliente |
| Mié 25 nov | Video corto · *Así preparamos tu capuchino* | Guion 2 (sección 4) | Se graba en la visita al local |
| Vie 27 nov | Publicación · *Llegó la Navidad al local* | Guion 3 (sección 4): foto y video del local decorado | Se toma cuando el local esté decorado |

**Piezas de respaldo.** Si un dato pendiente no llega a tiempo, la publicación de esa fecha se sustituye por una pieza del banco que no requiere confirmación: `03-cafe-y-pan.png`, `05-chilaquiles.png`, `06-frappes.png` u `08-opinion.png`.

**Publicaciones fijadas en Instagram:** el carrusel del 12 de noviembre, `07-como-pedir.png` y, a partir del 23 de noviembre, la preventa de cajas de regalo.

---

## 3. Textos para publicar (copys)

Enlace directo a WhatsApp para Facebook y la biografía de Instagram: `https://wa.me/522231430025`. En Instagram los enlaces dentro del texto no son clicables; ahí se escribe el número o se indica "enlace en nuestro perfil".

Cuando se defina la **promoción exclusiva de los anuncios** (dato 12), su frase se agrega al final de los textos que se usen como anuncio, por ejemplo: *"Menciona este anuncio y llévate [promoción]"*. Así se cuentan los clientes que llegan por la publicidad.

### Jue 12 nov · Carrusel *Conoce Bajo el Árbol*
```
Un lugar para disfrutar, compartir y crear momentos inolvidables. 🌳☕

Somos Bajo el Árbol, panadería y café en INFONAVIT San José Xilotzingo. Desliza y conoce nuestros cafés, desayunos y cómo pedir. 👉

📍 Camelia local C, INFONAVIT San José Xilotzingo, Puebla
🕖 7:00 AM a 9:00 PM
📲 Pide por WhatsApp al 223 143 0025 o visítanos.

#BajoElArbol #CafeteriaPuebla #CafePuebla #Xilotzingo #PanaderiaPuebla #DesayunosPuebla
```

### Vie 13 nov · *Fin de semana largo*
```
¡Llegó el fin de semana largo! ☕🥐

Del viernes 13 al martes 17 de noviembre: [PRODUCTO Y PRECIO DE LA PROMOCIÓN, POR CONFIRMAR].

Ven a disfrutarlo bajo el árbol o pídelo por WhatsApp al 223 143 0025.

📍 Camelia local C, INFONAVIT San José Xilotzingo
🕖 7:00 AM a 9:00 PM

#BajoElArbol #FinDeSemanaLargo #CafeYPan #CafePuebla #Xilotzingo
```

### Lun 16 nov · *Día festivo*
```
Lunes de puente = desayuno sin prisas. 🍳☕

Hoy también te esperamos de 7:00 AM a 9:00 PM. Desayunos desde $39: huevos al gusto, chilaquiles, enchiladas, arrachera y más.

📲 Pide por WhatsApp al 223 143 0025 y pasa por él, o desayuna con nosotros.

#BajoElArbol #DesayunosPuebla #DiaFestivo #Xilotzingo #CafeteriaPuebla
```

### Vie 20 nov · Carrusel *Desayunos Bajo el Árbol*
```
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

📲 Reserva o pide por WhatsApp: 223 143 0025
🕖 Desde las 7:00 AM

Guarda esta publicación para tu próximo desayuno. 📌

#BajoElArbol #DesayunosPuebla #Chilaquiles #Xilotzingo #ComidaMexicana
```

### Piezas del banco
Los textos siguientes sirven cuando una pieza del banco se publica sola, como respaldo o como anuncio.

**`03-cafe-y-pan.png`**
```
La pausa perfecta: café + pan dulce por $20. ☕🥐
Tu café de siempre y una concha, bajo el árbol.
📍 Camelia local C, INFONAVIT San José Xilotzingo · 📲 223 143 0025
#BajoElArbol #PanDulce #CafeYPan #CafePuebla #Xilotzingo
```

**`05-chilaquiles.png`**
```
El favorito del desayuno: chilaquiles. 🔥
🍳 Con huevo o pollo deshebrado — $49
🥩 Con bisteck o pechuga asada — $59
Y tú, ¿con qué los pides? Cuéntanos. 👇
📲 Pide por WhatsApp: 223 143 0025 · 🕖 Desde las 7:00 AM
#BajoElArbol #Chilaquiles #DesayunosPuebla #Xilotzingo
```

**`06-frappes.png`**
```
¿Cuál es tu favorito? 🥤
☕ Frappé Café $65 · 🍫 Frappé Moka $75 · 🍪 Frappé Oreo $80
Comenta Café, Moka u Oreo y etiqueta a quien te invitaría uno. 👇
📲 223 143 0025
#BajoElArbol #Frappe #CafePuebla #Xilotzingo
```

**`08-opinion.png`**
```
"Que café más rico y muy bonito lugar." ⭐⭐⭐⭐⭐
Gracias por sus palabras en Google. Comentarios así nos motivan a preparar cada taza con el mismo cariño. 💚
¿Ya nos visitaste? Déjanos tu opinión en Google Maps.
#BajoElArbol #ClientesFelices #CafePuebla #Xilotzingo
```
> La cita es una opinión pública de Google Maps; la pieza no muestra el nombre de la persona.

### Historias: stickers que se agregan en la aplicación

| Pieza | Sticker | Ubicación |
|---|---|---|
| `historias/01-grupo-whatsapp.png` | **Enlace** al grupo de WhatsApp (dato 11) con el texto "Unirme al grupo" | Debajo del código QR |
| `historias/02-encuesta.png` | **Encuesta**: "Calientito ☕" / "Frappé 🥤" | Espacio libre bajo las bebidas |
| `historias/03-ya-abrimos.png` | **Enlace** a `https://wa.me/522231430025` con el texto "Pedir ahora" | Sobre el botón verde |

Las historias dejan libres los 250 px superiores e inferiores para que la interfaz de la aplicación no tape el contenido.

---

## 4. Guiones de video corto (visita al local)

Duración recomendada: 15 a 25 segundos, formato vertical 9:16, grabado con el teléfono en posición vertical y con buena luz natural. Se publican como Reel en Instagram y se comparten en Facebook.

### Guion 1 · Mié 18 nov · *Detrás de cámaras: así se prepara el pan*
| Toma | Imagen | Texto en pantalla |
|---|---|---|
| 1 (0–3 s) | Manos amasando o formando conchas, plano cerrado | "¿Alguna vez viste cómo nace tu pan?" |
| 2 (3–8 s) | Charola entrando al horno | "Todo empieza muy temprano" |
| 3 (8–14 s) | Pan saliendo del horno; vapor | — |
| 4 (14–20 s) | Pan en la vitrina junto a una taza de café | "Bajo el Árbol · Panadería y café" |
| 5 (20–23 s) | Logotipo o fachada | "Síguenos para más" |

Texto: *"Así empieza el día en Bajo el Árbol. 🥐 Síguenos para ver más de lo que pasa detrás del mostrador. 📲 223 143 0025"*

### Guion 2 · Mié 25 nov · *Así preparamos tu capuchino*
| Toma | Imagen | Texto en pantalla |
|---|---|---|
| 1 (0–3 s) | Granos de café cayendo al molino | "Del grano…" |
| 2 (3–7 s) | Molienda y preparación del espresso | "…recién molido" |
| 3 (7–12 s) | Vaporizado de la leche | — |
| 4 (12–18 s) | Arte latte en la taza, plano cenital | "…a tu taza" |
| 5 (18–22 s) | Taza servida en la mesa, bajo el árbol | "Capuchino desde $40 · Ven por el tuyo" |

Texto: *"Del grano a la taza: así preparamos tu capuchino. ☕ Mediano $40 · Grande $50. Ven por el tuyo o pídelo al 223 143 0025."*

### Guion 3 · Vie 27 nov · *Llegó la Navidad al local*
| Toma | Imagen | Texto en pantalla |
|---|---|---|
| 1 (0–4 s) | Paneo del árbol y la terraza con las luces encendidas, al atardecer | "Llegó la Navidad bajo el árbol" |
| 2 (4–10 s) | Detalles de la decoración: luces, adornos, mesas | — |
| 3 (10–16 s) | Una taza o chocolate caliente sobre una mesa decorada | "Ven a tomarte la foto" |
| 4 (16–20 s) | Fachada con la dirección | "Camelia local C · Xilotzingo · 7:00 AM a 9:00 PM" |

Texto: *"La Navidad ya llegó a Bajo el Árbol. 🎄✨ Ven a tomarte la foto con nuestras luces y acompáñala con un café. 📍 Camelia local C, INFONAVIT San José Xilotzingo."*
> Este video se usa también en la campaña de reconocimiento (sección 5). Toma además 3 o 4 fotos fijas de la decoración para la publicación del día y para historias.

---

## 5. Publicidad pagada de la temporada

Según el plan y el calendario: **$1,000 MXN al mes**, pagados directamente a Meta con la tarjeta del negocio, divididos en **dos campañas**.

$$\text{Presupuesto diario} = \frac{\$1{,}000}{30 \text{ días}} \approx \$33.33 \text{ MXN}$$

| Campaña | Objetivo | Reparto | Presupuesto diario | Anuncios |
|---|---|---|---|---|
| 1. Mensajes por WhatsApp | Que los clientes escriban para pedir o preguntar | 70 % = $700 | $700 ÷ 30 ≈ **$23.33** | 16–22 nov: `02-desayunos.png` y `05-chilaquiles.png` como dos variantes · 23 nov–18 dic: cajas de regalo y pan para posadas · 19–31 dic: café y pan para el recalentado y fin de año |
| 2. Reconocimiento en la zona | Darse a conocer entre vecinos | 30 % = $300 | $300 ÷ 30 = **$10.00** | Carrusel del 12 nov y, desde el 27 nov, el video del local con luces navideñas |

**Segmentación de ambas campañas:** personas que viven en un radio de **2 a 3 km** alrededor del local o que estuvieron recientemente en esa zona; mayores de 18 años; ubicaciones en feed e historias de Facebook e Instagram. En un radio tan pequeño conviene no agregar demasiados intereses, para no reducir de más el público.

**Regla de ajuste semanal (calendario, p. 4):** se compara el costo por mensaje de cada anuncio y el presupuesto se concentra en el que tenga el menor costo. Por eso la primera semana de la campaña de mensajes lleva dos variantes (desayunos y chilaquiles).

---

## 6. Medición de resultados

### 6.1 Antes de empezar (mar 10 nov)
Registrar el **punto de partida**: seguidores en Facebook e Instagram, alcance de la última semana y mensajes de WhatsApp recibidos por semana. Con esos números se hará la comparación de antes y después del reporte final.

### 6.2 Reporte semanal por WhatsApp (formato sugerido)
```
Reporte semanal · Bajo el Árbol · [fechas]
💰 Gasto en anuncios: $___ (mensajes $___ · reconocimiento $___)
👥 Personas alcanzadas: ___
💬 Mensajes recibidos desde anuncios: ___ → costo por mensaje: $___
🎟️ Promociones del anuncio usadas: ___
📈 Lo que mejor funcionó: ___
🔧 Ajuste para la próxima semana: ___
```

### 6.3 Indicadores y fórmulas del plan

Los ejemplos siguientes usan **cifras hipotéticas del mes de prueba**, coherentes con el ejemplo del plan: inversión en anuncios de $1,000, servicio de $1,200, 50 mensajes, 20 promociones usadas por clientes nuevos e ingresos atribuidos de $6,000. No representan una promesa de resultados.

**Tasa de clics (CTR).** Meta la calcula como los clics en el enlace divididos entre las impresiones (Meta, s. f.-a):

$$CTR = \frac{\text{Clics}}{\text{Impresiones}} \times 100$$

*Ejemplo:* 300 clics ÷ 20,000 impresiones × 100 = **1.5 %**. Un CTR bajo indica que conviene cambiar la imagen o el texto.

**Costo por mensaje:**

$$\text{Costo por mensaje} = \frac{\text{Inversión en anuncios}}{\text{Mensajes recibidos}}$$

*Ejemplo:* $1,000 ÷ 50 = **$20.00 MXN** por mensaje.

**Tasa de conversión:**

$$\text{Tasa de conversión} = \frac{\text{Promociones usadas}}{\text{Mensajes recibidos}} \times 100$$

*Ejemplo:* 20 ÷ 50 × 100 = **40 %** de quienes escriben termina comprando.

**Costo de adquisición de cliente (CAC):**

$$CAC = \frac{\text{Inversión en anuncios} + \text{Servicio}}{\text{Clientes nuevos}}$$

*Ejemplo:* ($1,000 + $1,200) ÷ 20 = **$110.00 MXN** por cliente nuevo.

**Retorno sobre la inversión publicitaria (ROAS):**

$$ROAS = \frac{\text{Ingresos atribuidos}}{\text{Inversión en anuncios}}$$

*Ejemplo:* $6,000 ÷ $1,000 = **6.0**. Si el resultado es mayor que 1, los anuncios generan más ingresos de lo que cuestan.

**Retorno sobre la inversión (ROI):**

$$ROI = \frac{(\text{Ingresos atribuidos} \times \text{Margen bruto}) - \text{Costo total de marketing}}{\text{Costo total de marketing}} \times 100$$

*Ejemplo:* utilidad bruta = $6,000 × 0.60 = $3,600; costo total de marketing = $1,000 + $1,200 = $2,200; ROI = ($3,600 − $2,200) ÷ $2,200 × 100 = **63.6 %**.

**Punto de equilibrio del mes de prueba (ROI = 0).** Es el ingreso atribuido mínimo para que la utilidad bruta cubra todo el costo de marketing. Se obtiene igualando a cero el numerador del ROI y despejando:

$$\text{Ingresos}_{eq} = \frac{\text{Costo total de marketing}}{\text{Margen bruto}} = \frac{\$2{,}200}{0.60} = \$3{,}666.67 \text{ MXN}$$

Con un ticket promedio de $89 (por ejemplo, un desayuno de $49 y un latte mediano de $40), equivale a:

$$N_{eq} = \frac{\$3{,}666.67}{\$89} = 41.2 \approx 42 \text{ ventas atribuidas en el mes}$$

A partir del mes 2, con servicio de $1,800, el costo total de marketing sube a $2,800 y el punto de equilibrio a $2,800 ÷ 0.60 = **$4,666.67 MXN**. El margen de 60 % es un supuesto; debe sustituirse por el margen real del negocio.

---

## 7. Lista de verificación del arranque (mar 10 nov)
- [ ] Acceso de administrador en Meta Business Suite y tarjeta del negocio registrada en la cuenta publicitaria (datos 2 y 13).
- [ ] Registro del punto de partida (sección 6.1).
- [ ] Perfiles ajustados: foto, descripción, horario, botón de WhatsApp y enlace a la página web.
- [ ] Promoción exclusiva de los anuncios definida con el dueño (dato 12).
- [ ] Datos para la primera semana: producto y precio de la promoción de fin de semana largo (dato 4) y confirmación del horario del lunes 16 de noviembre.
- [ ] Aprobación del dueño de las piezas del 12, 13 y 16 de noviembre.
- [ ] Fecha de la visita al local para fotos y videos (guiones 1 y 2).

---

## Referencias

Meta. (s. f.-a). *CTR (link click-through rate)*. Meta Business Help Center. Recuperado el 9 de noviembre de 2026, de https://www.facebook.com/business/help/877711998984611

Meta. (s. f.-b). *Best practices for aspect ratios in Meta ads*. Meta Business Help Center. Recuperado el 9 de noviembre de 2026, de https://www.facebook.com/business/help/103816146375741

Meta. (s. f.-c). *Design specifications for carousel ads*. Meta Business Help Center. Recuperado el 9 de noviembre de 2026, de https://www.facebook.com/business/help/1114358518575630

Meta. (s. f.-d). *Design requirements for Instagram Feed ads*. Meta Business Help Center. Recuperado el 9 de noviembre de 2026, de https://www.facebook.com/business/help/430958953753149
