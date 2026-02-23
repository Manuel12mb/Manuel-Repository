
from modelos.producto import Producto
from servicios.gestion_inventario import Inventario


def menu():
    mi_inventario = Inventario()

    while True:
        print("\n--- MENÚ DE INVENTARIO (SISTEMA DE ARCHIVOS) ---")
        print("1. Añadir | 2. Eliminar | 3. Actualizar | 4. Buscar | 5. Listar | 6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_p = int(input("ID: "))
                nom = input("Nombre: ")
                cant = int(input("Cantidad: "))
                pre = float(input("Precio: "))

                nuevo = Producto(id_p, nom, cant, pre)
                # REQUISITO 4: Notificar éxito o fallo de la operación de archivo
                exito, msg = mi_inventario.añadir_producto(nuevo)
                print(f"Resultado: {msg}")
            except ValueError:
                print("Error: Datos de entrada inválidos.")

        elif opcion == "2":
            try:
                id_p = int(input("ID a eliminar: "))
                exito, msg = mi_inventario.eliminar_producto(id_p)
                # REQUISITO 4: Feedback de eliminación y persistencia
                print(f"Resultado: {msg}")
            except ValueError:
                print("Error: El ID debe ser numérico.")

        elif opcion == "3":
            try:
                id_p = int(input("ID a actualizar: "))
                c_input = input("Nueva cantidad (Enter para omitir): ")
                p_input = input("Nuevo precio (Enter para omitir): ")

                cant = int(c_input) if c_input else None
                prec = float(p_input) if p_input else None

                exito, msg = mi_inventario.actualizar_producto(id_p, cant, prec)
                # REQUISITO 4: Feedback de actualización
                print(f"Resultado: {msg}")
            except ValueError:
                print("Error: Datos numéricos inválidos.")

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            resultados = mi_inventario.buscar_por_nombre(nombre)
            if resultados:
                for r in resultados: print(r)
            else:
                print("No hay coincidencias.")

        elif opcion == "5":
            # MEJORA: El listado ahora refleja lo que hay cargado desde el archivo
            lista = mi_inventario.mostrar_inventario()
            if not lista:
                print("Inventario vacío.")
            else:
                for p in lista: print(p)

        elif opcion == "6":
            print("Saliendo... Datos guardados en inventario.txt")
            break


if __name__ == "__main__":
    menu()