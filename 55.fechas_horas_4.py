# Manejo de zonas horarias

import datetime

central_time = datetime.timezone(datetime.timedelta(hours=-6))
print(central_time)

pacific_time = datetime.timezone(datetime.timedelta(hours=-8))
print(pacific_time)

eastern_time = datetime.timezone(datetime.timedelta(hours=-5))
print(eastern_time)

now = datetime.datetime.now(central_time)
print('Horario central',now)

now = now.astimezone(pacific_time)
print('Horario del pacifico',now)

now = now.astimezone(eastern_time)
print('Horario del Este',now)