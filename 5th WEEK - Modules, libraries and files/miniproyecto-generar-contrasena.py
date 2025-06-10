import random
import string


# Funciones
def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + "!@#$%&*?"
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def guardar_contrasena(contrase, archivo="contrasena.txt"):
    with open(archivo, "a") as f:
        f.write(contrase + "\n")


# Menú simple
long = int(input("¿Longitud de la contraseña? "))
pw = generar_contrasena(long)
print("Tu contraseña es: ", pw)

guardar = input("Desea guardar la contraseña? (s/n): ")
if guardar.lower() == "s":
    guardar_contrasena(pw)
    print("Contraseña guardada en contrasena.txt")
else:
    print("Contraseña no guardada")
