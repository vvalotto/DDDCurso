"""
--------------------------
Proyecto = ddd-evaluaciones
Modulo = domicilio
Autor = admin
Fecha creación = 16/10/16
--------------------------
"""
from Dominio.base.objeto_valor import ObjetoValor
from Dominio.base.texto_no_vacio import TextoNoVacio

'''
Value Object: Domicilio
'''


class Domicilio(ObjetoValor):

    @property
    def calle(self):
        return self._calle

    @property
    def numero(self):
        return self._numero

    @property
    def piso(self):
        return self._piso

    @property
    def departamento(self):
        return self._departamento

    def __init__(self, calle, numero, piso, departamento):

        self._calle = TextoNoVacio(calle)
        self._numero = TextoNoVacio(numero)
        self._piso = TextoNoVacio(piso)
        self._departamento = TextoNoVacio(departamento)

    def obtener_atributos_incluidos_en_chequeo_igualdad(self):
        return [self._calle, self._numero, self._departamento, self._piso]

    def __repr__(self):
        return \
            "Domicilio: " + "\n" + \
            "  " + str(self._numero) + "\n" + \
            "  " + str(self._calle) + "\n" + \
            "  " + str(self._departamento) + "\n" + \
            "  " + str(self._piso) + "\n"

    def __str__(self):
        return \
            "Domicilio: " + "\n" + \
            "  " + str(self._numero) + "\n" + \
            "  " + str(self._calle) + "\n" + \
            "  " + str(self._departamento) + "\n" + \
            "  " + str(self._piso) + "\n"
