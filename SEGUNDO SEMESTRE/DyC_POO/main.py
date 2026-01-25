from servicios.gestor_log import GestorLog, registrar_evento
import time


def ejecutar_demostracion():
    print("--- INICIO DEL PROGRAMA ---\n")

    # 1. Instanciamos el servicio
    GestorLog()

    # 2. Registramos un par de eventos
    registrar_evento("bitacora.txt", "Inicio de sesión del usuario admin")
    time.sleep(1)  # Pausa breve para observar el flujo

    registrar_evento("bitacora.txt", "Cambio de contraseña realizado")

    print("\n--- FIN DE LA LÓGICA PRINCIPAL ---")


if __name__ == "__main__":
    ejecutar_demostracion()
    # Al terminar la función y el programa, verás los mensajes del destructor.