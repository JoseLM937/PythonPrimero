"""
Se cuenta con la siguiente información:
Las edades de 5 estudiantes del turno mañana.
Las edades de 6 estudiantes del turno tarde.
Las edades de 11 estudiantes del turno noche.
Las edades de cada estudiante deben ingresarse por teclado.
a) Obtener el promedio de las edades de cada turno (tres promedios)
b) Imprimir dichos promedios (promedio de cada turno)
c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor.

"""
mediaDia = 0
mediaTarde = 0
mediaNoche = 0
totalDia =0 
totalTarde = 0
totalNoche= 0
mayor = 0
menor = 0


for valor in range(5):
    dia = int(input("Introduce las edades de los alumnos del dia: "))
    totalDia = totalDia+dia


for valor in range(6):
    tarde = int(input("Introduce las edades de los alumnos de la tarde: "))
    totalTarde = totalTarde+tarde

for valor in range(11):
    noche = int(input("Introduce las edades de los alumnos de la noche: "))
    totalNoche = totalNoche+noche

mediaDia = totalDia/5
mediaTarde = totalTarde/6
mediaNoche = totalNoche/11
print("El promedio de los alumnos del dia es: ", mediaDia)
print("El promedio de los alumnos de la tarde es: ", mediaTarde)
print("El promedio de los alumnos de la noche es: ", mediaNoche)
lista = []
lista = mediaDia, mediaTarde, mediaNoche

for valor in range(len(lista)):
    if mayor == 0:
        mayor = lista[valor]
        menor = lista[valor]
    if lista[valor] > mayor:
        mayor = lista[valor]       
    if valor < menor:
        menor = lista[valor]
    
print("El mayor de todos los promedios es: ", mayor)

