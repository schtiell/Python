#Diccionario de calificaciones
calificaciones = {'joaquin':10,'luis':9,'pedro':8,'esteban':5,'ana':7,'elena':6}
print(calificaciones)

#Imprimir un solo elemento
print('La calificacion de luis es ' + str(calificaciones['luis']))

calificaciones['Andrea'] = 'cinco'
print(calificaciones)

#Método mas largo para construir diccionarios
agenda = dict([['joaquin',123123333],['valeria',364532342],['antonio',567567345]])
print(agenda)
print(type(agenda))
print(calificaciones)
