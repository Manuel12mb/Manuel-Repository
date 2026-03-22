import tkinter as tk
from tkinter import ttk, messagebox
from modelos.visitante import Visitante


class AppTkinter:
    def __init__(self, root, servicio):
        self.root = root
        self.servicio = servicio  # Inyección del servicio
        self.root.title("Sistema de Registro de Visitantes")
        self.root.geometry("600x400")

        # --- Formulario de Entrada ---
        frame_form = tk.LabelFrame(self.root, text="Datos del Visitante", padx=10, pady=10)
        frame_form.pack(fill="x", padx=20, pady=10)

        tk.Label(frame_form, text="Cédula:").grid(row=0, column=0, sticky="w")
        self.ent_cedula = tk.Entry(frame_form)
        self.ent_cedula.grid(row=0, column=1, pady=2)

        tk.Label(frame_form, text="Nombre:").grid(row=1, column=0, sticky="w")
        self.ent_nombre = tk.Entry(frame_form)
        self.ent_nombre.grid(row=1, column=1, pady=2)

        tk.Label(frame_form, text="Motivo:").grid(row=2, column=0, sticky="w")
        self.ent_motivo = tk.Entry(frame_form)
        self.ent_motivo.grid(row=2, column=1, pady=2)

        # --- Panel de Acciones ---
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Registrar", command=self.ejecutar_registro).pack(side="left", padx=5)
        tk.Button(frame_botones, text="Eliminar", command=self.ejecutar_eliminacion).pack(side="left", padx=5)
        tk.Button(frame_botones, text="Limpiar", command=self.limpiar_campos).pack(side="left", padx=5)

        # --- Visualización (Treeview) ---
        self.tabla = ttk.Treeview(self.root, columns=("Ced", "Nom", "Mot"), show="headings")
        self.tabla.heading("Ced", text="Cédula")
        self.tabla.heading("Nom", text="Nombre")
        self.tabla.heading("Mot", text="Motivo de Visita")
        self.tabla.pack(fill="both", expand=True, padx=20, pady=10)

    def ejecutar_registro(self):
        c, n, m = self.ent_cedula.get(), self.ent_nombre.get(), self.ent_motivo.get()

        if not (c and n and m):
            messagebox.showwarning("Error", "Todos los campos son obligatorios.")
            return

        nuevo_v = Visitante(c, n, m)
        exito, msj = self.servicio.registrar_visitante(nuevo_v)

        if exito:
            messagebox.showinfo("Éxito", msj)
            self.actualizar_tabla()
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", msj)

    def ejecutar_eliminacion(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "Seleccione un registro para eliminar.")
            return

        item = self.tabla.item(seleccion)
        cedula = item['values'][0]

        if self.servicio.eliminar_visitante(str(cedula)):
            messagebox.showinfo("Eliminado", "Registro borrado correctamente.")
            self.actualizar_tabla()

    def actualizar_tabla(self):
        # Limpia la tabla actual
        for row in self.tabla.get_children():
            self.tabla.delete(row)
        # Carga los datos desde el servicio
        for v in self.servicio.obtener_todos():
            self.tabla.insert("", "end", values=(v.cedula, v.nombre, v.motivo))

    def limpiar_campos(self):
        self.ent_cedula.delete(0, tk.END)
        self.ent_nombre.delete(0, tk.END)
        self.ent_motivo.delete(0, tk.END)