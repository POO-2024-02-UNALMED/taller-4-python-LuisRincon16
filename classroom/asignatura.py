class Asignatura:

    def __init__(self, nombre, salon):
        self._nombre = nombre
        self._salon = salon

    def __str__(self):
        return self.nombre + "remoto"
