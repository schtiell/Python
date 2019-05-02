import re
import os
    

file = open ("/home/jsayagot/Escritorio/Nuevas_cuentas/a_levantar", encoding="utf8")

contenido = file.read()

file.close()

print("El contenido del archivo es: ",contenido.lower())