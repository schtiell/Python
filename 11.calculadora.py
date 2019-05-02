#Calculadora....
#while bandera == true:

print('Bienvendio a la calculadora en Python')

def seleccionar_operacion():
	print('Estas son las operaciones que se pueden realizar')
	print('1 - Suma')
	print('2 - Resta')
	print('3 - Multiplicacion')
	print('4 - División')
	print('¿Qué operacion quieres realizar? ')
	oprcn = int(input('Presiona del 1 al 4 segun la operacion a realizar '))
	return oprcn

def sumar(num1,num2):
	resultado = num1 + num2
	return resultado

def restar(num1,num2):
	resultado = num1 - num2
	return resultado

def multiplicar(num1,num2):
	resultado = num1 * num2
	return resultado

def dividir(num1,num2):
	try:
		resultado = num1 / num2
		print('El resultado de la division es: ' + str(resultado))
	except ZeroDivisionError:
		print ('No es posible realizar la division entre 0')

def otra_operacion():
	try:
		respuesta = int(input('\nQuieres realizar otra operacion? \n 1 - Si \n 2 - No: '))
		return respuesta
	except ValueError:
		print('Tu respuesta no es valida')
		otra_operacion()

bandera = 1
while bandera == 1:
	try:
		operacion = seleccionar_operacion()

		if operacion >=1 and operacion <=4:
			numero1 = int(input('Primer numero: '))
			numero2 = int(input('segundo numero: '))

			if operacion == 1:
				resultado = sumar(numero1,numero2)
				print('El resultado de la suma es: ' + str(resultado))

			elif operacion == 2:
				resultado = restar(numero1,numero2)
				print('El resultado de la resta es: ' + str(resultado))
	
			elif operacion == 3:
				resultado = multiplicar(numero1,numero2)
				print('El resultado de la multiplicación es: ' + str(resultado))
	
			elif operacion == 4:
				dividir(numero1,numero2)

			respuesta = otra_operacion()
			if respuesta == 1:
				bandera = 1
				print()
			else:
				print('Gracias por utilizar la calculadora en Python')
				break
		else:
			print('La opcion elegida no corresponde a ninguna operacion')
	except ValueError:
		print('Por favor teclea solo el numero de la operacion 1 - 4, Gracias')
		break
		

		



	















