"""
Podemos recorrer el archivo leyendo línea a línea utilizando la estructura
repetitiva for:
"""

archi1=open("datos.txt","r")
for linea in archi1:
    print(linea, end='')
archi1.close()
