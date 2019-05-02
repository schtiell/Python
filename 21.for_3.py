#Range permite establecer rangos, en este ejemplo el rango es de 9 posisiciones de 0 - 8 
for i in range(9):
    print('Impresión del indice: ' + str(i)) 

print('--------------------') 

#Impresion de un rango del 5 al 9 ya que el valor final es exclusivo
for i in range(5,10):
    print(f"Impresión del indice :{i}")

for i in range(10,30,3):
    print('El valor es: ' + str(i))

print('--------------------') 

#Realizar el analisis del correo usando al funcion range
#la funcion len permite utilizar la longitu de una cadena o de una (lista/tupla/diccionario)
bandera = False
email = input('Cual es tu email: ')
for letra in range(len(email)):
    if email[letra] == '@':
        bandera = True

if bandera:
    print('El email es correcto')
else:
    print('Tu correo no es valido')