from modelos.producto import Producto
from servicios.gestion_inventario import Inventario


def menu():
    # Instanciamos la clase Inventario para empezar a trabajar
    mi_inventario = Inventario()

    while True:  # Bucle infinito para mantener el menú activo
        print("\n--- SISTEMA DE GESTIÓN DE INVENTARIO ---")
        print("1. Añadir producto\n2. Eliminar producto\n3. Actualizar producto\n4. Buscar\n5. Listar\n6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                # Solicitamos datos y los convertimos al tipo necesario
                id_p = int(input("ID único: "))
                nom = input("Nombre: ")
                cant = int(input("Cantidad: "))
                pre = float(input("Precio: "))

                # Creamos el objeto y lo enviamos al servicio
                nuevo = Producto(id_p, nom, cant, pre)
                exito, msg = mi_inventario.añadir_producto(nuevo)
                print(msg)
            except ValueError:
                print("Error: Entrada no válida. Use números para ID, Cantidad y Precio.")

        elif opcion == "2":
            id_p = int(input("ID del producto a eliminar: "))
            exito, msg = mi_inventario.eliminar_producto(id_p)
            print(msg)

        elif opcion == "3":
            id_p = int(input("ID del producto a actualizar: "))
            print("Presione Enter para omitir un campo.")
            c_input = input("Nueva cantidad: ")
            p_input = input("Nuevo precio: ")

            # Convertimos solo si el usuario escribió algo, sino enviamos None
            cant = int(c_input) if c_input else None
            prec = float(p_input) if p_input else None

            exito, msg = mi_inventario.actualizar_producto(id_p, cant, prec)
            print(msg)

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            resultados = mi_inventario.buscar_por_nombre(nombre)
            if resultados:
                # Imprimimos cada objeto encontrado (usa el método __str__ de la clase Producto)
                for r in resultados: print(r)
            else:
                print("Sin coincidencias.")

        elif opcion == "5":
            lista = mi_inventario.mostrar_inventario()
            if not lista:
                print("Inventario vacío.")
            else:
                for p in lista: print(p)

        elif opcion == "6":
            print("¡Hasta luego!")
            break  # Rompe el bucle while y cierra el programa
        else:
            print("Opción inválida.")


# Punto de ejecución principal
if __name__ == "__main__":
    menu()