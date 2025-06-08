print("CALCULADORA")
print("-----------")
print("")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

operacion = input("¿Qué operación desea realizar? ")
primero = float(input("Primer número: "))
segundo = float(input("Segundo número: "))

if operacion == "1":
    print(primero + segundo)
elif operacion == "2":
    print(primero - segundo)
elif operacion == "3":
    print(primero * segundo)
elif operacion == "4":
    if segundo == 0:
        print("No se puede dividir entre 0")
    else:
        print(primero / segundo)
else:
    print("Operación no válida")