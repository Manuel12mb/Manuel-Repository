class Visitante:
    def __init__(self, cedula, nombre, motivo):
        # Atributos privados (Encapsulamiento)
        self.__cedula = cedula
        self.__nombre = nombre
        self.__motivo = motivo

    # Getters para acceder a la información
    @property
    def cedula(self):
        return self.__cedula

    @property
    def nombre(self):
        return self.__nombre

    @property
    def motivo(self):
        return self.__motivo