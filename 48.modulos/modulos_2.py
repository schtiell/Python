# Import permite importar el codigo de otro modulo de codigo
# * permite indicarle a python que vamos a utilizar todo el codigo
# del archivo que le estamos indicando en la sentencia from
from modulos import sumar,restar,multiplicar

num1 = int(input("Introduce un numero:"))
num2 = int(input("Introduce otro numero: "))

#La sintaxis es nombre del modulo.atributo o funcion a utilizar
sumar(num1,num2)
restar(num1,num2)
multiplicar(num1,num2)