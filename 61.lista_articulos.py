# Lista de articulos
def menu():
    
    print("Este es el menu de opciones: \n")

def agregar_articulo(lista):

    lista.write(input("Que articulo vas a agregar a la lista: \n"))
    lista.close()

def ver_articulos(lista):
    lista.read()
    lista.close()

def nueva_lista():

    pass

def salir():    
    print ("Saliendo, gracias...")


lista_compras = open("/var/www/html/Cursos/Python/agenda.txt","a")
menu()

while True:

    try:

        opcion = int(input("Elige una opción: "))
        
    except ValueError:
        
        print("Error..")

    else:

        if opcion == 1:

            agregar_articulo(lista_compras)

        if opcion == 2:

            ver_articulos(lista_compras)
        
        if opcion == 3:

            salir()
            break

        else:

            print ("Error en la opcion capturada")
    


