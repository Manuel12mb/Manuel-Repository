# PROGRAMA: Convertidor de Temperatura Celsius a Fahrenheit

# DESCRIPCIÓN: Este programa recibe una temperatura en grados Celsius, realiza la conversión y determina si el clima es "caluroso".

def convertir_a_fahrenheit(celsius_valor):
    """Calcula la conversión de grados Celsius a Fahrenheit."""
    # Aplicamos la fórmula: (C * 9/5) + 32
    resultado_fahrenheit = (celsius_valor * 9 / 5) + 32
    return resultado_fahrenheit


def ejecutar_programa():
    print("--- Bienvenido al Sistema de Conversión ---")

    # 1. String (Cadena de texto)
    nombre_usuario = input("Por favor, ingresa tu nombre: ")

    # 2. Float (Número decimal)
    temperatura_celsius = float(input(f"Hola {nombre_usuario}, ingresa los grados Celsius: "))

    # Realizamos el cálculo llamando a la función
    resultado = convertir_a_fahrenheit(temperatura_celsius)

    # 3. Boolean (Booleano)
    # Consideramos caluroso si es mayor a 30 grados Celsius
    es_caluroso = temperatura_celsius > 30

    # Mostramos los resultados finales
    print("\n--- Resultados ---")
    print(f"Temperatura en Fahrenheit: {resultado}°F")

    # 4. Integer (Entero) - Ejemplo de uso de entero
    veces_consultado = 1
    print(f"Esta es tu consulta número: {veces_consultado}")

    if es_caluroso:
        print("Estado del clima: El clima es caluroso.")
    else:
        print("Estado del clima: El clima es templado o frío.")


# Ejecución del programa
if __name__ == "__main__":
    ejecutar_programa()