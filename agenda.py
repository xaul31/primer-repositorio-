#agenda
#tarea menu 1.agregar contacto 2.listar contacto 3.buscar contacto 4. salir y seleccionar opcion

contacto = []


def agregar_contactos(nombre, telefono):
    contacto.append({"nombre": nombre, "telefono": telefono})


def listar_contactos():
    print("\nLista de contactos:")
    for c in contacto:
        print(f"{c['nombre']} - {c['telefono']}")


def buscar_contacto(nombre):
    for c in contacto:
        if c['nombre'].lower() == nombre.lower():
            print(f"Contacto encontrado: {c['nombre']} - {c['telefono']}")
            return
    print("Contacto no encontrado")
