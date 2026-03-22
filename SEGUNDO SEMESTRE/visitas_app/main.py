import tkinter as tk
from servicios.visita_servicio import VisitaServicio
from ui.app_tkinter import AppTkinter


def main():
    # 1. Crear la raíz de Tkinter
    root = tk.Tk()

    # 2. Instanciar el servicio (Cerebro)
    servicio = VisitaServicio()

    # 3. Instanciar la UI pasando el servicio (Inyección de Dependencias)
    app = AppTkinter(root, servicio)

    # 4. Iniciar la aplicación
    root.mainloop()


if __name__ == "__main__":
    main()