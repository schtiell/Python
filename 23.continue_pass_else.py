#El programa cuenta las letras de una cadena, si el caracter es un espacio en blanco entonces salta la linea siguiente
cadena = input('Escribe una palabra, frase o cadena: ')
contador=0
for letra in cadena:
    if letra == ' ':
        continue
    contador+=1
print('El numero de letras de tu cadena es: ' + str(contador))
    