#Import permite importar o llamar a clases especiales de python
import math

#El programa pide un numero para obtener una raiz cuadrada
#Si se ponen numeros negativos o cero en 3 ocaciones se finaliza el programa
errores=0
numero = int(input('Dame un numero: '))
while numero <= 0:
    print('No se puede realizar la operacion')

    numero = int(input('Dame un numero: '))
    if numero <=0:
        errores=errores+1

    if errores == 2:
        print('Has intentado suficientes veces') 
        break
    
if numero > 0:
    raiz = math.sqrt(numero)
    print('La raiz de: ' + str(numero) + ' es ' + str(raiz))