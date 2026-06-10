from modules.core import login

from modules.messages import menu_principal

from modules.crud_contacts import (
    registrar_contacto,
    listar_contactos,
    buscar_contacto,
    actualizar_contacto,
    eliminar_contacto
)

from modules.crud_users import registrar_usuario

from modules.audit import auditar_datos


# ==========================
# LOGIN
# ==========================

usuario_autenticado = None

while usuario_autenticado is None:

    usuario_autenticado = login()


# ==========================
# MENÚ PRINCIPAL
# ==========================

while True:

    menu_principal()

    opcion = input(
        "\nSeleccione una opción: "
    )

    # Registrar usuario
    if opcion == "1":

        if usuario_autenticado["rol"] == "admin":

            registrar_usuario()

        else:

            print(
                "\nNo tiene permisos para registrar usuarios"
            )

    # Registrar contacto
    elif opcion == "2":

        registrar_contacto()

    # Listar contactos
    elif opcion == "3":

        listar_contactos()

    # Buscar contacto
    elif opcion == "4":

        buscar_contacto()

    # Actualizar contacto
    elif opcion == "5":

        actualizar_contacto()

    # Eliminar contacto
    elif opcion == "6":

        eliminar_contacto()

    # Auditar datos
    elif opcion == "7":

        auditar_datos()

    # Salir
    elif opcion == "8":

        print(
            "\nGracias por usar el sistema"
        )

        break

    else:

        print(
            "\nOpción inválida"
        )