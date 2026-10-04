import tkinter as tk
import os

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


def iniciar_aplicacion():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    ruta_productos = os.path.join(
        base_dir, "datos", "productos.json"
    )

    ruta_usuarios = os.path.join(
        base_dir, "datos", "usuarios.json"
    )

    ruta_ventas = os.path.join(
        base_dir, "datos", "ventas.json"
    )

    ruta_logo = os.path.join(
        base_dir, "assets", "logo.png"
    )

    # Crear el servicio de archivos
    archivo_servicio = ArchivoServicio()

    # Cargar los datos
    productos = archivo_servicio.cargar_datos(ruta_productos)
    usuarios = archivo_servicio.cargar_datos(ruta_usuarios)
    ventas = archivo_servicio.cargar_datos(ruta_ventas)

    # Crear el servicio principal
    servicio = RestauranteServicio(
        productos,
        usuarios,
        ventas,
        archivo_servicio,
        ruta_productos,
        ruta_usuarios,
        ruta_ventas
    )

    # Crear una única ventana
    root = tk.Tk()
    root.title("Restaurante App")
    root.geometry("760x680")
    root.resizable(False, False)

    # Ícono de la aplicación
    try:
        icono = tk.PhotoImage(file=ruta_logo)
        root.iconphoto(True, icono)
    except tk.TclError:
        pass

    def mostrar_login():
        for widget in root.winfo_children():
            widget.destroy()

        LoginView(
            root,
            servicio,
            mostrar_principal
        )

    def mostrar_principal(usuario):
        for widget in root.winfo_children():
            widget.destroy()

        MainView(
            root,
            servicio,
            mostrar_login,
            usuario
        )

    mostrar_login()

    root.mainloop()


if __name__ == "__main__":
    iniciar_aplicacion()