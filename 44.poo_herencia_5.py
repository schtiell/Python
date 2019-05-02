class Persona:
    

    # Método Constructor de la Clase Persona
    def __init__(self):

        self.nombre = input('Nombre del empleado: ')
        self.edad = input('Cual es la edad del empleado: ')

    def imprimir(self):

        print ('\nNombre: {}\nEdad: {} años'.format(self.nombre,self.edad))


class Empleado(Persona):

    def __init__(self):
        super().__init__()
        self.salario = float(input('Cual es el salario del empleado: '))
    
    def imprimir(self):
        print('\n------Datos del Empleado--------')
        super().imprimir()
        print('\nSalario: ${} pesos'.format(self.salario))
        print('--------------------------------\n')
    
    def pagar_impuestos(self):
        
        if self.salario > 3000:
            print('El empleado debe pagar impuestos.')
        else:
            print('El empleado excenta impuestos')
    
# Instancia de la clase Empleado
empleado = Empleado()
empleado.imprimir()
empleado.pagar_impuestos()



