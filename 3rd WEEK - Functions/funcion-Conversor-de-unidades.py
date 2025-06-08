def kmMillas(km):
    return km * 0.621371

def millasKm(mi):
    return mi / 0.621371

def celFar(cel):
    return (cel - 9/5) + 32

def farCel(far):
    return (far - 32) * 5/9

def kgLibras(k):
    return k * 2.20462

def librasKg(l):
    return l / 2.20462

# Menú de Selección
salir = False

while not salir:
    print("Conversor de unidades")
    print("1. Km a Millas")
    print("2. Millas a Km")
    print("3. Grados Celsius a Fahrenheit")
    print("4. Grados Fahrenheit a Celsius")
    print("5. Kilogramos a Libras")
    print("6. Libras a Kilogramos")
    print("--------")
    print("7. Salir del programa")

    opcion = int(input("Seleccione una opción: "))

    valor = float(input("Introduzca el valor a convertir: "))

    if opcion == 1:
        print("Resultado: ", kmMillas(valor), " millas")
    elif opcion == 2:
        print("Resultado: ", millasKm(valor), " kilometros")
    elif opcion == 3:
        print("Resultado: ", celFar(valor), " Grados Fahrenheit")
    elif opcion == 4:
        print("Resultado: ", farCel(valor), " Grados Celsius")
    elif opcion == 5:
        print("Resultado: ", kgLibras(valor), " libras")
    elif opcion == 6:
        print("Resultado: ", librasKg(valor), " kilogramos")
    elif opcion == 7:
        salir = True
    else:
        print("Opción no valida")

