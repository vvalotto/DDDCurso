"""
--------------------------
Proyecto = Admisiones
Modulo = nombre
Autor = admin
Fecha creación = 22/10/2018 11:00
--------------------------
"""

from Dominio.base.objeto_valor import *
from Dominio.base.texto_no_vacio import TextoNoVacio


class Nombre(ObjetoValor):

    """
    Propiedades accedidas
    """
    @property
    def nombres(self):
        return self._nombres

    @property
    def apellido(self):
        return self._apellido

    def __init__(self, nombres='Sin Nombre', apellido ='Sin Apellido'):
        """
        Creación del objeto valor nombre
        :param nombres:
        :param apellido:
        """

        self._nombres = TextoNoVacio(nombres)
        self._apellido = TextoNoVacio(apellido)

    def apellido_y_nombres(self):
        """
        Se devuelve de la manera apellido y nombre
        :return:
        """
        return str(self._apellido) + ', ' + str(self._nombres)

    def __repr__(self):
        return  str(self.nombres) + ' ' + str(self.apellido)

    def __str__(self):
        return str(self.nombres) + ' ' + str(self.apellido)
    def obtener_atributos_incluidos_en_chequeo_igualdad(self):
        return [self._nombres, self._apellido]

if __name__ == '__main__':
    nombre = Nombre('Juan', 'Perez')
    print(nombre)