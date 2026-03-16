class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        # Lista para almacenar los libros prestados actualmente
        self.libros_prestados = []

    def __str__(self):
        libros = ", ".join([l.info[0] for l in self.libros_prestados]) if self.libros_prestados else "Ninguno"
        return f"Usuario: {self.nombre} (ID: {self.user_id}) | Libros: {libros}"