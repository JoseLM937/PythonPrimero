"""

Crear una lista por asignación. La lista tiene que tener cuatro elementos.
Cada elemento debe ser una lista de 3 enteros.
Imprimir sus elementos accediendo de diferentes modos.

"""
lista=[[1,2,3], [4,5,6], [7,8,9], [10,11,12]]


print(lista)
print("---------")
print(lista[0])
print("---------")
print(lista[0][0])
print("---------")
for valor in range(len(lista[0])):
    print(lista[0][valor])
print("---------")
for k in range(len(lista)):
    for valor in range(len(lista[k])):
        print(lista[k][valor])
