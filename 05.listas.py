# Manejo de listas (arreglos, arrays, vectores, es lo mismo)

# nombrelista=[elemento,elemento2,elemento3,.....]

miLista=['joaquin',65,6.432,'sayago']
print (miLista)
print (type(miLista))

miLista=['joaquin',65,6.432,'sayago']
print (miLista[:])

#impresion de un elemento especifico de la lista
miLista=['joaquin',65,6.432,'sayago']
print (miLista[3])

#Impresion de la lista del final al principio
miLista=['joaquin',65,6.432,'sayago']
print (miLista[-2])

#Porcion de lista
miLista=['joaquin',65,6.432,'sayago']
print (miLista[1:3])

#Porcion de lista
miLista=['joaquin',65,6.432,'sayago']
print (miLista[:2])

#Porcion de lista
miLista=['joaquin',65,6.432,'sayago']
print (miLista[-2:-1])

#Agrega elemento al final de la lista, solo para agregar un elemento a la vez
miLista.append(234123)
print(miLista)

#Agrega elemento en posicion especifica
miLista.insert(2,'antonio')
print(miLista)

#Extender la lista con nuevos elementos, concatenacion de listas, para agregar mas de un argumento a la lista
miLista.extend(['jorge',33,45.56,'elena'])
#Imprime la posicion en el indice del elemento indicado
print(miLista.index('antonio'))

#Realiza una busqueda en la lista. Retorna true o false si encuentra el valor o false si no lo encuentra
print(87 in miLista)

#Elimina un elemento de la lista
miLista.remove('joaquin')
print(miLista)

#Eliminar el ultimo elemento de la lista
miLista.pop()
print(miLista)

#Las cadenas de caracteres no pueden ser modificadas ya que son inmutables
#Por tanto si se quiere eleminar une elemento de una cadena lo mejor es convertirla en lista y luego a cadena nuemvamente

vocales = 'aeiou'
#del vocales[4]
print (vocales)
lista_vocales = list(vocales)
print(lista_vocales)
del lista_vocales[4]
print (lista_vocales)

#La funcion in permite realizar busqueda de elemento en un string o en listas/tuplas
#Retorna un valor true o false dependiendo de si encuentra o no un valor
print('a' in vocales)
print('z' in lista_vocales)


if 'e' in  lista_vocales:
	print('El elemento es una vocal')
else:
	print('no se trata de una vocal')




