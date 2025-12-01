# Expresiones Regulares en Python

# importamos el modulo re
import re

# Inspeccionamos cadenas de texto con re.search()
texto = "Hola, mi numero es 123456789"
numero = re.search("123456789", texto)
print(numero)
# Estamos viendo que search nos devuelve un objeto.

# Encontrar un patron con re.match(), match() solo busca desde el inicio, por eso en nuestros ejemplos no nos encuentra nada.
texto = "Hola, mi numero es 123456789"
otro_texto = "En este texto no tenemos el numero buscado"
numero = re.match("123456789", texto)
numero2 = re.match("123456789", otro_texto)
print(numero)
print(numero2)
# Tercer texto
tercer_texto = "123456789 es el numero buscado"
numero3 = re.match("123456789", tercer_texto)
print(numero3) # Aqui si vemos que match() nos devuelve el objeto.
# Para imprimir que ha encontrado el patron y su longitud, usamos el metodo start() y end()
print(numero3.start())
print(numero3.end())
# Con el metodo span() obtenemos una tupla con el inicio y el final
print(numero3.span())
# Con el metodo group() obtenemos el texto encontrado
print(numero3.group())

# Parametro re.I en el match() para que ignore mayusculas y minusculas
numero4 = re.match("hola,", texto, re.I)
print(numero4.span())

# Una forma de extraer los valores inicio y final si queremos operar con ellos, aparte de start() y end()
# Es sacarlos a partir de span().
inicio, final = numero3.span()
print(inicio)
print(final)

# 
