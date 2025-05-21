class Plato:
    """Representa un plato del menú con nombre y precio."""
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f}"


class Menu:
    """Administra los platos disponibles en el restaurante."""
    def __init__(self):
        self.platos = {}

    def agregar_plato(self, nombre, precio):
        self.platos[nombre] = Plato(nombre, precio)

    def obtener_plato(self, nombre):
        return self.platos.get(nombre)

