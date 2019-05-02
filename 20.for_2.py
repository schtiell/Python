#Sintaxis básica del funcionamiento del bucle for
for i in [1,2,3,4,5,6]:
    print('hola')

print('--------------------')

for estaciones in ['primavera','verano','otoño','invierno']:
    print(estaciones)

print('--------------------')

#Imprimir elementos en una sola line con el argumento end
#Con el argumento end se le indica a la funcion print como debe terminar la impresion de la linea
for estaciones in ['primavera','verano','otoño','invierno']:
    print(estaciones)
    print(estaciones, end=' ')
print('\n')

print('--------------------')

#Recorrer un string
contador=0
for letra in 'jsayagot@veracruz.gob.mx':
    print("La letra " + letra + " está en la posición " + str(contador))
    contador+=1

print('--------------------')

#Evaluar el correo si es correcta o no
email=input('Favor de proporcionar un correo: ')
bandera = False
contador = 0

for caracter in email:
    if (caracter == '@' or caracter == '.'):
        contador+=1
    
    if (contador >=2):
        bandera = True

if bandera:
    print('correo correcto')
else:
    print('correo erroneo')

print('--------------------') 