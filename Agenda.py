import Contacts
import time


print("Agenda de contactos")
print("Ingrese los datos del contacto")

name = input("Ingrese el nombre")
last_name = input("Ingrese el apellido")
age = input ("Ingrese la edad")
email = input("Ingrese el email")

nuevo_contacto = Contacts.Contact(time.strftime("%x"), name, last_name, age, email)

print(nuevo_contacto.fecha_creado)