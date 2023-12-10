"""
Solicitar el ingreso de una clave por teclado y almacenarla en una cadena de caracteres. 
Controlar que el string ingresado tenga entre 10 y 20 caracteres para que sea válido, en caso contrario mostrar un mensaje de error.

"""

clave = input("Introduce una clave de ingreso: ")

if len(clave) < 10 or len(clave) > 20:
    print("La clave insertada no es valida")
else:
    print("La clave es valida")