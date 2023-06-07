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

fechaMes = []
valorMes = []

suma = 0
i = 0
cont = 0
while i < len(X):
    if X[i][3:6] == 'ene':
        suma = suma + Y[i]
        cont = cont + 1
    i = i + 1
promedio = suma /cont
fechaMes = fechaMes + ['ene']
valorMes = valorMes + [promedio]

suma = 0
i = 0
cont = 0
while i < len(X):
    if X[i][3:6] == 'feb':
        suma = suma + Y[i]
        cont = cont + 1
    i = i + 1
promedio = suma /cont
fechaMes = fechaMes + ['feb']
valorMes = valorMes + [promedio]

suma = 0
i = 0
cont = 0
while i < len(X):
    if X[i][3:6] == 'mar':
        suma = suma + Y[i]
        cont = cont + 1
    i = i + 1
promedio = suma /cont
fechaMes = fechaMes + ['mar']
valorMes = valorMes + [promedio]

suma = 0
i = 0
cont = 0
while i < len(X):
    if X[i][3:6] == 'abr':
        suma = suma + Y[i]
        cont = cont + 1
    i = i + 1
promedio = suma /cont
fechaMes = fechaMes + ['abr']
valorMes = valorMes + [promedio]


suma = 0
i = 0
cont = 0
while i < len(X):
    if X[i][3:6] == 'may':
        suma = suma + Y[i]
        cont = cont + 1
    i = i + 1
promedio = suma /cont
fechaMes = fechaMes + ['may']
valorMes = valorMes + [promedio]

suma = 0
i = 0
cont = 0
while i < len(X):
    if X[i][3:6] == 'jun':
        suma = suma + Y[i]
        cont = cont + 1
    i = i + 1
promedio = suma /cont
fechaMes = fechaMes + ['jun']
valorMes = valorMes + [promedio]

plt.plot(fechaMes, valorMes)
plt.show()

