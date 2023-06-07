nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
examen = float(input('Examen: '))
trabajo = float(input('Trabajo: '))
notas = (nota1 + nota2 + nota3)/3
promedio = notas*0.55 + examen*0.3 + trabajo*0.15

if (promedio >= 4):
    print('Logro aprobar el curso')
    print('con nota: ', promedio)
else:
    print('NO logro aprobar el curso')
    print('con nota: ', promedio)
print('Que la suerte este con usted')


