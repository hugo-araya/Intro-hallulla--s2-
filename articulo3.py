# Escribir un algoritmo que escriba el nombre de un articulo, 
# clave, precio original y su precio con descuento. 
# El descuento lo hace en base a la clave, si la clave es 01 el descuento 
# es del 10% y si la clave es 02 el descuento es del 20% 
# (solo existen dos claves).

# Datos de entrada: articulo(string), codigo(string), precio_o(Entero)
# Dato salida: precio_d (float)

import os 

if os.name == "posix":
   os.system("clear")
else:
   os.system ("cls")

articulo = input('-->> Nombre del articulo: ')
codigo = input('--> Ingrese codigo: ')
precio_o = int(input('--> Precio: '))

if (codigo == '01'):
    precio_d = precio_o * 0.9
else:
    if (codigo == '02'):
        precio_d = precio_o * 0.8
    else:
        codigo = "Codigo no existe"
        precio_d = 0
print('\tArticulo: \n\t\t' ,articulo)
print('\tCodigo: ', codigo)
print('\tPrecio con descuento: ' ,precio_d)
