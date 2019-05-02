# Los generadores son estructuras que extraen valores de una funcion y se almacenan en objetos iterables
# Estos se almacenan de uno en uno 
# Cada vez que un generador almacena un valor, este permanece en un estado pausado hasta que se solicita el siguiente
# esta caracteristica es conocida como "suspención de estado"

#Crear un programa que genere una lista de numeros pares

# Funcion tradicional de crear una lista con numero pares
def generador_pares(limite):
    numero = 1
    lista =[]

    while numero < limite:
        lista.append(numero*2)
        numero += 1
    
    return lista

#print (generador_pares(10))


# Funcion con manejo de generadores para crear una lista de numeros pares
# El generador crea los elementos del objeto iterable conforme se valla llamando
# A diferencia de las funciones tradicionales que crea toda la lista de golpe
# Mayor eficiencia en los recursos al utilizar los generadores
def generador_pares(limite):
    numero = 1
    while numero < limite:
        #yield crea el objeto iterable osea una lista por lo que ya no se declara una lista
        #Ya no se utiliza el return para retornar el resultado ya que ya esta yield
        yield numero*2
        numero += 1

devuelvepares=generador_pares(10)

#for i in devuelvepares:
# print(i)

#De esta forma unicamente se imprime el primer elemento del objeto iterable
#No imprime toda la lista generada se llama valor a valor
print(next(devuelvepares))
# Entre llamada y llamada el generador pasa al estado de suspencion
print(next(devuelvepares))