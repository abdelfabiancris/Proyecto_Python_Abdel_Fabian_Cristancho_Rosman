from modules.utils import cargar_datos, guardar_datos, validar_input



def registrar_contacto():
    

    datos = cargar_datos()

    print("\n===== REGISTRAR CONTACTO =====")

    id_contacto = validar_input("Número de identificación: ")

    # Validar ID repetido
    for contacto in datos["contactos"]:

        if contacto["id"] == id_contacto:

            print("\nEse contacto ya existe")

            return

    nombres = validar_input("Nombres: ")
    apellidos = validar_input("Apellidos: ")
    telefono = validar_input("Teléfono: ")
    email = validar_input("E-mail: ")
    direccion = validar_input("Dirección: ")
    tipo = validar_input("Tipo de contacto: ")
    notas = input("Notas: ")

    nuevo_contacto = {
        "id": id_contacto,
        "nombres": nombres,
        "apellidos": apellidos,
        "telefono": telefono,
        "email": email,
        "direccion": direccion,
        "tipo": tipo,
        "notas": notas
    }

    datos["contactos"].append(nuevo_contacto)

    guardar_datos(datos)

    print("\nContacto registrado correctamente")



def listar_contactos():

    datos = cargar_datos()

    print("\n===== LISTA DE CONTACTOS =====")

    # Validar si no hay contactos
    if len(datos["contactos"]) == 0:

        print("\nNo hay contactos registrados")

        return

    # Encabezados
    print(f"\n{'ID':<10} {'NOMBRE':<25} {'TELÉFONO':<15} {'EMAIL':<30} {'TIPO'}")

    print("-" * 90)

    # Recorrer contactos
    for contacto in datos["contactos"]:

        nombre_completo = contacto["nombres"] + " " + contacto["apellidos"]

        print(f"{contacto['id']:<10} {nombre_completo:<25} {contacto['telefono']:<15} {contacto['email']:<30} {contacto['tipo']}")



def buscar_contacto():

    datos = cargar_datos()

    print("\n===== BUSCAR CONTACTO =====")

    print("1. Buscar por ID")
    print("2. Buscar por nombre o apellido")
    print("3. Buscar por tipo")

    opcion = input("\nSeleccione una opción: ")

    encontrados = []

    # Buscar por ID
    if opcion == "1":

        id_buscar = validar_input("\nIngrese el ID: ")

        for contacto in datos["contactos"]:

            if contacto["id"] == id_buscar:

                encontrados.append(contacto)

    # Buscar por nombre o apellido
    elif opcion == "2":

        texto = validar_input("\nIngrese nombre o apellido: ").lower()

        for contacto in datos["contactos"]:

            nombre_completo = (
                contacto["nombres"] + " " + contacto["apellidos"]
            ).lower()

            if texto in nombre_completo:

                encontrados.append(contacto)

    # Buscar por tipo
    elif opcion == "3":

        tipo = validar_input("\nIngrese tipo de contacto: ").lower()

        for contacto in datos["contactos"]:

            if contacto["tipo"].lower() == tipo:

                encontrados.append(contacto)

    else:

        print("\nOpción inválida")

        return

    # Mostrar resultados
    if len(encontrados) == 0:

        print("\nNo se encontraron contactos")

    else:

        print(f"\n{'ID':<10} {'NOMBRE':<25} {'TELÉFONO':<15} {'EMAIL':<30} {'TIPO'}")

        print("-" * 90)

        for contacto in encontrados:

            nombre_completo = contacto["nombres"] + " " + contacto["apellidos"]

            print(f"{contacto['id']:<10} {nombre_completo:<25} {contacto['telefono']:<15} {contacto['email']:<30} {contacto['tipo']}")



def actualizar_contacto():

    datos = cargar_datos()

    print("\n===== ACTUALIZAR CONTACTO =====")

    id_buscar = validar_input("Ingrese el ID del contacto: ")

    for contacto in datos["contactos"]:

        if contacto["id"] == id_buscar:

            print("\nContacto encontrado")

            print("\nPresione ENTER para mantener el valor actual")

            nuevo_nombre = input(f"Nuevos nombres ({contacto['nombres']}): ").strip()

            if nuevo_nombre != "":
                contacto["nombres"] = nuevo_nombre

            nuevo_apellido = input(f"Nuevos apellidos ({contacto['apellidos']}): ").strip()

            if nuevo_apellido != "":
                contacto["apellidos"] = nuevo_apellido

            nuevo_telefono = input(f"Nuevo teléfono ({contacto['telefono']}): ").strip()

            if nuevo_telefono != "":
                contacto["telefono"] = nuevo_telefono

            nuevo_email = input(f"Nuevo email ({contacto['email']}): ").strip()

            if nuevo_email != "":
                contacto["email"] = nuevo_email

            nueva_direccion = input(f"Nueva dirección ({contacto['direccion']}): ").strip()

            if nueva_direccion != "":
                contacto["direccion"] = nueva_direccion

            nuevo_tipo = input(f"Nuevo tipo ({contacto['tipo']}): ").strip()

            if nuevo_tipo != "":
                contacto["tipo"] = nuevo_tipo

            nuevas_notas = input(f"Nuevas notas ({contacto['notas']}): ").strip()

            if nuevas_notas != "":
                contacto["notas"] = nuevas_notas

            guardar_datos(datos)

            print("\nContacto actualizado correctamente")

            return

    print("\nNo se encontró el contacto")



def eliminar_contacto():

    datos = cargar_datos()

    print("\n===== ELIMINAR CONTACTO =====")

    id_buscar = validar_input("Ingrese el ID del contacto: ")

    for contacto in datos["contactos"]:

        if contacto["id"] == id_buscar:

            print("\nContacto encontrado:")
            print(contacto["nombres"], contacto["apellidos"])

            confirmar = input("\n¿Desea eliminar este contacto? (s/n): ")

            if confirmar.lower() == "s":

                datos["contactos"].remove(contacto)

                guardar_datos(datos)

                print("\nContacto eliminado correctamente")

            else:

                print("\nEliminación cancelada")

            return

    print("\nNo se encontró el contacto")