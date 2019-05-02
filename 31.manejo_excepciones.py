# Manejo de Excepciones consecutivas
# Las Excepciones son errores en tiempo de ejecucion del programa

def division():
    try:
        numero1 = int(input('Insertar el primer valor: '))
        numero2 = int(input('Insertar el segundo valor: '))
        div = numero1/numero2
    
    # Captura errores erroneos de captura por teclado
    except ValueError:
        print('Error en los valores introducidos')
    
    # Captura de errores al intentar dividir entre cero
    except ZeroDivisionError:
        print('No es posible realizar una division entre cero')

    # Except sin especificar el tipo de error, permite capturar una excepcion general
    except:
        print('Ha ocurrido un error en tiempo de ejecución')
    
    else:
        print('El resultado de la division es {}'.format(div))
        print('Cálculo finalizado\n')
    
    # Permite imprimir un bloque de codigo aunque se presenten excepciones en el código
    finally:
        print('Este es un bloque de codigo que se imprime aunque existan o no excepciones')

division()