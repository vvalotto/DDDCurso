import unittest
from Dominio.base.texto_no_vacio import TextoNoVacio

class TestTextoNoVacio(unittest.TestCase):

    def test_texto_no_vacio(self):
        texto = TextoNoVacio("Hola")
        self.assertEqual(texto.texto, "Hola")

    def test_texto_vacio(self):
        with self.assertRaises(Exception) as context:
            TextoNoVacio("")
        self.assertTrue("Error: Esta Vacio" in str(context.exception))

    def test_texto_nulo(self):
        with self.assertRaises(Exception) as context:
            TextoNoVacio(None)
        self.assertTrue("Error: EsNulo" in str(context.exception))

    def test_texto_no_es_texto(self):
        with self.assertRaises(Exception) as context:
            TextoNoVacio(1)
        self.assertTrue("Error: No es texto" in str(context.exception))

if __name__ == '__main__':
    unittest.main()
