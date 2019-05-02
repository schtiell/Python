# Programa para una agenda telefonica
# El programa debe, agregar, remover, consultar, modificar.

# Bienvenida de la aplicacion
def bienvenido():
    print()
    print(' --  --  --  --  --  --  --  -- -')
    print('Bienvenido a la agenda telefónica')
    print(' --  --  --  --  --  --  --  --  ')
    print()

# Agregar contacto
def agregar_contacto():
    nombre = input('Nombre del Nuevo contacto: ').capitalize()
    no_telefono = input('Telefono de: ')
    agenda_telefonica[nombre] = no_telefono
    impresion = 'El contacto ' + nombre + ' ah sido agregado...'
    formato_impresion(impresion)
    
# Eliminar contacto
def remover_contacto():
    impresion = None
    if len(agenda_telefonica) != 0:
        nombre = input('Nombre del contacto que deseas borrar: ').capitalize()
        try:
            del(agenda_telefonica[nombre])
        #Excepcion KeyError por buscar un Key que no existe en el diccionario (key:value)
        except KeyError:
            impresion = 'El contacto no existe' 
        else:
            impresion = nombre + ' ah sido elimindo'
    else:
        impresion = 'No hay contactos registrados...'
    
    formato_impresion(impresion)

# Actualizar contacto
def actualizar_contacto():
    impresion = None
    if  len(agenda_telefonica) != 0:
        nombre = input('Nombre del contacto que vas a Actualizar: ').capitalize()
        numero = input('Nuevo numero para ' + str(nombre) + ': ')
        try:
            agenda_telefonica[nombre] = numero
            impresion = 'contacto actualizado'
        except KeyError:
            impresion = 'El contacto no existe'
    else:
        impresion='No hay contactos registrados'
    
    formato_impresion(impresion)
    
# Consultar contacto
def ver_contacto():
    impresion = None
    if len(agenda_telefonica) != 0:
        nombre = input('Nombre del contacto: ').capitalize()
        try:
            impresion = "{} \t {}".format(nombre,agenda_telefonica[nombre])
        except KeyError:
            impresion = 'El contacto no existe'    
    else:
        impresion = 'No hay contactos registrados'
    
    formato_impresion(impresion)

# Consultar toda la agenda
def ver_agenda():
    #Los elementos de un dicccionario son key:value
    #La variable contacto hace referencia a la key o indicie
    #Por lo tanto la variable contacto contiene el value osea el telefono del contacto
    impresion = None
    if len(agenda_telefonica) != 0:
        numero = 1
        for contacto in agenda_telefonica:
            #Formateo de la funcion print
            if impresion == None:
                impresion = "{} - {} \t {}".format(numero,contacto,agenda_telefonica[contacto])
                numero += 1
            else:
                impresion += "\n{} - {} \t {}".format(numero,contacto,agenda_telefonica[contacto])
                numero += 1
        print()
    else:
        impresion=('No hay contactos registrados')
    
    formato_impresion(impresion)

# Impresion de las funciones
def formato_impresion(impresion):
    print()
    print('--  --  -- Agenda Telefónica --  --  --')
    print(impresion)
    print('--  --  --  --  --  --  --  -- -- -- --')
    print()

# Salir de la Aplicación
def salir():
    print('--  --  --  --  --  --  --  --')
    print('Gracias por utilizar la agenda')
    print('Vuelve pronto!!!')
    print('--  --  --  --  --  --  --  --')
    print()

#Bienvenida de la aplicacion
bienvenido()

# Creacion del diccionario de datos
agenda_telefonica = dict()

while True:
    print('-- --  --  --  --  -- -- --')
    print('1. Agregar contacto')
    print('2. Eliminar contacto')
    print('3. Actualizar contacto')
    print('4. Ver contacto')
    print('5. Ver Todos los contactos')
    print('6. Salir')
    print('-- --  --  --  --  -- -- --')
    print()

    # Solicitud de Operacion...
    try:
        opcion = int(input(': '))
    except ValueError:
        formato_impresion('Opcion incorrecta!!!')
    else:
        if opcion == 1:
            agregar_contacto()
        elif opcion == 2:
            remover_contacto()
        elif opcion == 3:
            actualizar_contacto()
        elif opcion == 4:
             ver_contacto()
        elif opcion == 5:
            ver_agenda()
        elif opcion == 6:
            break
        else:
            formato_impresion('Operacion Desconocida')

# Llamado a la funcion de despedida
salir()