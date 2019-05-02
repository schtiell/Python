import datetime

# Sitio web que nos da los formatos de fecha y hora
# http://strftime.org/

now = datetime.datetime.now()
print(now)

ahora = datetime.datetime.today()
print(ahora)

# Las funciones now() y today() devuelven practicamente el mismo valor
# Pero now puede recibir un parametro para especificar uno zona horaria

# Crea un hora en 0's
print(datetime.time())

fecha_hoy = datetime.datetime.combine(datetime.datetime.today(),datetime.time())
print(fecha_hoy)

print(fecha_hoy.day)
print(fecha_hoy.minute)
print(fecha_hoy.year)
print(fecha_hoy.month)
print(fecha_hoy.hour) 


# Formateando Fechas y Horas

ahora = datetime.datetime.now()
dia = datetime.datetime.now()
dia = int(dia.strftime('%j'))
ahora = ahora.strftime("%B %a %d, %Y, dia %j")
print (ahora,'quedan,',365 - dia,'para el año 2019')

# o bien
# print (ahora.strftime("%B %d, %Y"))