from haraya import *

def maxi(a, b):
    if a > b:
        return a
    else:
        return b
    
def max_de_tres(a, b, c):
    return maxi(maxi(a, b), c)

def saludo():
    limpiaPantalla()
    print('Bienvenido al programa')
    print()

saludo()
n1 = int(input("N1: "))
n2 = int(input('N2: '))
n3 = int(input('N3: '))
mayor = max_de_tres(n1, n2, n3)
print(mayor)