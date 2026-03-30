class Tarea:
    def __init__(self, id_tarea, descripcion):
        self.id = id_tarea
        self.descripcion = descripcion
        self.completada = False  # Por defecto, una tarea no está lista

    def marcar_completada(self):
        self.completada = True

    def __str__(self):
        estado = "[Hecho]" if self.completada else "[Pendiente]"
        return f"{estado} {self.descripcion}"