from models.Persona import Persona


class Personal(Persona):

    def __init__(self, legajo, apeynom, dni, direccion, telefono, tarea):
        super().__init__(legajo, apeynom, dni, direccion, telefono)
        self.__tarea = tarea

    def get_tarea(self):
        return self.__tarea

    def set_tarea(self, tarea):
        self.__tarea = tarea

    # Creado de legajo
    def crear_legajo(self):
        self.legajo = "PER_" + self.get_dni()[-3:]

    def __str__(self):
        return "Legajo: {}, Nombre y Apellido: {}, DNI: {}, Dirección: {}, Tel: {}, Tarea: {}".format(self.legajo, self.get_apeynom(), self.get_dni(), self.get_direccion(), self.get_telefono(), self.get_tarea())
