class Vehiculo:
    """Representa un auto dentro del inventario."""
    def __init__(self, marca, modelo, precio, anio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.anio = anio
        self.vendido = False

    def __str__(self):
        estado = "Vendido" if self.vendido else "Disponible"
        return f"{self.marca} {self.modelo} ({self.anio}) - ${self.precio:,} [{estado}]"


class Cliente:
    """Representa a un comprador potencial."""
    def __init__(self, nombre, presupuesto):
        self.nombre = nombre
        self.presupuesto = presupuesto
        self.compras = []

    def puede_comprar(self, precio_vehiculo):
        """Verifica si el cliente tiene fondos suficientes."""
        return self.presupuesto >= precio_vehiculo


class Concesionario:
    """Gestiona la lógica del negocio: inventario y ventas."""
    def __init__(self, nombre_negocio):
        self.nombre = nombre_negocio
        self.inventario = []

    def agregar_al_inventario(self, vehiculo):
        """Añade un objeto Vehiculo a la lista del concesionario."""
        self.inventario.append(vehiculo)
        print(f"Ingresado al sistema: {vehiculo.marca} {vehiculo.modelo}")

    def mostrar_catalogo(self):
        """Filtra y muestra solo los vehículos disponibles."""
        print(f"\n--- Catálogo de {self.nombre} ---")
        disponibles = [v for v in self.inventario if not v.vendido]
        if not disponibles:
            print("No hay vehículos disponibles por el momento.")
        for v in disponibles:
            print(v)

    def realizar_venta(self, modelo_auto, cliente):
        """Lógica de interacción entre Cliente, Vehiculo y Concesionario."""
        # Buscar el vehículo en el inventario por modelo
        vehiculo = next((v for v in self.inventario if v.modelo == modelo_auto and not v.vendido), None)

        if not vehiculo:
            print(f"Lo sentimos {cliente.nombre}, el modelo '{modelo_auto}' no está disponible.")
            return

        if cliente.puede_comprar(vehiculo.precio):
            # Proceso de venta: actualizar estados
            vehiculo.vendido = True
            cliente.presupuesto -= vehiculo.precio
            cliente.compras.append(vehiculo)
            print(f"¡Venta exitosa! {cliente.nombre} ha comprado un {vehiculo.marca} {vehiculo.modelo}.")
            print(f"Saldo restante del cliente: ${cliente.presupuesto:,}")
        else:
            print(f"Fondos insuficientes: {cliente.nombre} necesita ${vehiculo.precio:,} pero solo tiene ${cliente.presupuesto:,}.")

# --- Ejecución del Programa ---

# 1. Instanciamos el concesionario
mi_agencia = Concesionario("AutoPremium S.A.")

# 2. Creamos instancias de Vehículos
auto1 = Vehiculo("Toyota", "Corolla", 25000, 2024)
auto2 = Vehiculo("Tesla", "Model 3", 45000, 2023)
auto3 = Vehiculo("Ford", "Ranger", 35000, 2022)

# 3. Llenamos el inventario
mi_agencia.agregar_al_inventario(auto1)
mi_agencia.agregar_al_inventario(auto2)
mi_agencia.agregar_al_inventario(auto3)

# 4. Creamos un Cliente
comprador = Cliente("Maria Fernanda", 40000)

# 5. Interacción del sistema
mi_agencia.mostrar_catalogo()

# Intento de compra 1: Tesla (No alcanza el dinero)
mi_agencia.realizar_venta("Model 3", comprador)

# Intento de compra 2: Ford (Venta exitosa)
mi_agencia.realizar_venta("Ranger", comprador)

# Verificamos catálogo actualizado
mi_agencia.mostrar_catalogo()