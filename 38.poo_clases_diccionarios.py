# help (clase)
# Python proporciona ayuda sobre sintaxis


class Automovil:

    # **kwargs indica a python un desempaquetamiento de diccionario como argumento
    # Los argumentos no es necesario que se envíen en orden en que se declaran en el metodo constructor
    def __init__(self,**kwargs):
        self.color = kwargs.get('color')
        self.marca = kwargs.get('marca')
        self.transmision = kwargs.get('transmision')

        # Este atributo toma el valor por default de gasolina si no se especifica el parametro
        self.combustible = kwargs.get('combustible','gasolina')
    
    def imprimir(self):

        print('El auto es un ',self.marca,'color',self.color,'trasmision',
            self.transmision,self.combustible)



# Al enviar los parametros como un diccionario, no es necesario
# respetar el orden de los parametros ya que se reconocen por la key 
# del diccionario los parametros del constructor
miAuto = Automovil(color = 'rojo', marca = 'Honda',
                    transmision = 'standar')
miAuto.imprimir()

miCamioneta = Automovil(color = 'beige', marca = 'Ford', 
                        transmision = 'Automatica',combustible = 'diesel')
miCamioneta.imprimir()
