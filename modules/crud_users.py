from modules.utils import cargar_datos, guardar_datos


def registrar_usuario():

    datos = cargar_datos()

    print("\n===== REGISTRAR USUARIO =====")

    id_usuario = input("Número de identificación: ")

    # Validar ID repetido
    for usuario in datos["usuarios"]:

        if usuario["id"] == id_usuario:

            print("\nEse ID ya existe")

            return

    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    telefono = input("Teléfono: ")
    email = input("Correo corporativo: ")
    direccion = input("Dirección: ")
    password = input("Contraseña: ")
    rol = input("Rol (admin/operario): ")

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