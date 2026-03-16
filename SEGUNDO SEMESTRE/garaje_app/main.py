# Importamos la lógica y la interfaz
from servicios.garaje_servicio import GarajeServicio
from ui.app_tkinter import AppGaraje


def principal():
    # 1. Inicializamos la capa de servicios (Lógica)
    servicio_logica = GarajeServicio()

    # 2. Inicializamos la interfaz y le pasamos el servicio (Inyección de dependencias)
    ventana_principal = AppGaraje(servicio_logica)

    # 3. Iniciamos el ciclo de eventos de la aplicación
    ventana_principal.mainloop()


# Verificamos que el script se ejecute directamente
if __name__ == "__main__":
    principal()