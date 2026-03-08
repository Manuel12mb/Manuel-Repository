class BibliotecaServicio:
    def __init__(self):
        # Diccionario: Clave ISBN (str) -> Valor Objeto Libro
        self.libros_disponibles = {}
        # Diccionario: Clave User_ID -> Valor Objeto Usuario
        self.usuarios_registrados = {}
        # Conjunto (set) para garantizar IDs de usuarios únicos
        self.ids_usuarios = set()

    def añadir_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro añadido: {libro.info[0]}")
        else:
            print("Error: El ISBN ya existe.")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            eliminado = self.libros_disponibles.pop(isbn)
            print(f"Libro '{eliminado.info[0]}' eliminado del sistema.")
        else:
            print("Error: Libro no encontrado.")

    def registrar_usuario(self, usuario):
        if usuario.user_id not in self.ids_usuarios:
            self.ids_usuarios.add(usuario.user_id)
            self.usuarios_registrados[usuario.user_id] = usuario
            print(f"Usuario '{usuario.nombre}' registrado con éxito.")
        else:
            print("Error: El ID de usuario ya está en uso.")

    def dar_de_baja_usuario(self, user_id):
        if user_id in self.usuarios_registrados:
            user = self.usuarios_registrados[user_id]
            if not user.libros_prestados:
                self.ids_usuarios.remove(user_id)
                del self.usuarios_registrados[user_id]
                print(f"Usuario con ID {user_id} eliminado.")
            else:
                print("Error: No se puede eliminar un usuario con libros pendientes.")
        else:
            print("Error: Usuario no encontrado.")

    def prestar_libro(self, isbn, user_id):
        if isbn in self.libros_disponibles and user_id in self.usuarios_registrados:
            libro = self.libros_disponibles.pop(isbn)
            self.usuarios_registrados[user_id].libros_prestados.append(libro)
            print(f"Libro '{libro.info[0]}' prestado a {self.usuarios_registrados[user_id].nombre}.")
        else:
            print("Error: ISBN o ID de usuario no válidos.")

    def devolver_libro(self, isbn, user_id):
        if user_id in self.usuarios_registrados:
            user = self.usuarios_registrados[user_id]
            for i, libro in enumerate(user.libros_prestados):
                if libro.isbn == isbn:
                    libro_devuelto = user.libros_prestados.pop(i)
                    self.libros_disponibles[isbn] = libro_devuelto
                    print(f"Libro '{libro_devuelto.info[0]}' devuelto correctamente.")
                    return
            print("Error: El usuario no tiene ese libro.")
        else:
            print("Error: Usuario no encontrado.")

    def buscar_libro(self, criterio, valor):
        # Buscamos en los valores del diccionario (objetos Libro)
        resultados = []
        valor = valor.lower()
        for libro in self.libros_disponibles.values():
            if (criterio == "titulo" and valor in libro.info[0].lower()) or \
               (criterio == "autor" and valor in libro.info[1].lower()) or \
               (criterio == "categoria" and valor in libro.categoria.lower()):
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, user_id):
        if user_id in self.usuarios_registrados:
            return self.usuarios_registrados[user_id].libros_prestados
        return None