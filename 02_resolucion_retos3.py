# Por limpieza iremos creando diveras paginas de resolucion de retos con unos o dos retos por pagina
# El modulo sera siempre el mismo, donde iremos creando las funciones para resolver los retos, modulo_retos.py

# Importamos area desde modulo_retos
from modulo_retos import area

# Reto 5: 

"""
 
 * Area de poligono

 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.

"""

# Debemos crear una funcion que reciba un poligono y nos devuelva el area del poligono
# Tenemos tres tipos de poligonos, el triangulo, el cuadrado y el rectangulo
# El triangulo es un poligono de 3 lados, el cuadrado es un poligono de 4 lados y el rectangulo es un poligono de 4 lados
# El area de un triangulo es base * altura / 2
# El area de un cuadrado es base * altura
# El area de un rectangulo es base * altura

# Debemos crear una funcion que reciba el tipo de poligono y los valores de los lados
# y nos devuelva el area del poligono

tupla_poligonos = ("triangulo", "cuadrado", "rectangulo") # Creamos una tupla ya que los valores son constantes e inmutables

poligono = input("Introduce el poligono: ")

# Debemos comprobar que el valor introducido es un poligono
poligono = poligono.lower()

if poligono not in tupla_poligonos:
    print("El poligono introducido no es valido")
elif poligono == "triangulo":
    print("Introduce los valores del triangulo")
    base = int(input("Introduce la base del triangulo: "))
    altura = int(input("Introduce la altura del triangulo: "))
    # Vamos a la funcion creada para comprobar el area de los poligonos
    area_triangulo = area(poligono, base, altura)
    print(f"El area del triangulo es: {area_triangulo}")
elif poligono == "cuadrado":
    print("Introduce los valores del cuadrado")
    lado = int(input("Introduce el lado del cuadrado: "))
    # Vamos a la funcion creada para comprobar el area de los poligonos
    area_cuadrado = area(poligono, lado, lado) # Como es un cuadrado, los lados son iguales
    print(f"El area del cuadrado es: {area_cuadrado}")
elif poligono == "rectangulo":
    print("Introduce los valores del rectangulo")
    base = int(input("Introduce la base del rectangulo: "))
    altura = int(input("Introduce la altura del rectangulo: "))
    # Vamos a la funcion creada para comprobar el area de los poligonos
    area_rectangulo = area(poligono, base, altura)
    print(f"El area del rectangulo es: {area_rectangulo}")

    
