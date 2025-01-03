from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        if asignaturas == None:
            self._asignaturas = []
        else:
            self._asignaturas = asignaturas
        if estudiantes == None:
            self.listadoAlumnos = []
        else:
            self.listadoAlumnos = estudiantes
        

    def listadoAsignaturas(self, **kwargs):
        #self._asignaturas = []
        for key, value in kwargs.items():
            asig = Asignatura(value)
            self._asignaturas.append(asig)

    def agregarAlumno(self, alumno, lista=None):
        if lista == None:
            lista = []
            lista.append(alumno)
            self.listadoAlumnos = self.listadoAlumnos + lista
        else:
            lista.append(alumno)
            self.listadoAlumnos = self.listadoAlumnos + lista

    def __str__(self):
        return "Grupo de estudiantes: " + self._grupo

    #@ classmethod
    #def asignarNombre(cls, nombre="Grado 10"):
    #    cls.grado = nombre

    #@ classmethod
    #def asignarNombre(cls, nombre="Grado 5"):
    #    cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
