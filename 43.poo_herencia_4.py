class Persona:

    # Atributos de la clase en un contructor
    def __init__(self,nombre,edad,telefono,municipio):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.municipio = municipio
    
    # Métodos de la clase
    def encabezado_impresiones(self):
        print('\n------------Datos-----------')

    def imprimir_datos_persona(self):
        print('Los datos de la persona son: \nNombre: {}\nEdad: {}años \nTelefono {}\nMunicipio {}'
        .format(self.nombre,self.edad,self.telefono,self.municipio))


class Empleado(Persona):

    def __init__(self,id,puesto,salario,antiguedad,nombre,edad,telefono,municipio):
        
        # La funcion super() permite indicarle a la clase cuales son los parametros que debe 
        # enviar a la clase padre

        # La clase Empleado recibe tanto los propios parametros para su contructor como los parametros que 
        # debe enviar al constructor de la superclase

        #Super() invoca al contructor de la clase padre y envia parametros
        super().__init__(nombre,edad,telefono,municipio)

        self.id = id
        self.puesto = puesto
        self.salario = salario
        self.antiguedad = antiguedad
    
    # Métodos de la clase
    def immpresion_datos_empleado(self):
        print('Los datos del empleado son: \nNombre: {}\nId: {}\nPuesto: {}\nSalario: ${}.00 \nAntigüedad: {} años'
        .format(self.nombre,self.id,self.puesto,self.salario,self.antiguedad))


# Al instanciar a la clase Empleado, se envían los parametros para su propio contructor 
# y los parametros que va a enviar a la superclase o clase padre Persona     
nvoEmpleado = Empleado(43233,'Analista de BD',7500,7,'Joaquin Sayago',32,2281080457,'Xalapa')

nvoEmpleado.encabezado_impresiones()
nvoEmpleado.imprimir_datos_persona()
nvoEmpleado.encabezado_impresiones()
nvoEmpleado.immpresion_datos_empleado()

# PRINCIPIO DE SUSTITUCION APLICABLE SIEMPRE EN LA HERENCIA
# ---------------- ES SIEMPRE UN o UNA --------------------
# Un Empleado SIEMPRE será UNA PERSONA
# Pero
# Una PERSONA NO SIEMPRE será un EMPLEADO

# La funcion isinstance(objetos de la intancia, clase)
# Retorna True o False si un objeto es perteneciente a la clase
print(isinstance(nvoEmpleado,Empleado))
print(isinstance(nvoEmpleado,Persona))

otroEmepleado = Persona('Martin',60,2727266012,'Toronto')

print(isinstance(otroEmepleado,Persona))
print(isinstance(otroEmepleado,Empleado))