with open("datos.txt", "w") as f:
    f.write("Primera frase\n")
    f.write("Segunda frase\n")
    f.write("Tercera frase\n")

with open("datos.txt", "r") as f:
    for linea in f:
        print(linea.strip())
