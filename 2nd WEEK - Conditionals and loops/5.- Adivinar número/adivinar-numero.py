adivinado = False
num_secreto = 7

while not adivinado:
    intento = input("Adivine el número secreto: ")
    if int(intento) == num_secreto:
        print(f"Felicidades, el número secreto es {num_secreto}")
        adivinado = True
    else:
        print("No es correcto, inténtelo de nuevo")
        