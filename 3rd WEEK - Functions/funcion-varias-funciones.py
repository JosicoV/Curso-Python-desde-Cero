def pedirNombre():
    return input("Introduzca su nombre: ")

def saludar(nombre):
    print("Hola, " + nombre)

def nameLen(name):
    print("La longitud de " + name + " es " + str(len(name)) + " caracteres")

nom = pedirNombre()
saludar(nom)
nameLen(nom)