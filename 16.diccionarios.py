"""Los diccionarios son estructuras de datos que permiten almacenar diferentes valores de 
diferentes tipos (enteros, cadenas, listas e incluso otros diccionarios)

Su caracteristica principal es que los datos se almacenan asociados a una clave de tal forma que se crea 
una asociación de tipo clave:valor"""

#En este diccionario la clave es el pais y la capital corresponde al valor
midiccionario={"alemania":"berlin","francia":"paris","reino unido":"londres", "españa":"madrid"}
print(midiccionario['alemania'])
print(midiccionario)

#Agregar mas elementos a un diccionario
midiccionario['italia']='lisboa'
print(midiccionario)

#Como ya existe una clave llamada italia, no agregara nuevamente italia con valor roma
#lo que se realiza es una actualización a la clave italia con su nuevo valor roma
midiccionario['italia']='roma'
print(midiccionario)

#Eliminar un elemento del diccionario
del(midiccionario['italia'])
print(midiccionario)

nuevodiccionario = {'Mexico':'cdmx','joaquin':32,12:'meses','anho':1986,'lista':[1,2,3,4,5]}
print(nuevodiccionario)
nuevodiccionario['tupla']=('a','b','c')
print(nuevodiccionario)

#Imprime las claves que corresponden al diccionario
print(nuevodiccionario.keys())

#Imprime los valores que integran el diccionario
print(nuevodiccionario.values())

#Imprime que la longitud del diccionario es de 6 ya que la clave:valor son un elemento separados por comas,,,,,,
print(len(nuevodiccionario))