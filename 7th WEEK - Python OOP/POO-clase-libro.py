class Libro:
    def __init__(self, titulo, autor, ano_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacion = ano_publicacion

    def mostrar_libro(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.ano_publicacion}")

    def es_antiguo(self):
        return int(self.ano_publicacion) < 2000

l1 = Libro("Estudio Python", "Josico", "2030")
l2 = Libro("El señor de los Anillos", "J.R.R. Tolkien", "1954")
l3 = Libro("Harry Potter", "J.K. Rowling", "1997")

l1.ano_publicacion = "2050"

for libro in [l1, l2, l3]:
    libro.mostrar_libro()
    if libro.es_antiguo():
        print("Este libro es antiguo.")
    else:
        print("Este libro es nuevo.")



