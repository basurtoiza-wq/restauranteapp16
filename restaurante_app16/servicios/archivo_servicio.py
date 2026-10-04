import json


class ArchivoServicio:

    @staticmethod
    def cargar_datos(ruta):
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    @staticmethod
    def guardar_datos(ruta, datos):
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(
                datos,
                archivo,
                indent=4,
                ensure_ascii=False
            )