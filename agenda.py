#agenda
contacto =[]


def agregar_contactos(nombre,telefono):
    contacto.append({"nombre": nombre,"telefono:":telefono})


def listar_contactos():
    print("\nlista de contactos : ")
    for c in contacto:
        print(f"{c['nombre']} - {c['telefono']}")

def buscar_contacto(nombre):
    for c in contacto:
        if c ['nombre'].lower() == nombre.lower():
            print(f"contacto encontrado :  {c['nombre']} - {c['telefono']}")
            return
        print("contacto no encontrado")

listar_contactos()


nombre = input("ingresar el nombre : ")
telefono = input("ingresar el telefono : ")
agregar_contactos(nombre,telefono)
print("contacto agregado")