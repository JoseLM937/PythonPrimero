"""
Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas. Contar la cantidad de vocales. 
Crear un segundo string con toda la oración en minúsculas para que sea más fácil disponer la condición que verifica que es una vocal.

"""

frase = input("Introduce una oracion: ")
minus = frase.lower()
cont = 0
valor = 0
while valor < len(minus):
    if minus[valor]=="a" or minus[valor]=="e" or minus[valor]=="i" or minus[valor]=="o" or minus[valor]=="u":
        cont = cont+1
    
    valor = valor+1


print("La cantidad de vocales es de: ", cont)