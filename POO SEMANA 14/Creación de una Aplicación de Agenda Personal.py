# POOO SEMANA 14 FABIAN GUAMBUGUETE

import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import json
import os

ARCHIVO = "eventos.json"

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal ✨")
        self.root.geometry("780x480")
        self.root.configure(bg="#0f172a")  # fondo oscuro elegante

        self.estilos()

        # ===================== CONTENEDOR PRINCIPAL =====================
        main = tk.Frame(root, bg="#0f172a")
        main.pack(fill="both", expand=True, padx=12, pady=12)

        # ===================== HEADER =====================
        header = tk.Frame(main, bg="#1e293b", bd=0)
        header.pack(fill="x", pady=(0,10))

        tk.Label(header, text="📅 Mi Agenda Personal",
                 bg="#1e293b", fg="#e2e8f0",
                 font=("Segoe UI", 16, "bold")).pack(side="left", padx=10, pady=10)

        # ===================== ENTRADA =====================
        frame_input = tk.Frame(main, bg="#111827")
        frame_input.pack(fill="x", pady=6)

        tk.Label(frame_input, text="Fecha", bg="#111827", fg="#f1f5f9").grid(row=0, column=0, padx=6, pady=6)
        self.fecha_entry = DateEntry(frame_input, date_pattern='yyyy-mm-dd')
        self.fecha_entry.grid(row=0, column=1, padx=6, pady=6)

        tk.Label(frame_input, text="Hora", bg="#111827", fg="#f1f5f9").grid(row=0, column=2, padx=6, pady=6)
        self.hora_entry = ttk.Entry(frame_input)
        self.hora_entry.grid(row=0, column=3, padx=6, pady=6)

        tk.Label(frame_input, text="Descripción", bg="#111827", fg="#f1f5f9").grid(row=1, column=0, padx=6, pady=6)
        self.desc_entry = ttk.Entry(frame_input, width=50)
        self.desc_entry.grid(row=1, column=1, columnspan=3, padx=6, pady=6)

        # ===================== BOTONES =====================
        frame_btn = tk.Frame(main, bg="#0f172a")
        frame_btn.pack(fill="x", pady=8)

        ttk.Button(frame_btn, text="➕ Agregar Evento", style="Success.TButton",
                   command=self.agregar_evento).pack(side="left", padx=5)

        ttk.Button(frame_btn, text="🗑 Eliminar", style="Danger.TButton",
                   command=self.eliminar_evento).pack(side="left", padx=5)

        ttk.Button(frame_btn, text="❌ Salir", style="Secondary.TButton",
                   command=root.quit).pack(side="right", padx=5)

        # ===================== TABLA =====================
        frame_table = tk.Frame(main, bg="#111827")
        frame_table.pack(fill="both", expand=True)

        columnas = ("Fecha", "Hora", "Descripción")
        self.tree = ttk.Treeview(frame_table, columns=columnas, show="headings")

        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")

        self.tree.pack(fill="both", expand=True, padx=6, pady=6)

        # Scrollbar
        scrollbar = ttk.Scrollbar(frame_table, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        self.cargar_eventos()

    # ===================== ESTILOS =====================
    def estilos(self):
        style = ttk.Style()
        style.theme_use("clam")

        # Botones modernos
        style.configure("Success.TButton", background="#22c55e", foreground="white", padding=6)
        style.map("Success.TButton", background=[("active", "#16a34a")])

        style.configure("Danger.TButton", background="#ef4444", foreground="white", padding=6)
        style.map("Danger.TButton", background=[("active", "#dc2626")])

        style.configure("Secondary.TButton", background="#3b82f6", foreground="white", padding=6)
        style.map("Secondary.TButton", background=[("active", "#2563eb")])

        # Tabla
        style.configure("Treeview",
                        background="#020617",
                        foreground="#e5e7eb",
                        fieldbackground="#020617",
                        rowheight=28)

        style.map("Treeview", background=[("selected", "#22c55e")])

    # ===================== FUNCIONES =====================
    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.desc_entry.get()

        if not fecha or not hora or not descripcion:
            messagebox.showwarning("Advertencia", "Completa todos los campos")
            return

        self.tree.insert("", "end", values=(fecha, hora, descripcion))
        self.guardar_eventos()

        self.hora_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    def eliminar_evento(self):
        seleccionado = self.tree.selection()

        if not seleccionado:
            messagebox.showwarning("Advertencia", "Selecciona un evento")
            return

        if messagebox.askyesno("Confirmar", "¿Eliminar evento?"):
            for item in seleccionado:
                self.tree.delete(item)

        self.guardar_eventos()

    def guardar_eventos(self):
        eventos = []
        for item in self.tree.get_children():
            eventos.append(self.tree.item(item)['values'])

        with open(ARCHIVO, 'w') as f:
            json.dump(eventos, f)

    def cargar_eventos(self):
        if os.path.exists(ARCHIVO):
            with open(ARCHIVO, 'r') as f:
                eventos = json.load(f)
                for evento in eventos:
                    self.tree.insert("", "end", values=evento)

# ===================== EJECUCIÓN =====================
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
