# Por claridad, vamos a crear un fichero nuevo de manejo de ficheros.

# En este fichero gestionaremos los ficheros xml
import xml

# Un fichero de tipo xml es un archivo de texto que usa etiquetas personalizadas para estructurar, almacenar y transportar 
# datos de manera que puedan ser leídos tanto por humanos como por máquinas.
# Tiene una caracteristicas determinadas a tener en cuenta
# - Son archivos de texto
# - Son archivos que usan etiquetas personalizadas
# - Los datos se estructuran de manera jerarquica, usamos etiquetas anidadas
# - Cada etiqueta debe estar correctamente cerrada, sino generara error

# Creamos el fichero xml y cerramos, gestionaremos lecturas y escrituras con el with.
fichero_xml = open("PythonIntermedio/fichero_xml.xml", "w")
fichero_xml.close()

# Añadir contenido al fichero xml
# Vamos a añadir un registro al fichero xml
cabecera_xml =  ("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n") # Usamos /" para poder poner la comilla doble dentro de un string

# Usamos try y with para gestionar errores y cerrar el fichero xml
try:
    with open("PythonIntermedio/fichero_xml.xml", "w") as fichero_xml:
        fichero_xml.write(cabecera_xml)
except FileNotFoundError:
    print("El fichero no se ha encontrado")
except Exception as e:
    print(e)

# Añadimos varios registros al fichero xml
linea_1 = "<libro><titulo>Libro 1</titulo><autor>Autor 1</autor></libro>\n"
linea_2 = "<libro><titulo>Libro 2</titulo><autor>Autor 2</autor></libro>\n"
linea_3 = "<libro><titulo>Libro 3</titulo><autor>Autor 3</autor></libro>\n"

# Como no queremos perder los datos del fichero debemos sacar los datos del fichero a una variable
try:
    with open("PythonIntermedio/fichero_xml.xml", "r") as fichero_xml:
        datos_fichero_xml = fichero_xml.read() # Leemos el fichero xml y lo guardamos en una variable, datos_fichero_xml
except FileNotFoundError:
    print("El fichero no se ha encontrado")
except Exception as e:
    print(e)

# Añadimos los registros al fichero xml, partimos de lo que tenemos guardado en datos_fichero_xml y añadimos lo demas.
try:
    with open("PythonIntermedio/fichero_xml.xml", "w") as fichero_xml:
        fichero_xml.write(datos_fichero_xml)
        fichero_xml.write(linea_1)
        fichero_xml.write(linea_2)
        fichero_xml.write(linea_3)
except FileNotFoundError:
    print("El fichero no se ha encontrado")
except Exception as e:
    print(e)

# Leemos el fichero xml
try:
    with open("PythonIntermedio/fichero_xml.xml", "r") as fichero_xml:
        for indice in fichero_xml:
            print(indice)
except FileNotFoundError:
    print("El fichero no se ha encontrado")
except Exception as e:
    print(e)


