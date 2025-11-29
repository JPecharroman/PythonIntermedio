# Por claridad, vamos a crear un fichero nuevo de manejo de ficheros.

# Podemos crear varios ficheros para otro tipo de ficheros, aunque no los veremos por tiempo, por ejemplo
# xlxs debemos importar xlrd
# pdf debemos importar pdfplumber
# xml debemos importar xml
# xlrd debemos importar xlrd

# En este fichero gestionaremos los ficheros csv

import csv

# Creacion de fichero csv
fichero_csv = open("PythonIntermedio/fichero_csv.csv", "w")

# csv almacena datos en formato tabular, donde la primera línea suele contener los encabezados de las columnas y 
# las líneas subsiguientes contienen los datos separados por comas
# Hacemos un paso de datos analogo al del fichero json creado anteriormente
cabecera_csv = ["nombre", "apellidos", "edad", "email", "genero", "soltero"]

# Escribimos la cabecera en el fichero csv, para ellos necesitamos
# definir una variable que cargamos con el writer del csv, csv.writer(nombre_fichero)
escribir_csv = csv.writer(fichero_csv)

# Escribimos la cabecera en el fichero csv mediante la funcion writerow(variable_con_los_datos)
escribir_csv.writerow(cabecera_csv)

# Cargamos datos en el fichero csv
persona_1 = ["Jorge", "Perez", "30", "jorgeperez@gmail.com", "Masculino", True]
escribir_csv.writerow(persona_1)

persona_2 = ["Ana", "Garcia", "25", "anagarcia@gmail.com", "Femenino", False]
escribir_csv.writerow(persona_2)

# Podemos cargar mas de una linea con la funcion writerows()
escribir_csv.writerows([
    ["Luis", "Rodriguez", "28", "luisrodriguez@gmail.com", "Masculino", True],
    ["Elena", "Lopez", "22", "elenalopez@gmail.com", "Femenino", False]
])

# Para operar con claridad creamos variables con los datos
persona_3 = ["Pedro", "Perez", "38", "pedroperez@gmail.com", "Masculino", True]
persona_4 = ["Luisa", "Hernandez", "22", "luisahernandez@gmail.com", "Femenino", False]

# Y cargamos datos en el fichero csv con writerows(), writerows() lleva corchetes despues del parentesis
escribir_csv.writerows([persona_3, persona_4])

# Cerramos el fichero
fichero_csv.close()

# Podemos leer el fichero csv

# Abrimos el fichero para lectura
fichero_csv = open("PythonIntermedio/fichero_csv.csv", "r")

# Leemos el fichero csv, definimos una variable que cargamos con el reader del csv, csv.reader(nombre_fichero)
leer_csv = csv.reader(fichero_csv)

# Recorremos el fichero csv con un bucle for
for persona in leer_csv:
    print(persona)

# Cerramos el fichero
fichero_csv.close()

# Otra forma de leer el fichero es usar la instruccion with
# with es una palabra reservada que sirve para abrir y cerrar el fichero
with open("PythonIntermedio/fichero_csv.csv", "r") as fichero_csv:
    leer_csv = csv.reader(fichero_csv)
    for persona in leer_csv:
        print(persona)

# Añadir valores a un fichero csv sigue la dinamica anterior, debemos sacar los datos del fichero csv a una variable temporal,
# añadirle los datos que queramos y luego escribirlos en el fichero csv

try:
    with open("PythonIntermedio/fichero_csv.csv", "r") as fichero_csv:
        leer_csv = csv.reader(fichero_csv)
        datos_csv = []
        for persona in leer_csv:
            datos_csv.append(persona)
except FileNotFoundError:
    print("El fichero no existe")
except Exception as e:
    print(e)

# Añadimos datos al fichero csv
persona_5 = ["Maria", "Garcia", "22", "maria@gmail.com", "Femenino", False]
datos_csv.append(persona_5) # datos_csv es de tipo lista, podemos hacerle un append y que nos añada los datos al final

# Escribimos los datos en el fichero csv
try:
    with open("PythonIntermedio/fichero_csv.csv", "w") as fichero_csv:
        escribir_csv = csv.writer(fichero_csv)
        escribir_csv.writerows(datos_csv)
except FileNotFoundError:
    print("El fichero no existe")
except Exception as e:
    print(e)

# Leemos el fichero csv para ver si nos ha añadido el nuevo registro
try:    
    with open("PythonIntermedio/fichero_csv.csv", "r") as fichero_csv:
        leer_csv = csv.reader(fichero_csv)
        for persona in leer_csv:
            print(persona)
except FileNotFoundError:
    print("El fichero no existe")
except Exception as e:
    print(e)
