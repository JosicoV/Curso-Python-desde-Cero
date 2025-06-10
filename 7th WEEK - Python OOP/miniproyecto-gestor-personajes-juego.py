class Personaje:
    def __init__(self, nombre, clase, nivel=1):
        self.nombre = nombre
        self.clase = clase
        self.nivel = nivel
    
    def subir_nivel(self):
        self.nivel += 1

    def mostrar_estado(self):
        print(f"Nombre: {self.nombre}")
        print(f"Clase: {self.clase}")
        print(f"Nivel: {self.nivel}")
    

# Lista de personajes
personajes = []

# Crear personajes
personaje1 = Personaje("Gandalf", "Mago", 125)
personaje2 = Personaje("Legolas", "Arquero", 90)
personaje3 = Personaje("Gimli", "Guerrero", 88)

# Agregar personajes a la lista
personajes.append(personaje1)
personajes.append(personaje2)
personajes.append(personaje3)

# Mostrar estado
for personaje in personajes:
    personaje.mostrar_estado()

# Subir de nivel a todos
for personaje in personajes:
    personaje.subir_nivel()

print("\nDespués de subir de nivel:")
for personaje in personajes:
    personaje.mostrar_estado()