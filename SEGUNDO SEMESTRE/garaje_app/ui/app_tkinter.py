import tkinter as tk
from tkinter import ttk, messagebox  # ttk para la tabla y messagebox para alertas


class AppGaraje(tk.Tk):
    def __init__(self, servicio):
        super().__init__()
        self.servicio = servicio  # Recibimos la lógica del servicio
        self.title("Sistema de Gestión de Garaje")
        self.geometry("600x450")

        # --- Contenedor del Formulario ---
        frame_form = tk.LabelFrame(self, text="Registro de Vehículo", padx=10, pady=10)
        frame_form.pack(pady=10, fill="x", padx=20)

        # Campo Placa
        tk.Label(frame_form, text="Placa:").grid(row=0, column=0, sticky="w")
        self.entry_placa = tk.Entry(frame_form)
        self.entry_placa.grid(row=0, column=1, padx=5, pady=2)

        # Campo Marca
        tk.Label(frame_form, text="Marca:").grid(row=1, column=0, sticky="w")
        self.entry_marca = tk.Entry(frame_form)
        self.entry_marca.grid(row=1, column=1, padx=5, pady=2)

        # Campo Propietario
        tk.Label(frame_form, text="Propietario:").grid(row=2, column=0, sticky="w")
        self.entry_propietario = tk.Entry(frame_form)
        self.entry_propietario.grid(row=2, column=1, padx=5, pady=2)

        # --- Botones de Acción ---
        self.btn_agregar = tk.Button(frame_form, text="Agregar Vehículo", command=self.agregar, bg="#4CAF50",
                                     fg="white")
        self.btn_agregar.grid(row=3, column=0, pady=10)

        self.btn_limpiar = tk.Button(frame_form, text="Limpiar Campos", command=self.limpiar_campos)
        self.btn_limpiar.grid(row=3, column=1, pady=10)

        # --- Tabla de Visualización ---
        # Definimos las columnas de la tabla
        columnas = ("Placa", "Marca", "Propietario")
        self.tabla = ttk.Treeview(self, columns=columnas, show="headings")

        # Configuramos los encabezados
        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=150)

        self.tabla.pack(fill="both", expand=True, padx=20, pady=10)

    def agregar(self):
        # Obtenemos el texto de los inputs
        p = self.entry_placa.get()
        m = self.entry_marca.get()
        prop = self.entry_propietario.get()

        # Llamamos al servicio para procesar la lógica
        if self.servicio.registrar_vehiculo(p, m, prop):
            self.actualizar_tabla()  # Refrescamos la UI
            self.limpiar_campos()  # Vaciamos los inputs
            messagebox.showinfo("Sistema", "¡Vehículo guardado!")
        else:
            messagebox.showwarning("Atención", "Por favor llene todos los campos")

    def actualizar_tabla(self):
        # Primero borramos lo que hay actualmente en la tabla visual
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        # Obtenemos los datos actualizados del servicio y los insertamos
        for v in self.servicio.obtener_vehiculos():
            self.tabla.insert("", "end", values=(v.placa, v.marca, v.propietario))

    def limpiar_campos(self):
        # Borra el contenido de los cuadros de texto desde el inicio (0) hasta el final (END)
        self.entry_placa.delete(0, tk.END)
        self.entry_marca.delete(0, tk.END)
        self.entry_propietario.delete(0, tk.END)
