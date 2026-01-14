

from Dominio.base.objeto_valor import ObjetoValor
from Dominio.base.texto_no_vacio import TextoNoVacio
class Identificacion(ObjetoValor):

        @property
        def tipo(self):
            return self._tipo

        @property
        def numero(self):
            return self._numero

        def __init__(self, tipo, numero):
            self._tipo = TextoNoVacio(tipo)
            self._numero = TextoNoVacio(numero)

        def obtener_atributos_incluidos_en_chequeo_igualdad(self):
            return [self._tipo, self._numero]

        def __repr__(self):
            return \
                "Identificacion: " + "\n" + \
                "  " + str(self._tipo) + "\n" + \
                "  " + str(self._numero) + "\n"

        def __str__(self):
            return \
                "Identificacion: " + "\n" + \
                "  " + str(self._tipo) + "\n" + \
                "  " + str(self._numero) + "\n"