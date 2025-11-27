# Resolucion de retos en Python

# Importamos el modulo creado
from modulo_retos import fizzbuzz # Reto 1
from modulo_retos import anagrama # Reto 2

# Reto 1: 
"""
 * FIZZ BUZZ

 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 
 """

# Buscamos imprimir los numeros del 1 al 100 con un salto de linea entre ellos
# Los multiplos de 3 se imprimen como "fizz"
# Los multiplos de 5 se imprimen como "buzz"
# Los multiplos de 3 y 5 se imprimen como "fizzbuzz"

# Por claridad, creamos una lista con el rango de valores y se la pasaremos al for
lista = list(range(1, 101))
lista_fizzbuzz = fizzbuzz(lista)

# Imprimimos la lista con los valores en el formato especificado
indice = list(range(0, 100)) # La lista tiene 100 posiciones, del 0 al 100, las recorremos con este indice
for i in indice:
    print(lista_fizzbuzz[i])
    print("\n") # Añadimos el salto de linea

# Reto 2: 

"""

 * ANAGRAMA

 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.

"""

# Recibimos dos palabras por teclado y debemos comprobar sin son anagramas una de la otra
# Crearemos una funcion en el modulo_retos.py donde le pasaremos las dos palabras obtenidas por teclado y nos devolvera
# True o False dependiendo si son anagramas o no

primera_palabra = input("Introduce la primera palabra: ")
# Pasamos a minusculas la palabra porque mayusculas y minusculas no son iguales a efecto de comprobacion
primera_palabra_minuscula = primera_palabra.lower() 
segunda_palabra = input("Introduce la segunda palabra: ")
# Pasamos a minusculas la palabra porque mayusculas y minusculas no son iguales a efecto de comprobacion
segunda_palabra_minuscula = segunda_palabra.lower()

print(primera_palabra_minuscula)
print(segunda_palabra_minuscula)
anagrama = anagrama(primera_palabra_minuscula, segunda_palabra_minuscula)

if anagrama:
    print("Las palabras son anagramas")
else:
    print("Las palabras no son anagramas")  




