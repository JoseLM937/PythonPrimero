"""
Crea un programa llamado BuscaNumeros.py que le pida al usuario que escriba números. El
programa los irá añadiendo uno tras otro a una lista hasta que el usuario escriba 0. Entonces, le pedirá
que diga un número y le indicará en qué posiciones de la lista aparece ese número.

"""


listNumeros = []
numeros = int(input("Introduce numeros enteros: "))
pos = 0
while numeros != 0:
    listNumeros.append(numeros)
    numeros = int(input("Introduce numeros enteros: "))

pedirNumero = int(input("Introduce un numero: "))
size = len(listNumeros)

for pos in range(len(listNumeros)):
    posi = listNumeros.index(pedirNumero)
    if pos == posi:
        print("La posicion del numero es ", pos)
    



