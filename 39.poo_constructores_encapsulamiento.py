# Creacion de una clase coche

# Encapsulamiento de atributos, de metodos y metodo constructor

# El metodo encapsulado quiere decir que solo es posible utilizarlo desde dentro 
# de la clase. Fuera de la clase no es posible acceder a ellos

class Coche:

    # Metodo constructor de la clase
    def __init__(self):

        #Encapsulamiento de los atributos inicializados
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False

    # Métodos de la clase
    def arrancar(self, encendido):

        self.__enmarcha = encendido

        if (self.__enmarcha):
            revision=self.__revision_interna()

        if (self.__enmarcha and revision):
            return 'El auto esta encendido'
        elif self.__enmarcha and revision == False:
            return 'Algo ah estado mal en la revisión del auto, no se puede encender el auto'
        else:
            return 'El auto esta apagago'
    
    def estado(self):

        print('El auto tiene ',self.__ruedas,' ruedas.\nUn ancho de ',
        self.__anchoChasis,' cms \nY un largo de ',self.__largoChasis,' cms')

    # Encapsulamiento del Metódo
    def __revision_interna(self):

        print('Revision interna de los componentes del auto')
        
        self.gasolina = 'ok'
        self.aceite = 'ok'
        self.puertas = 'cerradas'
 
        if self.gasolina == 'ok' and self.aceite == 'ok' and self.puertas == 'cerradas':
            return True
        else:
            return False

print()
print('--------Primer Objeto de la Clase Coche------------')

# Instancias de la clase
miCoche = Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print('--------Segundo Objeto de la Clase Coche------------')
miNuevoCoche = Coche()
print(miNuevoCoche.arrancar(False))
miNuevoCoche.estado()