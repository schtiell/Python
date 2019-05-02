import datetime

now = datetime.datetime.now()
print(now)

# Cambiar los datos de datetime.now()
# Avanzar 5 dias, 13 horas y 34 minutos en el futuro a la fecha actual

fecha_futura = now + datetime.timedelta(days=5,hours=13,minutes=34)
print(fecha_futura)

# Timedelta, realiza los calculos en suma de minutos para hacer una hora o de 
# horas para cambiar a un nuevo dia, etc.

# Retroceder en el tiempo, 13 horas y 34 minutos
# Se puede retroceder el tiempo con una simple resta
fecha_pasada = now - datetime.timedelta(days=5,hours=13,minutes=34)
print(fecha_pasada)

# o bien
# Se puede hacer una suma de parametros negativos
# Realiza una suma algebraica
fecha_pasada_ = now + datetime.timedelta(days=-5,hours=-13,minutes=-34)
print(fecha_pasada_)


# Conocer unicamente la fecha

print(now.date())
print(now.time())