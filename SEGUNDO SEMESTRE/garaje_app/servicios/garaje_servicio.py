# Importamos el modelo para poder crear instancias de Vehiculo
from modelos.vehiculo import Vehiculo

class GarajeServicio:
    def __init__(self):
        # Lista privada en memoria para almacenar los vehículos registrados
        self.vehiculos = []

    def registrar_vehiculo(self, placa, marca, propietario):
        # Validación simple: que los campos no estén vacíos
        if placa and marca and propietario:
            # Creamos el objeto con los datos recibidos
            nuevo_vehiculo = Vehiculo(placa, marca, propietario)
            # Lo guardamos en nuestra "base de datos" temporal (la lista)
            self.vehiculos.append(nuevo_vehiculo)
            return True # Registro exitoso
        return False # Fallo en el registro

    def obtener_vehiculos(self):
        # Retorna la lista completa para ser mostrada en la UI
        return self.vehiculos