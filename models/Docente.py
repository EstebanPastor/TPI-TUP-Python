from models.Persona import Persona


class Docente(Persona):

    def __init__(self, legajo, apeynom, dni, direccion, telefono, telurgencia, titulo, materia):
        super().__init__(legajo, apeynom, dni, direccion, telefono)
        self.__telurgencia = telurgencia
        self.__titulo = titulo
        self.__materia = materia

    # Telefono de urgencia.
    def get_telurgencia(self):
        return self.__telurgencia

    def set_telurgencia(self, telurgencia):
        self.__telurgencia = telurgencia

    # Titulo.
    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    # Materia.
    def get_materia(self):
        return self.__materia

    def set_materia(self, materia):
        self.__materia = materia

    # Creado de legajo
    def crear_legajo(self):
        self.legajo = "DOC_" + self.get_dni()[-3:]

    def __str__(self):
        return "Legajo: {}, Nombre y Apellido: {}, DNI: {}, Dirección: {}, Tel: {}, Tel Urgencia: {}, Titulo: {}, Materia: {}".format(self.legajo, self.get_apeynom(), self.get_dni(), self.get_direccion(), self.get_telefono(), self.get_telurgencia(), self.get_titulo(), self.get_materia())
