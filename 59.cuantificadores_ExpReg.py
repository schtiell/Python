import re
import os

file = open("/home/jsayagot/Escritorio/Nuevas_cuentas/a_levantar", encoding="utf8")

contenido_archivo = file.read()

file.close()

print (os.system("clear"))

print (contenido_archivo)

#Los cuantificadores permiten contar o representar cuantas veces queremos buscar la expresion
print (re.search(r"\+\d-\(\d{3}\)-\d{3}-\d{4}",contenido_archivo))

#Los ? permiten indicar que el caracter puede estar o no dentro de la expresion regular a buscar
print (re.search(r"\+\d-\(?\d{3}\)?-\d{3}-\d{4}",contenido_archivo))
