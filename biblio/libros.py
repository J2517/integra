class Libro:
    """Representa un libro con un título."""
    def __init__(self, titulo):
        self.titulo = titulo

    def __eq__(self, other):
        return isinstance(other, Libro) and self.titulo == other.titulo

    def __str__(self):
        return self.titulo


class Biblioteca:
    """Contiene un listado de libros y permite adicionar y buscar títulos."""
    def __init__(self):
        self.libros = []

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return None
        return None

    def adicionar_libro(self, titulo):
        self.libros.append(Libro(titulo))

    def cantidad_libros(self):
        return len(self.libros)

