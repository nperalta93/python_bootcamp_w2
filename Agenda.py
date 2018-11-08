import Contacts
import time

lista_contactos = []

print("Agenda de contactos")

def newContact():
    print("Ingrese los datos del contacto")
    telefono = input("Ingrese el número telefónico ")
    tipo_numero = input("Casa, oficina, movil? ")
    name = input("Ingrese el nombre ")
    last_name = input("Ingrese el apellido ")
    age = input ("Ingrese la edad ")
    email = input("Ingrese el email ")

    nuevo_contacto = Contacts.Contact(time.strftime("%x"), name, last_name, age, email)
    sirvio = nuevo_contacto.addNumber(tipo_numero, telefono)
    if sirvio:
        print("Ajam")
    else:
        print("naaa")

    lista_contactos.append(nuevo_contacto)

def showContacts():
    lista_contactos.sort(key=time.strftime("%x"))

    for cont in lista_contactos:
        print(cont.nombre," ", cont.apellido, cont.edad, cont.email)
        for type, tel in cont.phones.items():
            print(type,": ", tel)

def menu(option):
    menu = {1: newContact,
          2: showContacts}

    func = menu.get(option, lambda : "Opción inexistente")
    func()

rta = 's'
while rta == 's' or rta == 'S':
    opc = int(input("Ingrese la opcion deseada "))
    menu(opc)
    rta = input("Desea continuar? Presione S/s")