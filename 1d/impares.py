numero1 = int(input("Introduce un numero"))
for valor in range(numero1):
    if valor%2 != 0:
        print(valor , end=",")