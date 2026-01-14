
class Contacto:
    def __init__(self, nombre, telefono, correo, direccion):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__correo = correo
        self.__direccion = direccion

    @property
    def nombre(self): return self.__nombre
    @property
    def telefono(self): return self.__telefono
    @property
    def correo(self): return self.__correo
    @property
    def direccion(self): return self.__direccion

    def editar(self, telefono=None, correo=None, direccion=None):
        if telefono: self.__telefono = telefono
        if correo: self.__correo = correo
        if direccion: self.__direccion = direccion

    def to_dict(self):
        return {
            "nombre": self.__nombre,
            "telefono": self.__telefono,
            "correo": self.__correo,
            "direccion": self.__direccion
        }

    @staticmethod
    def from_dict(data):
        return Contacto(data["nombre"], data["telefono"], data["correo"], data["direccion"])

    def __str__(self):
        return f"Nombre: {self.__nombre} | Tel: {self.__telefono} | Mail: {self.__correo}"
