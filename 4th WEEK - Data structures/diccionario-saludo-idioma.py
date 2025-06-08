saludos = {
    "es" : "Hola",
    "en" : "Hi",
    "fr" : "Bonjour"
}

opcion = input("""
En que idoma quiere que le salude
1.- Español
2.- Inglés
3.- Francés
Elija una opción: """)

if opcion == "1":
    print(saludos["es"])
elif opcion == "2":
    print(saludos["en"])
elif opcion == "3":
    print(saludos["fr"])
else:
    print("Opción no valida. Estoy estudiando más idiomas, pero ese no lo conozco.")