import os 

def limpiaPantalla():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')