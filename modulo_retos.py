# Creamos el modulo para gestionar los retos de resolucion retos

# Reto 1: FizzBuzz

#  En este modulo nos entrara como parametro una lista con el rango de valores a comprobar y devolveremos la lista con los valores
#  en el formato especificado:
#  - Múltiplos de 3 por la palabra "fizz".
#  - Múltiplos de 5 por la palabra "buzz".
#  - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#  el numero si no es multiplo de 3 ni de 5
#  linea en blanco entre cada impresion

def fizzbuzz(lista):
    lista_formateada = []
    for i in lista: # Rango de 1 a 101 para nos imprima el 100
        # Buscamos los multiplos de 3 y 5
        if i % 3 == 0 and i % 5 == 0:
            # print("fizzbuzz") # Si es multiplo de 3 y 5 imprimimos "fizzbuzz"
            lista_formateada.append("fizzbuzz")
        elif i % 3 == 0:
            # print("fizz") # Si es multiplo de 3 imprimimos "fizz"
            lista_formateada.append("fizz")
        elif i % 5 == 0:
            # print("buzz") # Si es multiplo de 5 imprimimos "buzz"
            lista_formateada.append("buzz")
        else: # Nno es necesario el else, lo dejamos para operar con la estructura completa y recordar.
            # print(i) # Si no es multiplo de 3 o 5 imprimimos el numero
            lista_formateada.append(i)
    
    return lista_formateada # Retornamos la lista con los valores en el formato especificado por el ejercicio

# Reto 2: Anagrama

# Recibimos dos palabras por teclado y debemos comprobar sin son anagramas una de la otra
# Crearemos una funcion en el modulo_retos.py donde le pasaremos las dos palabras obtenidas por teclado y nos devolvera
# True o False dependiendo si son anagramas o no

def anagrama(palabra1, palabra2):
    # Tenemos que comprobar dos cosas, primero la longitud de las palabras, si no lo son ya no son anagramas y podemos 
    # retornar False
    if len(palabra1) != len(palabra2):
        return False
    elif palabra1 == palabra2: # Dos palabras iguales no son un anagrama, son iguales xD
        return False
    else:
        # Usamos la primera palabra como indice
        # Debemos buscar cada letra de la primera palabra en la segunda palabra
        # Todas las letras de la primera palabra deben estar en la segunda palabra para que sea un anagrama
        # En el momento que no encontremos una letra de la primera palabra en la segunda palabra retornamos False y 
        # rompemos el bucle
        for i in palabra1: # Recorremos la palabra 1
            if i not in palabra2: # Buscamos cada letra de la palabra 1 en la palabra 2, si no la encontramos retornamos False
                return False
        return True # Si llegamos aqui es que todas las letras de la palabra 1 estan en la palabra 2, retornamos True
    
# Reto 3: Fibonacci

# Una succesion de fibonacci es una secuencia de numeros donde cada numero es la suma de los dos anteriores
# Empezamos en el 0 y el 1, a partir de ahi debemos crear una lista con el rango pasado como parametro

def fibonacci(rango):
    lista_fibonacci = [0, 1] # Creamos la lista con los dos primeros numeros de la succesion
    for i in rango: # Recorremos el rango pasado como parametro
        lista_fibonacci.append(lista_fibonacci[i] + lista_fibonacci[i + 1]) 
        # Sumamos los dos ultimos numeros de la lista y los agregamos a la lista
    return lista_fibonacci # Retornamos la lista con los numeros de la succesion de fibonacci
    
