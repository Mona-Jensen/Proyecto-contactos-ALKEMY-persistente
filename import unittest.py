import unittest
import os
from gestion_persistente import SistemaGestion

class TestSistemaGestionPersistente(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Eliminar archivo de datos antes de ejecutar las pruebas
        if os.path.exists("contactos.json"):
            os.remove("contactos.json")

    def setUp(self):
        self.sistema = SistemaGestion()

    def test_agregar_contacto(self):
        self.sistema.agregar("Ana", "123", "ana@mail.com", "Santiago")
        resultado = self.sistema.buscar("Ana")
        self.assertEqual(len(resultado), 1)

    def test_buscar_contacto(self):
        self.sistema.agregar("Pedro", "456", "pedro@mail.com", "Valparaíso")
        resultado = self.sistema.buscar("456")
        self.assertEqual(resultado[0].nombre, "Pedro")

    def test_editar_contacto(self):
        self.sistema.agregar("Lucía", "789", "lucia@mail.com", "Concepción")
        self.sistema.editar("Lucía", tel="999")
        resultado = self.sistema.buscar("Lucía")
        self.assertEqual(resultado[0].telefono, "999")

    def test_eliminar_contacto(self):
        self.sistema.agregar("Juan", "111", "juan@mail.com", "La Serena")
        eliminado = self.sistema.eliminar("Juan")
        self.assertTrue(eliminado)

if __name__ == "__main__":
    unittest.main()

