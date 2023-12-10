lectura = open("personas.txt", "r")
lineas = lectura.readlines()
numLinea = 0

personas = []
for linea  in lineas:
    nombre, edad = linea.strip().split(';')
    personas.append({'nombre': nombre, 'edad': int(edad)})

joven = personas[0]
mayor = personas[0]

for persona in personas:
    if persona['edad'] < joven['edad']:
        joven = persona
    if persona['edad'] > mayor['edad']:
        mayor = persona

print('Persona más joven: ', joven)
print('Persona más vieja: ', mayor)
