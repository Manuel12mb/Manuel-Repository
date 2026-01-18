# modelos/mascota.py

class Mascota:
    """CLASE BASE: Define atributos comunes para todos los animales."""

    def __init__(self, nombre, edad, salud_inicial):
        self.nombre = nombre
        self.edad = edad
        # ENCAPSULAMIENTO: Salud es privado (__), no se debe modificar desde afuera
        self.__salud = salud_inicial

        # Método para obtener el valor privado

    def obtener_salud(self):
        return self.__salud

    def emitir_sonido(self):
        """Este método será usado para el POLIMORFISMO."""
        return "Sonido genérico"


# HERENCIA: Perro 'hereda' de Mascota
class Perro (Mascota):
    def emitir_sonido(self):
        # POLIMORFISMO: Sobrescribimos el método para que sea específico
        return "¡Guau! ¡Guau!"


# HERENCIA: Gato 'hereda' de Mascota
class Gato (Mascota):
    def emitir_sonido(self):
        # POLIMORFISMO: Comportamiento diferente para el mismo método
        return "¡Miau! ¡Miau!"