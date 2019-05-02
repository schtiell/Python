
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
        print('Marca: {} \nModelo: {}\nEncendido: {}\nAcelerar: {}\nFrenar: {}'.format(self.marca,
        self.modelo,self.encendido,self.acelerar,self.frenar))


class Motocicleta(Vehiculos):
    
    hcaballito = ''

    # Podria imprimirse el valor de hcaballito de esta forma tambien
    def hacer_caballito(self):
        self.hcaballito = 'Voy haciendo el caballito'
        # return self.hcaballito

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


class Vehiculos_Electricos:

    def __init__(self,marca,modelo):
        self.autonomia = 100
        super().__init__(marca,modelo)

    def cargarEnergia(self):
        self.cargando = True
    
    def imprimirVE(self):
        print('se esta usando la clase vehiculos electricos')


class Bicicleta_Electríca(Vehiculos,Vehiculos_Electricos):
    
    def usando_belectrica(self):
        print('Probando mi nueva bicicleta eléctrica')




# Instancia de la clase Motocicleta
miMotocicleta = Motocicleta('Honda','CRV500')
miMotocicleta.encender_vehiculo()
miMotocicleta.hacer_caballito()
miMotocicleta.estado_vehiculo()

# Instancia de la clase Camioneta
miCamioneta = Camioneta('Ford','Raptor')
miCamioneta.encender_vehiculo()
miCamioneta.estado_vehiculo()
print(miCamioneta.cargar(True)) 

# Instancia de la clase Bicicleta_Electríca
miBici = Bicicleta_Electríca('Mercurio','ElectricM1000')
miBici.imprimirVE()
miBici.estado_vehiculo()