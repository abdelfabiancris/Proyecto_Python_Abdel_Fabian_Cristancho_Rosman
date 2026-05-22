from modules.core import login
from modules.messages import menu_principal
from modules.crud_users import registrar_usuario
from modules.crud_contacts import registrar_contacto, listar_contactos, buscar_contacto, actualizar_contacto, eliminar_contacto

usuario_autenticado = login()


if usuario_autenticado:

    while True:

        opcion = menu_principal()

        if opcion == "1":

            if usuario_autenticado["rol"] == "admin":

                registrar_usuario()

            else:

                print("\nNo tienes permisos para esta opción")

        elif opcion == "2":
            registrar_contacto()

        elif opcion == "3":
            listar_contactos()

        elif opcion == "4":
            buscar_contacto()

        elif opcion == "5":
            actualizar_contacto()

        elif opcion == "6":
            eliminar_contacto()

        elif opcion == "7":
            print("\nSesión finalizada")
            break

        else:
            print("\nOpción inválida")

else:

    print("\nAcceso denegado")