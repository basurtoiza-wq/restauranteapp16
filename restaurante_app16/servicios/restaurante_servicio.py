from datetime import datetime

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class RestauranteServicio:

    def __init__(self, productos, usuarios, ventas, archivo_servicio,
                 ruta_productos, ruta_usuarios, ruta_ventas):

        self.productos = [
            Producto(
                producto["nombre"],
                producto["precio"],
                producto["cantidad"]
            )
            for producto in productos
        ]

        self.usuarios = [
            Usuario(
                usuario["nombre"],
                usuario["contrasena"],
                usuario.get("rol", "Cliente")
            )
            for usuario in usuarios
        ]

        self.ventas = [
            Venta(
                venta["usuario"],
                venta["producto"],
                venta["fecha"]
            )
            for venta in ventas
        ]

        self.archivo_servicio = archivo_servicio

        self.ruta_productos = ruta_productos
        self.ruta_usuarios = ruta_usuarios
        self.ruta_ventas = ruta_ventas

    # ==================================
    # USUARIOS
    # ==================================

    def validar_usuario(self, nombre, contrasena):
        for usuario in self.usuarios:
            if usuario.nombre == nombre and usuario.contrasena == contrasena:
                return True
        return False

    def obtener_usuario_autenticado(self, nombre, contrasena):
        for usuario in self.usuarios:
            if usuario.nombre == nombre and usuario.contrasena == contrasena:
                return usuario
        return None

    def listar_usuarios(self):
        return self.usuarios

    def buscar_usuario(self, nombre):
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                return usuario
        return None

    def registrar_usuario(self, nombre, contrasena, rol):
        if self.buscar_usuario(nombre) is not None:
            return False

        nuevo_usuario = Usuario(
            nombre,
            contrasena,
            rol
        )

        self.usuarios.append(nuevo_usuario)
        self.guardar_usuarios()

        return True

    def actualizar_usuario(self, nombre_original, nuevo_nombre,
                           nueva_contrasena, nuevo_rol):

        usuario = self.buscar_usuario(nombre_original)

        if usuario is None:
            return False

        usuario.nombre = nuevo_nombre
        usuario.contrasena = nueva_contrasena
        usuario.rol = nuevo_rol

        self.guardar_usuarios()

        return True

    def eliminar_usuario(self, nombre):
        usuario = self.buscar_usuario(nombre)

        if usuario is None:
            return False

        self.usuarios.remove(usuario)
        self.guardar_usuarios()

        return True

    def guardar_usuarios(self):
        datos = []

        for usuario in self.usuarios:
            datos.append({
                "nombre": usuario.nombre,
                "contrasena": usuario.contrasena,
                "rol": usuario.rol
            })

        self.archivo_servicio.guardar_datos(
            self.ruta_usuarios,
            datos
        )

    # ==================================
    # PRODUCTOS
    # ==================================

    def listar_productos(self):
        return self.productos

    def registrar_producto(self, nombre, precio, cantidad):
        nuevo_producto = Producto(
            nombre,
            float(precio),
            int(cantidad)
        )

        self.productos.append(nuevo_producto)
        self.guardar_productos()

    def consultar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto

        return None

    def actualizar_producto(self, nombre, nuevo_nombre,
                            nuevo_precio, nueva_cantidad):

        producto = self.consultar_producto(nombre)

        if producto is None:
            return False

        producto.nombre = nuevo_nombre
        producto.precio = float(nuevo_precio)
        producto.cantidad = int(nueva_cantidad)

        self.guardar_productos()
        return True

    def eliminar_producto(self, nombre):
        producto = self.consultar_producto(nombre)

        if producto is None:
            return False

        self.productos.remove(producto)
        self.guardar_productos()
        return True

    def guardar_productos(self):
        datos = []

        for producto in self.productos:
            datos.append({
                "nombre": producto.nombre,
                "precio": producto.precio,
                "cantidad": producto.cantidad
            })

        self.archivo_servicio.guardar_datos(
            self.ruta_productos,
            datos
        )

    # ==================================
    # VENTAS
    # ==================================

    def listar_ventas(self):
        return self.ventas

    def registrar_venta(self, nombre_usuario, nombre_producto):

        usuario = self.buscar_usuario(nombre_usuario)
        producto = self.consultar_producto(nombre_producto)

        if usuario is None or producto is None:
            return False

        fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

        nueva_venta = Venta(
            usuario.nombre,
            producto.nombre,
            fecha
        )

        self.ventas.append(nueva_venta)
        self.guardar_ventas()

        return True

    def guardar_ventas(self):
        datos = []

        for venta in self.ventas:
            datos.append({
                "usuario": venta.usuario,
                "producto": venta.producto,
                "fecha": venta.fecha
            })

        self.archivo_servicio.guardar_datos(
            self.ruta_ventas,
            datos
        )