#Se crea una funcion que defina si es posible realizar el tramite de la identificacion oficial en México
#Por convencion se utiliza el _ para separar las palabras en los nombres de las funciones
def analizar_Edad(edad): 
	if edad >= 18:
		print ('Ya puedes tramitar tu ID')
	else:
		print ('Aun no cubres la edad necesaria')

def pedir_Normbre():
	print ('Solicitar el nombre')

analizar_Edad(17)
pedir_Normbre()