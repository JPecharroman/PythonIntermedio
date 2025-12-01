# Expresiones Regulares en Python

# importamos el modulo re
import re

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



# Inspeccionamos cadenas de texto con re.search()
texto = "Hola, mi numero es 123456789"
numero = re.search("123456789", texto)
print(numero)
# Estamos viendo que search() nos devuelve un objeto. Podemos realizar operaciones analogas a las que haciamos con el match()
inicio = numero.start()
final = numero.end()
print(inicio)
print(final)
print(numero.span())
print(numero.group())


# Inspeccionamos cadenas de texto con el metodo findall(), findall() nos devuelve una lista con todos los resultados encontrados
texto = " Este es un texto de prueba del metodo findall(), este metodo nos devuelve una lista con todos los resultados encontrados, findall() nos devuelve una lista con todos los resultados encontrados"
lista = re.findall("findall", texto)
print(lista)
# Nos devuelve una lista, podemos darle el tratamiento clasico de listas
print(len(lista))
print(lista[0])
print(lista[1])
# Como en los casos anteriores podemos usar el metodo re.I para que ignore mayusculas y minusculas
texto = " Vemos un texto con la palabra texto es distintas formas, con mayusculas, TEXTO, con alguna mayuscula, TeXTo y solo la primera mayuscula, Texto"
lista = re.findall("texto", texto, re.I)
print(lista)
print(len(lista))   
for indice in lista:
    print(indice)
# La cadena pasada como parametro al findall() aparece cinco veces con independencia de si esta en mayusculas o minusculas.
# findall() si que distingue si la palabra lleva tilde, esta y está son palabras distintas.
texto = "Esta palabra esta y está son palabras distintas, la tilde de está hace que para findall() sea distinta de está"
lista1 = re.findall("esta", texto, re.I)
lista2 = re.findall("está", texto, re.I)
print(lista1)
print(lista2)
print(len(lista1))
print(len(lista2))

# Cadenas de texto con el metodo split(), split() nos devuelve una lista con todos los resultados encontrados
texto = "Hola, mi numero es 123456789"
numero = re.split(" ", texto)
print(numero)
print(len(numero))
# Divide la cadena de texto en una lista, en este caso divide por espacios, ya que es el parametro buscado
# Podemos usar otro parametros, por ejemplo la coma ,
numero = re.split(",", texto)
print(numero) # Vemos que nos encuetra una coma, asi que divide la cadena en dos partes, hasta la coma y despues de la coma
print(len(numero))

# Cadenas de texto con el metodo sub(), sub() nos devuelve una cadena de texto con todos los resultados encontrados
texto = "Hola, mi numero es 123456789"
numero = re.sub("m", "M", texto)
print(numero)
print(len(numero))
# Sustituye todas las ocurrencias del patron por el reemplazo, en este caso cambia m por M
# con | en el patron podemos buscar varias cadenas de texto
numero = re.sub("m|e", "M", texto)
print(numero)
print(len(numero))
# Sustituye todas las ocurrencias del patron por el reemplazo, en este caso cambia m por M y e por M
# Podemos usar la | solo como una variante de una letra en una palabra, por ejemplo mayusculas y minusculas
texto = "En este texto buscamos la palabra Texto y vamos a sustituir la palabra texto por escrito independientemente que Texto empiece con mayuscula o minuscula"
numero = re.sub("[t|T]exto", "escrito", texto)
print(numero)
