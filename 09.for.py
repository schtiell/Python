
#Manejo del ciclo for

lista_numeros=[1,2,3,4,5,6,7,8,9,10]

#Sintaxis básica del ciclo for
for numero in lista_numeros:
	print('Estoy en la posicion: ' + str(numero))

print('fin del ciclo for')

#Uso de la palabra reservada break
for numero in lista_numeros:
	print(numero)
	if numero == 5:
		print('fin del ciclo')
		break

#Uso de la palabra reservada continue
for numero in lista_numeros:
	if numero>4 and numero<8:
		continue
	print(numero)


#REEEEEEEEEEEEEEEEEEEEETTTTTTTTTTTTTTTTTTTOOOOOOOOOOOOOOOOO	
#Imprimir las vocales en mayusculas
print('------REEEEETTTTTOOOOO!!!!------')
lista_vocales=['a','e','i','o','u']
for vocal in lista_vocales:
	print(vocal.upper())
print('--------------------------------')

#REEEEEEEEEEEEEEEEEEEEETTTTTTTTTTTTTTTTTTTOOOOOOOOOOOOOOOOO	
#Imprimir las vocales en mayusculas
contador=0
lista_vocales=['a','e','i','o','u']
while contador < len(lista_vocales):
	print(lista_vocales[contador].upper())
	contador+=1
