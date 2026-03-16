# Definición de la clase que representa a un vehículo en el sistema
class Vehiculo:
    def __init__(self, placa, marca, propietario):
        # Atributos básicos requeridos por el proyecto
        self.placa = placa
        self.marca = marca
        self.propietario = propietario

    # Método para representar el objeto como una cadena de texto (opcional)
    def __str__(self):
        return f"{self.placa} - {self.marca} ({self.propietario})"
