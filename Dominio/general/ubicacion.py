"""
--------------------------
Proyecto = ddd-evaluaciones
Modulo = ubicacion
Autor = admin
Fecha creación = 29/10/16
--------------------------
"""

from Dominio.general.domicilio import Domicilio
from Dominio.base.objeto_valor import ObjetoValor


class Ubicacion(ObjetoValor):

    @property
    def domicilio(self):
        return self._domicilio

    @property
    def pais(self):
        return self._pais

    @property
    def provincia(self):
        return self._provincia

    @property
    def ciudad(self):
        return self._ciudad

    @property
    def codigo_postal(self):
        return self._codigo_postal

    def obtener_atributos_incluidos_en_chequeo_igualdad(self):
        return [self._domicilio, self._pais, self._provincia, self._ciudad, self._codigo_postal]

    def __init__(self, domicilio,
                       pais,
                       provincia,
                       ciudad,
                       codigo_postal):

        self._domicilio = domicilio
        self._pais = pais
        self._provincia = provincia
        self._ciudad = ciudad
        self._codigo_postal = codigo_postal

    def __repr__(self):
        return \
            "Ubicacion: " + "\n" + \
            "  " + str(self._domicilio) + "\n" + \
            "  " + str(self._pais) + "\n" + \
            "  " + str(self._provincia) + "\n" + \
            "  " + str(self._ciudad) + "\n" + \
            "  " + str(self._codigo_postal) + "\n"

    def __str__(self):
        return \
            "Ubicacion: " + "\n" + \
            "  " + str(self._domicilio) + "\n" + \
            "  " + str(self._pais) + "\n" + \
            "  " + str(self._provincia) + "\n" + \
            "  " + str(self._ciudad) + "\n" + \
            "  " + str(self._codigo_postal) + "\n"







