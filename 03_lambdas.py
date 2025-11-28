# Lambdas en Python

# Las Lambdas son funciones anonimas, es decir, funciones que no tienen nombre
# Son funciones que se definen en una sola linea de codigo
# Son funciones que se definen con la palabra clave lambda
# Son funciones que se definen con la sintaxis lambda argumentos : expresion
# 

lambda x: x + 1

# Una Lambda puede tener parametros de entrada
lambda primer_valor, segundo_valor: primer_valor + segundo_valor

# Para llamar a una Lambda, debemos asignarla a una variable
mi_lambda = lambda x: x + 1

# Llamamos a la Lambda
print(mi_lambda(1)) # Devuelve 2

mi_lambda = lambda primer_valor, segundo_valor: primer_valor + segundo_valor
print(mi_lambda(1, 2)) # Devuelve 3

# El uso mas comun de las Lambdas es como parte de una funcion de orden superior

def suma_valores(primer_valor, segundo_valor):
    return mi_lambda(primer_valor, segundo_valor)

print(suma_valores(1, 2)) # Devuelve 3

# Otra forma de usar una Lambda
# Operamos con la lambda implicita sin darle valores en la definicion de la funcion, se los pasaremos posteriormente
# en la llamada a la funcion.
def suma_tres_valores(valor):
    return lambda primer_valor, segundo_valor: valor + primer_valor + segundo_valor

print(suma_tres_valores(1)(2, 3)) # Devuelve 6, los valores de lambda van entre parentesis despues del paramentro de la funcion

