# Metodos de Cadenas de Caracteres
# Python considera objetos a las palabras, letras, frases. Objetos String
 
# Upper(). Mayusculas un string
# Lower(). Minusculas un string
# Capitalize(). Letra capital un string
# Count(). Cuenta el numero de veces que aparece  una letra o cadena en un texto
# find(). Representa el indice en el que aparece un caracter
# isdigit(). Devuelve un booleano si el caracter introducido es un digito
# isalum(). Comprueba si el string o caracter es alfanumerico
# isalpha(). Comprueba si solo hay letras, los espacios no cuentan
# split(). Separa por palabras utilizando espacios
# strip(). Borra los espacios en blanco al principio y al final
# replace(). Cambia una palabra o una letra por otra
# rfind(). Representa el indice de un caracter, de reversa "reversa find"


nombre = input('Introduce tu nombre: ')

print('El nombre es: ', nombre.upper())

print('El nombre es: ', nombre.lower())

print('El nombre es: ', nombre.capitalize())

print('El nombre es: ', nombre.count('q'))

edad = input('Introduce tu edad: ')
print(edad.isdigit())


