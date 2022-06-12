from models.Persona import Persona


class Alumno(Persona):

    def __init__(self, legajo, apeynom, dni, direccion, telefono, email, nacionalidad, residencia, canthnos, telpadre, telmadre, teladi):
        super().__init__(legajo, apeynom, dni, direccion, telefono)
        self.__email = email
        self.__nacionalidad = nacionalidad
        self.__residencia = residencia
        self.__canthnos = canthnos
        self.__telpadre = telpadre
        self.__telmadre = telmadre
        self.__teladi = teladi

    # Email
    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    # Nacionalidad
    def get_nacionalidad(self):
        return self.__nacionalidad

    def set_nacionalidad(self, nacionalidad):
        self.__nacionalidad = nacionalidad

    # Residencia
    def get_residencia(self):
        return self.__residencia

    def set_residencia(self, residencia):
        self.__residencia = residencia

    # Cantidad hermanos
    def get_canthnos(self):
        return self.__canthnos

    def set_canthnos(self, canthnos):
        self.__canthnos = canthnos

    # Telefono del padre.
    def get_telpadre(self):
        return self.__telpadre

    def set_telpadre(self, telpadre):
        self.__telpadre = telpadre

    # Telefono de la madre.
    def get_telmadre(self):
        return self.__telmadre

    def set_telmadre(self, telmadre):
        self.__telmadre = telmadre

    # Telefono adicional.
    def get_teladi(self):
        return self.__teladi

    def set_teladi(self, teladi):
        self.__teladi = teladi

    # Creado de legajo
    def crear_legajo(self):
        self.legajo = "ALU_" + self.get_dni()[-3:]

    def __str__(self):
        return "Legajo: {}, Nombre y Apellido: {}, DNI: {}, Dirección: {}, Tel: {}, Email: {}, Nacionalidad: {}, Residencia: {}, Cant. Hnos: {}, Tel. Padre: {}, Tel. Madre: {}, Tel. Adicional: {}".format(self.legajo, self.get_apeynom(), self.get_dni(), self.get_direccion(), self.get_telefono(), self.get_email(), self.get_nacionalidad(), self.get_residencia(), self.get_canthnos(), self.get_telpadre(), self.get_telmadre(), self.get_teladi())
