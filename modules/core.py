from modules.utils import cargar_datos


def login():

    datos = cargar_datos()

    print("\n===== LOGIN =====")

    email = input("Correo corporativo: ")

    password = input("Contraseña: ")

    for usuario in datos["usuarios"]:

        if (
            usuario["email"] == email
            and
            usuario["password"] == password
        ):

            print(
                f"\nBienvenido {usuario['nombres']}"
            )

            return usuario

    print("\nCorreo o contraseña incorrectos")

    return None