def validaCorreo1(correo):
    indice = correo.find('@')
    if indice == -1:
        mensa = 'INCORRECTO'
    else:
        mensa = 'CORRECTO'
    return mensa

def validaCorreo2(correo):
    if "@" in correo:
        mensa = 'CORRECTO'
    else:
        mensa = 'INCORRECTO'
    return mensa

def validaCorreo3(correo):
    i = 0
    largo = len(correo)
    mensa = 'INCORRECTO'
    while i < largo:
        if correo[i] == '@':
            mensa = "CORRECTO"
        i = i + 1
    return mensa

def validaCorreo4(correo):
    cant = correo.count('@')
    if cant == 1:
        mensa = 'CORRECTO'
    else:
        mensa = 'INCORRECTO'
    return mensa

correo = input("Ingrese su e-mail: ")
mensaje = validaCorreo1(correo)
print(mensaje)
mensaje = validaCorreo2(correo)
print(mensaje)
mensaje = validaCorreo3(correo)
print(mensaje)
mensaje = validaCorreo4(correo)
print(mensaje)
