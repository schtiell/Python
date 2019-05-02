# Ejercicio hacer una lista de compras
# La lista de compras debe permitir:
# Agregar articulos
# Eliminar articulos
# Ver/Constular articulos

# Se crea una lista de articulos vacia es lo mismo que lista_articulos=[]
lista_articulos = list()

# Bloque de funciones determinadas

# Funcion para agregar los articulos del usuario a la lista
def agregar_articulo():
    #print('Agregar articulo')
    while True:
        articulo = input('Articulo: ')
        if articulo != '':
            #La funcion capitalize convierte la primera letra en mayuscula
            lista_articulos.append(articulo.capitalize())
        else:
            print()
            break

# Funcion para eliminar los articulos de la lista
def remover_articulo():
    try:
        articulo = input('Que articulo quieres remover: ')
        lista_articulos.remove(articulo.capitalize())
        print()
        print(' --  --  --  --  --  --  --  --  --  --  --  -- ')
        print('El articulo ' + articulo + ' ha sido removido...')
        print(' --  --  --  --  --  --  --  --  --  --  --  -- ')
        print()

    except ValueError:
        print()
        print(' --  --  --  --  --  --  --  --  --  --  --  --  --')
        print('El articulo: ' + articulo + ' no existe en la lista')
        print(' --  --  --  --  --  --  --  --  --  --  --  --  --')
        print()


# Funcion para consultar los articulos de la lista
def ver_articulo():
    print(' --  --  -- -Lista de Articulos --  --  --  -- ')
    if len(lista_articulos) == 0:
        print('¡No hay ningun elemento en la lista!')
    else:
        numero = 1
        for articulo in lista_articulos:
            print(str(numero) + '.- ' + articulo)
            numero += 1
    print(' --  --  --  --  --  --  -- ')
    print()

# Menú de opaciones de la aplicación
print('Bienvenido a la lista de compras')
print()
while True:
    print('Estas son las operaciones que se pueden realzar: \n')
    print(' --  --  --  --  --  --  --  --  --  -- ')
    print('1. Agregar articulo')
    print(' --  --  --  --  --  --  --  --  --  -- ')
    print('2. Remover articulo')
    print(' --  --  --  --  --  --  --  --  --  -- ')
    print('3. Ver articulos')
    print(' --  --  --  --  --  --  --  --  --  -- ')
    print('4. Salir')
    print(' --  --  --  --  --  --  --  --  --  -- ')
    print()

    operacion = int(input('Respuesta: '))
    print()

    if operacion == 1:
        agregar_articulo()
    elif operacion == 2:
        remover_articulo()
    elif operacion == 3:
        ver_articulo()
    else:
        break

# Mensaje de cierre del programa
print()
print(' --  --  --  --  --  --  --  --  --  --  -')
print('Gracias por utilizar la lista de compras!!')
print('--  --  --  -- Vuelve pronto --  --  --  -')
print()
