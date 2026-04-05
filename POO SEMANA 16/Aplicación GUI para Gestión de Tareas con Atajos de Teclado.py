# POO SEMANA 16 Fabian Guambuguete


import tkinter as tk
from tkinter import messagebox

class ModernTaskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager Moderno")
        self.root.geometry("520x450")
        self.root.configure(bg="#1e1e2f")

        self.tasks = []

        # ===== ESTILOS =====
        self.bg = "#1e1e2f"
        self.card = "#2a2a40"
        self.accent = "#6c63ff"
        self.text = "#ffffff"
        self.done = "#888888"

        # ===== CONTENEDOR =====
        container = tk.Frame(root, bg=self.bg)
        container.pack(pady=15)

        # ===== ENTRY =====
        self.entry = tk.Entry(container, width=30, font=("Segoe UI", 12), bd=0, relief="flat")
        self.entry.grid(row=0, column=0, padx=10, ipady=6)

        add_btn = tk.Button(container, text="Añadir", bg=self.accent, fg="white",
                            font=("Segoe UI", 10, "bold"), bd=0, padx=10,
                            command=self.add_task)
        add_btn.grid(row=0, column=1, padx=5)

        # ===== LISTBOX =====
        self.listbox = tk.Listbox(root, width=50, height=15,
                                 font=("Segoe UI", 11),
                                 bg=self.card, fg=self.text,
                                 selectbackground=self.accent,
                                 bd=0, highlightthickness=0)
        self.listbox.pack(pady=15)

        # ===== BOTONES =====
        btn_frame = tk.Frame(root, bg=self.bg)
        btn_frame.pack()

        complete_btn = tk.Button(btn_frame, text="✔ Completar", bg="#00c896", fg="white",
                                 font=("Segoe UI", 10, "bold"), bd=0, padx=10,
                                 command=self.complete_task)
        complete_btn.grid(row=0, column=0, padx=5)

        delete_btn = tk.Button(btn_frame, text="🗑 Eliminar", bg="#ff5c5c", fg="white",
                               font=("Segoe UI", 10, "bold"), bd=0, padx=10,
                               command=self.delete_task)
        delete_btn.grid(row=0, column=1, padx=5)

        # ===== ATAJOS =====
        root.bind("<Return>", lambda e: self.add_task())
        root.bind("<c>", lambda e: self.complete_task())
        root.bind("<Delete>", lambda e: self.delete_task())
        root.bind("<Escape>", lambda e: root.quit())

    # ===== FUNCIONES =====
    def add_task(self):
        text = self.entry.get().strip()
        if text == "":
            messagebox.showwarning("Aviso", "Escribe una tarea")
            return

        self.tasks.append((text, False))
        self.entry.delete(0, tk.END)
        self.update_list()

    def complete_task(self):
        try:
            index = self.listbox.curselection()[0]
            task, _ = self.tasks[index]
            self.tasks[index] = (task, True)
            self.update_list()
        except:
            messagebox.showwarning("Aviso", "Selecciona una tarea")

    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            del self.tasks[index]
            self.update_list()
        except:
            messagebox.showwarning("Aviso", "Selecciona una tarea")

    def update_list(self):
        self.listbox.delete(0, tk.END)
        for i, (task, done) in enumerate(self.tasks):
            if done:
                self.listbox.insert(tk.END, f"✔ {task}")
                self.listbox.itemconfig(i, fg=self.done)
            else:
                self.listbox.insert(tk.END, f"• {task}")
                self.listbox.itemconfig(i, fg=self.text)


if __name__ == "__main__":
    root = tk.Tk()
    app = ModernTaskApp(root)
    root.mainloop()
