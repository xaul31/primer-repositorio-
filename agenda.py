#agenda
contacto =[]


def agregar_contactos(nombre,telefono):
    contacto.append({"nombre": nombre,"telefono:":telefono})


def listar_contactos():
    print("\nlista de contactos : ")
    for c in contacto:
        print(f"{c['nombre']} - {c['telefono']}")

listar_contactos()


nombre = input("ingresar el nombre : ")
telefono = input("ingresar el telefono : ")
agregar_contactos(nombre,telefono)
print("contacto agregado")