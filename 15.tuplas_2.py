#Con asignarle valores separados por comas a una variable, python lo identifica  automaticamente en una tupla
tupla = 1,2,3,4
print(tupla)

#Los parentesis no siempre indican a python que se trata de ua tupla
#Es necesario poner una coma al elemento unico para indicarle que es una tupla
tupla_2=(1)
print(tupla_2)

#De esta manera se indica a python que es una tupla de un elemento por la coma ,
tupla_3=(1,)
print(tupla_3)

#Tupla de 2 enteros y una lista. Las listas si son mutables por lo que si es posible modificar las listas en tuplas sin eliminarlas
tupla_4 = 1,2,[1,2,3]
print(tupla_4)

#Es posible usar las funciones de las listas en una tupla con elementos que sean listas
#Nombre de la tupla en la posicion 2, como es lista agrega al final de esta el 4
tupla_4[2].append(4)
print(tupla_4)

#Nombre de la tupla en la posicion 2, como es lista inserta en el indice 1 la letra 'a'
tupla_4[2].insert(1,'a')
print(tupla)