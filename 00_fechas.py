# Trabajar con fechas en Python

# Importar el módulo datetime, lo ponemos en comentario al traer una funcion en el ejemplo posterior
# import datetime

# Como en el caso de modulos podemos traer solo una funcion determinada
from datetime import datetime

# Obtener la fecha actual
fecha_actual = datetime.now()
print("Fecha actual:", fecha_actual)

# Acceder a parametros de la fecha
dia = fecha_actual.day
mes = fecha_actual.month
anio = fecha_actual.year
hora = fecha_actual.hour
minuto = fecha_actual.minute
segundo = fecha_actual.second

print("Dia:", dia) # Dia del mes   
print("Mes:", mes) # Mes del año
print("Anio:", anio) # Anio
print("Hora:", hora) # Hora
print("Minuto:", minuto) # Minuto
print("Segundo:", segundo) # Segundo

# Formatear la fecha
fecha_formateada = fecha_actual.strftime(f"Fecha: {dia}/{mes}/{anio}") # Formatear la fecha, dia/mes/año
print("Fecha formateada:", fecha_formateada)

# timestamp
# El timestamp es el numero de segundos que han pasado desde el 1 de enero de 1970
timestamp = fecha_actual.timestamp()
print("Timestamp:", timestamp)

minutos_timestamp = timestamp // 60
print("Minutos:", minutos_timestamp) 

horas_timestamp = minutos_timestamp // 60
print("Horas:", horas_timestamp)

dias_timestamp = horas_timestamp // 24
print("Dias:", dias_timestamp) 

meses_timestamp = dias_timestamp // 30
print("Meses:", meses_timestamp) 

anios_timestamp = meses_timestamp // 12
print("Anios:", anios_timestamp) 
