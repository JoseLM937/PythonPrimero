nota1 = int(input("Escribe tu primera nota:"))
nota2 = int(input("Escribe tu segunda nota:"))
nota3 = int(input("Escribe tu tercera nota:"))

if nota1 < 4 and nota2 < 4 and nota3 < 4:
    print("La nota final es un 0")
elif nota1 > 4 and nota2 > 4 and nota3 > 4:
    notaFinal = ((nota1*0,3) + (nota2*0,2) + (nota3*0,5))
    print("La nota final es ", notaFinal)       
else:
    print("Nota final es 2")