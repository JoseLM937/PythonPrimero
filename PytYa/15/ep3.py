"""
Almacenar en una lista los sueldos (valores float) de 5 operarios. Imprimir la lista y el promedio de sueldos.

"""

lista = []
suma = 0

for valor in range(5):
    sueldo = int(input("Introduce el sueldo de 5 operarios: "))
    lista.append(sueldo)
    suma = suma+sueldo
print("Los sueldos de los operarios son: ", lista)
promedio = suma/5
print("El promedio de los sueldos es: ", promedio)


    
