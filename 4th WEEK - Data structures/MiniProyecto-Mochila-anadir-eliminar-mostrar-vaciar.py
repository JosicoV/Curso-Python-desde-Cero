mochila = [] # Mochila vacía incialmente y variable global (podemos utilizarla en las funciones)

# Funciones
def anadir(objeto):
    mochila.append(objeto)
    print(f"{objeto} añadido a la mochila.")

def eliminar(objeto):
    if objeto in mochila:
        mochila.remove(objeto)
        print(f"{objeto} eliminado de la mochila")
    else:
        print(f"{objeto} no estaba en la mochila")

def mostrar():
    if mochila:
        print("Contenido de la mochila\n", mochila)
    else:
        print("La mochila está vacía")

def vaciar():
    mochila.clear()
    print("Se vació la mochila")

salir = False
while not salir:
    print("""
Opciones: añadir, eliminar, mostrar, vaciar y salir  
""")
    opcion = input("Qué opción elige: ").lower()

    match opcion:
        case "añadir":
            obj = input("Qué objeto quiere añadir? ")
            anadir(obj)
        case "eliminar":
            obj = input("Qué objeto quiere eliminar? ")
            eliminar(obj)
        case "mostrar":
            mostrar()
        case "vaciar":
            vaciar()
        case "salir":
            salir = True
            print("Vuelve cuando quieras!")
        case _:
            print("Opción no valida. Esta mochila no es el Sombrero de Harry Potter")