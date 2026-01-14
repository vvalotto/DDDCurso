"""
--------------------------
Proyecto = ddd-evaluaciones
Modulo = persona
Autor = admin
Fecha creación = 23/10/16
--------------------------
"""
from Dominio.base.entidad import Entidad
from Dominio.general.domicilio import Domicilio
from Dominio.general.nombre import Nombre
from Dominio.general.ubicacion import Ubicacion
from Dominio.general.identificacion import Identificacion

class Persona(Entidad):

    @property
    def id(self):
        return self._identificacion

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
        return

    @property
    def ubicacion(self):
        return self._ubicacion

    @ubicacion.setter
    def ubicacion(self, valor):
        self._ubicacion = valor
        return

    def __init__(self, identificacion,
                       nombre,
                       ubicacion):
        self._identificacion = identificacion
        self._nombre = nombre
        self._ubicacion = ubicacion
        return


if __name__ == '__main__':
    una_identificacion = Identificacion('DNI', '12345678')
    un_nombre = Nombre("Victor", "Valotto")
    un_domicilio = Domicilio('Calle Falsa', '123', '1', 'A')
    una_ubicacion = Ubicacion(un_domicilio, 'Argentina', 'Buenos Aires', 'CABA', '1234')
    una_persona = Persona(una_identificacion, un_nombre, una_ubicacion)
    print(una_persona.id)
    print(una_persona.nombre)
    print(una_persona.ubicacion)