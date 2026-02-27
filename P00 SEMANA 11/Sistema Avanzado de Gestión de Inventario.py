# Fabian Guambuguete POO SEMANA 11

import json
import os

# ==============================
# CLASE PRODUCTO
# ==============================
class Producto:
    """
    Representa un producto dentro del inventario.
    Utiliza encapsulamiento mediante getters y setters.
    """

    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    # Convertir objeto a diccionario (para guardar en archivo)
    def to_dict(self):
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "cantidad": self.__cantidad,
            "precio": self.__precio
        }

    # Crear objeto desde diccionario (al cargar archivo)
    @staticmethod
    def from_dict(data):
        return Producto(data["id"], data["nombre"], data["cantidad"], data["precio"])


# ==============================
# CLASE INVENTARIO
# ==============================
class Inventario:
    """
    Gestiona los productos utilizando un diccionario.
    - Clave: ID del producto
    - Valor: Objeto Producto
    """

    def __init__(self):
        self.productos = {}  # Diccionario principal
        self.archivo = "inventario.json"
        self.cargar_archivo()

    # --------------------------
    # Añadir producto
    # --------------------------
    def añadir_producto(self, producto):
        if producto.get_id() in self.productos:
            print(" Error: El ID ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            print("Producto añadido correctamente.")

    # --------------------------
    # Eliminar producto
    # --------------------------
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(" Producto eliminado correctamente.")
        else:
            print(" Producto no encontrado.")

    # --------------------------
    # Actualizar producto
    # --------------------------
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            print(" Producto actualizado correctamente.")
        else:
            print(" Producto no encontrado.")

    # --------------------------
    # Buscar por nombre
    # --------------------------
    def buscar_por_nombre(self, nombre):
        encontrados = [
            p for p in self.productos.values()
            if nombre.lower() in p.get_nombre().lower()
        ]

        if encontrados:
            for p in encontrados:
                self.mostrar_producto(p)
        else:
            print(" No se encontraron productos.")

    # --------------------------
    # Mostrar producto
    # --------------------------
    def mostrar_producto(self, producto):
        print("----------------------------")
        print(f"ID: {producto.get_id()}")
        print(f"Nombre: {producto.get_nombre()}")
        print(f"Cantidad: {producto.get_cantidad()}")
        print(f"Precio: ${producto.get_precio():.2f}")

    # --------------------------
    # Mostrar todos
    # --------------------------
    def mostrar_todos(self):
        if not self.productos:
            print(" Inventario vacío.")
        else:
            for producto in self.productos.values():
                self.mostrar_producto(producto)

    # --------------------------
    # Guardar en archivo (JSON)
    # --------------------------
    def guardar_archivo(self):
        with open(self.archivo, "w") as f:
            json.dump(
                {id: p.to_dict() for id, p in self.productos.items()},
                f,
                indent=4
            )
        print("💾 Inventario guardado correctamente.")

    # --------------------------
    # Cargar desde archivo
    # --------------------------
    def cargar_archivo(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as f:
                datos = json.load(f)
                for id, info in datos.items():
                    self.productos[id] = Producto.from_dict(info)


# ==============================
# MENÚ INTERACTIVO
# ==============================
def menu():
    inventario = Inventario()

    while True:
        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id_producto = input("Ingrese ID a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese ID a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío si no cambia): ")
            precio = input("Nuevo precio (dejar vacío si no cambia): ")

            inventario.actualizar_producto(
                id_producto,
                int(cantidad) if cantidad else None,
                float(precio) if precio else None
            )

        elif opcion == "4":
            nombre = input("Ingrese nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            inventario.guardar_archivo()

        elif opcion == "0":
            inventario.guardar_archivo()
            print(" Saliendo del sistema...")
            break

        else:
            print(" Opción inválida.")


# Ejecutar programa
if __name__ == "__main__":
    menu()