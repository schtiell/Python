import re
import os

file = open("/home/jsayagot/Escritorio/Nuevas_cuentas/a_levantar", encoding="utf8")

contenido_archivo = file.read()

file.close()

print (os.system("clear"))

print(contenido_archivo)

# Método de busqueda re.match
# Realiza una busqueda en la primera linea y palabra del archivo
print(re.match(r"APLICACIONES",contenido_archivo))

# Método de busqueda re.search
# Realiza una busqueda en el archivo
print(re.search(r"ADMINCITAS",contenido_archivo))

# Expresion Regular que busca un digito
print(re.search(r"\d",contenido_archivo))

# Expresion Regular que busca espacios en blanco
print(re.search(r"\#######",contenido_archivo))

# Expresión regular para buscar numero telefonicos con este formato
print(re.search(r"\+\d-\(\d\d\d\)-\d\d\d-\d\d\d\d",contenido_archivo))



