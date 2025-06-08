base = int(input("Introduzca la longitud de la base del triangulo: "))
altura = int(input("Introduzca la longitud de la altura del triangulo: "))

def areaTriangulo(b, h):
    return (b * h) / 2

strAreaTriangulo = str(areaTriangulo(base, altura))

print("El area del triangulo para los datos dados es: " + strAreaTriangulo)