
# 1. HERENCIA y ABSTRACCIÓN: Clase Padre Abstracta
# La clase 'Vehiculo' define la estructura básica y el comportamiento común.
class Vehiculo:
    """Clase base que representa un vehículo genérico."""

    def __init__(self, marca, modelo, velocidad_max):
        # 2. ENCAPSULACIÓN: Uso de '__' para proteger los atributos.
        self.__marca = marca
        self.__modelo = modelo
        self.__velocidad_max = velocidad_max
        self.__encendido = False  # Estado interno protegido

    # 2. ENCAPSULACIÓN: Métodos públicos (getters) para acceder a los atributos protegidos.
    def obtener_marca(self):
        return self.__marca

    def obtener_modelo(self):
        return self.__modelo

    # 1. ABSTRACCIÓN: Métodos comunes (Interfaz)
    def encender(self):
        """Define el comportamiento de encendido."""
        self.__encendido = True
        print(f"{self.__marca} {self.__modelo} se ha encendido.")

    def apagar(self):
        """Define el comportamiento de apagado."""
        self.__encendido = False
        print(f"{self.__marca} {self.__modelo} se ha apagado.")

    # 3. POLIMORFISMO: Método abstracto (debe ser implementado por las clases hijas)
    def moverse(self):
        """Método abstracto: Cada vehículo debe definir su movimiento."""
        raise NotImplementedError("Este método debe ser sobrescrito por la subclase.")


# 1. HERENCIA: 'Coche' hereda propiedades y métodos de 'Vehiculo'.
class Coche(Vehiculo):
    """Representa un coche de pasajeros."""

    def __init__(self, marca, modelo, velocidad_max, numero_puertas):
        # Llama al constructor de la clase padre
        super().__init__(marca, modelo, velocidad_max)
        self.__numero_puertas = numero_puertas

    # 3. POLIMORFISMO: Sobrescritura del método 'moverse'.
    def moverse(self):
        print(f"El {self.obtener_marca()} {self.obtener_modelo()} está rodando sobre el pavimento.")

    # Método específico de Coche
    def abrir_puertas(self):
        print(f"Abriendo las {self.__numero_puertas} puertas del coche.")


# 1. HERENCIA: 'Moto' hereda propiedades y métodos de 'Vehiculo'.
class Moto(Vehiculo):
    """Representa una motocicleta."""

    # 3. POLIMORFISMO: Sobrescritura del método 'moverse'.
    def moverse(self):
        print(f"La {self.obtener_marca()} {self.obtener_modelo()} está inclinándose en una curva.")


# --- Uso del código ---

# Creación de objetos (instancias de las clases)
mi_coche = Coche("Toyota", "Corolla", 180, 4)
mi_moto = Moto("Yamaha", "R6", 260)

print("--- Demostración de Encapsulación y Abstracción ---")
mi_coche.encender()
# Intentar acceder a un atributo protegido directamente fallaría: print(mi_coche.__encendido)
print(f"Marca del vehículo (Acceso Encapsulado): {mi_coche.obtener_marca()}")
mi_coche.abrir_puertas()

print("\n--- Demostración de Polimorfismo y Herencia ---")

# Una lista puede contener objetos de diferentes clases hijas.
flota = [mi_coche, mi_moto]

# El mismo llamado al método 'moverse()' se comporta diferente según el objeto.
for vehiculo in flota:
    print(f"Tipo: {type(vehiculo).__name__}")
    vehiculo.moverse()  # ¡Polimorfismo en acción!
    vehiculo.apagar()