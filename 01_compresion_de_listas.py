# Compresion de listas en Python
# Zippeo de listas, vamos a crear dos listas y vamos a zippearlas

lista1 = list(range(5)) # range(parametro) crea una lista con valores desde 0 hasta el parametro - 1
print("Lista 1: ", lista1)
lista2 = list(range(5, 10)) # range(parametro, parametro) crea una lista con valores desde el primer parametro hasta el segundo parametro - 1
print("Lista 2: ", lista2)

# Operaciones con listas basadas en range
lista3 = [i * 2 for i in range(5)]
print("Lista 3, multiplicamos por dos cada elemento: ", lista3)
lista4 = [i * 2 for i in range(5) if i % 2 == 0]
print("Lista 4, multiplicamos por dos cada elemento que sea par: ", lista4)

# zip es una funcion del modulo built-in que zippea dos listas, es decir, une dos listas en una lista de tuplas
# Es util para unir pares de listas con valores relaccionados (nombre, edad, etc)
zippeo = list(zip(lista1, lista2)) # zip(lista1, lista2) crea una lista de tuplas con los valores de las dos listas
print("Zippeo: ", zippeo)