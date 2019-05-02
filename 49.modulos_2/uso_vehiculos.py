from modulos_vehiculos import Vehiculos, Motocicleta, Camioneta, Vehiculos_Electricos

miAutomovil = Vehiculos("Ford","Fiesta")
miMoto = Motocicleta('Yamaha','FZ16')
miCamioneta = Camioneta('Chevrolet','S10')
miAutoElectrico = Vehiculos_Electricos('Tesla','Model S')

miAutomovil.encender_vehiculo()
miAutomovil.estado_vehiculo()

miMoto.hacer_caballito()
miMoto.estado_vehiculo()

miCamioneta.encender_vehiculo()
miCamioneta.frena_vehiculo()
miCamioneta.estado_vehiculo()

miAutoElectrico.encender_vehiculo()
miAutoElectrico.autonomia_bateria(58)