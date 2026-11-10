import sys
from datetime import date, timedelta
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.comments import Comment
from openpyxl.utils import get_column_letter

sys.path.insert(0, sys.argv[2])
from datos import CAL, PENDIENTES, SEMANAS

SALIDA = sys.argv[1]
F = "Arial"
VERDE = "1D3F26"
ORO = "B48A45"
AMARILLO = PatternFill("solid", fgColor="FFF2B3")
GRIS = PatternFill("solid", fgColor="F2F2F2")
CABECERA = PatternFill("solid", fgColor=VERDE)
CREMA = PatternFill("solid", fgColor="FBF3E4")
fino = Side(style="thin", color="D9CDB4")
BORDE = Border(left=fino, right=fino, top=fino, bottom=fino)

f_normal = Font(name=F, size=10)
f_input = Font(name=F, size=10, color="0000FF")
f_link = Font(name=F, size=10, color="008000")
f_bold = Font(name=F, size=10, bold=True)
f_cab = Font(name=F, size=10, bold=True, color="FFFFFF")
f_tit = Font(name=F, size=16, bold=True, color=VERDE)
f_sub = Font(name=F, size=10, italic=True, color="6B5A3E")
f_ej = Font(name=F, size=10, italic=True, color="808080")
ENVUELTO = Alignment(wrap_text=True, vertical="top")
CENTRO = Alignment(horizontal="center", vertical="top", wrap_text=True)

wb = Workbook()


def titulo(ws, texto, sub, ultima_col):
    ws["A1"] = texto
    ws["A1"].font = f_tit
    ws["A2"] = sub
    ws["A2"].font = f_sub
    ws.row_dimensions[1].height = 26


def cabecera(ws, fila, textos, anchos):
    for i, (t, w) in enumerate(zip(textos, anchos), 1):
        c = ws.cell(row=fila, column=i, value=t)
        c.font = f_cab
        c.fill = CABECERA
        c.alignment = CENTRO
        c.border = BORDE
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.row_dimensions[fila].height = 30
    ws.freeze_panes = ws.cell(row=fila + 1, column=1)


def lista(ws, opciones, rango):
    dv = DataValidation(type="list", formula1='"' + ",".join(opciones) + '"', allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(rango)


def colores_estado(ws, rango):
    ws.conditional_formatting.add(rango, CellIsRule(operator="equal", formula=['"Sí"'], fill=PatternFill("solid", fgColor="D8EFD3")))
    ws.conditional_formatting.add(rango, CellIsRule(operator="equal", formula=['"Listo"'], fill=PatternFill("solid", fgColor="D8EFD3")))
    ws.conditional_formatting.add(rango, CellIsRule(operator="equal", formula=['"Recibido"'], fill=PatternFill("solid", fgColor="D8EFD3")))
    ws.conditional_formatting.add(rango, CellIsRule(operator="equal", formula=['"Pendiente"'], fill=PatternFill("solid", fgColor="FDE2C8")))
    ws.conditional_formatting.add(rango, CellIsRule(operator="equal", formula=['"Con cambios"'], fill=PatternFill("solid", fgColor="FFF2B3")))
    ws.conditional_formatting.add(rango, CellIsRule(operator="equal", formula=['"Guion listo"'], fill=PatternFill("solid", fgColor="E3ECF7")))


# ------------------------------------------------------------------ 1. Inicio
ws = wb.active
ws.title = "Inicio"
titulo(ws, "Control de tareas · Bajo el Árbol", "Temporada navideña 2026 · Publicidad en Facebook e Instagram", 2)
ws.column_dimensions["A"].width = 26
ws.column_dimensions["B"].width = 90
filas = [
    ("Cómo usar este archivo", ""),
    ("Celdas amarillas", "Son las que usted llena o actualiza. El resto se calcula solo."),
    ("Texto azul", "Datos que usted escribe (gasto, alcance, mensajes, etc.)."),
    ("Texto verde", "Datos que vienen de otra pestaña; no los escriba a mano."),
    ("Listas desplegables", "Las columnas de estado tienen opciones (Listo, Pendiente, Sí, No…). Elija en vez de escribir."),
    ("", ""),
    ("Pestañas", ""),
    ("Calendario", "Todas las publicaciones del 10 nov al 31 dic con su estado: diseño, revisión, aprobación y publicación."),
    ("Pendientes cliente", "Datos que debe entregar el negocio y su fecha límite. Marque Recibido cuando lleguen."),
    ("Rutina semanal", "Qué hacer cada día de la semana. Marque con ✓ cada tarea cumplida."),
    ("Punto de partida", "Números antes de empezar y al final del mes, para compararlos."),
    ("Reporte semanal", "Gasto, alcance y mensajes de cada semana; calcula CTR, costo por mensaje y tasa de conversión."),
    ("Indicadores del mes", "CAC, ROAS, ROI y punto de equilibrio con las fórmulas del plan de trabajo."),
    ("", ""),
    ("Regla de oro", "Nada se publica sin la aprobación del dueño (Plan de trabajo, sección 6)."),
]
for i, (a, b) in enumerate(filas, 4):
    ws.cell(row=i, column=1, value=a).font = f_bold if a and not b else f_normal
    ws.cell(row=i, column=2, value=b).font = f_normal
    ws.cell(row=i, column=2).alignment = ENVUELTO
ws["A4"].font = Font(name=F, size=12, bold=True, color=VERDE)
ws["A10"].font = Font(name=F, size=12, bold=True, color=VERDE)
ws["A5"].fill = AMARILLO
ws["A6"].font = f_input
ws["A7"].font = f_link
ws["A18"].font = Font(name=F, size=10, bold=True, color="9C0006")

# ------------------------------------------------------------------ 2. Calendario
ws = wb.create_sheet("Calendario")
titulo(ws, "Calendario de publicaciones", "Fuente: Calendario de contenido · Temporada navideña 2026. Actualice las columnas amarillas.", 14)
cols = ["Fecha", "Día", "Semana", "Formato", "Pilar", "Publicación", "Llamado a la acción", "Carpeta",
        "Diseño", "Enviado a revisión", "Aprobado", "Publicado", "Notas"]
anchos = [12, 11, 8, 13, 12, 46, 26, 40, 12, 12, 13, 11, 38]
cabecera(ws, 4, cols, anchos)
DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
fila = 5
for (fe, sem, formato, pilar, pub, cta, carpeta, dis, nota) in CAL:
    enviado = "No"
    if formato == "Tarea interna":
        enviado = "—"
    vals = [fe, DIAS[fe.weekday()], sem, formato, pilar, pub, cta, carpeta, dis, enviado,
            "Pendiente" if enviado != "—" else "—", "No" if enviado != "—" else "—", nota]
    for c, v in enumerate(vals, 1):
        cell = ws.cell(row=fila, column=c, value=v)
        cell.font = f_normal
        cell.alignment = ENVUELTO
        cell.border = BORDE
        if c in (9, 10, 11, 12, 13):
            cell.fill = AMARILLO
    ws.cell(row=fila, column=1).number_format = "dd/mm/yyyy"
    ws.cell(row=fila, column=3).alignment = CENTRO
    fila += 1
# historias: una fila por semana
for (n, rango, tema) in SEMANAS:
    vals = [None, "—", n, "3 historias", "Comunidad", f"Historias de la semana {n} ({rango})", "—",
            f"03_Publicaciones/Semana_{n}_*", "Listo" if n == 1 else "Pendiente",
            "No", "Pendiente", "No", "Encuestas, detrás de cámaras, fotos de clientes (con permiso)"]
    for c, v in enumerate(vals, 1):
        cell = ws.cell(row=fila, column=c, value=v)
        cell.font = f_normal
        cell.alignment = ENVUELTO
        cell.border = BORDE
        if c in (9, 10, 11, 12, 13):
            cell.fill = AMARILLO
    ws.cell(row=fila, column=3).alignment = CENTRO
    fila += 1
ultima = fila - 1
lista(ws, ["Listo", "Guion listo", "Pendiente", "En proceso"], f"I5:I{ultima}")
lista(ws, ["Sí", "No", "—"], f"J5:J{ultima}")
lista(ws, ["Sí", "Con cambios", "Pendiente", "No publicar", "—"], f"K5:K{ultima}")
lista(ws, ["Sí", "No", "—"], f"L5:L{ultima}")
colores_estado(ws, f"I5:L{ultima}")
ws.auto_filter.ref = f"A4:M{ultima}"
# resumen
r = ultima + 2
ws.cell(row=r, column=1, value="Resumen").font = Font(name=F, size=12, bold=True, color=VERDE)
resumen = [
    ("Publicaciones y bloques de historias", f'=COUNTA(F5:F{ultima})-COUNTIF(D5:D{ultima},"Tarea interna")'),
    ("Diseño listo", f'=COUNTIF(I5:I{ultima},"Listo")'),
    ("Aprobadas por el cliente", f'=COUNTIF(K5:K{ultima},"Sí")+COUNTIF(K5:K{ultima},"Con cambios")'),
    ("Publicadas", f'=COUNTIF(L5:L{ultima},"Sí")'),
    ("Avance de publicación", f"=IFERROR(B{r+4}/B{r+1},0)"),
]
for i, (t, fml) in enumerate(resumen, 1):
    ws.cell(row=r + i, column=1, value=t).font = f_normal
    c = ws.cell(row=r + i, column=2, value=fml)
    c.font = f_bold
    if t.startswith("Avance"):
        c.number_format = "0.0%"

# ------------------------------------------------------------------ 3. Pendientes cliente
ws = wb.create_sheet("Pendientes cliente")
titulo(ws, "Datos que debe entregar el negocio", "Fuente: Calendario navideño (p. 5) más los que surgieron al preparar las piezas. Marque Recibido cuando lleguen.", 7)
cabecera(ws, 4, ["#", "Dato o material", "Para qué se usa", "Fecha límite", "Estado", "Fecha recibido", "Días de atraso", "Notas"],
         [5, 52, 40, 13, 12, 14, 13, 36])
for i, (dato, para, lim) in enumerate(PENDIENTES, 1):
    f = i + 4
    vals = [i, dato, para, lim, "Pendiente", None, None, ""]
    for c, v in enumerate(vals, 1):
        cell = ws.cell(row=f, column=c, value=v)
        cell.font = f_normal
        cell.alignment = ENVUELTO
        cell.border = BORDE
    ws.cell(row=f, column=4).number_format = "dd/mm/yyyy"
    ws.cell(row=f, column=6).number_format = "dd/mm/yyyy"
    for c in (5, 6, 8):
        ws.cell(row=f, column=c).fill = AMARILLO
    ws.cell(row=f, column=6).font = f_input
    ws.cell(row=f, column=7, value=f'=IF(E{f}="Recibido",IF(F{f}="","",MAX(0,F{f}-D{f})),MAX(0,TODAY()-D{f}))')
    ws.cell(row=f, column=7).alignment = CENTRO
ult = len(PENDIENTES) + 4
lista(ws, ["Pendiente", "Recibido", "No aplica"], f"E5:E{ult}")
colores_estado(ws, f"E5:E{ult}")
ws.conditional_formatting.add(f"G5:G{ult}", CellIsRule(operator="greaterThan", formula=["0"], font=Font(name=F, color="9C0006", bold=True)))
ws.cell(row=ult + 2, column=2, value="Pendientes sin recibir").font = f_bold
ws.cell(row=ult + 2, column=3, value=f'=COUNTIF(E5:E{ult},"Pendiente")').font = f_bold
ws.cell(row=ult + 3, column=2, value="Fórmula de atraso").font = f_sub
ws.cell(row=ult + 3, column=3, value="Días de atraso = fecha de hoy (o de recepción) − fecha límite; 0 si llegó a tiempo.").font = f_sub

# ------------------------------------------------------------------ 4. Rutina semanal
ws = wb.create_sheet("Rutina semanal")
titulo(ws, "Rutina semanal", "Marque ✓ en la columna de la semana cuando cumpla cada tarea. Las instrucciones para Cowork están en la guía (sección 5).", 12)
cab = ["Día", "Tarea", "Dónde"] + [f"Sem {n}" for n, _, _ in SEMANAS]
cabecera(ws, 4, cab, [12, 62, 22] + [8] * len(SEMANAS))
RUTINA = [
    ("Lunes", "Publicar la pieza del lunes y una historia", "Meta Business Suite"),
    ("Lunes", "Revisar respuestas del cliente y actualizar Calendario y Pendientes", "Este Excel"),
    ("Martes", "Preparar las piezas y textos de la semana siguiente", "Cowork"),
    ("Martes", "Revisar anuncios: costo por mensaje de cada anuncio", "Administrador de anuncios"),
    ("Miércoles", "Publicar la pieza del miércoles y una historia", "Meta Business Suite"),
    ("Miércoles", "Enviar al cliente el PDF de revisión de la semana siguiente", "Cowork + WhatsApp"),
    ("Jueves", "Aplicar los cambios que pidió el cliente", "Cowork"),
    ("Jueves", "Programar las publicaciones aprobadas de la semana siguiente", "Meta Business Suite"),
    ("Viernes", "Publicar la pieza del viernes y una historia", "Meta Business Suite"),
    ("Viernes", "Llenar el Reporte semanal y enviarlo por WhatsApp", "Este Excel + Cowork"),
    ("Viernes", "Mover el presupuesto al anuncio con menor costo por mensaje", "Administrador de anuncios"),
]
for i, (d, t, donde) in enumerate(RUTINA, 5):
    for c, v in enumerate([d, t, donde], 1):
        cell = ws.cell(row=i, column=c, value=v)
        cell.font = f_bold if c == 1 else f_normal
        cell.alignment = ENVUELTO
        cell.border = BORDE
    for c in range(4, 4 + len(SEMANAS)):
        cell = ws.cell(row=i, column=c)
        cell.fill = AMARILLO
        cell.border = BORDE
        cell.alignment = CENTRO
ultr = 4 + len(RUTINA)
lista(ws, ["✓", "—"], f"D5:{get_column_letter(3 + len(SEMANAS))}{ultr}")
ws.cell(row=ultr + 1, column=2, value="Tareas cumplidas en la semana").font = f_bold
for c in range(4, 4 + len(SEMANAS)):
    L = get_column_letter(c)
    ws.cell(row=ultr + 1, column=c, value=f'=COUNTIF({L}5:{L}{ultr},"✓")&" / {len(RUTINA)}"').alignment = CENTRO

# ------------------------------------------------------------------ 5. Punto de partida
ws = wb.create_sheet("Punto de partida")
titulo(ws, "Punto de partida y comparación final", "Llene la columna Antes el día de arranque y la columna Después al terminar el mes de prueba.", 5)
cabecera(ws, 4, ["Indicador", "Antes", "Después", "Variación", "Variación %"], [44, 14, 14, 14, 14])
IND = ["Seguidores en Facebook", "Seguidores en Instagram", "Alcance semanal en Facebook",
       "Alcance semanal en Instagram", "Mensajes de WhatsApp por semana", "Reseñas en Google Maps"]
for i, t in enumerate(IND, 5):
    ws.cell(row=i, column=1, value=t).font = f_normal
    for c in (2, 3):
        cell = ws.cell(row=i, column=c)
        cell.fill = AMARILLO
        cell.font = f_input
        cell.number_format = "#,##0"
    ws.cell(row=i, column=4, value=f'=IF(OR(B{i}="",C{i}=""),"",C{i}-B{i})').number_format = "#,##0;(#,##0);-"
    ws.cell(row=i, column=5, value=f'=IF(OR(B{i}="",C{i}="",B{i}=0),"",(C{i}-B{i})/B{i})').number_format = "0.0%;(0.0%);-"
    for c in range(1, 6):
        ws.cell(row=i, column=c).border = BORDE
ws.cell(row=12, column=1, value="Fórmulas").font = f_bold
ws.cell(row=13, column=1, value="Variación = Después − Antes").font = f_sub
ws.cell(row=14, column=1, value="Variación % = (Después − Antes) ÷ Antes").font = f_sub

# ------------------------------------------------------------------ 6. Reporte semanal
ws = wb.create_sheet("Reporte semanal")
titulo(ws, "Reporte semanal de anuncios", "Escriba los datos en azul (Administrador de anuncios y conteo de promociones). Las columnas negras se calculan solas.", 16)
cols = ["Semana", "Fechas", "Gasto mensajes ($)", "Gasto reconocimiento ($)", "Gasto total ($)", "Alcance de la semana",
        "Impresiones", "Clics", "Mensajes recibidos", "Promociones usadas", "Ventas atribuidas ($)",
        "CTR", "Costo por mensaje ($)", "Tasa de conversión", "Lo que mejor funcionó", "Ajuste para la próxima semana"]
cabecera(ws, 4, cols, [9, 16, 12, 14, 12, 11, 12, 9, 11, 12, 13, 9, 12, 12, 32, 32])
ws.row_dimensions[4].height = 42
# fila de ejemplo
ej = ["Ejemplo", "(no se suma)", 160, 70, None, 4800, 9500, 140, 12, 5, 1450]
for c, v in enumerate(ej, 1):
    cell = ws.cell(row=5, column=c, value=v)
    cell.font = f_ej
    cell.fill = GRIS
    cell.border = BORDE
ws.cell(row=5, column=15, value="Anuncio de desayunos").font = f_ej
ws.cell(row=5, column=16, value="Subir presupuesto al de desayunos").font = f_ej
INI = 6
for k, (n, rango, tema) in enumerate(SEMANAS):
    f = INI + k
    ws.cell(row=f, column=1, value=n).alignment = CENTRO
    ws.cell(row=f, column=2, value=rango)
    for c in (3, 4, 6, 7, 8, 9, 10, 11, 15, 16):
        cell = ws.cell(row=f, column=c)
        cell.fill = AMARILLO
        cell.font = f_input
        cell.alignment = ENVUELTO if c >= 15 else Alignment()
for f in range(5, INI + len(SEMANAS)):
    ws.cell(row=f, column=5, value=f'=IF(AND(C{f}="",D{f}=""),"",SUM(C{f}:D{f}))')
    ws.cell(row=f, column=12, value=f'=IF(OR(G{f}="",G{f}=0),"",H{f}/G{f})')
    ws.cell(row=f, column=13, value=f'=IF(OR(I{f}="",I{f}=0),"",E{f}/I{f})')
    ws.cell(row=f, column=14, value=f'=IF(OR(I{f}="",I{f}=0),"",J{f}/I{f})')
    for c in range(1, 17):
        cell = ws.cell(row=f, column=c)
        cell.border = BORDE
        if f == 5 and c in (5, 12, 13, 14):
            cell.font = f_ej
for f in range(5, INI + len(SEMANAS) + 1):
    for c in (3, 4, 5, 11, 13):
        ws.cell(row=f, column=c).number_format = "$#,##0.00;($#,##0.00);-"
    for c in (6, 7, 8, 9, 10):
        ws.cell(row=f, column=c).number_format = "#,##0;(#,##0);-"
    for c in (12, 14):
        ws.cell(row=f, column=c).number_format = "0.0%;(0.0%);-"
T = INI + len(SEMANAS)
U = T - 1
ws.cell(row=T, column=1, value="Total").font = f_bold
ws.cell(row=T, column=2, value="semanas 1 a 8").font = f_bold
for c in (3, 4, 5, 7, 8, 9, 10, 11):
    L = get_column_letter(c)
    ws.cell(row=T, column=c, value=f"=SUM({L}{INI}:{L}{U})").font = f_bold
ws.cell(row=T, column=6, value="ver nota").font = f_sub
ws.cell(row=T, column=12, value=f'=IF(G{T}=0,"",H{T}/G{T})').font = f_bold
ws.cell(row=T, column=13, value=f'=IF(I{T}=0,"",E{T}/I{T})').font = f_bold
ws.cell(row=T, column=14, value=f'=IF(I{T}=0,"",J{T}/I{T})').font = f_bold
for c in range(1, 17):
    ws.cell(row=T, column=c).fill = CREMA
    ws.cell(row=T, column=c).border = BORDE
r = T + 2
notas = [
    "Fórmulas (Plan de trabajo, sección 5):",
    "Gasto total = Gasto mensajes + Gasto reconocimiento",
    "CTR = Clics ÷ Impresiones (Meta: clics en el enlace ÷ impresiones)",
    "Costo por mensaje = Gasto total en anuncios ÷ Mensajes recibidos (para comparar anuncios entre sí, use el gasto de cada anuncio)",
    "Tasa de conversión = Promociones usadas ÷ Mensajes recibidos",
    "Presupuesto de referencia: $1,000 al mes = $700 mensajes + $300 reconocimiento (≈ $23.33 y $10.00 al día).",
    "Promociones usadas: clientes que mencionaron el anuncio y canjearon la promoción exclusiva.",
    "El alcance no se suma entre semanas (una persona puede verse en varias); para el mes use el alcance mensual de Meta.",
]
for i, t in enumerate(notas):
    ws.cell(row=r + i, column=1, value=t).font = f_bold if i == 0 else f_sub
ws["M4"].comment = Comment("Fórmula del plan: inversión en anuncios ÷ mensajes recibidos. Para decidir qué anuncio conservar, compare el costo por mensaje de cada anuncio en el Administrador de anuncios.", "Guía")

# ------------------------------------------------------------------ 7. Indicadores del mes
ws = wb.create_sheet("Indicadores del mes")
titulo(ws, "Indicadores del mes de prueba", "Fórmulas del Plan de trabajo (sección 5). Las celdas verdes vienen del Reporte semanal; las amarillas las llena usted.", 4)
ws.column_dimensions["A"].width = 44
ws.column_dimensions["B"].width = 16
ws.column_dimensions["C"].width = 70
cabecera(ws, 4, ["Concepto", "Valor", "Fórmula o fuente"], [44, 16, 70])
RS = "'Reporte semanal'"
filas = [
    ("Datos", None, None, "sec"),
    ("Inversión en anuncios ($)", f"={RS}!E{T}", "Suma del gasto total del Reporte semanal", "link"),
    ("Pago del servicio ($)", 1200, "Mes de prueba: $1,200 · a partir del mes 2: $1,800 (Plan, sección 4)", "input"),
    ("Mensajes recibidos", f"={RS}!I{T}", "Suma del Reporte semanal", "link"),
    ("Clientes nuevos (promociones usadas)", f"={RS}!J{T}", "Suma del Reporte semanal", "link"),
    ("Ingresos atribuidos ($)", f"={RS}!K{T}", "Suma del Reporte semanal", "link"),
    ("Margen bruto", 0.60, "SUPUESTO del plan (60 %). Sustitúyalo por el margen real del negocio.", "input"),
    ("Ticket promedio ($)", 89, "SUPUESTO: desayuno de $49 + latte mediano de $40. Ajústelo con datos reales.", "input"),
    ("Resultados", None, None, "sec"),
    ("Costo total de marketing ($)", "=B6+B7", "Fórmula: Inversión en anuncios + Pago del servicio", "f"),
    ("Costo por mensaje ($)", '=IF(B8=0,"",B6/B8)', "Fórmula: Inversión en anuncios ÷ Mensajes recibidos", "f"),
    ("Tasa de conversión", '=IF(B8=0,"",B9/B8)', "Fórmula: Clientes nuevos ÷ Mensajes recibidos", "f"),
    ("CAC: costo por cliente nuevo ($)", '=IF(B9=0,"",B14/B9)', "Fórmula: (Inversión en anuncios + Servicio) ÷ Clientes nuevos", "f"),
    ("ROAS", '=IF(B6=0,"",B10/B6)', "Fórmula: Ingresos atribuidos ÷ Inversión en anuncios. Mayor que 1: los anuncios generan más de lo que cuestan.", "f"),
    ("Utilidad bruta atribuida ($)", "=B10*B11", "Fórmula: Ingresos atribuidos × Margen bruto", "f"),
    ("ROI", '=IF(B14=0,"",(B19-B14)/B14)', "Fórmula: (Utilidad bruta − Costo total de marketing) ÷ Costo total de marketing", "f"),
    ("Punto de equilibrio: ingresos necesarios ($)", '=IF(B11=0,"",B14/B11)', "Fórmula: Costo total de marketing ÷ Margen bruto (ingresos con los que ROI = 0)", "f"),
    ("Punto de equilibrio: ventas necesarias", '=IF(OR(B12=0,B21=""),"",ROUNDUP(B21/B12,0))', "Fórmula: Ingresos de equilibrio ÷ Ticket promedio, redondeado hacia arriba", "f"),
    ("Avance hacia el equilibrio", '=IF(OR(B21="",B21=0),"",B10/B21)', "Fórmula: Ingresos atribuidos ÷ Ingresos de equilibrio (100 % = se recuperó la inversión)", "f"),
]
for i, (t, v, nota, tipo) in enumerate(filas, 5):
    a = ws.cell(row=i, column=1, value=t)
    b = ws.cell(row=i, column=2, value=v)
    c = ws.cell(row=i, column=3, value=nota)
    c.font = f_sub
    c.alignment = ENVUELTO
    if tipo == "sec":
        a.font = Font(name=F, size=11, bold=True, color=VERDE)
        continue
    a.font = f_normal
    for x in (a, b, c):
        x.border = BORDE
    if tipo == "link":
        b.font = f_link
    elif tipo == "input":
        b.font = f_input
        b.fill = AMARILLO
    else:
        b.font = f_bold
fmt = {6: "$#,##0.00;($#,##0.00);-", 7: "$#,##0.00", 8: "#,##0", 9: "#,##0", 10: "$#,##0.00;($#,##0.00);-",
       11: "0.0%", 12: "$#,##0.00", 14: "$#,##0.00;($#,##0.00);-", 15: "$#,##0.00;($#,##0.00);-", 16: "0.0%;(0.0%);-",
       17: "$#,##0.00;($#,##0.00);-", 18: '0.00"x";(0.00"x");-', 19: "$#,##0.00;($#,##0.00);-", 20: "0.0%;(0.0%);-",
       21: "$#,##0.00", 22: "#,##0", 23: "0.0%;(0.0%);-"}
for row, nf in fmt.items():
    ws.cell(row=row, column=2).number_format = nf
ws["B11"].comment = Comment("Supuesto del plan de trabajo (ejemplo ilustrativo). Cámbielo por el margen real.", "Guía")
ws["B12"].comment = Comment("Supuesto: desayuno de huevos al gusto ($49) + latte mediano ($40), precios del sitio web.", "Guía")

for hoja in wb.worksheets:
    hoja.sheet_view.showGridLines = False
    hoja.sheet_properties.tabColor = VERDE if hoja.title == "Inicio" else ORO
wb.save(SALIDA)
print("ok", SALIDA, "ultima fila calendario", ultima, "total reporte", T)
