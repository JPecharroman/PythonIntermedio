# Por limpieza iremos creando diveras paginas de resolucion de retos con unos o dos retos por pagina
# El modulo sera siempre el mismo, donde iremos creando las funciones para resolver los retos, modulo_retos.py

from modulo_retos import fibonacci # Reto 3.

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
print(lista_fibonacci)