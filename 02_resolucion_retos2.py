# Por limpieza iremos creando diveras paginas de resolucion de retos con unos o dos retos por pagina
# El modulo sera siempre el mismo, donde iremos creando las funciones para resolver los retos, modulo_retos.py

from modulo_retos import fibonacci # Reto 3.
from modulo_retos import numero_primo # Reto 4.

# Reto 3:

"""

 * LA SUCESION DE FIBONACCI

 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...

"""

rango_a_listar = range(50) # Queremos imprimir los 50 primeros numeros de la sucesion de fibonacci

# Llamamos a la funcion fibonacci y le pasamos el rango a listar
lista_fibonacci = fibonacci(rango_a_listar)

# Imprimimos la lista
for i in rango_a_listar:
    print(f"{i+1} valor de la lista de fibonacci: {lista_fibonacci[i]}")


# Reto 4: 

"""

 * NUMEROS PRIMOS

 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Un numero es primo si solo es divisible por 1 y por si mismo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 
 """

# Debemos comprobar que el valor introducido es un numero
try:
    numero_a_comprobar = int(input("Introduce el numero a comprobar: ")) # Recogemos el numero a comprobar y lo pasamos a entero
except ValueError: # Si no es un numero, saltamos el error
    print("Debes introducir un numero")
    exit()

# Llamamos a la funcion numero primo para que me compruebe si es primo o no
primo = numero_primo(numero_a_comprobar)

if primo:
    print(f"El numero {numero_a_comprobar} es primo")
else:
    print(f"El numero {numero_a_comprobar} no es primo")