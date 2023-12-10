dinero = int(input())
billetes = [500,200,100,50,20,10,5]
cantBilletes = []

for billete in billetes:
    numero = dinero // billete
    cantBilletes.append(numero)
    dinero = dinero -(numero * billete)

total = sum(cantBilletes)
print(total)
