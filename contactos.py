import math
contactos = []
while True:
    print("\n--- Menu Contactos ---")
    print("1. Agregar Contacto")
    print("2. Ver Contactos")
    print("3. Eliminar contacto")
    print("4. Salir")
    try:
        opcion = int(input("Elige una opción: "))
        if int(opcion) <= 0 or int(opcion) > 4 or math.isnan(float(opcion)) or opcion == 1e309:
            print("Por favor, ingrese una opcion valida.")
            continue
        elif opcion == 1:
            while True:
                existe = False
                nombre = input("Ingrese el nombre del contacto: ")
                telefono = input("Ingrese el telefono del contacto (sin el + y de 11 digitos): ")
                correo = input("Ingrese el correo del contacto: ")
                if nombre == "" or telefono == "" or correo == "":
                    print("Por favor, ingrese todos los campos.")
                elif not telefono.isdigit() or len(telefono) != 11:
                    print("Por favor, ingrese un telefono valido.")
                else:
                    if len(contactos) != 0:
                        for contacto in contactos:
                            if contacto["nombre"] == nombre:
                                print("El contacto ya existe.") 
                                existe = True
                                break
                        if not existe:    
                            contactos.append({"nombre": nombre, "telefono": "+"+str(telefono), "correo": correo})
                            print("Contacto agregado exitosamente.")
                        break                              
                    else:
                        contactos.append({"nombre": nombre, "telefono": "+"+str(telefono), "correo": correo})
                        print("Contacto agregado exitosamente.")
                        break
        elif opcion == 2:
            print("\n--- Contactos ---")
            for contacto in contactos:
                print(f"Nombre: {contacto['nombre']}")
                print(f"Telefono: {contacto['telefono']}")
                print(f"Correo: {contacto['correo']}")
                print("------------------")
        elif opcion == 3:
            while True:
                existe = False
                print("\n--- Eliminar Contacto ---")
                nombre = input("Ingrese el nombre del contacto a eliminar: ")
                if nombre == "":
                    print("Por favor, ingrese el nombre del contacto a eliminar.")
                else:
                    if len(contactos) != 0:
                        for contacto in contactos:
                            if contacto["nombre"] == nombre:
                                contactos.remove(contacto)
                                print("Contacto eliminado exitosamente.")
                                existe = True
                            break
                        if not existe:
                            print("Contacto no encontrado.")
                        break
                    else:
                        print("No hay contactos en la agenda.")
                        break
        elif opcion == 4:
            print("Saliendo...")
            break

    except ValueError:
        print("Por favor, ingrese solo numeros.")
    