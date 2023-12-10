"""
Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos valores fueron pares y cuántos impares.
Emplear el operador “%” en la condición de la estructura condicional (este operador retorna el resto de la división de dos valores, por ejemplo 11%2 retorna un 1):

"""

n = int(input("Cuantos numeros quiere introducir"))
pares = 0
impares = 0
for valor in range(n):
    numeros = int(input("Introduce numeros enteros"))
    if numeros%2==0:
        pares = pares+1
    else:
        impares = impares+1

print("Cantidad de numeros pares: ", pares)
print("Cantidad de numeros impares: ", impares)
