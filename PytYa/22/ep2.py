"""
Crear una lista y almacenar 10 enteros pedidos por teclado.
Eliminar todos los elementos que sean iguales al número entero 5.

"""

lista=[]
for x in range(10):
    valor=int(input("Ingrese valor:"))
    lista.append(valor)

print(lista)

pos=0
while pos<len(lista):
    if lista[pos]==5:
        lista.pop(pos)
    else:
        pos=pos+1
    
print(lista)
