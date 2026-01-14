
import json, os
from contacto_persistente import Contacto

ARCHIVO = "contactos.json"

class SistemaGestion:
    def __init__(self):
        self.contactos = []
        self.indice = {}
        self.cargar()

    def guardar(self):
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            json.dump([c.to_dict() for c in self.contactos], f, indent=4, ensure_ascii=False)

    def cargar(self):
        if os.path.exists(ARCHIVO):
            with open(ARCHIVO, "r", encoding="utf-8") as f:
                datos = json.load(f)
                for d in datos:
                    c = Contacto.from_dict(d)
                    self.contactos.append(c)
                    self.indice[c.nombre.lower()] = c

    def agregar(self, nombre, tel, mail, dir):
        nuevo = Contacto(nombre, tel, mail, dir)
        self.contactos.append(nuevo)
        self.indice[nombre.lower()] = nuevo
        self.guardar()
        return "¡Contacto guardado con éxito!"

    def buscar(self, dato):
        dato = dato.lower()
        return [c for c in self.contactos if dato in c.nombre.lower() or dato in c.telefono]

    def editar(self, nombre, tel=None, mail=None, dir=None):
        c = self.indice.get(nombre.lower())
        if c:
            c.editar(tel, mail, dir)
            self.guardar()
            return True
        return False

    def eliminar(self, nombre):
        c = self.indice.get(nombre.lower())
        if c:
            self.contactos.remove(c)
            del self.indice[nombre.lower()]
            self.guardar()
            return True
        return False
