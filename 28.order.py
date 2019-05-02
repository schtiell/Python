cadena = input('Insertar una cadena: ')
cadena2 = sorted(cadena)
letras = 0
for letra in cadena2:
    if letra == ' ':
        continue
    else:
        print(letra,end=" ")
        letras += 1    
#print (cadena2)
print ('\n' + str(letras))
