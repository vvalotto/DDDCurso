import unittest
from Dominio.general.identificacion import Identificacion

class TestIdentificacion(unittest.TestCase):
    def test_identificacion(self):

        mi_identificacion = Identificacion("CC", "123456789")
        self.assertEqual(str(mi_identificacion.tipo), 'CC')
        self.assertEqual(str(mi_identificacion.numero), '123456789')

if __name__ == '__main__':
    unittest.main()
