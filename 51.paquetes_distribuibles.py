# Paquetes Distribuibles
# https://www.youtube.com/watch?v=Zf9sN-w0BVE&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=36

# Son paquetes que puedan ser reutilizados para otros proyectos
# crear el paquete e instalarlo en el equipo propio son los 2 pasos a seguir

# Ventajas:
# Al instalar un paquete le permite a python hacer uso de el sin importar 
# el directorio en el que se encuentre


# CREAR PAQUETE PARA DISTRIBUIRLO

# Crear un archivo llamado setup.py
# El cual contiene una descripcion del paquete que se va a distribuir

"""
from setuptools import setup

setup(

    # Datos_obligatorios

    name = "Nombredelpaquete",
    version="numero de version",
    description = "Breve descripcion del paquete y su funcionamiento", 
    author = "Nombre del creador del paquete",

    # Datos_no_obligatorios

    author_email = " correo electrónico del autor del paquete",
    url = "Sitio de referencia",

    # Ruta donde se encuentra el paquete o subpaquete 
    # packages = ["paquete","paquete.subpaquete"]

    packages = ["paquetes","paquetes.redondeos"]


)
"""



# Ir al directorio del paquete desde el promp(windows) o terminal(linux)
# python setup.py sdist.
# Donde setup.py es el archivo de python que contiene los datos del paquete
# sdist permite la creacion del paquete distribuible 
# Si todo va bien ha creado una carpeta del paquete y otra dist con un archivo *.tar.gz


# INSTALAR EL PAQUETE EN OTRO EQUIPO

# Ir a la carpeta dist que contiene el archivo *.tar.gz desde la terminal
# pip3 install *.tar.gz
# con esto podemos ejecutar el los modulos sin problemas de que python no los reconozca
# con la sentencia from - import
# podemos mover el archivo en cualqueir directorio y no debe haber problemas


# DESINSTALAR EL PAQUETE DEL EQUIPO

# el paquete puede ser leido desde cualqueir parte, ya que ha pasado a formar parte de python
# para desinstalar el paquete pip3 uninstall *.tar.gz

