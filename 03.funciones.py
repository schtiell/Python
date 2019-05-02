#Manejo de funciones en python

def impresion():
	print ('Ejemplo de manejo de una funcion con Python')

#Funcion que recibe 2 parametros o argumentos a y b
def suma(a,b):
	c = a + b
	return c

def resta(a,b):
	c = a - b
	return c

#FLujo de ejecucion del codigo es de arriba hacia abajo
#Llamado de la funcion impresion
impresion()

print (suma(9,18))
impresion()

num1=874.245
num2=733.8776

c = resta(num1,num2)
print(c)
