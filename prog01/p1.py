import matplotlib.pyplot as plt
ar = open("datos.txt")
total = 0
comuna = []
habi = []
linea = ar.readline().rstrip('\n')
while linea != '':
    lista = linea.split(',')
    if lista[1] == '7':
        print(lista[2], lista[4])
        total = total + float(lista[4])
        comuna.append(lista[2])
        habi.append(float(lista[4]))
    linea = ar.readline().rstrip('\n')
print("-----------------> Total : ", total)
ar.close()

plt.plot(comuna,habi,color='r')
plt.show()


