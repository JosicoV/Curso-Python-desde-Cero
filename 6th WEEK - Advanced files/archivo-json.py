import json

persona = {
    "nombre": "Josico",
    "edad": "Incalculable"
    }

with open("persona.json", "w") as archivo:
    json.dump(persona, archivo)

with open("persona.json", "r") as archivo:
    persona = json.load(archivo)
    print(persona["nombre"])
