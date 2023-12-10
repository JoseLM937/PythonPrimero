"""

Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
a) La cantidad de valores ingresados negativos.
b) La cantidad de valores ingresados positivos.
c) La cantidad de múltiplos de 15.
d) El valor acumulado de los números ingresados que son pares.

"""
positivo = 0
negativo = 0
multiplo = 0
pares = 0
for valor in range(10):
    numeros = int(input("Introduce numeros"))

    if numeros > 0:
        positivo = positivo +1
    else:
        negativo = negativo +1
    if 15%numeros == 0 or numeros%15==0:
        multiplo = multiplo+1
    
    if numeros%2==0:
        pares = pares+1

print("Cantidad de numeros positivos: ", positivo)
print("Cantidad de numeros negativos: ", negativo)
print("Cantidad de numeros multiplos de 15: ", multiplo)
print("Cantidad de numeros pares: ", pares)

