# Fabian Guambuguete Semana 15

import tkinter as tk
from tkinter import messagebox

# ==============================
# Aplicación: Lista de Tareas (Diseño Moderno)
# ==============================
# Mejoras aplicadas:
# - Colores modernos (modo oscuro)
# - Botones estilizados
# - Tipografía más limpia
# - Mejor distribución con frames

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas Moderna")
        self.root.geometry("420x500")
        self.root.config(bg="#1e1e2f")

        self.tareas = []

        # ====== Título ======
        titulo = tk.Label(root, text=" Mis Tareas", font=("Segoe UI", 18, "bold"), bg="#1e1e2f", fg="#ffffff")
        titulo.pack(pady=10)

        # ====== Frame Entrada ======
        frame_input = tk.Frame(root, bg="#1e1e2f")
        frame_input.pack(pady=10, padx=10, fill=tk.X)

        self.entry = tk.Entry(frame_input, font=("Segoe UI", 12), bg="#2a2a40", fg="white", insertbackground="white", relief="flat")
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=6, padx=(0, 5))
        self.entry.bind("<Return>", self.añadir_tarea_evento)

        btn_add = tk.Button(frame_input, text="+", font=("Segoe UI", 12, "bold"), bg="#6c63ff", fg="white", relief="flat", command=self.añadir_tarea)
        btn_add.pack(side=tk.RIGHT, ipadx=10, ipady=5)

        # ====== Lista ======
        self.listbox = tk.Listbox(root, font=("Segoe UI", 12), bg="#2a2a40", fg="white",
                                 selectbackground="#6c63ff", activestyle="none", relief="flat")
        self.listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.listbox.bind("<Double-Button-1>", self.marcar_completada_evento)

        # ====== Botones ======
        frame_botones = tk.Frame(root, bg="#1e1e2f")
        frame_botones.pack(pady=10)

        btn_complete = tk.Button(frame_botones, text="✔ Completar", font=("Segoe UI", 10),
                                 bg="#00c896", fg="white", relief="flat", command=self.marcar_completada)
        btn_complete.grid(row=0, column=0, padx=5, ipadx=5, ipady=5)

        btn_delete = tk.Button(frame_botones, text="🗑 Eliminar", font=("Segoe UI", 10),
                               bg="#ff5c5c", fg="white", relief="flat", command=self.eliminar_tarea)
        btn_delete.grid(row=0, column=1, padx=5, ipadx=5, ipady=5)

    # ==============================
    # Añadir tarea
    # ==============================
    def añadir_tarea(self):
        texto = self.entry.get().strip()

        if texto == "":
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía")
            return

        self.tareas.append({"texto": texto, "completada": False})
        self.actualizar_lista()
        self.entry.delete(0, tk.END)

    def añadir_tarea_evento(self, event):
        self.añadir_tarea()

    # ==============================
    # Marcar completada
    # ==============================
    def marcar_completada(self):
        try:
            index = self.listbox.curselection()[0]
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea")
            return

        self.tareas[index]["completada"] = not self.tareas[index]["completada"]
        self.actualizar_lista()

    def marcar_completada_evento(self, event):
        self.marcar_completada()

    # ==============================
    # Eliminar tarea
    # ==============================
    def eliminar_tarea(self):
        try:
            index = self.listbox.curselection()[0]
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea")
            return

        del self.tareas[index]
        self.actualizar_lista()

    # ==============================
    # Actualizar lista
    # ==============================
    def actualizar_lista(self):
        self.listbox.delete(0, tk.END)

        for tarea in self.tareas:
            texto = tarea["texto"]

            if tarea["completada"]:
                texto = "✔ " + texto

            self.listbox.insert(tk.END, texto)


# ==============================
# Main
# ==============================
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
