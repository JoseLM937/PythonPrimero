"""

Crear y cargar dos listas con los nombres de 5 productos en una y
sus respectivos precios en otra. Definir dos listas paralelas.
Mostrar cuantos productos tienen un precio mayor al primer producto ingresado.

"""

nombres = []
precios = []
cont = 0
for valor in range(5):
    nombre = input("Escriba el nombre del producto: ")
    nombres.append(nombre)
    precio = int(input("Introduce los precios de los productos: "))
    precios.append(precio)



for valor in range(5):
    if precios[valor] > precios[0]:
        cont = cont+1
        print("Producto que tiene un precio mayor al primer ingresado: ",nombres[valor])
print("Cantidad de productos que tienen un mayor precio que el primero introducido: ", cont)
