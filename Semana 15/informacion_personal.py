# Crear un diccionario con información ficticia de una persona.
persona = {
    "nombre": "Isabel Montes",
    "edad": 35,
    "ciudad": "Guayaquil",
    "profesion": "Ingeniera Civil" # Se incluye la profesión desde el inicio
}

print("Diccionario Inicial:")
print(persona)
print("-" * 30)

# 1. Acceder y Modificar Valores:
# Accede al valor asociado con la clave "ciudad" y modifícalo.
persona["ciudad"] = "Quito"
print("Ciudad modificada a:", persona["ciudad"])
# La clave "profesion" ya fue agregada en la creación inicial del diccionario.

# 2. Verificar Existencia de Claves:
# Verifica si la clave "telefono" existe en el diccionario.
if "telefono" not in persona:
    # Si no existe, agrégala con un número de teléfono ficticio.
    persona["telefono"] = "0987-654-321"
    print("Clave 'telefono' no existía, ha sido agregada.")

# 3. Eliminar una Clave:
# Elimina la clave "edad" del diccionario.
if "edad" in persona:
    del persona["edad"]
    print("Clave 'edad' eliminada.")

# 4. Imprimir el Diccionario Final:
print("-" * 30)
print("Diccionario Final después de todas las operaciones:")
print(persona)