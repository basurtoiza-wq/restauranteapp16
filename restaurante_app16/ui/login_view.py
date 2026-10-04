import tkinter as tk
from tkinter import messagebox


class LoginView:

    def __init__(self, root, servicio, mostrar_principal):
        self.root = root
        self.servicio = servicio
        self.mostrar_principal = mostrar_principal

        self.frame = tk.Frame(root)
        self.frame.pack(pady=50)

        tk.Label(
            self.frame,
            text="Restaurante App",
            font=("Arial", 20)
        ).pack(pady=10)

        tk.Label(self.frame, text="Usuario").pack()
        self.usuario_entry = tk.Entry(self.frame)
        self.usuario_entry.pack(pady=5)

        tk.Label(self.frame, text="Contraseña").pack()
        self.contrasena_entry = tk.Entry(
            self.frame,
            show="*"
        )
        self.contrasena_entry.pack(pady=5)

        tk.Button(
            self.frame,
            text="Ingresar",
            command=self.iniciar_sesion
        ).pack(pady=15)

    def iniciar_sesion(self):
        nombre = self.usuario_entry.get().strip()
        contrasena = self.contrasena_entry.get().strip()

        if not nombre or not contrasena:
            messagebox.showwarning(
                "Campos vacíos",
                "Ingrese usuario y contraseña."
            )
            return

        usuario = self.servicio.obtener_usuario_autenticado(
            nombre,
            contrasena
        )

        if usuario is not None:
            self.frame.destroy()

            self.mostrar_principal(usuario)

        else:
            messagebox.showerror(
                "Acceso incorrecto",
                "Usuario o contraseña incorrectos."
            )