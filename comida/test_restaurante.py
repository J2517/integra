import unittest
from unittest.mock import MagicMock

from restaurante import Restaurante, Pedido
from menu import Plato


class TestRestauranteIntegracion(unittest.TestCase):

    def setUp(self):
        self.plato = Plato("Ensalada", 10)
        self.menu= MagicMock()
        self.pedido = MagicMock()

    def test_crear_pedido_agrega_a_lista_de_pedidos(self):
        pedido = self.restaurante.crear_pedido()
        self.assertIn(pedido, self.restaurante.pedidos)
        self.assertIsInstance(pedido, Pedido)

    def test_agregar_plato_a_pedido_con_plato_existente(self):
        plato_mock = MagicMock()
        plato_mock.precio = 15

        self.menu_mock.obtener_plato.return_value = plato_mock

        pedido = self.restaurante.crear_pedido()
        resultado = self.restaurante.agregar_plato_a_pedido(pedido, "Pizza")

        self.assertTrue(resultado)
        self.assertIn(plato_mock, pedido.platos)
        self.menu_mock.obtener_plato.assert_called_once_with("Pizza")

    def test_agregar_plato_a_pedido_con_plato_inexistente(self):
        self.menu_mock.obtener_plato.return_value = None

        pedido = self.restaurante.crear_pedido()
        resultado = self.restaurante.agregar_plato_a_pedido(pedido, "Sushi")

        self.assertFalse(resultado)
        self.assertEqual(len(pedido.platos), 0)
        self.menu_mock.obtener_plato.assert_called_once_with("Sushi")

    def test_calcular_total_pedido_con_mock_platos(self):
        plato1 = MagicMock()
        plato1.precio = 10
        plato2 = MagicMock()
        plato2.precio = 20

        pedido = Pedido()
        pedido.agregar_plato(plato1)
        pedido.agregar_plato(plato2)

        total = pedido.calcular_total()
        self.assertEqual(total, 30)
  
        
if __name__ == '__main__':
    unittest.main()
