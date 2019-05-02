# La libreria datetime permite trabajar con fechas y horas
import datetime

# Impresion de las funciones del modulo datetime
print(dir(datetime))

# La funcion datetime.now() obtiene la fecha y hora actual.
now = datetime.datetime.now()

print('La fecha y hora actual es:',now)
print('La fecha y hora actual UTC es:',now.utcnow()) # Obtiene la fecha y hora actual UTC
print('El dia es:', now.day) # Obtiene (numero) el dia del mes
print('El mes es:', now.month) # Obtiene (numero) del mes
print('El mes es:', now.year) # Obtiene (numero) del mes
print("Hora:", now.hour)  # Muestra hora
print("Minutos:", now.minute)  # Muestra minuto
print("Segundos:", now.second)  # Muestra segundo
print("Microsegundos:", now.microsecond)  # Muestra microsegundo
print()

print(now)

# Los valores de la hora pueden ser modificados con el método replace
# El siguiente ejemplo modifica mediante parametros preestablecidos la funcion datetime
now = now.replace(year=2020,month=2,day=12)
now = now.replace(hour=18,minute=54,second=55,microsecond=343423)

print(now)

tiempo_transcurrido = datetime.datetime.now() - now
print(tiempo_transcurrido)
