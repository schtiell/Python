#Creando un diccionario con el dia y la fecha del mes
calendario = {'lunes':1,'martes':2,'miercoles':3,'jueves':4,'viernes':5}
print(calendario)

#agregando un nuevo elemento:valor
calendario['sabado'] = 6
print(calendario)

#eliminando un elemento
del calendario['lunes']
print(calendario)

#Actualizando varios elementos a la vez
#En el caso del elemento domingo no existe por lo cual lo creara dentro del diccionario con su valor
calendario.update({'viernes':13,'sabado':14,'domingo':15})
print(calendario)

#Los elementos de un diccionario no se guardan necesariamente en el orden que se registran
#La variable dia contiene el indice del recorrido, por lo cual imprmie los elementos(indices)
for dia in calendario:
    print(dia)

#Al imprimir el calendario con el valor del indice, se imprimen los valores de los elementos
for dia in calendario:
    print(calendario[dia])

#Elementos del calendario
print(calendario.keys())

#Valores del calendario
print(calendario.values())

#Obetener elemento:valor
for item in calendario.items():
    print(item)

#Realizando una copia completa de un diccionario
calendario_copia = calendario.copy()
print(type(calendario_copia))
print('Copiando un diccionario completo ' + str(calendario_copia))
