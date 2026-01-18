# main.py
from Modelo.Mascotas import Perro, Gato
from Servicios.Atencion import ServicioVeterinario, realizar_chequeo


def inicio():
    # 1. Creamos las INSTANCIAS (Objetos)
    mi_perro = Perro("Rex", 5, 95)
    mi_gato = Gato("Pelusa", 3, 100)

    # 2. Creamos el servicio
    ServicioVeterinario()

    # 3. Demostramos el funcionamiento
    print("BIENVENIDOS A LA VETERINARIA\n")

    realizar_chequeo(mi_perro)
    realizar_chequeo(mi_gato)


if __name__ == "__main__":
    inicio()