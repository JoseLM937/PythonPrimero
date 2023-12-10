numero = int(input("Introduce un numero a invertir: "))

num = numero
temp = 0

while numero != 0:
   temp = temp*10+numero%10
   numero //=10

    
print(temp)

    