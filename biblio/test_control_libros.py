import unittest
from unittest.mock import MagicMock
from control_libros import ControlBiblioteca

class TestControlBiblioteca(unittest.TestCase):
    """Pruebas unitarias para el método crear_libro de ControlBiblioteca."""
    
    def setUp(self):
        """Configura un mock de Biblioteca para cada prueba."""
        self.mock_biblioteca = MagicMock()
        self.control = ControlBiblioteca(self.mock_biblioteca)

    def test_crear_libro_exitoso(self):
        """Debe retornar True cuando el libro no existe y se agrega correctamente."""
        self.mock_biblioteca.buscar_libro.return_value = None  # Simula que el libro no existe

        resultado = self.control.crear_libro("El principito")
        self.assertTrue(resultado)

    def test_crear_libro_duplicado(self):
        """Debe retornar False cuando el libro ya existe en la biblioteca."""
        self.mock_biblioteca.buscar_libro.return_value = MagicMock()  # Simula que el libro ya existe

        resultado = self.control.crear_libro("El principito")
        self.assertFalse(resultado)


if __name__ == "__main__":
    unittest.main()
