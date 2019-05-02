#Manejo de tuplas

#Mas rapidass que las lista
#No permiten ser modificadas
#Mas adecuadas para el manejo de datos que unicamente serán de lectura

#Sintaxis de la tupla
#tupla = ('a','b','c','d','e')

#convertir una lista en tupla, funcion tupl

miLista = ['a',1,3,'b','v',5,4,2,5,2,3,5,7,4,3,5,75,3,45,3,56]
mitupla = tuple(miLista)
print (mitupla)

#Conocer si mi objeto es una tupla
print (type(mitupla))

#Saber el indice de un elemento
print (mitupla.index(4))

#Convertir una tupla en lista y comprobar
mitupla = list(miLista)
print (miLista)
print (type(miLista))

#Busca un elemento especificado en la tupla, retorna false o true
print('z' in mitupla)
print('a' in mitupla)

#Cuenta el numero de veces que se encuentra el elemento en la tupla
print(mitupla.count(3))
print(mitupla.count(5))

#Imprime el numero de elementos o la longitud de la tupla o la lista
print(len(mitupla))
print(len(miLista))

#Ejemplo de tupla unitaria, debe incluirse la , despues del elemento para indicar que es tupla unitaria
tupla=('Joaquin',)
print(len(tupla)) 

#Empaquetado de tupla, ya que python lo guarda como una tupla
mitupla = 'joaquin','antonio','sayago','trujillo'
print(mitupla)

#Desempaquetado de tuplas
fecha_tupla='viernes','mayo',2018
dia,mes,anho = fecha_tupla
print(dia)
print(mes)
print(anho)