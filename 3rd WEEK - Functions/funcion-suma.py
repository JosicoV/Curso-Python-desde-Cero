n1 = int(input("Escriba el primer número: "))
n2 = int(input("Escriba el segundo número: "))

def suma(num1, num2):
    return num1 + num2

strSuma = str(suma(n1, n2))

print("la suma de los dos números es " + strSuma)