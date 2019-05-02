
#Superclase Vehiculos
class Vehiculos:
    
    # Atributos de la clase Vehiculos
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
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


# -------------------------------------------------------------------------------------------------------------------

# Clase Motocicleta que hereda de la superclase Vehiculos
# Una clase hijo tambien puede tener atributos, métodos y caracteristicas propias
class Motocicleta(Vehiculos):
    
    hcaballito = ''

    # Podria imprimirse el valor de hcaballito de esta forma tambien
    def hacer_caballito(self):
        self.hcaballito = 'Voy haciendo el caballito'
        # return self.hcaballito

    # Se escribe el método de la clase vehiculo agregando el valor de hcaballito
    # Por lo cual se sobre escribe y el metodo de la superclase y se agrega una variable mas
    def estado_vehiculo(self):
        print('\n-----Datos del Vehiculo------')
        print('Marca: {} \nModelo: {}\nEncendido: {}\nAcelerar: {}\nFrenar: {} \n{}'.format(self.marca,
        self.modelo,self.encendido,self.acelerar,self.frenar,self.hcaballito))

# Instancia de la clase Motocicleta
miMotocicleta = Motocicleta('Honda','CRV500')
miMotocicleta.encender_vehiculo()
miMotocicleta.hacer_caballito()
miMotocicleta.estado_vehiculo()
# print(miMotocicleta.hacer_caballito())

# ------------------------------------------------------------------------------------------------------------------------

# Nueva clase Camioneta que hereda de la superclase vehiculos
# Tiene un metodo propio de las camionetas que es el de poder cargar
class Camioneta(Vehiculos):
    
    def cargar(self, carga):
        self.cargado = carga
        if self.cargado:
            return 'La camioneta esta cargada'
        else:
            return 'La camioneta no esta cargada'

# Se envian los 2 paramtros (marca ymodelo) que necesita el constructor de la clase vehiculos
# Se invoca a los metodos
miCamioneta = Camioneta('Ford','Raptor')
miCamioneta.encender_vehiculo()
miCamioneta.estado_vehiculo()
print(miCamioneta.cargar(True)) 


# ------------------------------------------------------------------------------------------------------------------------

class Vehiculos_Electricos:

    def __init__(self,nombre):
        self.autonomia = 100
        self.nombre = nombre
    
    def cargarEnergia(self):
        self.cargando = True
    
    def imprimirVE(self):
        print('se esta usando la clase vehiculos electricos')
        print('Vamos a imprimir la variable',self.nombre)


# ------------------------------------------------------------------------------------------------------------------------
# Herencia Multiple, al heredar de 2 clases o mas
class Bicicleta_Electríca(Vehiculos,Vehiculos_Electricos):
    pass

# Cuando se hereda de 2 clases que reciben parametros por sus metodos constructores
# se deben indicar los parametros deacuerdo como se especifico el orden de la herencia de las clases
# En la class Bicicleta_Electríca(Vehiculos,Vehiculos_Electricos): 
# Está PRIMERO Vehiculos:
# SEGUNDO Vehiculos_Electrícos
# Por lo cual primero se deben enviar los parametros (marca y modelo) ya que en ese orden esta la herencia
miBici = Bicicleta_Electríca('Mercury','T1000')
#miBici = Vehiculos_Electricos('joaquin')
miBici.imprimirVE()

