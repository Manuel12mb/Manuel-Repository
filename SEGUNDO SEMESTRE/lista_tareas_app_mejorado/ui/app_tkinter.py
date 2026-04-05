import tkinter as tk
from tkinter import messagebox
from servicios.tarea_servicio import TareaServicio


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas Pro")
        self.servicio = TareaServicio()

        # Componentes
        tk.Label(root, text="Atajos: Enter (Añadir) | C (Completar) | D (Eliminar) | Esc (Salir)").pack(pady=5)

        self.entrada = tk.Entry(root, width=40)
        self.entrada.pack(pady=5)
        self.entrada.focus_set()  # Para empezar a escribir de una vez

        self.lista_box = tk.Listbox(root, width=50, height=10)
        self.lista_box.pack(pady=10)

        # --- MANEJO DE EVENTOS (Requisito Nuevo) ---

        # 1. Añadir con Enter
        self.entrada.bind("<Return>", lambda e: self.añadir_tarea())

        # 2. Completar con tecla "C" (o doble clic)
        self.root.bind("<c>", lambda e: self.marcar_completada())
        self.root.bind("<C>", lambda e: self.marcar_completada())
        self.lista_box.bind("<Double-1>", lambda e: self.marcar_completada())

        # 3. Eliminar con tecla "D" o "Delete"
        self.root.bind("<d>", lambda e: self.eliminar_tarea())
        self.root.bind("<D>", lambda e: self.eliminar_tarea())
        self.root.bind("<Delete>", lambda e: self.eliminar_tarea())

        # 4. Cerrar con Escape
        self.root.bind("<Escape>", lambda e: self.root.destroy())

        # Botones (usando command= como pide la tarea)
        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack(pady=5)

        tk.Button(self.btn_frame, text="Añadir", command=self.añadir_tarea).pack(side=tk.LEFT, padx=5)
        tk.Button(self.btn_frame, text="Completar (C)", command=self.marcar_completada).pack(side=tk.LEFT, padx=5)
        tk.Button(self.btn_frame, text="Eliminar (D)", command=self.eliminar_tarea).pack(side=tk.LEFT, padx=5)

    def actualizar_lista_visual(self):
        self.lista_box.delete(0, tk.END)
        for tarea in self.servicio.obtener_todas():
            self.lista_box.insert(tk.END, str(tarea))
            if tarea.completada:
                self.lista_box.itemconfig(tk.END, fg="green")  # Feedback visual mejorado

    def añadir_tarea(self):
        desc = self.entrada.get()
        if self.servicio.agregar_tarea(desc):
            self.entrada.delete(0, tk.END)
            self.actualizar_lista_visual()

    def marcar_completada(self):
        try:
            indice = self.lista_box.curselection()[0]
            self.servicio.completar_tarea(indice)
            self.actualizar_lista_visual()
        except IndexError:
            pass  # Ignorar si no hay selección para que no moleste el atajo

    def eliminar_tarea(self):
        try:
            indice = self.lista_box.curselection()[0]
            self.servicio.eliminar_tarea(indice)
            self.actualizar_lista_visual()
        except IndexError:
            pass