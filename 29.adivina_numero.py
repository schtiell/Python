# ---------------------------------------------------------------------------
# Adivina el numero
# El jugador tiene 3 vidas(intentos para adivinar)
# Dar pistas si el numero es mayor o menor
# Volver a jugar generando un numero diferente
# Imprimir si adivino a la primera o si no en que intento adivicnó el usuario
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# RETO:
# FACIL: Rango entre 1 y 10, 5 intentos
# MEDIO: Aumentar el rango entre 1 y 20, 4 oportunidades
# DIFICIL: Aumentar rango entre 1 y 30 y 3 oportunidades
# ---------------------------------------------------------------------------


# Permite generar elemento aleatorios
import random

def impresion_mensajes(mensaje):
    print('\n------------------------------')
    print(mensaje)
    print('------------------------------\n')
    
def dificultad_juego():

    print('1. Facil \n2. Medio \n3. Dificil\n')

    try:
        dificultad = int(input('Elige la dificultad del juego: '))
    
    except ValueError:
        print('Opción incorrecto')
    
    else:
        if dificultad == 1:
            iniciar_juego(5,1,10)
        elif dificultad == 2:
            iniciar_juego(4,1,20)
        elif dificultad == 3:
            iniciar_juego(3,1,30)
        else:
            print('Opcion incorrecta')


def iniciar_juego(intentos_dificultad, r_inicial, r_final):
    
    # La funcion random requiere 2 parametros para indicarle el rango para generar el numero
    # Rango de 1 a 10, principio y fin, un rango
    numero_aleatorio = random.randint(r_inicial,r_final)
    intentos = 0

    while intentos < intentos_dificultad:

        try:
            adivinanza = int(input('¿cual es el numero? '))

        except ValueError:
            print('Valor incorrecto')
            
        else:

            if adivinanza < r_inicial or adivinanza > r_final:

                impresion_mensajes('El numero indicado esta fuera del rango')

            else:

                if adivinanza == numero_aleatorio:

                    if intentos == 0:
                        impresion_mensajes('Felicidades atinaste al primer intento')

                    else:
                        impresion_mensajes('Adivinaste el numero es: ' + str(numero_aleatorio) + '. Necesitaste ' + str(intentos + 1) + ' intentos para adivinar')
                    
                        respuesta = input('Deseas volver a jugar? \n 1. Si \n 2. No \n: ')

                        if respuesta.lower() == 'si':
                           impresion_mensajes('Vuelve a elegir una opcion')
                           dificultad_juego()

                        else:
                            impresion_mensajes('Gracias por jugar')
                            break

                elif adivinanza > numero_aleatorio:
                    print('El numero aleatorio es menor, intenta nuevamente')
                
                elif adivinanza < numero_aleatorio:
                    print('El numero aleatorio es mayor, intenta nuevamente')
            
                intentos += 1
                print('Intentos {}/{}'.format(intentos,intentos_dificultad))

    else:
       
        impresion_mensajes('Agotaste el numero de intentos\nno adivinaste el numero')

        respuesta = input('Deseas volver a jugar? \n 1. Si \n 2. No \n ')

        if respuesta.lower() == 'si':
            impresion_mensajes('Vuelve a elegir una opcion')
            dificultad_juego()

        else:
            impresion_mensajes('Gracias por jugar')

impresion_mensajes('Bienvenido a adivina el numero')
dificultad_juego()