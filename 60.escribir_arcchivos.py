import re

def escribir_archivos(articulo):

    file = open("/home/jsayagot/Escritorio/Nuevas_cuentas/a_levantar", "a")

    file.write("{}\n".format(articulo))

    file.close()


escribir_archivos(input("Que deseas agregar al archivo: "))




    