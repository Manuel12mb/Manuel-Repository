# --- 1. Clase Base (Herencia) ---
class Registro:
    """Clase base que maneja el almacenamiento y cálculo del promedio."""

    def __init__(self):
        # Encapsulamiento del atributo principal
        self.datos = []

    def ingresar_datos(self):
        """Método común para la entrada de datos (temperaturas)."""
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

        for dia in dias:
            while True:
                try:
                    dato = float(input(f"Ingrese la temperatura del {dia} (°C): "))
                    self.datos.append(dato)
                    break
                except ValueError:
                    print("Error: Ingrese un número válido.")

    def calcular_promedio(self):
        """Método común para calcular el promedio."""
        if not self.datos:
            return 0.0

        return sum(self.datos) / len(self.datos)

    def mostrar_informe(self):
        """Método base para presentar el resultado."""
        promedio = self.calcular_promedio()
        print(f"\n--- INFORME BÁSICO ---")
        print(f"El promedio de los datos registrados fue: {promedio:.2f}")


# --- 2. Clase Derivada (Herencia y Polimorfismo) ---
class RegistroClimaExtendido(Registro):
    """
    Hereda de Registro y añade funcionalidad para registrar la humedad.
    """

    def __init__(self):
        # Llama al constructor de la clase base
        super().__init__()
        self.humedad_promedio = 0.0

    def ingresar_datos(self):
        """Sobrescribe el método base para incluir también la humedad."""
        super().ingresar_datos()  # Llama al método de la clase padre

        while True:
            try:
                self.humedad_promedio = float(input("Ingrese la humedad promedio semanal (%): "))
                break
            except ValueError:
                print("Error: Ingrese un número válido para la humedad.")

    def mostrar_informe(self):
        """
        Sobrescribe el método base para mostrar más información (Polimorfismo).
        """
        promedio_temp = self.calcular_promedio()
        print(f"\n--- INFORME CLIMÁTICO DETALLADO ---")
        print(f"El promedio de temperatura semanal fue: {promedio_temp:.2f}°C")
        print(f"La humedad promedio semanal registrada fue: {self.humedad_promedio:.2f}%")


# --- Ejecución POO con Conceptos Avanzados ---
def main_avanzado():
    # 1. Creamos un objeto de la clase base
    registro_basico = Registro()
    print("\n--- Ejecutando Registro Básico (Clase Padre) ---")
    registro_basico.ingresar_datos()
    registro_basico.mostrar_informe()

    # 2. Creamos un objeto de la clase derivada
    registro_detallado = RegistroClimaExtendido()
    print("\n--- Ejecutando Registro Detallado (Clase Hija) ---")
    registro_detallado.ingresar_datos()
    # Mismo nombre de método, diferente comportamiento (Polimorfismo)
    registro_detallado.mostrar_informe()


if __name__ == "__main__":
    main_avanzado()