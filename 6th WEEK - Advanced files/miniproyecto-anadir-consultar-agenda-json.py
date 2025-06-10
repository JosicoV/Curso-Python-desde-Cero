import json
from pathlib import Path

archivo = "agenda.json"

def cargar_agenda():
    if Path(archivo).exists():
        with open(archivo, "r") as f:
            return json.load(f)
    else:
        return []
    
def guardar_agenda(agenda):
    with open(archivo, "w") as f:
        json.dump(agenda, f, indent=4)

def agregar_contacto(nombre, telefono):
    agenda = cargar_agenda()
    agenda.append({"nombre": nombre, "telefono": telefono})
    guardar_agenda(agenda)
    print("Contacto agregado con éxito.")

def mostrar_agenda():
    agenda = cargar_agenda()
    if not agenda:
        print("La agenda está vacía.")
    else:
        print("Agenda:\n")
        for contacto in agenda:
            print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}\n")

while True:
    print("Menú:\n1.- Ver contactos\n2.- Agregar contacto\n3.- Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        mostrar_agenda()
    elif opcion == "2":
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        agregar_contacto(nombre, telefono)
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
