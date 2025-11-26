# Para practicar modulos vamos a crear un modulo que nos gestione fechas y usaremos el programa 00_fechas2.py
# para operar y visualizar con fechas

import datetime
import time
# Trabajamos con el metodo date del modulo datetime
from datetime import date
# Operar con diferentes fechas
from datetime import timedelta

# Funciones para gestionar fechas
# Funcion para obtener la fecha actual, nos devuelve la fecha actual
def obtener_fecha_actual():
    fecha_actual = datetime.datetime.now()
    return fecha_actual

def formatear_fecha(fecha):
    fecha_formateada = fecha.strftime("%d/%m/%Y") # Obtiene el dia, mes y año de la fecha
    return fecha_formateada

def formatear_hora(hora):
    hora_formateada = hora.strftime("%H:%M:%S") # Obtiene la hora, minutos y segundos de la hora
    return hora_formateada

def formatear_fecha_hora(fecha_hora):
    fecha_hora_formateada = fecha_hora.strftime("%d/%m/%Y %H:%M:%S") # Obtiene el dia, mes y año de la fecha y la hora, minutos y segundos de la hora
    return fecha_hora_formateada

def formatear_fecha_hora_timestamp(timestamp):
    fecha_hora_formateada = datetime.datetime.fromtimestamp(timestamp) # Obtiene la fecha y hora a partir de un timestamp
    return fecha_hora_formateada

# Funcion para obtener la fecha a partir de tres parametros pasados, año, mes y dia
def fecha_personalizada(anio: int = 2025, mes: int = 1, dia: int = 1):
    fecha_personalizada = datetime.datetime(anio, mes, dia)
    return fecha_personalizada

# Trabajamos con la funcion time
def tiempo_actual():
    tiempo_actual = time.time()
    return tiempo_actual

# Hallamos el tiempo actual formateado a partir de la funcion localtime, localtime nos devuelve la fecha y hora local
def formatear_tiempo(tiempo):
    tiempo_formateado = time.strftime("%H:%M:%S", time.localtime(tiempo))
    return tiempo_formateado

# Trabajamos con el metodo date de la funcion datetime, al haberlo importado de datetime no necesitamos añadir el modulo
# Obtenemos la fecha actual
def fecha_hoy():
    fecha_hoy = date.today()
    return fecha_hoy

# La formateamos en formato dia/mes/año
def formatear_fecha_hoy(fecha_hoy):
    fecha_hoy_formateada = fecha_hoy.strftime("%d/%m/%Y") # Fecha en formato dia/mes/año
    return fecha_hoy_formateada

# Operamos con diferentes fechas con el metodo timedelta
# timedelta nos permite operar con fechas, restar, sumar, etc
# Veamos un ejemplo de timedelta
def sumar_dias(fecha, dias):
    fecha_sumada = fecha + timedelta(days=dias)
    return fecha_sumada

# Pasar una fecha, dada en segundos, a una fecha en formato años, meses, dias
def fecha_segundos(segundos):
    anios = segundos // 31536000 # Numero de segundos que tiene un año
    meses = (segundos % 31536000) // 2592000 # Una vez hallamos los años, restamos los segundos que han pasado y hallamos los meses
    dias = (segundos % 2592000) // 86400 # Una vez hallamos los meses, restamos los segundos que han pasado y hallamos los dias
    # Pasamos los valores a enteros
    anios = int(anios)
    meses = int(meses)
    dias = int(dias)
    fecha_segundos = f"La diferencia es de {anios} años, {meses} meses y {dias} dias"
    return fecha_segundos

# Hallar la diferencia entre dos fechas pasadas como parametros, deben ser del mismo tipo para poder operar con ellas
def diferencia_fechas(fecha1, fecha2):
    diferencia = timedelta.total_seconds(fecha1 - fecha2) # Diferencia, en segundos, entre las dos fechas pasadas
    diferencia_formateada = fecha_segundos(diferencia)
    return diferencia_formateada