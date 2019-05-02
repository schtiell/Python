numeros = [0,1,2,3,4,5,6,7,8,9,10]

#Borra el elemento de la lista en el indice que se le indique
del numeros[0]
print (numeros)

#Eliminar los elemento de la posicion 1 al 5 sin tomar en cuenta el 5
del (numeros[1:5])
print (numeros)

#Para agregar elementos a la lista se hace de la siguiente manera
#Agrega a partir del indice 1 hasta el 2 que no es inclusivo los valores que se indican
numeros[1:2] = [2,3,4,5,6]
print(numeros)

#Para reemplazar valores se realiza lo mismo
#Lo cual convierte los valores de los indices 8 y 9 en 90 y 10
numeros[8:10] = [90,100]
print(numeros)

#Con el -1 le indicamos que debe moverse de derecha a izquierda en el recorrido
numeros[-5:-8:-1] = [60,50,40]
print(numeros)

