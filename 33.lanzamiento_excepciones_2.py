# Lanzamiento de Excepciones propias, es decir deifinidas por el usuario

# Se importa la clase math para utilizar la funcion sqrt() para calcular la raíz cuadrada
import math


def calcular_raizcuadrada(numero):

    # Si se envía un numero negativo se levanta una excepcion propia de tipo ValueError
    if numero < 0:
        raise ValueError ('No es posible calcular la raíz cuadrada a un numero negativo')

    else:
        raiz = math.sqrt(numero)
        return raiz

numero = int(input('Numero para calcular la raíz cuadrada: '))


try:
    print(calcular_raizcuadrada(numero))

# En caso de ocurrir una excepción del tipo levantado se identifica la excepcion con un nombre y se imprime
except ValueError as error_raiz_cuadrada:
    print(error_raiz_cuadrada)

# Si no existen excepciones el flujo del programa continua
print('Impresion para comprobar el flujo de ejecución del programa')