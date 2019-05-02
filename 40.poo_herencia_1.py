# Herencia

# La herencia permite la reutilización del codigo generado en otras clases
# La clase principal que hereda metodos y atributos se le llama clase padre o superclase
# La sintaxis para heredad class nuevaclase(clase a heredar)
# Al realizar una herencia de clase, se hereda todo, atributos, metetodos, constructores, y caracteristicas de de la clase
# 


#Construccion de la clase padre o superclase Vehiculos
class Vehiculos:
    
    # Atributos de la clase Vehiculos
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        # Se inician propiedades encendido = false xq esta apagado
        # Acelerar = false porque no se esta acelerando
        # Frenar = false por que no se esta frenando
        self.encendido = False
        self.acelerar = False
        self.frenar = False

    # Métodos de la clase Vehiculo
    def encender_vehiculo(self):
        self.encendido = True
    
    def acelerar_vehiculo(self):
        self.acelerar = True
    
    def frena_vehiculo(self):
        self.frenar = True

    def estado_vehiculo(self):
        print('\n-----Datos del Vehiculo------')
        print('Marca: {} \nModelo: {}\nEncendido: {}\nAcelerar: {}\nFrenar: {}'.format(self.marca,
        self.modelo,self.encendido,self.acelerar,self.frenar))



#Creación de una nueva clase Motocicleta, que hereda de la clase Vehiuclos
class Motocicleta(Vehiculos):
    pass

# Como la clase motocicleta hereda de la superclase vehiculos que tiene un método constructor 
# que recibe 2 parametros, es necesario mandar esos 2 parametros (marca y modelo)

#Instancia de la clase Motocicleta
miMotocicleta = Motocicleta('Honda','CRV500')
miMotocicleta.encender_vehiculo()
miMotocicleta.estado_vehiculo()

