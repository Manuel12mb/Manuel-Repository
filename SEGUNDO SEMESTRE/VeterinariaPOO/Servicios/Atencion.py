# servicios/atencion.py

def realizar_chequeo(mascota):
    print(f"--- Chequeo de {mascota.nombre} ---")
    print(f"Edad: {mascota.edad} años")
    # Accedemos al dato protegido mediante el método público
    print(f"Estado de salud actual: {mascota.obtener_salud()}%")
    # POLIMORFISMO en acción:
    print(f"La mascota dice: {mascota.emitir_sonido()}")
    print("Resultado: Mascota saludable.\n")


class ServicioVeterinario:
    """CLASE DE SERVICIO: Maneja la lógica del negocio."""

