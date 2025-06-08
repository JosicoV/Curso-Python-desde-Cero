def sumaLista(lista):
    suma = 0
    for x in range(0, len(lista)):
        suma += lista[x]
    print("La suma de todos los números de la lista es: " + str(suma))

numeros = [1, 2, 3, 4]
sumaLista(numeros)
