#Manejo del ciclo while

#sintaxis

contador = 0
while contador < 10:
	contador += 1
#No es posible concatener string e integers por lo cual se usa la funcion str para convertir el integer a string	
print ('el contador es: '+str(contador)+', fin del ciclo')

print('--------------------') 

#El programa pide un numero a reducir negativamente y pide de cuantas posiciones debe hacer la cuenta regresiva
numero = int(input('Que numero quieres reducir a 0: '))
reductor = int(input('De cuanto en cuanto deseas reducir el numero: '))
while numero>0:
	#La funcion print recibe el parametro end que permite indicar como debe imprimir las lineas
	#En este caso imprime linealmente separado por una ,
	print (numero, end='' + ',')
	#La variable numero funciona como un contador al poner -= se le indica que debe restar
	numero-=reductor
print('\n')

