# MANEJO DE PAQUETES
# ¿Qué son?
# Son directorios donde se almancenaran modulos relacionados entre si

# ¿Para que sirve?
# Sirven para organizar y reutilizar los modulos

# ¿Como se crea un paquete?
# Se crean con una carpeta con un archivo llamado __init__.py
# con el nombre como si se definiera un método constructor

# Es posible para ordenar aun mas el codigo generar submodulos
# es decir subcarpetas, solo deben contener el archivo __init__py
# sintaxis:
# from carpeta.subcarpeta.archivo import atributo y/o funcion y/o clase
# o bien:
# from paquete.subpaquete.modulo import atributo y/o funcion y/o clase

from paquetes.basicos.calculos_basico import *
from paquetes.potencia.calculo_potencia import potencia
from paquetes.redondeos.redondeo import redondear

numero1 = int(input("Dame un numero: "))
numero2 = int(input("Dame otro numero: "))

sumar(numero1,numero2)
restar(numero1,numero2)
multiplicar(numero1,numero2)
dividir(numero1,numero2)

potencia(numero1,numero2)

redondear(numero1)
redondear(numero2)