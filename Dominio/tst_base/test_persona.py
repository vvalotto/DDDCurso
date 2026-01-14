import unittest
from Dominio.general.persona import Persona
from Dominio.general.nombre import Nombre

class TestPersona(unittest.TestCase):

    def test_persona(self):

        mi_persona = Persona(1, nombre=Nombre("Juan","Perez"))
        self.assertEqual(mi_persona.id, 1)
        self.assertEqual(str(mi_persona.nombre), 'Juan Perez')
        self.assertEqual(str(mi_persona.ubicacion), 'Sin Ubicacion')
        self.assertEqual(str(mi_persona.identificacion), 'Sin Información')


if __name__ == '__main__':
    unittest.main()
