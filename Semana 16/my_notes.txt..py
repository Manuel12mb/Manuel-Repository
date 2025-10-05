# Abre el archivo en modo de escritura ('w').
# El modo 'w' crea un nuevo archivo o sobrescribe el existente.
# El bloque 'with' se encarga de cerrar el archivo automáticamente al final.
with open('my_notes.txt', 'w') as file:
    # Escribe tres líneas de notas personales en el archivo.
    file.write("Mi primera nota: ¡Programacion es increible!\n")
    file.write("Segunda nota: Hoy aprendí sobre archivos.\n")
    file.write("Tercera nota: No olvides practicar todos los días.\n")

print("Archivo 'my_notes.txt' creado y escrito exitosamente.")

# --- 2. Lectura de Archivo de Texto ---
# Abre el archivo en modo de lectura ('r').
with open('my_notes.txt', 'r') as file:
    print("\nContenido del archivo 'my_notes.txt':")
    # Lee y muestra cada línea del archivo.
    for line in file:
        print(line.strip()) # .strip() elimina el salto de línea al final.

# --- 3. Cierre de Archivos ---
# El archivo se cierra automáticamente al salir del bloque 'with'.
print("\nEl archivo se ha cerrado automáticamente.")