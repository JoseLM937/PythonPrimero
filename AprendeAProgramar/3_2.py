x = int(input())

numeros = []
for valor in range(x):
    numero = int(input())
    numeros.append(numero)

mayor = max(numeros)
menor = min(numeros)
print(mayor, menor)
