from modelos.libro import Libro
from modelos.usuario import Usuario
from servicios.biblioteca_servicio import BibliotecaServicio


def menu():
    servicio = BibliotecaServicio()

    while True:
        print("\n--- SISTEMA DE GESTIÓN DE BIBLIOTECA ---")
        print("1. Añadir Libro")
        print("2. Registrar Usuario")
        print("3. Prestar Libro")
        print("4. Devolver Libro")
        print("5. Buscar Libro")
        print("6. Listar Libros de Usuario")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            t = input("Título: ")
            a = input("Autor: ")
            c = input("Categoría: ")
            i = input("ISBN: ")
            servicio.añadir_libro(Libro(t, a, c, i))

        elif opcion == "2":
            n = input("Nombre de usuario: ")
            uid = input("ID de usuario: ")
            servicio.registrar_usuario(Usuario(n, uid))

        elif opcion == "3":
            isbn = input("ISBN del libro: ")
            uid = input("ID del usuario: ")
            servicio.prestar_libro(isbn, uid)

        elif opcion == "4":
            isbn = input("ISBN del libro: ")
            uid = input("ID del usuario: ")
            servicio.devolver_libro(isbn, uid)

        elif opcion == "5":
            crit = input("Buscar por (titulo/autor/categoria): ").lower()
            val = input("Texto a buscar: ")
            res = servicio.buscar_libro(crit, val)
            if res:
                print("\nLibros encontrados:")
                for l in res: print(f" - {l}")
            else:
                print("No se encontraron coincidencias.")

        elif opcion == "6":
            uid = input("ID del usuario: ")
            prestados = servicio.listar_libros_prestados(uid)
            if prestados is not None:
                print(f"\nLibros de {servicio.usuarios_registrados[uid].nombre}:")
                for l in prestados: print(f" - {l}")
            else:
                print("Usuario no existe.")

        elif opcion == "7":
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()