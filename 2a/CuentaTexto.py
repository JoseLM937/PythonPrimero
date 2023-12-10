texto = input("Introduce un texto: ")
cont = 0

while texto.find("python")> 0:
    cont = cont+1
    texto = texto[texto.find("python")+6:]
print("La cantidad es de ", cont)