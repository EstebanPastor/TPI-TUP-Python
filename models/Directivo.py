from models.Persona import Persona


class Directivo(Persona):

    def __init__(self, legajo, apeynom, dni, direccion, telefono, telurgencia):
        super().__init__(legajo, apeynom, dni, direccion, telefono)
        self.__telurgencia = telurgencia
        #Docente.__init__(telurgencia, titulo, materia)

    # Telefono de urgencia.
    def get_telurgencia(self):
        return self.__telurgencia

    def set_telurgencia(self, telurgencia):
        self.__telurgencia = telurgencia

    # Creado de legajo
    def crear_legajo(self):
        self.legajo = "DIR_" + self.get_dni()[-3:]

    def __str__(self):
        return "Legajo: {}, Nombre y Apellido: {}, DNI: {}, Dirección: {}, Tel: {}, Tel Urgencia: {}".format(self.legajo, self.get_apeynom(), self.get_dni(), self.get_direccion(), self.get_telefono(), self.get_telurgencia())
