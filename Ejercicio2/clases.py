class Contacto:
    def __init__(self, nombre, numerotelf):
        self.nombre = nombre
        self.numerotelf = numerotelf

    def __str__(self):
        return f"""Contacto: {self.nombre}, 
        numero: {self.numerotelf}"""

class Agendas:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)

    def mostrar_contactos(self):
        for contacto in self.contactos:
            print(contacto)