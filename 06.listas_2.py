#Manejo de listas 2

miLista=['joaquin','sayago','trujillo',8421400,32,'febrero']
miLista2=['sandra','lucia','Mexico']

#Union o concatenacion de listas
miLista3=miLista+miLista2
print(miLista3)

#Repetir listas

miLista2=['sandra','lucia','Mexico'] * 3
print(miLista2)

#Funcion sort ordena de menos a mayor una lista
miListaNumerica = [2,5,12,79,47,23,56,4,3,1,6,7,33,45,221,97,86]
print (miListaNumerica)
miListaNumerica = miListaNumerica.sort()
print (miListaNumerica)

#La funcion sort tambien ordena listas alfabeticamente
miListaAlfabetica = ['a','f','w','e','h','s','o','i','c','p','q','l','k','z','?','-','/','¿']
print(miListaAlfabetica)
miListaAlfabetica.sort()
print(miListaAlfabetica)

#La funcion sort no permite el ordenamiento entre valores str y los int, por lo cual al intentar ordenar mara error
#Not supported between instances of 'str' and 'int'
#miListaAlfanumerica = [1,8,3,0,'h',6,'w','t','a',9,'r','g',4]
#miListaAlfanumerica.sort()
#print (miListaAlfanumerica)










