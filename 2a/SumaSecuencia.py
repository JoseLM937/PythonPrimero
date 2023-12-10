texto1 = input("Introduce una secuencia de numeros: ")
partes = texto1.split(" ")
suma = 0
for valor in range(len(partes)):
    suma  = suma + int(partes[valor])

print("La suma total es ", suma)