# ---------------------------------------
# Conjuntos
# Un conjunto es una colección desordenada sin elementos duplicados. Los usos básicos incluyen 
# pruebas de membresía y eliminación de entradas duplicadas. Los objetos establecidos también
# admiten operaciones matemáticas como unión, intersección, diferencia y diferencia simétrica.

# Se pueden utilizar llaves o la función set () para crear conjuntos. 
# Nota: para crear un conjunto vacío debe usar set (), no {}; 
# El último crea un diccionario vacío, una estructura de datos que discutimos en la siguiente sección.
# ---------------------------------------

# ---------------------------------------
# Funciones de la aplicación:
# Obtener los sets del usuario, A y B
# Realizar funcion de union
# Realizar funcion de interseccion
# Realizar funcion de diferencia
# Realizar funcon de diferencia simetrica
# ---------------------------------------

# Bloque de funciones

def union(conjuntoa,conjuntob):
    # La union de dos conjuntos puede imprimirse mediante la funcion s.union(t)
    # o bien mediante el uso del signo pipe |

    print('\nLa union de A y B es {}\n'.format(conjuntoa.union(conjuntob)))
    #print ('\nLa union de A y B es {}\n'.format(conjuntoa | conjuntob))
    
def interseccion(conjuntoa, conjuntob):
    # La interseciion de dos conjuntos puede imprimirse mediante la funcion s.intersection(t)
    # o bien mediante el uso del signo and &
    
    if len(conjuntoa.intersection(conjuntob)) != 0:
        print('\nLa interseccion de A y B es {}\n'.format(conjuntoa.intersection(conjuntob)))
        #print('\nLa interseccion de A y B es {}\n'.format( conjuntoa & conjuntob))
    
    else:
        print('No hay interseccion en los conjuntos especificados\n')

def diferencia(conjuntoa, conjuntob):
    # La diferencia de dos conjuntos puede imprimirse mediante la funcion s.diference(t)
    # o bien mediante el uso del signo - 

    print('Selecciona la diferencia: \n1. A - B\n2. B - A\n')
    
    try:
        dif=int(input(': '))

    except ValueError:
        print('Opcion incorrecta, introduce 1 o 2')
        diferencia(conjuntoa,conjuntob)

    else:
        if dif == 1:
            print('\nLa diferencia de A - B es {}\n'.format(conjuntoa.difference(conjuntob)))
            #print('\nLa diferencia de A - B es {}\n'.format(conjuntoa - conjuntob))
        
        elif dif == 2:
            print('\nLa diferencia de B - A es {}\n'.format(conjuntob.difference(conjuntoa)))
            #print('\nLa diferencia de B - A es {}\n'.format(conjuntob - conjuntoa))
        
        else:
            print('Opcion no reconocida')
            diferencia(conjuntoa,conjuntob)

def diferencia_simetrica(conjuntoa, conjuntob):
    # La diferencia simetrica de dos conjuntos puede imprimirse mediante la funcion s.symmetric_difference(t)
    # o bien mediante el uso del signo ^

    print('\nLa diferencia simetrica de A y B {}\n'.format(conjuntoa.symmetric_difference(conjuntob)))
    #print('\nLa diferencia simetrica de A y B {}\n'.format(conjuntoa ^ conjuntob))

def saliendo():
    print('Saliendo de la aplicación \nGracias por utilizar la calculadora de conjuntos\n')

def bienvenido():
    print('\nBienvenido a las operaciones con conjuntos')
    print('Introduce los elementos de los conjuntos separados por espacios')
    print('ejemplo: 1 3 5 8 2\n')
    
def menu_opciones():
    print('-----------------------')
    print('1. Union')
    print('2. Interseccion')
    print('3. Diferencia')
    print('4. Diferencia Simétrica')
    print('5. Insertar nuevos conjuntos')
    print('6. Salir')
    print('-----------------------\n')

def opciones():
    # La funcion split permite separar los elemento de un arreglo especificando como se van a separar
    # Split separa elementos por los espacios por default si no se le indica.
    conjunto_a = set(input('Insertar el conjunto A: ').split())
    conjunto_b = set(input('Insertar el conjunto B: ').split())

    if len(conjunto_a) and len(conjunto_b) != 0:

        menu_opciones()

        while True:

            try:
                operacion = int(input('Selecciona la operacion: '))

            except ValueError:
                print('Error en la operacion indicada')

            else:
                if operacion == 1:
                    union(conjunto_a, conjunto_b)

                elif operacion == 2:
                    interseccion(conjunto_a, conjunto_b)

                elif operacion == 3:
                    diferencia(conjunto_a,conjunto_b)
                    
                elif operacion == 4:
                    diferencia_simetrica(conjunto_a,conjunto_b)
                
                elif operacion == 5:
                    opciones()
                    
                elif operacion == 6:
                    saliendo()
                    break

                else:
                    print('Opcion desconocida, vuelve a intentarlo')
        
    else:
        print('\nDebes especificar los 2 conjuntos para realizar las operaciones\n')
        opciones()

bienvenido()
opciones()