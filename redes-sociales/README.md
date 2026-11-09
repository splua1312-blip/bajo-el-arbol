# Bajo el Árbol · Plan de arranque en Facebook e Instagram

**Cliente:** Bajo el Árbol, Panadería y Café — Camelia local C, INFONAVIT San José Xilotzingo, Puebla.
**Servicio:** gestión de publicidad en Facebook e Instagram.
**Objetivo de esta primera etapa (3 semanas):** dar a conocer el lugar en la zona y convertir a quien vea las publicaciones en **pedidos por WhatsApp (223 143 0025)** y **visitas al local**.

Todos los datos de las piezas (precios, horario, dirección, opinión de Google) se tomaron de la página web del negocio (`index.html`). Antes de publicar, confirme con el cliente que los precios siguen vigentes.

---

## 1. Contenido de esta carpeta

| Carpeta | Contenido |
|---|---|
| `publicaciones/` | 9 piezas para el feed, formato vertical 4:5 (1080 × 1350 px). |
| `historias/` | 3 piezas para historias, formato 9:16 (1080 × 1920 px). |
| `fuente/` | Archivo editable `publicaciones.html`, imágenes y tipografías de la marca, y el script `exportar.js` para regenerar los PNG. |

**Por qué estos formatos.** Para anuncios de una sola imagen en el feed de Facebook, Meta recomienda la relación vertical 4:5 (Meta, s. f.-b). Asimismo, recomienda una resolución de 1080 × 1350 px para la relación 4:5 en el feed y de 1080 × 1920 px para la relación 9:16 en historias (Meta, s. f.-c). Además, el feed de Instagram admite imágenes de hasta 9:16, pero las recorta automáticamente a la relación recomendada de 4:5 (Meta, s. f.-d), por lo que 4:5 aprovecha al máximo el espacio vertical sin recortes.

**Cómo editar una pieza.** Abra `fuente/publicaciones.html`, cambie el texto o el precio y ejecute desde la raíz del repositorio:

```bash
node redes-sociales/fuente/exportar.js
```

---

## 2. Estrategia de contenido

### 2.1 Público objetivo
1. **Vecinos de Xilotzingo y colonias cercanas** que buscan desayunar o tomar un café sin desplazarse lejos.
2. **Trabajadores y estudiantes** de la zona con poco tiempo por la mañana (pedido rápido por WhatsApp).
3. **Parejas, amigos y familias** que buscan un lugar agradable por la tarde-noche (terraza bajo el árbol).

### 2.2 Pilares de contenido
Cada pieza responde a una etapa del embudo AIDA (Atención → Interés → Deseo → Acción):

| Pilar | Propósito | Piezas |
|---|---|---|
| **Ambiente** | Atención: mostrar el lugar y su identidad. | 01, 09 |
| **Antojo / producto** | Interés y deseo: platillos y bebidas con precio visible. | 02, 03, 04, 05, 06 |
| **Confianza** | Prueba social: opinión real de un cliente. | 08 |
| **Conversión** | Acción: explicar cómo pedir y dar el número. | 07, historias 01 y 03 |
| **Comunidad** | Interacción: preguntas y encuestas que generan comentarios. | 05, 06, historia 02 |

### 2.3 Reglas de comunicación de la marca
- **Tono:** cálido, cercano y sencillo; se habla de "tú".
- **Colores:** verde bosque `#0f1f14` / `#1d3f26`, dorado `#c8a25e`, crema `#fbf3e4` (los mismos del sitio web).
- **Tipografías:** Playfair Display (títulos), Barlow y Barlow Condensed (textos), Allura (frases manuscritas).
- **Siempre** cerrar con una llamada a la acción: pedir por WhatsApp, visitar o comentar.

---

## 3. Calendario de publicación (3 semanas)

Frecuencia propuesta: **3 publicaciones de feed por semana** (martes, jueves y sábado) y **al menos 1 historia diaria**.

| Fecha | Feed | Historias del día |
|---|---|---|
| Mar 10 nov 2026 | 01 · Bienvenida | H03 · Ya abrimos |
| Jue 12 nov 2026 | 02 · Desayunos desde $39 | H02 · Encuesta |
| Sáb 14 nov 2026 | 03 · Café + pan dulce $20 | H01 · Grupo de WhatsApp |
| Mar 17 nov 2026 | 04 · Nuestros cafés | H03 · Ya abrimos |
| Jue 19 nov 2026 | 05 · Chilaquiles | Compartir la publicación 05 en historia |
| Sáb 21 nov 2026 | 06 · Frappés | H02 · Encuesta |
| Mar 24 nov 2026 | 07 · Cómo pedir | H01 · Grupo de WhatsApp |
| Jue 26 nov 2026 | 08 · Opinión de cliente | H03 · Ya abrimos |
| Sáb 28 nov 2026 | 09 · Visítanos | Compartir la publicación 09 en historia |

**Horario sugerido:** las piezas de desayuno (02, 05) entre 7:00 y 8:00 AM, cuando se decide qué desayunar; las de bebidas y ambiente (03, 06, 09) entre 5:00 y 7:00 PM. Después de dos semanas, ajuste los horarios con los datos de **Meta Business Suite → Estadísticas → Público** (horas en que sus seguidores están conectados).

**Fijar en el perfil de Instagram:** 01 (Bienvenida), 07 (Cómo pedir) y 09 (Visítanos).

> Nota sobre la cuadrícula: las piezas alternan fondo oscuro y claro. Si se publican en el orden indicado, el perfil mostrará un patrón de tablero de ajedrez ordenado.

---

## 4. Textos listos para publicar (copys)

Enlace directo a WhatsApp para usar en Facebook y en la biografía de Instagram:
`https://wa.me/522231430025`

> En Instagram los enlaces dentro del texto no son clicables; ahí se indica "enlace en nuestro perfil" o se escribe el número.

### 01 · Bienvenida — `publicaciones/01-bienvenida.png`
```
Un lugar para disfrutar, compartir y crear momentos inolvidables. 🌳☕

Somos Bajo el Árbol, panadería y café en INFONAVIT San José Xilotzingo, Puebla. Café recién molido, desayunos hechos con amor y una terraza para quedarte un ratito más.

📍 Camelia local C, INFONAVIT San José Xilotzingo
🕖 7:00 AM a 9:00 PM
📲 Pedidos por WhatsApp: 223 143 0025

¿Ya nos conoces? Etiqueta a la persona con la que vendrías. 👇

#BajoElArbol #CafeteriaPuebla #CafePuebla #Xilotzingo #PanaderiaPuebla #DesayunosPuebla
```

### 02 · Desayunos — `publicaciones/02-desayunos.png`
```
Empieza tu día perfecto. 🍳

Huevos al gusto (revueltos con jamón, salchicha, estrellados u omelette) con frijoles y totopos desde $39.

¿Prefieres algo más? Tenemos chilaquiles, enchiladas, sopes, enfrijoladas, tacos dorados y arrachera.

📲 Pide por WhatsApp al 223 143 0025 y pasa por él, o desayuna con nosotros.
🕖 Desde las 7:00 AM.

#BajoElArbol #DesayunosPuebla #Xilotzingo #DesayunoMexicano #CafeteriaPuebla
```

### 03 · Café + pan dulce — `publicaciones/03-cafe-y-pan.png`
```
La pausa perfecta: café + pan dulce por $20. ☕🥐

Porque la tarde siempre sabe mejor con una concha y tu café de siempre, bajo el árbol.

📍 Camelia local C, INFONAVIT San José Xilotzingo
📲 223 143 0025

¿Concha de vainilla o de chocolate? Te leemos. 👇

#BajoElArbol #PanDulce #CafeYPan #CafePuebla #Xilotzingo
```
> Antes de publicar, confirme con el cliente qué sabores de pan maneja para que la pregunta final sea exacta.

### 04 · Nuestros cafés — `publicaciones/04-nuestros-cafes.png`
```
Preparado con café recién molido, hecho con pasión para ti. ☕

▫️ Americano desde $25
▫️ Latte desde $40
▫️ Capuchino desde $40
▫️ Flat White desde $40
▫️ Chocolate desde $40
▫️ Mocaccino desde $50

¿Cuál es el tuyo? Guarda esta publicación para tu próximo antojo. 📌

📲 Pedidos: 223 143 0025

#BajoElArbol #CafePuebla #Latte #Capuchino #CafeteriaPuebla #Xilotzingo
```

### 05 · Chilaquiles — `publicaciones/05-chilaquiles.png`
```
El favorito del desayuno: chilaquiles. 🔥

🍳 Con huevo o pollo deshebrado — $49
🥩 Con bisteck o pechuga asada — $59

Y tú, ¿con qué los pides? Cuéntanos en los comentarios. 👇

📲 Pide por WhatsApp: 223 143 0025
🕖 Desde las 7:00 AM

#BajoElArbol #Chilaquiles #DesayunosPuebla #Xilotzingo #ComidaMexicana
```

### 06 · Frappés — `publicaciones/06-frappes.png`
```
¿Cuál es tu favorito? 🥤

☕ Frappé Café — $65
🍫 Frappé Moka — $75
🍪 Frappé Oreo — $80

Comenta Café, Moka u Oreo y etiqueta a quien te invitaría uno. 👇

📲 223 143 0025

#BajoElArbol #Frappe #FrappeOreo #CafePuebla #Xilotzingo
```

### 07 · Cómo pedir — `publicaciones/07-como-pedir.png`
```
Pedir en Bajo el Árbol es muy fácil. 📲

1️⃣ Elige lo que se te antoje del menú.
2️⃣ Escríbenos por WhatsApp al 223 143 0025 con tu pedido (y una nota si la necesitas).
3️⃣ Te confirmamos por ahí y listo: pasa por él o disfrútalo aquí.

Sin filas y sin esperas. 🌳

#BajoElArbol #PedidosWhatsApp #CafeteriaPuebla #Xilotzingo
```

### 08 · Opinión — `publicaciones/08-opinion.png`
```
"Que café más rico y muy bonito lugar." ⭐⭐⭐⭐⭐

Gracias por sus palabras en Google. Comentarios así nos motivan a seguir preparando cada taza con el mismo cariño. 💚

¿Ya nos visitaste? Déjanos tu opinión en Google Maps; nos ayuda muchísimo.

#BajoElArbol #ClientesFelices #CafePuebla #Xilotzingo
```
> La cita es una opinión pública de Google Maps. Buena práctica: no mostrar el nombre de la persona sin su permiso (la pieza no lo muestra).

### 09 · Visítanos — `publicaciones/09-visitanos.png`
```
¡Te esperamos! 🌳

📍 Camelia local C, INFONAVIT San José Xilotzingo, Puebla
🕖 De 7:00 AM a 9:00 PM
📲 Pedidos por WhatsApp: 223 143 0025

Guarda esta publicación y compártela con quien siempre dice "¿a dónde vamos por un café?". ☕

#BajoElArbol #CafeteriaPuebla #Xilotzingo #PueblaCafe #DesayunosPuebla
```

### Historias (agregar los stickers dentro de Instagram/Facebook)
| Pieza | Sticker que debe agregarse | Dónde colocarlo |
|---|---|---|
| `historias/01-grupo-whatsapp.png` | **Enlace** → `https://chat.whatsapp.com/GNZ0RQuA6ud8ayOPIg0raE` con el texto "Unirme al grupo" | Debajo del código QR |
| `historias/02-encuesta.png` | **Encuesta** con las opciones "Calientito ☕" y "Frappé 🥤" | En el espacio libre bajo las dos bebidas |
| `historias/03-ya-abrimos.png` | **Enlace** → `https://wa.me/522231430025` con el texto "Pedir ahora" | Sobre el botón verde |

Las historias dejan libres los 250 px superiores e inferiores para que la interfaz de la aplicación no tape el contenido.

---

## 5. Pauta publicitaria (Meta Ads)

### 5.1 Qué publicaciones promocionar
1. **02 · Desayunos** y **05 · Chilaquiles** → anuncio de **mensajes a WhatsApp** (objetivo *Interacción* → ubicación de la conversión *Apps de mensajes* → *WhatsApp*). Son las piezas con precio visible y llamada directa a pedir.
2. **01 · Bienvenida** → anuncio de **reconocimiento / alcance** para dar a conocer el lugar en la colonia.
3. **03 · Café + pan $20** → prueba A/B contra 02 para comparar cuál genera conversaciones más baratas.

### 5.2 Segmentación inicial
- **Ubicación:** radio de 3 a 5 km alrededor de la dirección del local, opción "Personas que viven en esta ubicación o que estuvieron recientemente en ella".
- **Edad:** 18 a 55 años.
- **Intereses (opcional):** café, desayuno, panadería, cafeterías. En radios pequeños conviene dejar la segmentación amplia para que Meta encuentre al público.
- **Ubicaciones de anuncio:** feed e historias de Facebook e Instagram.

### 5.3 Presupuesto de prueba (ejemplo ilustrativo)
Los montos siguientes son una propuesta de arranque; deben ajustarse al presupuesto que acuerde con el cliente.

**Presupuesto total del periodo**

$$P_{total} = P_{diario} \times D$$

Con un presupuesto diario de $70 MXN durante 21 días:

$$P_{total} = 70 \times 21 = \$1{,}470 \text{ MXN}$$

**Reparto sugerido:** 60 % mensajes a WhatsApp ($882), 25 % alcance ($367.50) y 15 % prueba A/B ($220.50).

---

## 6. Métricas y fórmulas para medir resultados

Revise los datos cada semana en **Meta Business Suite** y en el **Administrador de anuncios**, y registre además en una hoja de cálculo cuántos pedidos por WhatsApp llegaron "porque vieron la publicidad" (pregunte al cliente: "¿cómo nos conociste?").

### 6.1 Métricas de anuncios

Los ejemplos de esta sección usan cifras hipotéticas de la **primera semana**: inversión de $70 × 7 días = **$490 MXN**. Sustitúyalas por los datos reales del Administrador de anuncios.

**CTR (tasa de clics en el enlace).** Meta la define como los clics en el enlace divididos entre las impresiones (Meta, s. f.-a):

$$CTR = \frac{\text{Clics en el enlace}}{\text{Impresiones}} \times 100$$

*Ejemplo:* 180 clics ÷ 12,000 impresiones × 100 = **1.5 %**.

**CPM (costo por cada mil impresiones):**

$$CPM = \frac{\text{Importe gastado}}{\text{Impresiones}} \times 1{,}000$$

*Ejemplo:* $490 ÷ 12,000 × 1,000 = **$40.83 MXN**.

**CPC (costo por clic):**

$$CPC = \frac{\text{Importe gastado}}{\text{Clics en el enlace}}$$

*Ejemplo:* $490 ÷ 180 = **$2.72 MXN**.

**Costo por conversación iniciada (la métrica principal de esta campaña):**

$$C_{conv} = \frac{\text{Importe gastado}}{\text{Conversaciones de WhatsApp iniciadas}}$$

*Ejemplo:* $490 ÷ 35 conversaciones = **$14.00 MXN** por conversación.

### 6.2 Métricas de negocio

**Tasa de cierre (de conversación a pedido):**

$$TC = \frac{\text{Pedidos concretados}}{\text{Conversaciones iniciadas}} \times 100$$

*Ejemplo:* 21 pedidos ÷ 35 conversaciones × 100 = **60 %**.

**Costo de adquisición por cliente (CAC):**

$$CAC = \frac{\text{Inversión en anuncios}}{\text{Clientes nuevos}}$$

*Ejemplo:* $490 ÷ 21 = **$23.33 MXN** por cliente.

**Ticket promedio:**

$$TP = \frac{\text{Ventas atribuidas a la campaña}}{\text{Número de pedidos}}$$

*Ejemplo:* un desayuno de $49 + un latte mediano de $40 = $89; si 21 pedidos suman $1,869, TP = $1,869 ÷ 21 = **$89 MXN**.

**ROAS (retorno sobre la inversión publicitaria):**

$$ROAS = \frac{\text{Ventas atribuidas a la campaña}}{\text{Inversión en anuncios}}$$

*Ejemplo:* $1,869 ÷ $490 = **3.81** (por cada peso invertido regresaron $3.81 en ventas).

**Punto de equilibrio de la publicidad.** Como el ROAS se calcula sobre ventas y no sobre utilidad, el negocio recupera la inversión solo si la ganancia bruta cubre el gasto. Con un margen bruto *m* (proporción de cada venta que queda después del costo de los insumos):

$$ROAS_{equilibrio} = \frac{1}{m}$$

*Ejemplo con margen supuesto de 60 % (confirmar con el cliente):* ROAS de equilibrio = 1 ÷ 0.60 = **1.67**. Un ROAS de 3.81 está por encima, por lo que la campaña sería rentable. El número mínimo de pedidos para recuperar la inversión sería:

$$N_{min} = \frac{\text{Inversión}}{TP \times m} = \frac{490}{89 \times 0.60} = 9.18 \approx 10 \text{ pedidos}$$

### 6.3 Métricas orgánicas (publicaciones sin pago)

**Tasa de interacción sobre alcance:**

$$TI = \frac{\text{Reacciones} + \text{Comentarios} + \text{Compartidos} + \text{Guardados}}{\text{Alcance}} \times 100$$

*Ejemplo:* (95 + 18 + 7 + 12) ÷ 2,400 × 100 = **5.5 %**.

**Crecimiento de seguidores:**

$$CS = \frac{\text{Seguidores al final} - \text{Seguidores al inicio}}{\text{Seguidores al inicio}} \times 100$$

### 6.4 Cómo decidir con los datos
- Si el **CTR** es bajo pero el **CPM** es normal, el problema es la pieza o el texto: pruebe otra imagen u otro gancho.
- Si hay muchos clics pero pocas **conversaciones**, revise el mensaje de bienvenida de WhatsApp y la rapidez de respuesta.
- Si hay conversaciones pero baja **tasa de cierre**, el problema está en la atención (tiempos de respuesta, disponibilidad o precios).
- Pause los anuncios con costo por conversación superior al promedio y traslade el presupuesto a los que mejor funcionan.

---

## 7. Lista de verificación antes de publicar
- [ ] Precios y horario confirmados con el cliente.
- [ ] Biografía de Instagram con dirección, horario y enlace a WhatsApp.
- [ ] Botón "Enviar mensaje" de WhatsApp activo en la página de Facebook.
- [ ] Cuentas de Facebook e Instagram vinculadas en Meta Business Suite.
- [ ] Respuestas rápidas preparadas en WhatsApp Business (menú, horario, ubicación).
- [ ] Hoja de registro de pedidos con la columna "¿Cómo nos conociste?".

---

## Referencias

Meta. (s. f.-a). *CTR (link click-through rate)*. Meta Business Help Center. Recuperado el 9 de noviembre de 2026, de https://www.facebook.com/business/help/877711998984611

Meta. (s. f.-b). *Best practices for aspect ratios in Meta ads*. Meta Business Help Center. Recuperado el 9 de noviembre de 2026, de https://www.facebook.com/business/help/103816146375741

Meta. (s. f.-c). *Design specifications for carousel ads*. Meta Business Help Center. Recuperado el 9 de noviembre de 2026, de https://www.facebook.com/business/help/1114358518575630

Meta. (s. f.-d). *Design requirements for Instagram Feed ads*. Meta Business Help Center. Recuperado el 9 de noviembre de 2026, de https://www.facebook.com/business/help/430958953753149
