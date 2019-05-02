def realizar_suma(num1,num2):
	suma = num1 + num2
	return suma

def numeros_suma():
	try:
		numero1 = int(input('Primer numero a sumar: '))
		numero2 = int(input('Segundo numero a sumar: '))
	except ValueError:
		print('El valor no es un numero')
	else:
		resultado = realizar_suma(numero1,numero2)
		print(resultado)
	
numeros_suma()
