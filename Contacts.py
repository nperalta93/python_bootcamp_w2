# Code by Nicolás Peralta

class Contact:

    def __init__(self, fecha_creado, nombre, apellido, edad, email):
        self.fecha_creado = fecha_creado
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.phones = {}
        self.email = email
        self.escondido = False

    def phoneType(self, type):
        phone_type = {1: "Casa",
                     2: "Movil",
                     3: "Oficina",
                     }

        return phone_type.get(type, lambda : print("Opción inexistente"))



    def addNumber(self, phone_type, numero):
        try:
            self.phones.setdefault(phone_type, numero)
            return True
        except:
            return False