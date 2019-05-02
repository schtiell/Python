# Polimorfismo = muchas formas
# poli - muchas
# morfismo - formas
# Un objeto puede cambiar de forma y de comportamiento
# Un objeto puede cambiar de un tipo
# Python permite el polimorfismo, no necesita especificar el tipo de clase 
# al que instancia el objeto

class Automivil:
    
    def desplazamiento(self):
        
        print('El automovil se mueve sobre 4 ruedas')

class Motocicleta:
    
    def desplazamiento(self):

        print('La motocicleta se mueve sobre 2 ruedas')

class Camion:
    
    def desplazamiento(self):
        
        print('El camion se mueve sobre 6 ruedas')

# Objetos sin polimorfismo, se crean cada uno instanciando a su respectiva clase

"""miAuto = Automivil()
miAuto.desplazamiento()

miMoto = Motocicleta()
miMoto.desplazamiento()

miCamion = Camion()
miCamion.desplazamiento()"""

# Utilizando el porlimorfismo, creando un objeto generidco 
# Es decir sin especificar la clase a la que pertenece
# Para poder instanciar a la clase que se requiera


# EL polimorfismo ocurre en el parametro vehiculo que recibe la función 
# Ya que este parametro puede instanciar a la clase Automovil, Motocicleta
# O cualquier otro clase que se requiera

def desplazamiento_vehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo = Automivil()
desplazamiento_vehiculo(miVehiculo)    

