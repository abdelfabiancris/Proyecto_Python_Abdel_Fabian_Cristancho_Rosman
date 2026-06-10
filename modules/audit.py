import json

from modules.utils import cargar_datos


def auditar_datos():

    datos = cargar_datos()

    reporte = {

        "usuarios_con_errores": [],

        "contactos_con_errores": [],

        "resumen": {

            "total_usuarios": len(datos["usuarios"]),

            "total_contactos": len(datos["contactos"]),

            "usuarios_con_errores": 0,

            "contactos_con_errores": 0,

            "usuarios_con_email_duplicado": 0,

            "contactos_con_id_duplicado": 0
        }
    }

    roles_validos = [

        "admin",
        "operario"
    ]

    tipos_validos = [

        "cliente",
        "proveedor",
        "aliado",
        "personal"
    ]

    emails_vistos = []

    ids_vistos = []



    for usuario in datos["usuarios"]:

        errores = []

        campos_obligatorios = [

            "id",
            "nombres",
            "apellidos",
            "telefono",
            "email",
            "direccion",
            "password",
            "rol"
        ]

        for campo in campos_obligatorios:

            if campo not in usuario:

                errores.append(
                    f"Falta el campo {campo}"
                )

            elif str(usuario[campo]).strip() == "":

                errores.append(
                    f"Campo vacío: {campo}"
                )

        if "telefono" in usuario:

            if not str(
                usuario["telefono"]
            ).isdigit():

                errores.append(
                    "Teléfono inválido"
                )

        if "email" in usuario:

            email = usuario["email"]

            if (
                "@" not in email
                or
                "." not in email
            ):

                errores.append(
                    "Email inválido"
                )

            if email in emails_vistos:

                errores.append(
                    "Email duplicado"
                )

                reporte["resumen"][
                    "usuarios_con_email_duplicado"
                ] += 1

            else:

                emails_vistos.append(email)

        if "rol" in usuario:

            if usuario["rol"] not in roles_validos:

                errores.append(
                    "Rol inválido"
                )

        if len(errores) > 0:

            reporte[
                "usuarios_con_errores"
            ].append({

                "id": usuario.get("id", "Sin ID"),

                "email": usuario.get(
                    "email",
                    "Sin Email"
                ),

                "errores": errores
            })



    for contacto in datos["contactos"]:

        errores = []

        campos_obligatorios = [

            "id",
            "nombres",
            "apellidos",
            "telefono",
            "email",
            "tipo"
        ]

        for campo in campos_obligatorios:

            if campo not in contacto:

                errores.append(
                    f"Falta el campo {campo}"
                )

            elif str(
                contacto[campo]
            ).strip() == "":

                errores.append(
                    f"Campo vacío: {campo}"
                )

        if "telefono" in contacto:

            if not str(
                contacto["telefono"]
            ).isdigit():

                errores.append(
                    "Teléfono inválido"
                )

        if "email" in contacto:

            email = contacto["email"]

            if (
                "@" not in email
                or
                "." not in email
            ):

                errores.append(
                    "Email inválido"
                )

        if "tipo" in contacto:

            if (
                contacto["tipo"]
                not in tipos_validos
            ):

                errores.append(
                    "Tipo de contacto inválido"
                )

        if "id" in contacto:

            if contacto["id"] in ids_vistos:

                errores.append(
                    "ID duplicado"
                )

                reporte["resumen"][
                    "contactos_con_id_duplicado"
                ] += 1

            else:

                ids_vistos.append(
                    contacto["id"]
                )

        if len(errores) > 0:

            reporte[
                "contactos_con_errores"
            ].append({

                "id": contacto.get(
                    "id",
                    "Sin ID"
                ),

                "errores": errores
            })



    reporte["resumen"][
        "usuarios_con_errores"
    ] = len(
        reporte["usuarios_con_errores"]
    )

    reporte["resumen"][
        "contactos_con_errores"
    ] = len(
        reporte["contactos_con_errores"]
    )

    if (
        len(
            reporte[
                "usuarios_con_errores"
            ]
        ) == 0
        and
        len(
            reporte[
                "contactos_con_errores"
            ]
        ) == 0
    ):

        reporte[
            "mensaje"
        ] = "No se encontraron errores"

    with open(

        "data/reporte_auditoria_datos.json",

        "w",

        encoding="utf-8"

    ) as archivo:

        json.dump(

            reporte,

            archivo,

            indent=4,

            ensure_ascii=False
        )

    print(
        "\nAuditoría completada correctamente"
    )

    print(
        "\nReporte generado en:"
    )

    print(
        "data/reporte_auditoria_datos.json"
    )