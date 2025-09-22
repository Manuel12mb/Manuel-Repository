def calcular_descuento(monto_total, porcentaje_descuento=10):
  """
  Calcula el monto del descuento aplicando un porcentaje a un monto total.

  Args:
    monto_total (float): El monto total de la compra.
    porcentaje_descuento (int): El porcentaje de descuento. Por defecto es 10.

  Returns:
    float: El monto del descuento calculado.
  """
  descuento = monto_total * (porcentaje_descuento / 100)
  return descuento

# Llamada a la función desde el programa principal
monto_compra_1 = 200
monto_descuento_1 = calcular_descuento(monto_compra_1)
monto_final_1 = monto_compra_1 - monto_descuento_1

# Llamada a la función con un porcentaje de descuento diferente
monto_compra_2 = 150
porcentaje_descuento_2 = 25
monto_descuento_2 = calcular_descuento(monto_compra_2, porcentaje_descuento_2)
monto_final_2 = monto_compra_2 - monto_descuento_2

# Salida de los resultados
print("--- Compra 1 ---")
print(f"Monto total: ${monto_compra_1}")
print(f"Monto de descuento: ${monto_descuento_1}")
print(f"Monto final a pagar: ${monto_final_1}")
print()
print("--- Compra 2 ---")
print(f"Monto total: ${monto_compra_2}")
print(f"Monto de descuento: ${monto_descuento_2}")
print(f"Monto final a pagar: ${monto_final_2}")