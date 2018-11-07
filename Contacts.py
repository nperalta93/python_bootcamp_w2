#Code by Nicolás Peralta

class Contact:

    def __init__(self, fecha_creado, nombre, apellido, edad, email):
        self.fecha_creado = fecha_creado
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.phones = {}
        self.email = email
        self.escondido = False

