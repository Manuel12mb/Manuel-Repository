import os  # MEJORA: Importado para verificar si el archivo existe antes de leerlo
from modelos import Producto


class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.productos = []
        self.archivo = archivo
        #Carga automática de datos al instanciar la clase
        self.cargar_desde_archivo()

    def guardar_en_archivo(self):
        """CAMBIO: Nueva función para persistencia de datos ."""
        try:
            with open(self.archivo, 'w', encoding='utf-8') as f:
                for p in self.productos:
                    # Formateamos los datos como CSV simple (valores separados por coma)
                    f.write(f"{p.id},{p.nombre},{p.cantidad},{p.precio}\n")
            return True, "Sincronizado con disco."
        except PermissionError:  # Manejo de error de permisos
            return False, "Error de permisos: No se pudo escribir en el archivo."
        except Exception as e:
            return False, f"Error inesperado al guardar: {e}"

    def cargar_desde_archivo(self):
        """CAMBIO: Nueva función para reconstruir el inventario ."""
        # Verificar si el archivo existe; si no, crearlo vacío
        if not os.path.exists(self.archivo):
            try:
                open(self.archivo, 'w').close()
                return
            except Exception as e:
                print(f"No se pudo crear el archivo: {e}")
                return

        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                self.productos = []  # Limpiamos para evitar duplicados al recargar
                for linea in f:
                    # Parseo de línea y reconstrucción del objeto Producto
                    datos = linea.strip().split(',')
                    if len(datos) == 4:
                        id_p, nom, cant, pre = int(datos[0]), datos[1], int(datos[2]), float(datos[3])
                        self.productos.append(Producto(id_p, nom, cant, pre))
        except FileNotFoundError:  #Captura específica de archivo no encontrado
            print("Archivo no encontrado. Se iniciará con inventario vacío.")
        except ValueError:  # MEJORA: Maneja errores si el archivo de texto está corrupto
            print("Error: El archivo contiene datos con formato inválido.")

    def añadir_producto(self, producto):
        if any(p.id == producto.id for p in self.productos):
            return False, "Error: El ID ya existe."

        self.productos.append(producto)
        # MEJORA: Cada cambio se refleja inmediatamente en el archivo
        return self.guardar_en_archivo()

    def eliminar_producto(self, id_buscar):
        for p in self.productos:
            if p.id == id_buscar:
                self.productos.remove(p)
                # MEJORA: Sincronización tras eliminar
                return self.guardar_en_archivo()
        return False, "Producto no encontrado."

    def actualizar_producto(self, id_buscar, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.id == id_buscar:
                if nueva_cantidad is not None: p.cantidad = nueva_cantidad
                if nuevo_precio is not None: p.precio = nuevo_precio
                # MEJORA: Sincronización tras actualizar
                return self.guardar_en_archivo()
        return False, "Producto no encontrado."

    def buscar_por_nombre(self, nombre_buscar):
        return [p for p in self.productos if nombre_buscar.lower() in p.nombre.lower()]

    def mostrar_inventario(self):
        return self.productos