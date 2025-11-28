# Funciones de orden superior en Python

# Son funciones que toman otras funciones como argumentos
# Son funciones que devuelven otras funciones

from functools import reduce # Importamos la funcion reduce desde functools para testearla
# Creamos una funcion
def suma_dos_valores(primer_valor, segundo_valor):
    return primer_valor + segundo_valor

# print(suma_dos_valores(1, 2))

# Creamos una funcion para restar 
def resta_dos_valores(primer_valor, segundo_valor):
    return primer_valor - segundo_valor

# Creamos una funcion que toma otra funcion como argumento
def operacion_dos_valores(primer_valor, segundo_valor, funcion):
    return funcion(primer_valor, segundo_valor)

print(operacion_dos_valores(1, 2, suma_dos_valores))   # Devuelve 3, pasamos la funcion suma_dos_valores como argumento

# Para que una funcion pueda llamar a otra necesitamos que sea definida antes de ser llamada

# Reutilizamos la funcion operacion_dos_valores, en este caso en vez de pasarle la funcion suma_dos_valores le pasamos la
# funcion resta_dos_valores
print(operacion_dos_valores(1, 2, resta_dos_valores))   # Devuelve -1

# Closures 
# Son funciones que toman otras funciones como argumentos y devuelven una funcion

# Creamos una funcion que toma otra funcion como argumento y devuelve una funcion
def suma_diez():
    def suma(valor):
        return valor + 10
    return suma

suma = suma_diez()
print(suma(10)) # Devuelve 20, pero este 20 no es un valor, es una funcion

# En este caso suma_diez() no tiene parametros, pero podria tenerlos
def suma_diez(primer_valor):
    def suma(valor):
        return valor + 10
    return suma(primer_valor) # Devolvemos la funcion suma pasandole como parametro el primer valor dado en la funcion superior

suma = suma_diez(10) # Le damos a nuestra variable suma el valor de la funcion suma_diez(10)
print(suma) # Devuelve 20 

def suma_diez(primer_valor):
    def suma(valor):
        return valor + primer_valor + 10
    return suma 
    # Devolvemos la suma del valor del parametro de la funcion superior y el valor del parametro de la funcion interna mas 10

suma = suma_diez(10)
print(suma(15)) # Devuelve 35 

# Otra forma de pasar valores es ejecutarlo como si fuera una lambda
suma = suma_diez(10)(15) 
# Le damos a nuestra variable suma el valor de la funcion suma_diez(10)(15), siendo 15 el valor del parametro de la funcion interna suma
print(suma) # Devuelve 35

# Funciones de orden superior predefinidas en Python
# Funcion map()

numeros = [1, 2, 3, 4, 5]

# map() toma dos argumentos, la funcion y la lista, la lista debe ser iterable
# map() crea una nueva lista con los resultados de aplicar la funcion a cada elemento de la lista
# El primer argumento es la funcion que se aplicara a cada elemento de la lista
# El segundo argumento es la lista iterable

# Vamos a crear una funcion map que reciba la lista de numeros y los pase a binario
def pasar_a_binario(valor):
    return bin(valor) # bin es una funcion predefinida en Python que convierte un numero entero a binario

def pasar_a_binario_sin_0b(valor):
    return bin(valor)[2:] # Eliminamos los dos primeros caracteres de la cadena binaria 

# Nos imprime la lista, los numeros en binario nos los representa con 0b delante, para indicar que es binario
print(list(map(pasar_a_binario, numeros))) # Creamos una lista, con list, que nos devuelve [0b1, 0b10, 0b11, 0b100, 0b101]
# Si quisieramos que no nos devolviera el 0b delante, debemos imprimir a partir de b, no imprimir los dos primeros elementos de cada valor
print(list(map(pasar_a_binario_sin_0b, numeros))) # Creamos una lista, con list, que nos devuelve [1, 10, 11, 100, 101]
# Esto mismo podriamos hacerlo con una lambda
print(list(map(lambda valor: bin(valor)[2:], numeros))) # Creamos una lista, con list, que nos devuelve [1, 10, 11, 100, 101]
# Esta lamba usa la funcion bin para convertir el numero a binario y luego [2:] para eliminar los dos primeros caracteres 
# de la cadena binaria

# Funcion filter()
# filter() toma dos argumentos, la funcion y la lista, la lista debe ser iterable
# filter() crea una nueva lista con los elementos que cumplen la condicion de la funcion
# El primer argumento es la funcion que se aplicara a cada elemento de la lista
# El segundo argumento es la lista iterable

def filtrar_impares(valor):
    return valor % 2 != 0

def filtrar_pares(valor):
    return valor % 2 == 0

print(list(filter(filtrar_impares, numeros))) # Creamos una lista, con list, que nos devuelve [1, 3, 5]
# Al igual que en el caso anterior podemos hacerlo con una lambda
print(list(filter(lambda valor: valor % 2 != 0, numeros))) # Creamos una lista, con list, que nos devuelve [1, 3, 5]

# Recibimos una lista y vamos a separarla en pares e impares
nueva_lista = [7, 3, 2, 8, 27, 13, 12, 15, 22, 25]

# Vamos a crear una lista con los pares e impares
lista_pares = list(filter(filtrar_pares, nueva_lista)) # Filtramos la lista quedandonos solo con los pares
lista_impares = list(filter(filtrar_impares, nueva_lista)) # Filtramos la lista quedandonos solo con los impares

print(f"Lista pares, creada con funcion filtrar_pares: {lista_pares}")
print(f"Lista impares, creada con funcion filtrar_impares: {lista_impares}")

# Ahora lo hacemos con lambda
lista_pares = list(filter(lambda valor: valor % 2 == 0, nueva_lista)) # Filtramos la lista quedandonos solo con los pares
lista_impares = list(filter(lambda valor: valor % 2 != 0, nueva_lista)) # Filtramos la lista quedandonos solo con los impares

print(f"Lista pares, creada con lambda: {lista_pares}")
print(f"Lista impares, creada con lambda: {lista_impares}")


# Funcion reduce()

# reduce() toma dos argumentos, la funcion y la lista, la lista debe ser iterable
# La funcion reduce() aplica la funcion a los dos primeros elementos de la lista y luego aplica la funcion al resultado
# de la aplicacion de la funcion a los dos primeros elementos y al siguiente elemento de la lista, y asi sucesivamente
# reduce() crea una nueva lista con los elementos que cumplen la condicion de la funcion

lista_reduce = [1,2,3,4,5,6,7,8,9]

def mayor(valor1, valor2):
    if valor1 >= valor2:
        return valor1
    else:
        return valor2

print(reduce(mayor, lista_reduce))

# Lo que hace reduce() es aplicar la funcion a los dos primeros elementos de la lista, con lo que se queda con el mayor
# en el primer caso se quedaria con el 1 y el 2, aplicando la funcion mayor, que devuelve el mayor de los dos, el 2
# luego se aplica la funcion mayor al 2 y el 3, que devuelve el 3
# luego se aplica la funcion mayor al 3 y el 4, que devuelve el 4
# y asi sucesivamente, hasta que se queda con el mayor de todos los elementos de la lista, el 9
# Esto es, reduce() devuelve un valor, no una lista como los dos casos anteriores.

# Hacemos lo mismo con lambda
print(reduce(lambda valor1, valor2: valor1 if valor1 >= valor2 else valor2, lista_reduce)) 
# Que hace lambda? 
# lambda valor1, valor2: valor1 if valor1 >= valor2 else valor2
# Toma dos valores, valor1 y valor2. Devuelve valor1 si es mayor o igual que valor2, si no, devuelve valor2.
# Lambda no necesita return, ya que devuelve el valor de la operacion