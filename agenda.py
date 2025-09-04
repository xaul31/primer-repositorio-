#agenda
contacto =[]


def agregar_contactos(nombre,telefono):
    contacto.append({"nombre": nombre,"telefono:":telefono})

nombre = input("ingresar el nombre : ")
telefono = input("ingresar el telefono : ")
agregar_contactos(nombre,telefono)
print("contacto agregado")