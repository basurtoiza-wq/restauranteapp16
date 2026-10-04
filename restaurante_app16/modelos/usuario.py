class Usuario:
    def __init__(self, nombre, contrasena, rol="Cliente"):
        self.nombre = nombre
        self.contrasena = contrasena
        self.rol = rol

    def __str__(self):
        return self.nombre