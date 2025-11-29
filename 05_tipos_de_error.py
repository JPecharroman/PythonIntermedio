# Veamos los tipos de errores que hay en Python

# Recordemos la sintaxis completo del try
# try:



"""
try:
    
except error_a_capturar:

except otro_error_a_capturar:

except Exception: # Captura cualquier error que no se haya capturado antes

else:    # Se ejecuta si no se produce ningun error

finally:    # Se ejecuta siempre, haya o no haya error
    
"""

# Veamos las excepciones que hay en Python para capturar en except
# Exception es la excepcion base
# SyntaxError: Error de sintaxis
# NameError: Error de nombre
# IndexError: Error de indice
# ModuleNotFoundError: Error de modulonotfound
# AttributeError: Error de atributo
# KeyError: Error de clave
# TypeError: Error de tipo
# ImportError: Error de importacion
# ValueError: Error de valor
# ZeroDivisionError: Error de division por cero
# FileNotFoundError: Error de archivo no encontrado
# EOFError: Error de fin de archivo
# RecursionError: Error de recursion
# MemoryError: Error de memoria
# FloatingPointError: Error de punto flotante
# RecursionError: Error de recursion
# SystemError: Error de sistema
# ReferenceError: Error de referencia
# TabError: Error de tabulacion
# UnboundLocalError: Error de variable local no asignada
# UnicodeError: Error de unicode
# UnicodeEncodeError: Error de codificacion unicode
# UnicodeDecodeError: Error de decodificacion unicode
# UnicodeTranslateError: Error de traduccion unicode

# Vamos a ver un ejemplo de cada error

# SyntaxError: Error de sintaxis
# print(Hola mundo) # SyntaxError: Error de syntaxis, olvidamos los " ".
print("Hola mundo") # Con " ".

# NameError: Error de nombre de variable
try:
    print(nombre)
except NameError:
    print("Error de nombre de variable, no esta definida")

# IndexError: Error de indice
lista = [1, 2, 3]
try:
    print(lista[3]) # Error de indice, el indice va de 0 a 2, el 3 no existe
except IndexError:
    print("Error de indice, el indice no existe")

# ModuleNotFoundError: Error de modulonotfound
try:
    import maht # Tratamos de importar un modulo que no existe o lo hemos definido mal
    # maht no existe ya que el modulo se denomina math, nos dara error
except ModuleNotFoundError:
    print("Error de modulonotfound, el modulo no existe")

# AttributeError: Error de atributo
try:
    import math
    print(math.Pi) # Error de atributo, al ser Python Case Sensitive, Pi no existe, es pi.
except AttributeError:
    print("Error de atributo, el atributo no existe en el modulo math")

# KeyError: Error de clave
# Recordamos los diccionarios, vamos a definir el diccionario persona

persona = {
    "nombre": "Jorge",
    "apellido": "Garcia",
    "edad": 30
}

# La clave en el diccionario persona son nombre, apellido y edad
try:
    print(persona["Apellido"]) # DE nuevo es case sensitive, Apellido no existe, es apellido, peta por clave no existente
except KeyError:
    print("Error de clave, la clave no existe")

# TypeError: Error de tipo
try:
    print(persona + persona) # Error de tipo, no se puede sumar un diccionario con otro diccionario
except TypeError:
    print("Error de tipo, no se puede sumar un diccionario con otro diccionario")

try:
    print(persona + 10) # Error de tipo, no se puede sumar un diccionario con un entero
except TypeError:
    print("Error de tipo, no se puede sumar un diccionario con un entero")

lista = ["nombre", "apellido", "edad", "direccion"]
try:
    print(lista["nombre"]) # Error de tipo, no se puede acceder a una lista con una clave de tipo string, debe ser int o slice
except TypeError:
    print("Error de tipo, no se puede acceder a una lista con una clave de tipo string, debe ser int o slice")

# ImportError: Error de importacion
try:
    from math import PI # CASE SENSITIVE, PI no existe, es pi.
    print(PI)
except ImportError:
    print("Error de importacion, el modulo no existe")

# ValueError: Error de valor
try:
    print(int("Hola")) # Error de valor, no se puede convertir una cadena de texto en un entero
except ValueError:
    print("Error de valor, no se puede convertir una cadena de texto en un entero")

# ZeroDivisionError: Error de division por cero
try:
    print(10 / 0) # Error de division por cero
except ZeroDivisionError:
    print("Error de division por cero")

# FileNotFoundError: Error de archivo no encontrado
try:
    with open("archivo.txt", "r") as archivo:
        print(archivo.read())
except FileNotFoundError:
    print("Error de archivo no encontrado")

# Iremos añadiendo tipos de error cuando veamos mas de Python.