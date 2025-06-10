from pathlib import Path

Path("datos").mkdir(exist_ok=True)

with open("datos/info.txt", "w") as f:
    f.write("info.txt dentro de datos/")

with open("datos/info.txt", "r") as f:
    print(f.read())