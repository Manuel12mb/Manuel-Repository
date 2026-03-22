class VisitaServicio:
    def __init__(self):
        # Lista privada que actúa como persistencia en memoria
        self.__visitantes = []

    def registrar_visitante(self, visitante):
        # Verifica que la cédula no esté duplicada
        for v in self.__visitantes:
            if v.cedula == visitante.cedula:
                return False, "La cédula ya existe."

        self.__visitantes.append(visitante)
        return True, "Visitante registrado con éxito."

    def eliminar_visitante(self, cedula):
        for i, v in enumerate(self.__visitantes):
            if v.cedula == cedula:
                del self.__visitantes[i]
                return True
        return False

    def obtener_todos(self):
        # Retorna la lista de objetos visitantes
        return self.__visitantes