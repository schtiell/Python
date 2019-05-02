empleado=int(input('Cual es el salario del empleado? \n'))
jefe = (int(input('Cual es el salario del jefe de area? \n')))
subdirector=(int(input('Cual es el salario del subdirector? \n')))
director=int(input('Cual es el salario del director? '))

def analisis_empleado(empleado,jefe,subdirector,director):
    if empleado<jefe and empleado<subdirector and empleado<director:
        print('Salario del empleado bien calculado')
    else:
        print('El salario del empleado debe estar mal calculado')

    if jefe>empleado and jefe<subdirector and jefe<director:
        print('El salario del jefe esta bien calculado')
    else:
        print('El salario del jefe debe estar mal calculado')
    
    if empleado<jefe and jefe<subdirector and subdirector<director:
        print('El salario del subdirector es correcto')
    else:
        print('El salario del subdirector debe estar mal calculado')

    if director>subdirector>jefe>empleado:
        print('El salario del director esta bien calculado')
    else:
        print('El salario del director es incorrecto')

analisis_empleado(empleado,jefe,subdirector,director)
