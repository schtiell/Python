# Raise permite levantar excepciones personalizadas en cualquier parte del código

def evalua_edad(edad):
    
    if edad<0:

        # Excepción personal levantada al introducir una edad negativa
        raise ValueError('No se aceptan valores negativos')
    
    elif edad<20:
        return 'Eres menor de edad'
    
    elif edad<40:
        return 'Eres joven aun'
    
    elif edad<60:
        return 'Eres maduro'
    
    elif edad<80:
        return 'Eres un adulto ya'
    
edad = int(input('Introduce tu edad: '))

# Al invocar la funcion y enviar el parametro si se genera la excepción levantada se llama al bloque
# except
try:
    print (evalua_edad(edad))

# La excepcion debe ser del mismo tipo que la levantada(raise) y se le asigna un identificador que contendrá
# el mensaje lanzado con la función raise
except ValueError as Error_numero_negativo:
    print(Error_numero_negativo)

# Este mensaje se imprime con la finalidad de comprobar la ejecucion del programa 
# dependiendo de si ocurren excepciones o no
# Si hay excepcion se imprime el mensaje (continua el flujo del programa) si no se lanza la excepcion
# y el flujo de ejecución es interrumpido
print('Programa terminado')