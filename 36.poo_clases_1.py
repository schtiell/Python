# Creacion de una clase coche
# https://www.youtube.com/watch?v=Y_SiIgxc-xI&index=26&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS

# DIFERENCIA ENTRE METRO Y FUNCION:

# Las funciones son bloques de codigo que no pertenecen a ninguna clase
# Utilizan la palabra reservada def para definirse en python

# Los métodos son bloques de codigo que si pertenecen a una clase
# Utilizan la palabra reservada defs (aunque igual aparecen def)
# Utilizan un parametro self para hacer referencia a la instancia de la clase

class Coche:

    # Atributos de la clase (Caracteristicas)
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False

    # Métodos de la clase (Comportamiento)
    # El parametro self hace referencia al propio objeto (miCoche) que instancía a la clase
    def arrancar(self):
       self.enmarcha = True

    # El parametro self = miCoche.enmarcha
    def estado(self):
        if self.enmarcha:
            return "El coche está en marcha"
        else:
            return "El coche está apagado"

# Creacion del objeto miCoche del tipo de la clase Coche
# Creacion de una instancia de la clase Coche
miCoche = Coche()

# Instancía o ejemplariza algunas de los atributos de la clase Coche
print('El auto tiene ',miCoche.ruedas,' ruedas')
print('EL auto mide ',miCoche.largoChasis,' cms de largo')

# Instancía al metodo de la clase Coche para cambiar el estado de enmarcha a True
# Como se ejemplariza el metodo arrancar el valor del atributo enmarcha cambia a True
miCoche.arrancar()

# Instancía al metodo de la clase Coche y verifica si el auto esta en marcha o apagado
print (miCoche.estado())

