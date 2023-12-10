sueldo = int(input("Introduzca su sueldo: "))
antiguedad = int(input("Introduzca su fecha de antiguedad: "))

if sueldo < 500 and antiguedad >= 10:
    print("Dar el 20%")
    print("Tu sueldo es ", sueldo*0.2)
elif sueldo < 500 and antiguedad < 10:
    print("Dar el 5%")
    print("Tu sueldo es ", sueldo*0.05)
else:
    print("Tu sueldo es ", sueldo)
