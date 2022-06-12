class Persona:
    def __init__(self, legajo, apeynom, dni, direccion, telefono):
        self.__legajo = legajo
        self.__apeynom = apeynom
        self.__dni = dni
        self.__direccion = direccion
        self.__telefono = telefono

    # get y set de Legajo
    @property
    def legajo(self):
        return self.__legajo

    # a setter function
    @legajo.setter
    def legajo(self, legajo):
        self.__legajo = legajo

    # get y set de Nombre y Apellido
    def get_apeynom(self):
        return self.__apeynom

    def set_apeynom(self, apeynom):
        self.__apeynom = apeynom

    # get y set de DNI
    def get_dni(self):
        return self.__dni

    def set_dni(self, dni):
        self.__dni = dni

    # get y set de dirección
    def get_direccion(self):
        return self.__direccion

    def set_direccion(self, direccion):
        self.__direccion = direccion

    # get y set de Telefono
    def get_telefono(self):
        return self.__telefono

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def crear_legajo(self):
        pass
