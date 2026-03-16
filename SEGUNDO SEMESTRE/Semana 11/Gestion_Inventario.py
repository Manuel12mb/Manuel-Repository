import json  # Para serialización de datos (almacenamiento en archivos)
import os  # Para verificar la existencia del archivo de datos


# =================================================================
# 1. CLASE PRODUCTO: Representa la entidad individual del inventario
# =================================================================
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Constructor que inicializa los atributos básicos.
        Se usa el prefijo '__' para aplicar encapsulamiento (atributos privados).
        """
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # --- Métodos Getters (Para obtener datos de forma controlada) ---
    def get_id(self): return self.__id

    def get_nombre(self): return self.__nombre

    def get_cantidad(self): return self.__cantidad

    def get_precio(self): return self.__precio

    # --- Métodos Setters (Para modificar datos con seguridad) ---
    def set_cantidad(self, cantidad): self.__cantidad = cantidad

    def set_precio(self, precio): self.__precio = precio

    def to_dict(self):
        """
        Serialización: Convierte el objeto a un formato de diccionario.
        Esto es necesario para que el módulo 'json' pueda guardarlo en un archivo.
        """
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "cantidad": self.__cantidad,
            "precio": self.__precio
        }

    def __str__(self):
        """Representación en texto del objeto para el usuario final."""
        return f"ID: {self.__id:<5} | Producto: {self.__nombre:<15} | Stock: {self.__cantidad:<5} | Precio: ${self.__precio:.2f}"


# =================================================================
# 2. CLASE INVENTARIO: Gestiona la lógica y la colección de productos
# =================================================================
class Inventario:
    def __init__(self):
        """
        Inicializa el inventario. Se usa un DICCIONARIO para optimizar la búsqueda.
        La clave (key) será el ID y el valor (value) será el objeto Producto.
        """
        self.productos = {}  # Colección principal
        self.nombre_archivo = "inventario.json"
        self.cargar_desde_archivo()  # Carga automática al iniciar

    def añadir_producto(self, producto):
        """Verifica que el ID no se repita antes de añadir."""
        if producto.get_id() in self.productos:
            print(f"Error: El ID '{producto.get_id()}' ya está registrado.")
        else:
            self.productos[producto.get_id()] = producto
            self.guardar_en_archivo()
            print("Producto añadido con éxito.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto de la colección usando su ID."""
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
            print(f"Producto {id_producto} eliminado del sistema.")
        else:
            print("Error: No se encontró un producto con ese ID.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """Actualiza selectivamente los atributos de un producto."""
        if id_producto in self.productos:
            if nueva_cantidad is not None:
                self.productos[id_producto].set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                self.productos[id_producto].set_precio(nuevo_precio)
            self.guardar_en_archivo()
            print("Datos actualizados correctamente.")
        else:
            print("Error: Producto no localizado.")

    def buscar_por_nombre(self, nombre):
        """Busca coincidencias parciales en los nombres de los productos."""
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            print("\n--- Resultados de búsqueda ---")
            for p in encontrados: print(p)
        else:
            print(f"No hay coincidencias para: '{nombre}'")

    def mostrar_todo(self):
        """Muestra todos los productos almacenados en el diccionario."""
        if not self.productos:
            print("\nEl inventario está actualmente vacío.")
        else:
            print("\n" + "=" * 55)
            print("LISTADO TOTAL DE PRODUCTOS")
            print("=" * 55)
            for p in self.productos.values():
                print(p)

    # --- Persistencia en Archivos ---
    def guardar_en_archivo(self):
        """Guarda la colección completa en el disco duro en formato JSON."""
        try:
            with open(self.nombre_archivo, 'w') as f:
                # Generamos una estructura de datos plana (diccionarios) para el archivo
                datos_para_guardar = {id_p: p.to_dict() for id_p, p in self.productos.items()}
                json.dump(datos_para_guardar, f, indent=4)
        except Exception as e:
            print(f"Error crítico al guardar: {e}")

    def cargar_desde_archivo(self):
        """Deserializa el archivo y reconstruye los objetos de la clase Producto."""
        if os.path.exists(self.nombre_archivo):
            try:
                with open(self.nombre_archivo, 'r') as f:
                    datos = json.load(f)
                    for d in datos.values():
                        # Recreamos la instancia de Producto con los datos guardados
                        p = Producto(d['id'], d['nombre'], d['cantidad'], d['precio'])
                        self.productos[p.get_id()] = p
            except Exception:
                print("Nota: El archivo de datos está vacío o corrupto. Iniciando nuevo.")


# =================================================================
# 3. INTERFAZ DE USUARIO (MENÚ)
# =================================================================
def menu_principal():
    sistema = Inventario()

    while True:
        print("\n>>> MENÚ DE GESTIÓN DE INVENTARIO <<<")
        print("1. [Añadir] Nuevo producto")
        print("2. [Eliminar] Producto por ID")
        print("3. [Actualizar] Cantidad o Precio")
        print("4. [Buscar] Por nombre")
        print("5. [Listar] Todo el inventario")
        print("6. [Salir] Cerrar programa")

        opcion = input("\nSeleccione una opción (1-6): ")

        if opcion == "1":
            try:
                id_p = input("ID único: ")
                nom = input("Nombre: ")
                cant = int(input("Stock inicial: "))
                prec = float(input("Precio unitario: "))
                sistema.añadir_producto(Producto(id_p, nom, cant, prec))
            except ValueError:
                print("Error: Ingrese valores numéricos válidos para Stock y Precio.")

        elif opcion == "2":
            id_p = input("ID del producto a remover: ")
            sistema.eliminar_producto(id_p)

        elif opcion == "3":
            id_p = input("ID del producto: ")
            print("(Deje en blanco para mantener el valor actual)")
            c = input("Nueva cantidad: ")
            p = input("Nuevo precio: ")
            # Convertimos solo si el usuario escribió algo
            cant = int(c) if c.strip() else None
            prec = float(p) if p.strip() else None
            sistema.actualizar_producto(id_p, cant, prec)

        elif opcion == "4":
            nom = input("Ingrese nombre a buscar: ")
            sistema.buscar_por_nombre(nom)

        elif opcion == "5":
            sistema.mostrar_todo()

        elif opcion == "6":
            print("Guardando cambios... Saliendo del sistema.")
            break
        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    menu_principal()