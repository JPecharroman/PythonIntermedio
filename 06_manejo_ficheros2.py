# Por claridad, vamos a crear un fichero nuevo de manejo de ficheros.abs

# Vamos a ver como manejar un fichero json.

# Un fichero json es un fichero que contiene datos en formato json.
# JSON es un formato de datos que se utiliza para almacenar y transferir datos.
# Los datos en un archivo JSON son almacenados en pares clave-valor, lo que vendria a ser un diccionario de Python.

# Veamos como podemos trabajar con un fichero .json
# Vamos a crear un fichero .json

import json

# Creamos el fichero .json

fichero_json = open("PythonIntermedio/fichero_json.json", "w")

# Recordatorio, los diccionarios en Python se escriben entre llaves {} y deben seguir el formato de pares "clave": "valor"
# Vamos a crear un diccionario para recordar el formato
persona = {
    "nombre": "Jorge", 
    "apellido": "Garcia",
    "edad": 30, 
    "ciudad": "Madrid",
    "trabajo": "Programador",
    "estado_civil": "Soltero",
    "nacional": True
    }

# Escribimos en el fichero .json, para ello usamos el metodo dumps de json
# Los argumentos que pasamos a un write de un fichero deben ser de tipo string, no podemos pasarle un diccionario
# dumps convierte el diccionario pasado como parametro en un string json
fichero_json.write(json.dumps(persona)) 
# Otra forma seria poner el fichero en el parametro file de json.dump, json.dump(persona, fichero_json)
# Nos ahorrariamos el write.
fichero_json.close()

# Podemos añadir parametros al json, vamos a indentar los valores del fichero para que no quede en una linea
# Nos crea una tabulacion de 4 posiciones entre cada valor
# Vamos a añadir sort_keys=True para ordenar los valores del fichero, los ordena alfabeticamente por claves.
fichero_json = open("PythonIntermedio/fichero_json.json", "w")
json.dump(persona, fichero_json, indent=4, sort_keys=True)
# Cerramos el fichero
fichero_json.close()


# Añadimos un nuevo diccionario al fichero
# Leemos el fichero y lo guardamos en una variable de tipo diccionario
fichero_json = open("PythonIntermedio/fichero_json.json", "r")
diccionario_temporal = json.load(fichero_json) # Cargamos el fichero en un diccionario
# print(diccionario_temporal)
# Cerramos el fichero
fichero_json.close()

# Creamos la otra persona
otra_persona = {
    "nombre": "Ana", 
    "apellido": "Garcia",
    "edad": 25, 
    "ciudad": "Madrid",
    "trabajo": "Peluquera",
    "estado_civil": "Soltera",
    "nacional": True
    }

# Abrimos el fichero en modo escritura
fichero_json = open("PythonIntermedio/fichero_json.json", "w")
# Creamos una lista con nuestros diccionarios, el cargado desde el json y el nuevo
lista_personas = [diccionario_temporal, otra_persona]
# Escribimos en el fichero .json, para ello usamos el metodo dumps de json
json.dump(lista_personas, fichero_json, indent=4)
# Cerramos el fichero
fichero_json.close()

# Leemos el fichero .json
fichero_json = open("PythonIntermedio/fichero_json.json", "r")
print(fichero_json.read())
# Otra forma seria usar json.load(fichero_json), aunque no lo presenta tan limpio al crear una lista para representar los datos.

# Cerramos el fichero
fichero_json.close()