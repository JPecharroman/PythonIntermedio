# Trabajar con fechas en Python
# Importar el módulo datetime
import datetime

# Obtener la fecha actual
fecha_actual = datetime.datetime.now()
print("Fecha actual:", fecha_actual)

# Formatear la fecha
fecha_formateada = fecha_actual.strftime(f"Fecha: %d/%m/%Y") # Formatear la fecha, dia, mes, año(year)
print("Fecha formateada:", fecha_formateada)
