import tkinter as tk
from tkinter import messagebox
from servicios.tarea_servicio import TareaServicio

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.servicio = TareaServicio()

        # --- Componentes de la UI ---
        self.label = tk.Label(root, text="Descripción de la tarea:")
        self.label.pack(pady=5)

        self.entrada = tk.Entry(root, width=40)
        self.entrada.pack(pady=5)
        # Evento de Teclado: Presionar Enter para añadir
        self.entrada.bind("<Return>", lambda event: self.añadir_tarea())

        self.btn_añadir = tk.Button(root, text="Añadir Tarea", command=self.añadir_tarea)
        self.btn_añadir.pack(pady=5)

        # Usamos un Listbox para mostrar las tareas
        self.lista_box = tk.Listbox(root, width=50, height=10)
        self.lista_box.pack(pady=10)
        # Evento de Ratón: Doble clic para completar
        self.lista_box.bind("<Double-1>", lambda event: self.marcar_completada())

        self.btn_completar = tk.Button(root, text="Marcar Completada", command=self.marcar_completada)
        self.btn_completar.pack(side=tk.LEFT, padx=20, pady=10)

        self.btn_eliminar = tk.Button(root, text="Eliminar", command=self.eliminar_tarea)
        self.btn_eliminar.pack(side=tk.RIGHT, padx=20, pady=10)

    def actualizar_lista_visual(self):
        """Refresca el Listbox con los datos actuales del servicio."""
        self.lista_box.delete(0, tk.END)
        for tarea in self.servicio.obtener_todas():
            self.lista_box.insert(tk.END, str(tarea))
            # Feedback visual: Cambiar color si está completada
            if tarea.completada:
                self.lista_box.itemconfig(tk.END, fg="gray")

    def añadir_tarea(self):
        desc = self.entrada.get()
        if self.servicio.agregar_tarea(desc):
            self.entrada.delete(0, tk.END)
            self.actualizar_lista_visual()
        else:
            messagebox.showwarning("Atención", "La tarea no puede estar vacía.")

    def marcar_completada(self):
        try:
            indice = self.lista_box.curselection()[0]
            self.servicio.completar_tarea(indice)
            self.actualizar_lista_visual()
        except IndexError:
            messagebox.showwarning("Atención", "Selecciona una tarea de la lista.")

    def eliminar_tarea(self):
        try:
            indice = self.lista_box.curselection()[0]
            self.servicio.eliminar_tarea(indice)
            self.actualizar_lista_visual()
        except IndexError:
            messagebox.showwarning("Atención", "Selecciona una tarea para eliminar.")