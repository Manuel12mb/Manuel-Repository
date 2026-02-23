class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # El prefijo '__' convierte al atributo en privado (Encapsulamiento)
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Decorador @property: Permite acceder al método como si fuera un atributo (Getter)
    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @property
    def cantidad(self):
        return self.__cantidad

    @property
    def precio(self):
        return self.__precio

    # Decorador .setter: Permite modificar el valor con validaciones de seguridad
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @cantidad.setter
    def cantidad(self, valor):
        # Validación: No permitimos que el stock sea menor a cero
        if valor >= 0:
            self.__cantidad = valor
        else:
            print("Error: La cantidad no puede ser negativa.")

    @precio.setter
    def precio(self, valor):
        # Validación: Un precio no puede ser negativo
        if valor >= 0:
            self.__precio = valor
        else:
            print("Error: El precio no puede ser negativo.")

    def __str__(self):
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}"