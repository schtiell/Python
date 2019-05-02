# Reloj mundial

import datetime


def instrucciones():

    print('Estas son las operaciones que puede realizar\n')
    print('1. Ver la hora')
    print('2. Ver la fecha y hora')
    print('3. Ver la hora en New York') 
    print('4. Ver la hora en San Francisco')
    print('5. Ver la hora en Tokio')
    print('6. Ver la hora en Paris')
    print('7. Ver las instrucciones nuevamente')
    print('\n8. Limpiar pantalla\n')
    print('9. Salir')


def impresion_hora(hora_pais):
    
        time_zone = datetime.timezone(datetime.timedelta(hours = hora_pais ))

        now = datetime.datetime.now(time_zone).time()
        
        return now.strftime("%-I:%M:%S %p")
    

def impresion_fecha_hora(hora_pais):

    time_zone = datetime.timezone(datetime.timedelta(hours = hora_pais))

    fecha_hora = datetime.datetime.now(time_zone)

    # print('Fecha: ', fecha_hora.strftime("%B %d, %Y. \nHora: %-I:%M:%S %p"))
    
    return fecha_hora.strftime("%c")


def despedida():
    
    print('Gracias por utilizar el reloj mundial')


def clear_screen():

    import os
    
    if os.name == "nt":

        os.system("cls")
    
    elif os.name == "posix":

        os.system("clear")
    
    else:

        # raise "No se puede limpiar la pantalla"

        print ("No se pudo borrar la pantalla")



def ver_reloj():

    print('\nBienvenido al reloj mundial\n')

    instrucciones()

    while True:

        try:

            operacion = int(input("\n: "))
        
        except ValueError:

            print('Error, opcion desconocida')

        else:
            
            if operacion == 1:
        
                print ('La hora actual en México es:', impresion_hora(-6),
                        'tiempo del Centro')
                    
            elif operacion == 2:

                print('La fecha y hora en México es: ',impresion_fecha_hora(-6))           

            elif operacion == 3:
            
                print ('La hora actual en New York es:', impresion_hora(-5),
                        'tiempo del Oeste')

            elif operacion == 4:
                
                print ('La hora actual en San Francisco es:', impresion_hora(-8),
                        'tiempo del Pácifico')

            elif operacion == 5:
                
                print('La fecha y hora en Tokio es: ',impresion_fecha_hora(+9))
            

            elif operacion == 6:
                
                print('La fecha y hora en Paris es: ',impresion_fecha_hora(+1))

            elif operacion == 7:

                instrucciones()

            elif operacion == 8:

                clear_screen()
                
                instrucciones()

            elif operacion == 9:

                despedida()
                
                break

            else:
                
                print('Opcion incorrecta')

clear_screen()

ver_reloj()

