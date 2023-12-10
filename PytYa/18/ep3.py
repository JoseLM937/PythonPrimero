"""

Crear una lista y almacenar los nombres de 5 países.
Ordenar alfabéticamente la lista e imprimirla.

"""

paises = []

for valor in range(5):
    pais = input("Introduce el nombre de un pais: ")
    paises.append(pais)
for i in range(4):
    for valor in range(4-i):
        if paises[valor]>paises[valor+1]:
            aux=paises[valor]
            paises[valor] = paises[valor+1]
            paises[valor+1] = aux
print("Lista de los paises ordenados: ", paises)
    
