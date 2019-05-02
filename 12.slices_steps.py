numeros = [0,1,2,3,4,5,6,7,8,9,10]

# Los 2 puntos en los corchetes separan el inicio : hasta
print (numeros [:])

#Imprime los valores desde el indice 0 hasta 5 ya que el valor del indice 6 no es inclusivo
print (numeros[0:6])

#Lo mismo si se quiere imprimir de atras para adelante
#El tercer elemento indica los STEPS
#Es decir de  cuanto en cuanto va a ir imprimiendo la lista
print(numeros[-1:-9:-1])

#Imprime toda la cadena de 2 en 2 y de 3 en 3
print(numeros[::2])
print(numeros[::3])

#imprime del indice uno al indice 3 al indice 5 al indice 7 y el indice 9 no se imprime ya que no se incluye
print (numeros[1:9:2])
#imprime del indice uno al indice 4 al indice 7 
print (numeros[1:9:3])

#El indice -1 es el valor 10, el 7 el 4
print(numeros[-1:-9:-3])