# Uso de yield from
# Utilizados para simplificar el codigo de generadores en el caso de de utilizar bucles anidades
# Permite acceder a arregles dentro de un arreglos. Muy parecido a las matrices en otros lenguajes

# El * indica a python que recibe un numero indeterminado de parametros
# El * indica que recibe tuplas
# Recorriendo arreglos dentro de un arreglo de forma tradicional
def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        #Recorre los elementos que componen al primer elemento
        for subelemento in elemento:
            yield subelemento

ciudades = devuelve_ciudades("Xalapa","Orizaba","Cordoba","Boca del Rio")

# La funcion next retorna el proximo valor del objeto iterador.
# Retorna el valor proximo cada vez que se invoca a la funcion.
print(next(ciudades))
print(next(ciudades))

print('--------------------------------------------------')

# Misma forma de hacer la funcion de arriba pero con el yield from
def devuelve_cdds(*ciudades):
    for elemento in ciudades:
        yield from elemento

cities = devuelve_cdds("Orizaba","Cordoba","Alvarado","Xalapa")
# La funcion next retorna el proximo valor del objeto iterador.
print(next(cities))
print(next(cities))



