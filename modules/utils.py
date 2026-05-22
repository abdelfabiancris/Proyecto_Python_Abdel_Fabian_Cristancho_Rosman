import json


RUTA_ARCHIVO = "data/agenda.json"


def cargar_datos():

    with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo) #convierte en diccionario

    return datos


def guardar_datos(datos):

    with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def validar_input(mensaje):

    while True:

        dato = input(mensaje).strip()

        # Verificar si está vacío
        if dato == "":

            print("\nEste campo no puede estar vacío")

        else:

            return dato