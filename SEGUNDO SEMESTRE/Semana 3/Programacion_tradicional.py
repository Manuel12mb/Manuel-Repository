# --- Funciones Separadas para la Lógica ---

def obtener_datos_diarios():
    """
    Solicita al usuario las temperaturas de los 7 días de la semana.
    Devuelve una lista de números flotantes.
    """
    temperaturas = []
    print("--- INGRESO DE TEMPERATURAS DIARIAS ---")
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    for dia in dias:
        while True:
            try:
                # Entrada de datos
                temp = float(input(f"Ingrese la temperatura del {dia} (°C): "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Error: Ingrese un número válido para la temperatura.")

    return temperaturas


def calcular_promedio(temperaturas):
    """
    Calcula el promedio de una lista de temperaturas.
    """
    if not temperaturas:
        return 0.0  # Evita división por cero si la lista está vacía

    # Cálculo del promedio
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio


def mostrar_resultado(promedio):
    """
    Muestra el promedio semanal de forma clara.
    """
    print("\n--- RESULTADO SEMANAL ---")
    print(f"El promedio semanal de temperaturas fue de: {promedio:.2f}°C")


# --- Función Principal (Orquestador) ---

def main():
    """
    Función principal que organiza el flujo del programa.
    """
    # 1. Entrada de datos
    datos = obtener_datos_diarios()

    # 2. Cálculo
    promedio_semanal = calcular_promedio(datos)

    # 3. Salida de resultados
    mostrar_resultado(promedio_semanal)


# Ejecución del programa
if __name__ == "__main__":
    main()