from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
        

    def listadoAsignaturas(self, **kwargs):
        self._asignaturas = []
        for x in kwargs.values():
            self._asignaturas.append(kwargs.get("as","valor"))

    def agregarAlumno(self, alumno, lista=None):
        if lista == None:
            lista = []
            lista.append(alumno)
            self.listadoAlumnos = lista
        else:
            lista.append(alumno)
            self.listadoAlumnos = lista

    def __str__(self):
        return "Grupo de estudiantes: " + self._grupo

    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 5"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
