def maxi(a, b):
    if a > b:
        return a
    else:
        return b

n1 = int(input("N1: "))
n2 = int(input('N2: '))
mayor = maxi(n1, n2)
print(mayor)
