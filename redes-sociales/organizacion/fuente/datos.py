# Datos compartidos del calendario navideño (tomados del PDF del cliente)
from datetime import date
D = lambda m, d: date(2026, m, d)

SEMANAS = [
    (1, "10 al 15 nov", "Arranque y fin de semana largo"),
    (2, "16 al 22 nov", "Desayunos"),
    (3, "23 al 29 nov", "Arranque navideño"),
    (4, "30 nov al 6 dic", "Temporada"),
    (5, "7 al 13 dic", "Posadas y Guadalupe"),
    (6, "14 al 20 dic", "Regalos"),
    (7, "21 al 27 dic", "Navidad"),
    (8, "28 al 31 dic", "Cierre de año"),
]

# (fecha, semana, formato, pilar, publicación, llamado a la acción, archivo/carpeta, estado de diseño, nota)
CAL = [
    (D(11,10), 1, "Tarea interna", "Arranque", "Reunión con el dueño, accesos, punto de partida, ajuste de perfiles y promoción exclusiva", "—", "—", "Pendiente", ""),
    (D(11,12), 1, "Carrusel", "Producto", "Conoce Bajo el Árbol: el lugar, el café y el menú con precios", "Pide por WhatsApp o visítanos", "03_Publicaciones/Semana_1_10-15nov/P1_Carrusel_Conoce_12nov", "Listo", "P1 del PDF de revisión"),
    (D(11,13), 1, "Publicación", "Promoción", "Fin de semana largo: promoción de café con pan (13 al 17 nov)", "Ven este fin de semana", "03_Publicaciones/Semana_1_10-15nov/P2_Fin_de_semana_largo_13nov", "Listo", "Falta producto y precio (va solo en el texto)"),
    (D(11,16), 2, "Publicación", "Promoción", "Día festivo: aviso de horario y desayuno de puente", "Te esperamos hoy", "03_Publicaciones/Semana_2_16-22nov/P4_Desayuno_de_puente_16nov", "Listo", "Confirmar que abren y el horario"),
    (D(11,18), 2, "Video corto", "Comunidad", "Detrás de cámaras: así se prepara el pan", "Síguenos para más", "03_Publicaciones/Semana_2_16-22nov/P5_Video_pan_18nov", "Guion listo", "Se graba en la visita al local"),
    (D(11,20), 2, "Carrusel", "Producto", "Desayunos Bajo el Árbol: platillos y precios", "Reserva o pide por WhatsApp", "03_Publicaciones/Semana_2_16-22nov/P6_Carrusel_Desayunos_20nov", "Listo", "Confirmar precios"),
    (D(11,23), 3, "Publicación", "Promoción", "Regalos Bajo el Árbol: preventa de cajas de pan", "Aparta la tuya por WhatsApp", "03_Publicaciones/Semana_3_23-29nov/P8_Cajas_de_regalo_23nov", "Pendiente", "Falta contenido, precio y foto de la caja"),
    (D(11,25), 3, "Video corto", "Producto", "Así preparamos tu capuchino: del grano a la taza", "Ven por el tuyo", "03_Publicaciones/Semana_3_23-29nov/P9_Video_capuchino_25nov", "Guion listo", "Se graba en la visita al local"),
    (D(11,27), 3, "Publicación", "Ambiente", "Llegó la Navidad al local: decoración y luces", "Ven a tomarte la foto", "03_Publicaciones/Semana_3_23-29nov/P10_Navidad_en_el_local_27nov", "Guion listo", "Fotos cuando el local esté decorado"),
    (D(11,30), 4, "Carrusel", "Producto", "Bebidas de temporada", "Pruébalas esta semana", "03_Publicaciones/Semana_4_30nov-6dic", "Pendiente", "Falta definir bebidas y precios"),
    (D(12,2), 4, "Video corto", "Comunidad", "Quiénes somos: la historia del negocio y del equipo", "Gracias por elegirnos", "03_Publicaciones/Semana_4_30nov-6dic", "Pendiente", ""),
    (D(12,4), 4, "Publicación", "Comunidad", "Sorteo navideño (cierra el 10 dic)", "Participa en los comentarios", "03_Publicaciones/Semana_4_30nov-6dic", "Pendiente", "Falta premio; publicar bases del sorteo"),
    (D(12,7), 5, "Publicación", "Promoción", "Pan para tus posadas: charolas y pan para reuniones", "Haz tu pedido con anticipación", "03_Publicaciones/Semana_5_7-13dic", "Pendiente", ""),
    (D(12,11), 5, "Publicación", "Comunidad", "Ganador del sorteo", "Felicidades y gracias", "03_Publicaciones/Semana_5_7-13dic", "Pendiente", ""),
    (D(12,12), 5, "Publicación", "Ambiente", "Día de la Virgen de Guadalupe: chocolate caliente y pan", "Te esperamos", "03_Publicaciones/Semana_5_7-13dic", "Pendiente", "Tono respetuoso"),
    (D(12,14), 6, "Carrusel", "Promoción", "Guía de regalos: cajas de pan para familia y compañeros", "Pide la tuya por WhatsApp", "03_Publicaciones/Semana_6_14-20dic", "Pendiente", ""),
    (D(12,16), 6, "Video corto", "Ambiente", "Empiezan las posadas: tu posada comienza con pan y café", "Pide para tu reunión", "03_Publicaciones/Semana_6_14-20dic", "Pendiente", ""),
    (D(12,18), 6, "Publicación", "Promoción", "Último llamado: fecha límite de pedidos navideños", "Asegura tu pedido hoy", "03_Publicaciones/Semana_6_14-20dic", "Pendiente", "Falta fecha límite"),
    (D(12,21), 7, "Publicación", "Promoción", "Horario especial del 24 y 25 de diciembre", "Planea tu visita", "03_Publicaciones/Semana_7_21-27dic", "Pendiente", "Falta horario"),
    (D(12,24), 7, "Publicación", "Comunidad", "Feliz Nochebuena", "—", "03_Publicaciones/Semana_7_21-27dic", "Pendiente", ""),
    (D(12,26), 7, "Publicación", "Producto", "Después de la cena: café y pan para el recalentado", "Ven o pide por WhatsApp", "03_Publicaciones/Semana_7_21-27dic", "Pendiente", ""),
    (D(12,28), 8, "Carrusel", "Comunidad", "Gracias por este año: momentos del local", "Comparte tu foto con nosotros", "03_Publicaciones/Semana_8_28-31dic", "Pendiente", ""),
    (D(12,30), 8, "Publicación", "Promoción", "Horario de fin de año y pedidos de último momento", "Pide con tiempo", "03_Publicaciones/Semana_8_28-31dic", "Pendiente", "Falta horario 31 dic y 1 ene"),
    (D(12,31), 8, "Publicación", "Comunidad", "Feliz Año Nuevo", "—", "03_Publicaciones/Semana_8_28-31dic", "Pendiente", ""),
]

# (dato, para qué, fecha límite)
PENDIENTES = [
    ("Dirección exacta y horario regular", "Perfiles y publicaciones", D(11,12)),
    ("Acceso de administrador en Meta Business Suite", "Programar publicaciones y anuncios", D(11,12)),
    ("Logotipo y fotos disponibles del local", "Diseño de publicaciones", D(11,12)),
    ("Producto y precio de la promoción de fin de semana largo", "Publicación del 13 nov (P2)", D(11,12)),
    ("¿Abren el lunes 16 de noviembre? ¿En qué horario?", "Publicación del 16 nov (P4)", D(11,12)),
    ("Menú de desayunos con precios (confirmar)", "Carrusel del 20 nov (P6) y página web", D(11,18)),
    ("Contenido, precio y foto de las cajas de regalo", "Preventa del 23 nov (P8)", D(11,20)),
    ("Bebidas de temporada y precios", "Carrusel del 30 nov", D(11,27)),
    ("Premio del sorteo", "Publicación del 4 dic", D(12,2)),
    ("Fecha límite de pedidos navideños", "Publicación del 18 dic", D(12,14)),
    ("Horarios del 24, 25 y 31 de diciembre y 1 de enero", "Publicaciones del 21 y 30 dic", D(12,18)),
    ("Enlace de invitación al grupo de WhatsApp (confirmar que funciona)", "Historias y página web", D(11,12)),
    ("Promoción exclusiva de los anuncios (definida juntos)", "Medir clientes que llegan por la publicidad", D(11,12)),
    ("Tarjeta registrada en la cuenta publicitaria de Meta", "Activar los anuncios", D(11,12)),
    ("Fecha de la visita al local (fotos y videos)", "Videos del 18 y 25 nov", D(11,13)),
    ("Día en que el local estará decorado", "Publicación del 27 nov (P10)", D(11,20)),
]
