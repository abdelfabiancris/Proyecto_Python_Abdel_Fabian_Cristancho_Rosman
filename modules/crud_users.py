from modules.utils import (
    cargar_datos,
    guardar_datos,
    validar_input
)


def registrar_usuario():

    datos = cargar_datos()

    print("\n===== REGISTRAR USUARIO =====")

    id_usuario = validar_input("ID: ")

    # Validar ID duplicado
    for usuario in datos["usuarios"]:

        if usuario["id"] == id_usuario:

            print("\nYa existe un usuario con ese ID")

            return

    nombres = validar_input("Nombres: ")

    apellidos = validar_input("Apellidos: ")

    # Validar teléfono
    while True:

        telefono = validar_input("Teléfono: ")

        if telefono.isdigit():

            break

        print("\nEl teléfono debe contener solo números")

    # Validar email
    while True:

        email = validar_input("Correo corporativo: ")

        if "@" in email and "." in email:

            break

        print("\nCorreo inválido")

    # Validar email duplicado
    for usuario in datos["usuarios"]:

        if usuario["email"] == email:

            print("\nEse correo ya está registrado")

            return

    direccion = validar_input("Dirección: ")

    # Validar rol
    while True:

        rol = validar_input(
            "Rol (admin/operario): "
        ).lower()

        if rol in ["admin", "operario"]:

            break

        print("\nRol inválido")

    password = validar_input("Contraseña: ")

    nuevo_usuario = {

        "id": id_usuario,

        "nombres": nombres,

        "apellidos": apellidos,

        "telefono": telefono,

        "email": email,

        "direccion": direccion,

        "password": password,

        "rol": rol
    }

    datos["usuarios"].append(nuevo_usuario)

    guardar_datos(datos)

    print("\nUsuario registrado correctamente")