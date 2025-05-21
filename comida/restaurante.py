class Pedido:
    """Representa un pedido con múltiples platos."""
    def __init__(self):
        self.platos = []

    def agregar_plato(self, plato):
        self.platos.append(plato)

    def calcular_total(self):
        return sum(plato.precio for plato in self.platos)


class Restaurante:
    """Gestiona pedidos y asigna platos desde el menú."""
    def __init__(self, menu):
        self.menu = menu
        self.pedidos = []

    def crear_pedido(self):
        pedido = Pedido()
        self.pedidos.append(pedido)
        return pedido

    def agregar_plato_a_pedido(self, pedido, nombre_plato):
        plato = self.menu.obtener_plato(nombre_plato)
        if plato:
            pedido.agregar_plato(plato)
            return True
        return False
    