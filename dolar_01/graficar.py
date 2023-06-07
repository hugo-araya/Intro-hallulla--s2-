import matplotlib.pyplot as plt
ent = open("dolar_clean.txt")
X = []
Y = []
for linea in ent:
    linea = linea.rstrip('\n')
    lista = linea.split(' ')
    fecha = lista[0]
    valor = float(lista[1])
    X.append(fecha)
    Y.append(valor)
ent.close()
plt.plot(Y)
plt.show()

