ent = open("dolar_raw.txt")
sal = open("dolar_clean.txt", 'w')
for linea in ent:
    linea = linea.rstrip('\n')
    lista = linea.split('\t')
    fecha = lista[0]
    valor = lista[1]
    valor = valor.replace(',', '.')
    if valor != '':
        sal.write(fecha+' '+valor+'\n')
ent.close()
sal.close()


