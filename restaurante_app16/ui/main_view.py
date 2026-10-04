import os
import tkinter as tk
from tkinter import ttk, messagebox


class MainView:

    def __init__(self, root, servicio, cerrar_sesion, usuario):
        self.root = root
        self.servicio = servicio
        self.cerrar_sesion = cerrar_sesion
        self.usuario_actual = usuario

        base_dir = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

        self.ruta_logo = os.path.join(
            base_dir,
            "assets",
            "logo.png"
        )

        # ==================================================
        # CONTENEDOR CON SCROLL
        # ==================================================

        contenedor_scroll = tk.Frame(
            root,
            bg="#FFF8F0"
        )
        contenedor_scroll.pack(
            fill="both",
            expand=True
        )

        canvas = tk.Canvas(
            contenedor_scroll,
            bg="#FFF8F0",
            highlightthickness=0
        )

        scrollbar = ttk.Scrollbar(
            contenedor_scroll,
            orient="vertical",
            command=canvas.yview
        )

        canvas.configure(
            yscrollcommand=scrollbar.set
        )

        self.frame = tk.Frame(
            canvas,
            bg="#FFF8F0"
        )

        canvas.create_window(
            (0, 0),
            window=self.frame,
            anchor="nw"
        )

        self.frame.bind(
            "<Configure>",
            lambda event: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        # ==================================================
        # ENCABEZADO
        # ==================================================

        encabezado = tk.Frame(
            self.frame,
            bg="#FFF8F0"
        )

        encabezado.pack(
            pady=(20, 5)
        )

        try:
            self.logo_img = tk.PhotoImage(
                file=self.ruta_logo
            ).subsample(4, 4)

            tk.Label(
                encabezado,
                image=self.logo_img,
                bg="#FFF8F0"
            ).pack(
                side="left",
                padx=(0, 10)
            )

        except tk.TclError:
            pass

        titulos = tk.Frame(
            encabezado,
            bg="#FFF8F0"
        )

        titulos.pack(
            side="left"
        )

        tk.Label(
            titulos,
            text="RESTAURANTE APP",
            font=("Arial", 22, "bold"),
            bg="#FFF8F0",
            fg="#8B4513"
        ).pack(
            anchor="w"
        )

        tk.Label(
            titulos,
            text="Gestión de productos, ventas y usuarios",
            font=("Arial", 13),
            bg="#FFF8F0",
            fg="#555555"
        ).pack(
            anchor="w"
        )

        tk.Label(
            titulos,
            text=(
                f"Sesión: {self.usuario_actual.nombre} "
                f"({self.usuario_actual.rol})"
            ),
            font=("Arial", 10, "italic"),
            bg="#FFF8F0",
            fg="#6B4F3A"
        ).pack(
            anchor="w"
        )

        # ==================================================
        # CONTENIDO
        # ==================================================

        contenido = tk.Frame(
            self.frame,
            bg="#FFF8F0"
        )

        contenido.pack(
            fill="both",
            expand=True,
            padx=25
        )

        # ==================================================
        # PRODUCTOS
        # ==================================================

        formulario = tk.LabelFrame(
            contenido,
            text="Información del producto",
            font=("Arial", 11, "bold"),
            bg="#FFF8F0",
            fg="#8B4513",
            padx=10,
            pady=10
        )

        formulario.pack(
            fill="x",
            pady=5
        )

        tk.Label(
            formulario,
            text="Nombre:",
            bg="#FFF8F0"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        self.nombre_entry = tk.Entry(
            formulario,
            width=25
        )

        self.nombre_entry.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        tk.Label(
            formulario,
            text="Precio:",
            bg="#FFF8F0"
        ).grid(
            row=0,
            column=2,
            padx=5,
            pady=5
        )

        self.precio_entry = tk.Entry(
            formulario,
            width=15
        )

        self.precio_entry.grid(
            row=0,
            column=3,
            padx=5,
            pady=5
        )

        tk.Label(
            formulario,
            text="Cantidad:",
            bg="#FFF8F0"
        ).grid(
            row=0,
            column=4,
            padx=5,
            pady=5
        )

        self.cantidad_entry = tk.Entry(
            formulario,
            width=15
        )

        self.cantidad_entry.grid(
            row=0,
            column=5,
            padx=5,
            pady=5
        )

        botones = tk.Frame(
            contenido,
            bg="#FFF8F0"
        )

        botones.pack(
            pady=10
        )

        tk.Button(
            botones,
            text="➕ Registrar",
            command=self.registrar_producto,
            bg="#D2691E",
            fg="white",
            font=("Arial", 10, "bold"),
            width=14,
            relief="flat"
        ).grid(
            row=0,
            column=0,
            padx=4
        )

        tk.Button(
            botones,
            text="🔎 Consultar",
            command=self.consultar_producto,
            bg="#A0522D",
            fg="white",
            font=("Arial", 10, "bold"),
            width=14,
            relief="flat"
        ).grid(
            row=0,
            column=1,
            padx=4
        )

        tk.Button(
            botones,
            text="✏️ Actualizar",
            command=self.actualizar_producto,
            bg="#CD853F",
            fg="white",
            font=("Arial", 10, "bold"),
            width=14,
            relief="flat"
        ).grid(
            row=0,
            column=2,
            padx=4
        )

        tk.Button(
            botones,
            text="🗑️ Eliminar",
            command=self.eliminar_producto,
            bg="#8B0000",
            fg="white",
            font=("Arial", 10, "bold"),
            width=14,
            relief="flat"
        ).grid(
            row=0,
            column=3,
            padx=4
        )

        # ==================================================
        # TABLA DE PRODUCTOS
        # ==================================================

        tabla_frame = tk.LabelFrame(
            contenido,
            text="Productos registrados",
            font=("Arial", 11, "bold"),
            bg="#FFF8F0",
            fg="#8B4513"
        )

        tabla_frame.pack(
            fill="both",
            expand=True,
            pady=5
        )

        columnas = (
            "nombre",
            "precio",
            "cantidad"
        )

        self.tabla = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings",
            height=6
        )

        self.tabla.heading(
            "nombre",
            text="Producto"
        )

        self.tabla.heading(
            "precio",
            text="Precio"
        )

        self.tabla.heading(
            "cantidad",
            text="Cantidad"
        )

        self.tabla.column(
            "nombre",
            width=300,
            anchor="center"
        )

        self.tabla.column(
            "precio",
            width=150,
            anchor="center"
        )

        self.tabla.column(
            "cantidad",
            width=150,
            anchor="center"
        )

        self.tabla.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        # ==================================================
        # VENTAS
        # ==================================================

        ventas_frame = tk.LabelFrame(
            contenido,
            text="🧾 Registro de ventas",
            font=("Arial", 11, "bold"),
            bg="#FFF8F0",
            fg="#8B4513",
            padx=10,
            pady=10
        )

        ventas_frame.pack(
            fill="x",
            pady=(15, 5)
        )

        tk.Label(
            ventas_frame,
            text="Usuario:",
            bg="#FFF8F0"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        self.usuario_combo = ttk.Combobox(
            ventas_frame,
            values=[
                usuario.nombre
                for usuario in self.servicio.listar_usuarios()
            ],
            state="readonly",
            width=22
        )

        self.usuario_combo.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        tk.Label(
            ventas_frame,
            text="Producto:",
            bg="#FFF8F0"
        ).grid(
            row=0,
            column=2,
            padx=5,
            pady=5
        )

        self.producto_combo = ttk.Combobox(
            ventas_frame,
            values=[
                producto.nombre
                for producto in self.servicio.listar_productos()
            ],
            state="readonly",
            width=22
        )

        self.producto_combo.grid(
            row=0,
            column=3,
            padx=5,
            pady=5
        )

        tk.Button(
            ventas_frame,
            text="🧾 Registrar venta",
            command=self.registrar_venta_callback,
            bg="#D2691E",
            fg="white",
            font=("Arial", 10, "bold"),
            width=18,
            relief="flat"
        ).grid(
            row=0,
            column=4,
            padx=10
        )

        # ==================================================
        # TABLA DE VENTAS
        # ==================================================

        ventas_tabla_frame = tk.LabelFrame(
            contenido,
            text="Ventas registradas",
            font=("Arial", 11, "bold"),
            bg="#FFF8F0",
            fg="#8B4513"
        )

        ventas_tabla_frame.pack(
            fill="both",
            expand=True,
            pady=5
        )

        columnas_venta = (
            "usuario",
            "producto",
            "fecha"
        )

        self.ventas_tabla = ttk.Treeview(
            ventas_tabla_frame,
            columns=columnas_venta,
            show="headings",
            height=6
        )

        self.ventas_tabla.heading(
            "usuario",
            text="Usuario"
        )

        self.ventas_tabla.heading(
            "producto",
            text="Producto"
        )

        self.ventas_tabla.heading(
            "fecha",
            text="Fecha"
        )

        self.ventas_tabla.column(
            "usuario",
            width=200,
            anchor="center"
        )

        self.ventas_tabla.column(
            "producto",
            width=200,
            anchor="center"
        )

        self.ventas_tabla.column(
            "fecha",
            width=200,
            anchor="center"
        )

        self.ventas_tabla.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        # ==================================================
        # USUARIOS
        # SOLO ADMINISTRADOR
        # ==================================================

        if self.usuario_actual.rol == "Administrador":
            self.crear_seccion_usuarios(contenido)

        # ==================================================
        # CERRAR SESIÓN
        # ==================================================

        tk.Button(
            contenido,
            text="Cerrar sesión",
            command=self.cerrar_sesion,
            bg="#555555",
            fg="white",
            font=("Arial", 10, "bold"),
            width=18,
            relief="flat"
        ).pack(
            pady=(10, 15)
        )

        # Cargar datos
        self.cargar_tabla()
        self.cargar_tabla_ventas()

    # ==================================================
    # GESTIÓN DE USUARIOS
    # ==================================================

    def crear_seccion_usuarios(self, contenido):

        usuarios_frame = tk.LabelFrame(
            contenido,
            text="👥 Gestión de usuarios - Administrador",
            font=("Arial", 11, "bold"),
            bg="#FFF8F0",
            fg="#8B4513",
            padx=10,
            pady=10
        )

        usuarios_frame.pack(
            fill="both",
            expand=True,
            pady=(15, 5)
        )

        # ------------------------------
        # NOMBRE
        # ------------------------------

        tk.Label(
            usuarios_frame,
            text="Nombre:",
            bg="#FFF8F0"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        self.usuario_nombre_entry = tk.Entry(
            usuarios_frame,
            width=22
        )

        self.usuario_nombre_entry.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        # ------------------------------
        # CONTRASEÑA
        # ------------------------------

        tk.Label(
            usuarios_frame,
            text="Contraseña:",
            bg="#FFF8F0"
        ).grid(
            row=0,
            column=2,
            padx=5,
            pady=5
        )

        self.usuario_contrasena_entry = tk.Entry(
            usuarios_frame,
            width=22,
            show="*"
        )

        self.usuario_contrasena_entry.grid(
            row=0,
            column=3,
            padx=5,
            pady=5
        )

        # ------------------------------
        # ROL
        # ------------------------------

        tk.Label(
            usuarios_frame,
            text="Rol:",
            bg="#FFF8F0"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5
        )

        self.rol_combo = ttk.Combobox(
            usuarios_frame,
            values=[
                "Administrador",
                "Empleado",
                "Cliente"
            ],
            state="readonly",
            width=20
        )

        self.rol_combo.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

        # Evento <<ComboboxSelected>>
        self.rol_combo.bind(
            "<<ComboboxSelected>>",
            self.cambio_rol
        )

        # ------------------------------
        # BOTONES
        # ------------------------------

        botones_usuario = tk.Frame(
            usuarios_frame,
            bg="#FFF8F0"
        )

        botones_usuario.grid(
            row=1,
            column=2,
            columnspan=2,
            padx=5,
            pady=5
        )

        tk.Button(
            botones_usuario,
            text="➕ Registrar",
            command=self.registrar_usuario,
            bg="#D2691E",
            fg="white",
            font=("Arial", 9, "bold"),
            width=12,
            relief="flat"
        ).grid(
            row=0,
            column=0,
            padx=3
        )

        tk.Button(
            botones_usuario,
            text="✏️ Actualizar",
            command=self.actualizar_usuario,
            bg="#CD853F",
            fg="white",
            font=("Arial", 9, "bold"),
            width=12,
            relief="flat"
        ).grid(
            row=0,
            column=1,
            padx=3
        )

        tk.Button(
            botones_usuario,
            text="🗑️ Eliminar",
            command=self.eliminar_usuario,
            bg="#8B0000",
            fg="white",
            font=("Arial", 9, "bold"),
            width=12,
            relief="flat"
        ).grid(
            row=0,
            column=2,
            padx=3
        )

        tk.Button(
            botones_usuario,
            text="🧹 Limpiar",
            command=self.limpiar_usuario_formulario,
            bg="#555555",
            fg="white",
            font=("Arial", 9, "bold"),
            width=12,
            relief="flat"
        ).grid(
            row=0,
            column=3,
            padx=3
        )

        # ------------------------------
        # TABLA TREEVIEW
        # ------------------------------

        tabla_usuarios_frame = tk.Frame(
            usuarios_frame,
            bg="#FFF8F0"
        )

        tabla_usuarios_frame.grid(
            row=2,
            column=0,
            columnspan=4,
            sticky="nsew",
            padx=5,
            pady=10
        )

        columnas_usuario = (
            "nombre",
            "usuario",
            "rol"
        )

        self.usuarios_tabla = ttk.Treeview(
            tabla_usuarios_frame,
            columns=columnas_usuario,
            show="headings",
            height=6,
            selectmode="browse"
        )

        self.usuarios_tabla.heading(
            "nombre",
            text="Nombre"
        )

        self.usuarios_tabla.heading(
            "usuario",
            text="Usuario"
        )

        self.usuarios_tabla.heading(
            "rol",
            text="Rol"
        )

        self.usuarios_tabla.column(
            "nombre",
            width=200,
            anchor="center"
        )

        self.usuarios_tabla.column(
            "usuario",
            width=180,
            anchor="center"
        )

        self.usuarios_tabla.column(
            "rol",
            width=150,
            anchor="center"
        )

        self.usuarios_tabla.pack(
            fill="both",
            expand=True
        )

        # ==================================================
        # EVENTO <<TreeviewSelect>>
        # ==================================================

        self.usuarios_tabla.bind(
            "<<TreeviewSelect>>",
            self.seleccionar_usuario
        )

        # ==================================================
        # EVENTO <Return>
        # ==================================================

        self.usuario_nombre_entry.bind(
            "<Return>",
            self.registrar_usuario_enter
        )

        self.usuario_contrasena_entry.bind(
            "<Return>",
            self.registrar_usuario_enter
        )

        self.rol_combo.bind(
            "<Return>",
            self.registrar_usuario_enter
        )

        # ==================================================
        # EVENTO <Escape>
        # ==================================================

        self.root.bind(
            "<Escape>",
            self.escape_usuario
        )

        self.cargar_tabla_usuarios()

        self.rol_combo.set(
            "Cliente"
        )

    # ==================================================
    # <<TreeviewSelect>>
    # ==================================================

    def seleccionar_usuario(self, event):

        seleccion = self.usuarios_tabla.selection()

        if not seleccion:
            return

        item = seleccion[0]

        valores = self.usuarios_tabla.item(
            item,
            "values"
        )

        if not valores:
            return

        nombre = valores[0]

        usuario = self.servicio.buscar_usuario(
            nombre
        )

        if usuario is None:
            return

        self.usuario_nombre_entry.delete(
            0,
            tk.END
        )

        self.usuario_nombre_entry.insert(
            0,
            usuario.nombre
        )

        self.usuario_contrasena_entry.delete(
            0,
            tk.END
        )

        self.usuario_contrasena_entry.insert(
            0,
            usuario.contrasena
        )

        self.rol_combo.set(
            usuario.rol
        )

    # ==================================================
    # <Return>
    # ==================================================

    def registrar_usuario_enter(self, event):
        self.registrar_usuario()

    # ==================================================
    # <Escape>
    # ==================================================

    def escape_usuario(self, event):
        if hasattr(
            self,
            "usuario_nombre_entry"
        ):
            self.limpiar_usuario_formulario()

    # ==================================================
    # <<ComboboxSelected>>
    # ==================================================

    def cambio_rol(self, event):

        rol = self.rol_combo.get()

        if rol:
            self.root.title(
                f"Restaurante App - Rol seleccionado: {rol}"
            )

    # ==================================================
    # REGISTRAR USUARIO
    # ==================================================

    def registrar_usuario(self):

        nombre = (
            self.usuario_nombre_entry
            .get()
            .strip()
        )

        contrasena = (
            self.usuario_contrasena_entry
            .get()
            .strip()
        )

        rol = (
            self.rol_combo
            .get()
            .strip()
        )

        if not nombre or not contrasena or not rol:
            messagebox.showwarning(
                "Datos incompletos",
                "Complete todos los campos del usuario."
            )
            return

        if self.servicio.buscar_usuario(nombre) is not None:
            messagebox.showwarning(
                "Usuario existente",
                "Ya existe un usuario con ese nombre."
            )
            return

        registrado = self.servicio.registrar_usuario(
            nombre,
            contrasena,
            rol
        )

        if registrado:

            self.cargar_tabla_usuarios()
            self.actualizar_combo_usuarios()
            self.limpiar_usuario_formulario()

            messagebox.showinfo(
                "Registro exitoso",
                "Usuario registrado correctamente."
            )

        else:

            messagebox.showerror(
                "Error",
                "No se pudo registrar el usuario."
            )

    # ==================================================
    # ACTUALIZAR USUARIO
    # ==================================================

    def actualizar_usuario(self):

        seleccion = self.usuarios_tabla.selection()

        if not seleccion:
            messagebox.showwarning(
                "Selección requerida",
                "Seleccione un usuario para actualizar."
            )
            return

        item = seleccion[0]

        valores = self.usuarios_tabla.item(
            item,
            "values"
        )

        nombre_original = valores[0]

        nuevo_nombre = (
            self.usuario_nombre_entry
            .get()
            .strip()
        )

        nueva_contrasena = (
            self.usuario_contrasena_entry
            .get()
            .strip()
        )

        nuevo_rol = (
            self.rol_combo
            .get()
            .strip()
        )

        if (
            not nuevo_nombre
            or not nueva_contrasena
            or not nuevo_rol
        ):
            messagebox.showwarning(
                "Datos incompletos",
                "Complete todos los campos."
            )
            return

        if nuevo_nombre != nombre_original:

            usuario_existente = (
                self.servicio.buscar_usuario(
                    nuevo_nombre
                )
            )

            if usuario_existente is not None:
                messagebox.showwarning(
                    "Usuario existente",
                    "Ya existe otro usuario con ese nombre."
                )
                return

        actualizado = (
            self.servicio.actualizar_usuario(
                nombre_original,
                nuevo_nombre,
                nueva_contrasena,
                nuevo_rol
            )
        )

        if actualizado:

            self.cargar_tabla_usuarios()
            self.actualizar_combo_usuarios()
            self.limpiar_usuario_formulario()

            messagebox.showinfo(
                "Actualización exitosa",
                "Usuario actualizado correctamente."
            )

        else:

            messagebox.showerror(
                "Error",
                "No se pudo actualizar el usuario."
            )

    # ==================================================
    # ELIMINAR USUARIO
    # ==================================================

    def eliminar_usuario(self):

        seleccion = self.usuarios_tabla.selection()

        if not seleccion:
            messagebox.showwarning(
                "Selección requerida",
                "Seleccione un usuario para eliminar."
            )
            return

        item = seleccion[0]

        valores = self.usuarios_tabla.item(
            item,
            "values"
        )

        nombre = valores[0]

        # No permitir eliminar la cuenta actual
        if nombre == self.usuario_actual.nombre:

            messagebox.showwarning(
                "Operación no permitida",
                "No puede eliminar la cuenta administrativa "
                "actualmente autenticada."
            )

            return

        usuario = self.servicio.buscar_usuario(
            nombre
        )

        if usuario is None:
            messagebox.showerror(
                "Error",
                "El usuario seleccionado no existe."
            )
            return

        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Desea eliminar al usuario '{nombre}'?"
        )

        if not confirmar:
            return

        eliminado = self.servicio.eliminar_usuario(
            nombre
        )

        if eliminado:

            self.cargar_tabla_usuarios()
            self.actualizar_combo_usuarios()
            self.limpiar_usuario_formulario()

            messagebox.showinfo(
                "Eliminación exitosa",
                "Usuario eliminado correctamente."
            )

        else:

            messagebox.showerror(
                "Error",
                "No se pudo eliminar el usuario."
            )

    # ==================================================
    # LIMPIAR USUARIO
    # ==================================================

    def limpiar_usuario_formulario(self):

        self.usuario_nombre_entry.delete(
            0,
            tk.END
        )

        self.usuario_contrasena_entry.delete(
            0,
            tk.END
        )

        self.rol_combo.set(
            "Cliente"
        )

        seleccion = (
            self.usuarios_tabla.selection()
        )

        if seleccion:
            self.usuarios_tabla.selection_remove(
                seleccion
            )

        self.usuarios_tabla.focus("")

    # ==================================================
    # CARGAR TABLA DE USUARIOS
    # ==================================================

    def cargar_tabla_usuarios(self):

        for item in self.usuarios_tabla.get_children():
            self.usuarios_tabla.delete(item)

        for usuario in self.servicio.listar_usuarios():

            self.usuarios_tabla.insert(
                "",
                "end",
                values=(
                    usuario.nombre,
                    usuario.nombre,
                    usuario.rol
                )
            )

    # ==================================================
    # PRODUCTOS
    # ==================================================

    def cargar_tabla(self):

        for item in self.tabla.get_children():
            self.tabla.delete(item)

        for producto in self.servicio.listar_productos():

            self.tabla.insert(
                "",
                "end",
                values=(
                    producto.nombre,
                    f"${producto.precio:.2f}",
                    producto.cantidad
                )
            )

    def limpiar_formulario(self):

        self.nombre_entry.delete(
            0,
            tk.END
        )

        self.precio_entry.delete(
            0,
            tk.END
        )

        self.cantidad_entry.delete(
            0,
            tk.END
        )

    def registrar_producto(self):

        nombre = self.nombre_entry.get().strip()
        precio = self.precio_entry.get().strip()
        cantidad = self.cantidad_entry.get().strip()

        if not nombre or not precio or not cantidad:

            messagebox.showwarning(
                "Datos incompletos",
                "Complete todos los campos."
            )

            return

        try:

            float(precio)
            int(cantidad)

        except ValueError:

            messagebox.showerror(
                "Datos inválidos",
                "Precio y cantidad deben ser valores numéricos."
            )

            return

        if self.servicio.consultar_producto(nombre):

            messagebox.showwarning(
                "Producto existente",
                "Ya existe un producto con ese nombre."
            )

            return

        self.servicio.registrar_producto(
            nombre,
            precio,
            cantidad
        )

        self.cargar_tabla()
        self.limpiar_formulario()
        self.actualizar_combo_productos()

        messagebox.showinfo(
            "Registro exitoso",
            "Producto registrado correctamente."
        )

    def consultar_producto(self):

        nombre = self.nombre_entry.get().strip()

        if not nombre:

            messagebox.showwarning(
                "Dato faltante",
                "Ingrese el nombre del producto."
            )

            return

        producto = self.servicio.consultar_producto(
            nombre
        )

        if producto is None:

            messagebox.showerror(
                "No encontrado",
                "El producto no existe."
            )

            return

        self.precio_entry.delete(
            0,
            tk.END
        )

        self.precio_entry.insert(
            0,
            str(producto.precio)
        )

        self.cantidad_entry.delete(
            0,
            tk.END
        )

        self.cantidad_entry.insert(
            0,
            str(producto.cantidad)
        )

    def actualizar_producto(self):

        nombre_original = (
            self.nombre_entry
            .get()
            .strip()
        )

        nuevo_nombre = (
            self.nombre_entry
            .get()
            .strip()
        )

        nuevo_precio = (
            self.precio_entry
            .get()
            .strip()
        )

        nueva_cantidad = (
            self.cantidad_entry
            .get()
            .strip()
        )

        if (
            not nombre_original
            or not nuevo_precio
            or not nueva_cantidad
        ):

            messagebox.showwarning(
                "Datos incompletos",
                "Complete todos los campos."
            )

            return

        try:

            float(nuevo_precio)
            int(nueva_cantidad)

        except ValueError:

            messagebox.showerror(
                "Datos inválidos",
                "Precio y cantidad deben ser valores numéricos."
            )

            return

        actualizado = (
            self.servicio.actualizar_producto(
                nombre_original,
                nuevo_nombre,
                nuevo_precio,
                nueva_cantidad
            )
        )

        if actualizado:

            self.cargar_tabla()
            self.actualizar_combo_productos()

            messagebox.showinfo(
                "Actualización exitosa",
                "Producto actualizado correctamente."
            )

        else:

            messagebox.showerror(
                "Error",
                "El producto no existe."
            )

    def eliminar_producto(self):

        nombre = self.nombre_entry.get().strip()

        if not nombre:

            messagebox.showwarning(
                "Dato faltante",
                "Ingrese el nombre del producto."
            )

            return

        producto = self.servicio.consultar_producto(
            nombre
        )

        if producto is None:

            messagebox.showerror(
                "No encontrado",
                "El producto no existe."
            )

            return

        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Desea eliminar '{producto.nombre}'?"
        )

        if not confirmar:
            return

        eliminado = self.servicio.eliminar_producto(
            nombre
        )

        if eliminado:

            self.cargar_tabla()
            self.limpiar_formulario()
            self.actualizar_combo_productos()

            messagebox.showinfo(
                "Eliminación exitosa",
                "Producto eliminado correctamente."
            )

    # ==================================================
    # VENTAS
    # ==================================================

    def cargar_tabla_ventas(self):

        for item in self.ventas_tabla.get_children():
            self.ventas_tabla.delete(item)

        for venta in self.servicio.listar_ventas():

            self.ventas_tabla.insert(
                "",
                "end",
                values=(
                    venta.usuario,
                    venta.producto,
                    venta.fecha
                )
            )

    def actualizar_combo_productos(self):

        self.producto_combo["values"] = [
            producto.nombre
            for producto in self.servicio.listar_productos()
        ]

    def actualizar_combo_usuarios(self):

        self.usuario_combo["values"] = [
            usuario.nombre
            for usuario in self.servicio.listar_usuarios()
        ]

    def registrar_venta_callback(self):

        usuario_seleccionado = (
            self.usuario_combo
            .get()
            .strip()
        )

        producto_seleccionado = (
            self.producto_combo
            .get()
            .strip()
        )

        if (
            not usuario_seleccionado
            or not producto_seleccionado
        ):

            messagebox.showwarning(
                "Datos incompletos",
                "Seleccione un usuario y un producto "
                "para registrar la venta."
            )

            return

        registrada = self.servicio.registrar_venta(
            usuario_seleccionado,
            producto_seleccionado
        )

        if registrada:

            self.cargar_tabla_ventas()

            self.usuario_combo.set("")
            self.producto_combo.set("")

            messagebox.showinfo(
                "Venta registrada",
                "La venta se registró correctamente."
            )

        else:

            messagebox.showerror(
                "Error al registrar",
                "El usuario o el producto seleccionado "
                "no existen."
            )
