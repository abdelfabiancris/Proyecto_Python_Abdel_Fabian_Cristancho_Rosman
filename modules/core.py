from modules.utils import cargar_datos


def login():

    # Cargar datos del JSON
    datos = cargar_datos()

    print("\n===== LOGIN =====")

    # Pedir datos al usuario
    email = input("Correo corporativo: ")
    password = input("Contraseña: ")

    # Recorrer usuarios del JSON
    for usuario in datos["usuarios"]:

        # Verificar email y contraseña
        if usuario["email"] == email and usuario["password"] == password:

            print(f"\nBienvenido {usuario['nombres']}")

            return usuario

    print("\nCorreo o contraseña incorrectos")

    return None