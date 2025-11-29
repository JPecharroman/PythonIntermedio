# Manejo de ficheros en Python

# Creamos un fichero de prueba para manejar ficheros fichero_prueba.txt

# Abrimos el fichero en modo lectura, para abrir el archivo necesitamos indicarle el directorio raiz donde esta
# guardado fichero_prueba.txt

fichero = open("PythonIntermedio/fichero_prueba.txt", "r") # Directorio raiz / fichero

print(fichero.read())

# Leemos el fichero, despues de leer el fichero el cursor se queda en la ultima linea, por lo que si queremos leerlo de nuevo
# debemos cerrar el fichero y abrirlo de nuevo

fichero.close()

fichero = open("PythonIntermedio/fichero_prueba.txt", "r") # Directorio raiz / fichero

# Leemos el fichero linea por linea
print(f"Linea 1: {fichero.readline()}")
print(f"\nLinea 2: {fichero.readline()}")
print(f"\nLinea 3: {fichero.readline()}")
print(f"\nLinea 4: {fichero.readline()}")

fichero.close()

# Leemos el fichero, despues de leer el fichero el cursor se queda en la ultima linea, por lo que si queremos leerlo de nuevo
# debemos cerrar el fichero y abrirlo de nuevo

fichero = open("PythonIntermedio/fichero_prueba.txt", "r") # Directorio raiz / fichero
print(fichero.readlines()) # Nos devuelve una lista con todas las lineas del fichero, finalizando en salto de linea \n.

fichero.close()

# Abrimos el fichero en modo r+, vamos a intentar escribir algo en el fichero
fichero = open("PythonIntermedio/fichero_prueba.txt", "r+") # Directorio raiz / fichero , "r+" modo lectura y escritura
# Leemos el fichero para posicionarnos al final
fichero.read()
fichero.write("Hola mundo") # Comentado para no borrar el contenido
fichero.close()

fichero = open("PythonIntermedio/fichero_prueba.txt", "r") # Directorio raiz / fichero
print(fichero.read())
fichero.close()

# Vamos a tratar de borrar una linea del fichero, la edad por ejemplo
# Lo haremos con un tratamiento de errores
try:
    fichero = open("PythonIntermedio/fichero_prueba.txt", "r+") # Directorio raiz / fichero , "r+" modo lectura y escritura
    # Creamos una lista con todas las lineas del fichero
    lineas = fichero.readlines()
    # Eliminamos la linea 2 de la lista
    lineas.__delitem__(2)
    # Volvemos a escribir el fichero
    fichero = open("PythonIntermedio/fichero_prueba.txt", "w") # Directorio raiz / fichero , "w" modo escritura
    fichero.writelines(lineas)
except FileNotFoundError:
    print("El fichero no existe")
except Exception as e:
    print(e)
finally:
    fichero.close()

# leemos nuestro nuevo fichero para ver si me ha borrado la edad.
fichero = open("PythonIntermedio/fichero_prueba.txt", "r") # Directorio raiz / fichero
print(fichero.read())
fichero.close()

# Crear un fichero nuevo, lo hacemos con el modo escritura, si el fichero no existe lo crea.
fichero = open("PythonIntermedio/fichero_nuevo.txt", "w") # Directorio raiz / fichero , "w" modo escritura
fichero.write("Hemos creado un fichero nuevo.") # Escribimos algo en el fichero
fichero.close()

fichero = open("PythonIntermedio/fichero_nuevo.txt", "r") # Directorio raiz / fichero
print(fichero.read())
fichero.close()

# Borrar un fichero, importamos el modulo os, concretamente necesitamos la funcion remove, asi que por economizar memoria
# Traremos solo la funcion que necesitamos
from os import remove
remove("PythonIntermedio/fichero_nuevo.txt")

# Creamos el fichero, lo llenamos con el mensaje, lo escribimos y lo borramos.