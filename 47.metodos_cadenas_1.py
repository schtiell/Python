def analisis_cadena(email):
    
    arroba = email.count('@')

    if arroba != 1 or email.find('@') == 0 or email.rfind('@') == (len(email)-1):
        print('email incorrecto')
    
    else:
        print('mail correcto')

email = input('Introduce un email: ')
analisis_cadena(email)