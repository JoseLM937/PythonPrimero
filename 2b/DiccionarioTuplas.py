
usuarios = {}
usuarios[input("Introduce los dni del usuario1: ")] = ( input("Introduce los datos del usuario1: ").split(" "))
usuarios[input("Introduce los dni del usuario1: ")] = ( input("Introduce los datos del usuario2: ").split(" "))
usuarios[input("Introduce los dni del usuario1: ")] = ( input("Introduce los datos del usuario3: ").split(" "))
usuarios[input("Introduce los dni del usuario1: ")] = ( input("Introduce los datos del usuario4: ").split(" "))
dni = input("Introduce un dni: ")

if dni == '111A' or dni == '222B' or dni == '333C' or dni == '444D':
    print(usuarios[dni])
else:
    print("El dni no se encuentra almacenado")












