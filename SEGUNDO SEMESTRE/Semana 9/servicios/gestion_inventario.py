from modelos.producto import Producto


class Inventario:
    def __init__(self):
        # Estructura principal: Una lista vacía para almacenar objetos de tipo Producto
        self.productos = []

    def añadir_producto(self, producto):
        # Usamos una "list comprehension" para revisar si el ID ya existe en la lista
        if any(p.id == producto.id for p in self.productos):
            return False, f"Error: Ya existe un producto con el ID {producto.id}."

        # Si el ID es único, lo agregamos a la lista
        self.productos.append(producto)
        return True, "Producto añadido con éxito."

    def eliminar_producto(self, id_buscar):
        # Recorremos la lista buscando el objeto con el ID coincidente
        for p in self.productos:
            if p.id == id_buscar:
                self.productos.remove(p)  # Eliminamos el objeto de la lista
                return True, "Producto eliminado."
        return False, "Producto no encontrado."

    def actualizar_producto(self, id_buscar, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.id == id_buscar:
                # Solo actualizamos si el usuario envió un valor (no es None)
                if nueva_cantidad is not None: p.cantidad = nueva_cantidad
                if nuevo_precio is not None: p.precio = nuevo_precio
                return True, "Producto actualizado correctamente."
        return False, "Producto no encontrado."

    def buscar_por_nombre(self, nombre_buscar):
        # Filtramos la lista: buscamos el texto dentro del nombre (case-insensitive)
        resultados = [p for p in self.productos if nombre_buscar.lower() in p.nombre.lower()]
        return resultados

    def mostrar_inventario(self):
        # Retornamos la lista completa para ser iterada en el main
        return self.productos