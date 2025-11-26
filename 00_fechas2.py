# Trabajamos con el modulo creado por nosotros modulo_fecha.py, se encargara de gestionar todo lo relativo a obtener
# fechas y tiempos y formatearlo para devolverlo como lo necesitamos para mostrarlo y trabajar con ello
import modulo_fecha

# Mostrar fecha actual, vamos a nuestro modulo y desde ahi accedemos a la funcion creada obtener_fecha_actual
fecha_actual = modulo_fecha.obtener_fecha_actual()
print("Fecha actual:", fecha_actual)

# Mostrar fecha formateada
print("Fecha formateada:", modulo_fecha.formatear_fecha(fecha_actual))

# Mostrar hora  
print("Hora:", modulo_fecha.formatear_hora(fecha_actual))

#Pasamos como parametros el año, mes y dia para obtener la fecha personalizada
anio_2026 = modulo_fecha.fecha_personalizada(2026, 1, 1)
print("La fecha a obtener es:", modulo_fecha.formatear_fecha(anio_2026))

# Mostrar tiempo actual
tiempo = modulo_fecha.tiempo_actual()
print("Tiempo actual:", tiempo)
# Formatear tiempo actual a horas minutos y segundos
print("Tiempo formateado:", modulo_fecha.formatear_tiempo(tiempo))

# Operamos con el metodo date del modulo datetime
fecha_hoy = modulo_fecha.fecha_hoy()
print("Fecha de hoy:", fecha_hoy)
print("Fecha formateada a formato dia/mes/año:", modulo_fecha.formatear_fecha_hoy(fecha_hoy))

# Modificar valores de la fecha, podemos modificar el año, mes y dia mediante la funcion replace
fecha_hoy = fecha_hoy.replace(year=2026)
print("Fecha de hoy:", fecha_hoy)
print("Fecha formateada a formato dia/mes/año:", modulo_fecha.formatear_fecha_hoy(fecha_hoy))

fecha1 = modulo_fecha.obtener_fecha_actual()
fecha2 = modulo_fecha.fecha_personalizada(2020, 1, 1)
diferencia = fecha1 - fecha2    
print("Diferencia entre dos fechas:", diferencia)

# Trabajamos con timedelta, nos permite operar con fechas, restar, sumar, etc

# sumar dias a una fecha
print("Sumar diez dias a la fecha actual:", modulo_fecha.sumar_dias(fecha_actual, 10))

# Diferencia entre dos fechas, nos la hallara en segundos pero la formateamos a horas minutos y segundos
# Usamos las fechas creadas arriba, deben ser del mismo objeto para que nos permita operar con ellas
print("Diferencia entre dos fechas:", modulo_fecha.diferencia_fechas(fecha1, fecha2))

