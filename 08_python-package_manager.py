# Gestor de paquetes de Python
# El gestor de paquetes de Python es pip
# Web de PIP https://pypi.org/

# pip se usa para instalar, actualizar y desinstalar paquetes de Python
# pip se usa para buscar paquetes de Python
# pip se usa para listar paquetes de Python
# pip se usa para mostrar informacion de un paquete de Python
# pip se usa para desinstalar paquetes de Python
# pip se usa para actualizar paquetes de Python
# pip se usa para instalar paquetes de Python desde un archivo requirements.txt
# pip se usa para desinstalar paquetes de Python desde un archivo requirements.txt
# pip se usa para actualizar paquetes de Python desde un archivo requirements.txt
# pip se usa para mostrar informacion de un paquete de Python desde un archivo requirements.txt
# pip se usa para listar paquetes de Python desde un archivo requirements.txt
# pip se usa para buscar paquetes de Python desde un archivo requirements.txt

# Vamos a comprobar si pip esta instalado
# pip --version
# Si no tenemos pip en el PATH de windows, para ver la version debemos colocar antes python -m
# python -m pip --version
# Para añadir pip en el PATH de windows 
# ir a variables de entorno --> pinchar en variables de entorno --> variables de usuario para usuario --> PATH --> Editar --> 
#    Nuevo --> C:\Users\usuario\AppData\Local\Programs\Python\Python313\Scripts
# Vamos a instalar pip desde consola, al no tener pip en el PATH de windows lo hacemos con python -m
# python -m pip install pip
# Nos dice que esta instalado y que si queremos actualizarlo usemos install --upgrade pip
# Ruta donde esta python.exe seguido de -m pip install --upgrade pip
# C:\Users\usuario\AppData\Local\Programs\Python\Python313\python.exe -m pip install --upgrade pip


# Vamos a instalar un paquete, numpy por ejemplo
# (python -m) pip install numpy
# veamos que hemos traido
import numpy
print(numpy.__version__) # Si hemos instalado correctamente numpy nos muestra la version
# Para acceder a la documentacion de numpy usamos numpy.__doc__
print(numpy.__doc__)


# Instalamos otro paquete, pandas por ejemplo
# (python -m) pip install pandas
import pandas as pd
print(pd.__version__)
print(pd.__doc__)
# Copias la documentacion de pandas en un archivo txt creado por nosotros
# (python -m) pip install pandas --help > pandas_help.txt
# Probamos el show de pandas
# (python -m) pip show pandas
# show nos devuelve informacion del paquete pandas, como la version, la ubicacion, autor y demas informacion, asi como donde esta instalado

# Vamos a listar todos los paquetes instalados
# (python -m) pip list
# list nos devuelve todos los paquetes instalados en el sistema asi como su version actual.

# Instalamos un paquete aleatorio que luego desinstalaremos, por ejemplo 'pycodestyle'
# (python -m) pip install pycodestyle
# Veamos si esta instalado
# (python -m) pip show pycodestyle
# Desinstalamos el paquete pycodestyle
# (python -m) pip uninstall pycodestyle

# Un paquete que necesitaremos para nuestro siguiente leccion es 'requests'
# Instalamos requests con pip
# (python -m) pip install requests
import requests as req

print(req.__version__)
print(req.__doc__)
# Copiamos la documentacion de requests en un archivo txt creado por nosotros
# (python -m) pip install requests --help > requests_help.txt

# Veamos que podemos hacer con requests
print(dir(req))
# Veamos que podemos hacer con requests.get
print(dir(req.get))
# Veamos que podemos hacer con requests.get.__doc__
print(req.get.__doc__)

# Hacemos una peticion a la API de Pokemon del github de MoureDev, queremos traer los primeros 151 Pokemon
respuesta = req.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(respuesta) # Nos muestra la respuesta de la peticion, en este caso nos devuelve un codigo 200 que significa que la peticion ha sido exitosa
# Podemos hallar el codigo directamente de la respuesta con respuesta.status_code
print(respuesta.status_code)
# Podemos hallar el contenido de la respuesta con respuesta.content
print(respuesta.content)
# Podemos hallar el contenido de la respuesta en formato JSON con respuesta.json()
print(respuesta.json())

