class ControlBiblioteca:
    """Clase con la lógica para gestionar los títulos de una biblioteca."""
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def crear_libro(self, titulo):
        """Intenta adicionar un libro. Retorna False si ya existe."""
        if self.biblioteca.buscar_libro(titulo):
            return False
        self.biblioteca.adicionar_libro(titulo)
        return True

    def consultar_cantidad_libros(self):
        return self.biblioteca.cantidad_libros()
