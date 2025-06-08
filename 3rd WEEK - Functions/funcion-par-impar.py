num = int(input("Introduzca un número: "))

def parImpar(n):
    if n % 2 == 0:
        print(f"{n} es un número par")
    else:
        print(f"{n} es un número impar")

parImpar(num)