with open("datos.txt", "w") as f:
    f.write("Primera frase\n")
    f.write("Segunda frase\n")
    f.write("Tercera frase\n")

with open("datos.txt", "a") as f:
    f.write("Cuarta frase\n")
    f.write("Quinta frase\n")
