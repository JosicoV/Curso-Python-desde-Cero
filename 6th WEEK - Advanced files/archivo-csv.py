import csv

with open("usuarios.csv", "w", newline="") as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerow(["Nombre", "Apellido", "Edad"])
    escritor_csv.writerow(["Juan", "Pérez", 30])
    escritor_csv.writerow(["María", "Gómez", 25])
    escritor_csv.writerow(["Carlos", "López", 35])

with open("usuarios.csv", "r") as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
        print(fila)
