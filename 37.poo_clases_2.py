# Creacion de una clase coche

class Coche:

    # Atributos de la clase
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False

    # Métodos de la clase
    def arrancar(self,encender):
        if encender == 'si':
            self.enmarcha = True
        else:
            self.enmarcha = False
    
    def estado(self):
        if self.enmarcha:
            return "Encendido"
        else:
            return "Apagado"

# Instancia de la clase
miCoche = Coche()
print('El auto tiene ',miCoche.ruedas,' ruedas')
print('EL auto mide ',miCoche.largoChasis,' cms de largo')
#miCoche.arrancar()
#print (miCoche.estado())

print('--------Segundo Objeto de la Clase Coche------------')

miNuevoCoche = Coche()
print('Mi nuevo auto mide de ancho: ',miNuevoCoche.anchoChasis,'cms')
# print('Mi nuevo auto actualmente está: '+miNuevoCoche.estado())

encender_auto = input('Deseas encender el motor: ').lower()
miNuevoCoche.arrancar(encender_auto)
if miNuevoCoche.estado() == 'Encendido':
    print('El motor del nuevo auto esta: ',miNuevoCoche.estado())
else:
    print('Tu auto sigue: ',miNuevoCoche.estado())







