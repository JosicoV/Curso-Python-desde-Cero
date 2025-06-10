tareas = ["Aprender Python", "Salir con los amigos", "Leer"]
with open("tareas.txt", "w") as archivo:
    for tarea in tareas:
        archivo.write(tarea + "\n")

with open("tareas.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())