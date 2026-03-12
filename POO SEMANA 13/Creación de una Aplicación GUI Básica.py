# Fabian Guambuguete POO semana 13

# Importar la librería Tkinter
import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Datos")
ventana.geometry("400x350")

# ------------------------------
# Función para agregar elementos
# ------------------------------
def agregar_dato():
    dato = entrada_texto.get()  # Obtener texto del campo

    if dato != "":
        lista_datos.insert(tk.END, dato)  # Agregar a la lista
        entrada_texto.delete(0, tk.END)   # Limpiar campo de texto
    else:
        messagebox.showwarning("Advertencia", "Ingrese un dato primero")

# ------------------------------
# Función para limpiar datos
# ------------------------------
def limpiar_datos():
    lista_datos.delete(0, tk.END)  # Borra toda la lista
    entrada_texto.delete(0, tk.END)  # Limpia campo de texto

# ------------------------------
# Componentes de la interfaz
# ------------------------------

# Etiqueta
label = tk.Label(ventana, text="Ingrese un dato:")
label.pack(pady=10)

# Campo de texto
entrada_texto = tk.Entry(ventana, width=30)
entrada_texto.pack(pady=5)

# Botón agregar
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Botón limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_datos)
boton_limpiar.pack(pady=5)

# Lista para mostrar datos
lista_datos = tk.Listbox(ventana, width=40, height=10)
lista_datos.pack(pady=15)

# Ejecutar la aplicación
ventana.mainloop()