numero1 = int(input("Dime cuantos numeros vas a introducir: "))
numero = 0
mayor = 0
menor = 0
print("Escirbe ", numero1, " numeros")
for valor in range(numero1):
    numero = int(input())
    if mayor == 0:
        mayor = numero
        menor = numero
    if numero > mayor:
        mayor = numero
        
    if numero < menor:
        menor = numero 
         
print("El numero mayor es ", mayor)  
print("El numero menor es ", menor)  
   
 