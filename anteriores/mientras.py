cont = 0
final = 0
N = int(input('Cantidad de estudiantes: '))
while cont < N: 
    Nota = float(input('Nota '+str(cont + 1)+': '))
    final = final + Nota
    cont = cont + 1
Promedio = final / N
print(Promedio)
