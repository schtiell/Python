#Superclase Vehiculos

class Vehiculos:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
        self.acelerar = False
        self.frenar = False

    def encender_vehiculo(self):
        self.encendido = True
    
    def acelerar_vehiculo(self):
        self.acelerar = True
    
    def frena_vehiculo(self):
        self.frenar = True

    def estado_vehiculo(self):
        print('\n-----Datos del Vehiculo------')
        print('Marca: {} \nModelo: {}\nEncendido:{}\nAcelerar:{}\nFrenar:{}'
            .format(self.marca, self.modelo,self.encendido,self.acelerar,self.frenar))


class Motocicleta(Vehiculos):
    
    hcaballito = ''

    def hacer_caballito(self):
        self.hcaballito = 'Voy haciendo el caballito'

    # Sobre escritura del método estado_vehiculo que 
    # hereda de la clase Vehiculos
    def estado_vehiculo(self):
        print('\n-----Datos del Vehiculo------')
        print('Marca: {} \nModelo: {}\nEncendido: {}\nAcelerar: {}\nFrenar: {} \n{}'.format(self.marca,
        self.modelo,self.encendido,self.acelerar,self.frenar,self.hcaballito))


class Camioneta(Vehiculos):
    
    def cargar(self, carga):
        self.cargado = carga
        if self.cargado:
            return 'La camioneta esta cargada'
        else:
            return 'La camioneta no esta cargada'


class Vehiculos_Electricos(Vehiculos):

    def __init__(self,marca,modelo):
        self.autonomia = 100
        #super().__init__(marca,modelo)

    # Por cada 10 kms recorridos se pierde 1% de bateria
    def autonomia_bateria(self,kilometros):
        self.kilometros_recorrido = kilometros/10
        self.autonomia = self.autonomia - self.kilometros_recorrido
        print('Te queda de bateria:',self.autonomia,'%')

    def cargarEnergia(self):
        self.cargando = True
    
    def imprimirVE(self):
        print('se esta usando la clase vehiculos electricos')



