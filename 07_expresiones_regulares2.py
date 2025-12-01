# Por claridad usamos un segundo fichero de expresiones regulares para hablar de los patrones personalizados, ya que el fichero principal se ha vuelto demasiado largo.

# Importamos el modulo re
import re

# Patrones personalizados de expresiones regulares
# Un patron personalizado es un patron que se compone de varios patrones
# Una web muy util para crear patrones personalizados es https://regex101.com/

# Si escribimos entre corchetes [] varios caracteres, el patron buscado sera cualquiera de ellos
# Por ejemplo, si escribimos [a-z], el patron buscado sera cualquier letra minuscula
# Si escribimos [A-Z], el patron buscado sera cualquier letra mayuscula
# Si escribimos [0-9], el patron buscado sera cualquier numero
# Si escribimos [a-zA-Z0-9], el patron buscado sera cualquier letra mayuscula o minuscula o numero
# \ se usa para buscar caracteres especiales, por ejemplo \n para buscar un salto de linea
# ^ se usa para buscar el inicio de una cadena de texto
# $ se usa para buscar el final de una cadena de texto
# . se usa para buscar cualquier caracter
# * se usa para buscar cero o mas ocurrencias
# + se usa para buscar una o mas ocurrencias
# ? se usa para buscar cero o una ocurrencia
# {n} se usa para buscar n ocurrencias
# {n,} se usa para buscar n o mas ocurrencias
# {n,m} se usa para buscar entre n y m ocurrencias
# | se usa para buscar varias cadenas de texto
# () se usa para agrupar patrones
# [^] se usa para buscar cualquier caracter excepto los que estan entre corchetes
# [^a-z] se usa para buscar cualquier caracter excepto las letras minusculas
# [^A-Z] se usa para buscar cualquier caracter excepto las letras mayusculas
# [^0-9] se usa para buscar cualquier caracter excepto los numeros
# [^a-zA-Z0-9] se usa para buscar cualquier caracter excepto las letras mayusculas, minusculas y numeros
# [^\n] se usa para buscar cualquier caracter excepto el salto de linea
# [^\s] se usa para buscar cualquier caracter excepto los espacios
# [^\S] se usa para buscar cualquier caracter excepto los espacios
# [^\w] se usa para buscar cualquier caracter excepto las palabras
# [^\W] se usa para buscar cualquier caracter excepto las palabras
# [^\d] se usa para buscar cualquier caracter excepto los numeros
# [^\D] se usa para buscar cualquier caracter excepto los numeros
# [^\b] se usa para buscar cualquier caracter excepto los bordes
# [^\B] se usa para buscar cualquier caracter excepto los bordes
# [^\r] se usa para buscar cualquier caracter excepto el retorno de carro
# [^\R] se usa para buscar cualquier caracter excepto el retorno de carro
# [^\t] se usa para buscar cualquier caracter excepto el tabulador
# [^\T] se usa para buscar cualquier caracter excepto el tabulador
# [^\v] se usa para buscar cualquier caracter excepto el salto vertical
# [^\V] se usa para buscar cualquier caracter excepto el salto vertical
# [^\f] se usa para buscar cualquier caracter excepto el salto de pagina
# [^\F] se usa para buscar cualquier caracter excepto el salto de pagina
# [^\a] se usa para buscar cualquier caracter excepto el sonido
# [^\A] se usa para buscar cualquier caracter excepto el sonido
# [^\e] se usa para buscar cualquier caracter excepto el escape
# [^\E] se usa para buscar cualquier caracter excepto el escape
# [^\c] se usa para buscar cualquier caracter excepto el control
# [^\C] se usa para buscar cualquier caracter excepto el control
# [\d] se usa para buscar cualquier numero
# [\D] se usa para buscar cualquier numero
# [\s] se usa para buscar cualquier espacio
# [\S] se usa para buscar cualquier espacio
# [\w] se usa para buscar cualquier palabra
# [\W] se usa para buscar cualquier palabra
# [\b] se usa para buscar cualquier borde
# [\B] se usa para buscar cualquier borde
# [\r] se usa para buscar cualquier retorno de carro
# [\R] se usa para buscar cualquier retorno de carro
# [\t] se usa para buscar cualquier tabulador
# [\T] se usa para buscar cualquier tabulador
# [\v] se usa para buscar cualquier salto vertical
# [\V] se usa para buscar cualquier salto vertical
# [\f] se usa para buscar cualquier salto de pagina
# [\F] se usa para buscar cualquier salto de pagina
# [\a] se usa para buscar cualquier sonido
# [\A] se usa para buscar cualquier sonido
# [\e] se usa para buscar cualquier escape
# [\E] se usa para buscar cualquier escape
# [\c] se usa para buscar cualquier control
# [\C] se usa para buscar cualquier control

# Buscamos un mayuscula o una minuscula con [a-zA-Z]
texto = "lorem ipsum dolor sit amet consectetur adipiscing elit, lorem ipsum dolor sit amet consectetur adipiscing elit, lorem ipsum dolor sit amet consectetur adipiscing elit"
patron_expreg = r"[a-zA-Z]"
numero = re.search(patron_expreg, texto)
print(numero)

patron_expreg = r"[r].[m]" # Buscamos una r, con algun caracter entre r y m, y que termine en m
texto = "lorem ipsum dolor sit amet consectetur adipiscing elit, lorem ipsum dolor sit amet consectetur adipiscing elit, lorem ipsum dolor sit amet consectetur adipiscing elit"
numero = re.findall(patron_expreg, texto)
print(numero)

# Buscamos varias palabras en el texto con |, r"texto1|texto2|texto3"
numero = re.findall("lorem|ipsum|dolor", texto)
print(numero)

# Recordar que Python distingue entre mayusculas y minusculas, por eso usamos [mayuscula|minuscula] para buscar ambas
texto = "Lorem ipsum dolor sit amet consectetur adipiscing elit, lorem Ipsum Dolor sit amet consectetur a   dipiscing elit, LOREM IPSUM DOLOR SIT AMET CONSECTETUR ADIPISCING ELIT"
numero = re.findall("[lL]orem|[I|i]psum|[D|d]olor|DOLOR", texto)
print(numero)

# Ejemplo de algo que hacemos habitualmente, expresion regular para saber si una cadena pasada como paramentro es un email
patron_expreg = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

email_valido = "jorge@jorge.com"
email_no_valido = "jorge#jorge.com"
numero = re.match(patron_expreg, email_valido)
print(numero) # Aqui vemos que match() nos devuelve el objeto, esto es, es un objeto que contiene la informacion de la coincidencia
numero = re.match(patron_expreg, email_no_valido)
print(numero) # Aqui vemos que match() nos devuelve None, esto es, no ha encontrado la coincidencia, no es una variable que case con un tipo email
# Podemos buscarlo con search() tambien
numero = re.search(patron_expreg, email_valido)
print(numero) # Aqui vemos que search() nos devuelve el objeto, esto es, es un objeto que contiene la informacion de la coincidencia
numero = re.search(patron_expreg, email_no_valido)
print(numero) # Aqui vemos que search() nos devuelve None, esto es, no ha encontrado la coincidencia, no es una variable que case con un tipo email

tercer_email = "jorge@pepe.d"
numero = re.match(patron_expreg, tercer_email)
print(numero) 
# Aqui vemos que match() nos devuelve None, esto es, no ha encontrado la coincidencia, la parte final de la expresion nos indica {2,} asociada a [a-zA-Z]
# que significa que debe haber al menos dos caracteres de tipo a-zA-Z despues del punto, expresado como \., veamoslo
tercer_email = "jorge@pepe.dd"
numero = re.match(patron_expreg, tercer_email)
print(numero) # Aqui vemos que match() nos devuelve el objeto, esto es, es un objeto que contiene la informacion de la coincidencia

# Ver si una cadena pasada es un N.I.F. Valido, para ser un nif valido tiene que ser una cadena de 8 valores de tipo 0-9 seguidos de una letra de tipo a-zA-Z
patron_expreg = r"[0-9]{8}[a-zA-Z]{1}"
nif_valido = "12345678J"
nif_no_valido = "123456789K"
numero = re.match(patron_expreg, nif_valido)
print(numero) # Aqui vemos que match() nos devuelve el objeto, esto es, es un objeto que contiene la informacion de la coincidencia
numero = re.match(patron_expreg, nif_no_valido)
print(numero) # Aqui vemos que match() nos devuelve None, esto es, no ha encontrado la coincidencia, ya que {8} indica que debe haber 8 valores de tipo 0-9 y 
# nif_no_valido tiene 9 valores de tipo 0-9