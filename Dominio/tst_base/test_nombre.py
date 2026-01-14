import unittest
from Dominio.general.nombre import Nombre
from Dominio.base.texto_no_vacio import TextoNoVacio

class Test_Nombre(unittest.TestCase):
    def test_nombre(self):
        nombre = Nombre("Juan","Perez")
        self.assertEqual(nombre.nombres, TextoNoVacio("Juan"))
        self.assertEqual(nombre.apellido, TextoNoVacio("Perez"))


if __name__ == '__main__':
    unittest.main()
