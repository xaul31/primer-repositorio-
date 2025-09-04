from agenda import agregar_contactos, listar_contactos, buscar_contacto

def menu():
    while True:
        print("\nMenú de Agenda")
        print("1. Agregar Contacto")
        print("2. Listar Contactos")
        print("3. Buscar Contacto")
        print("4. Salir")
            
        opcion = input("Seleccione una opción (1-4): ")
            
        if opcion == '1':
            nombre = input("Ingrese el nombre: ")
            telefono = input("Ingrese el teléfono: ")
            agregar_contactos(nombre, telefono)
            print("Contacto agregado.")
        elif opcion == '2':
            listar_contactos()
        elif opcion == '3':
            nombre = input("Ingrese el nombre a buscar: ")
            buscar_contacto(nombre)
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

