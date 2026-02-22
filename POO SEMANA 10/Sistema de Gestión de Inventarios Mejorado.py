

# ==============================
# SISTEMA DE INVENTARIO - TIENDA (MEJORADO)
# ==============================
# Ahora el sistema:
# ✔ Guarda los productos en un archivo inventario.txt
# ✔ Carga automáticamente los datos al iniciar
# ✔ Maneja excepciones de archivos
# ✔ Notifica al usuario sobre operaciones exitosas o fallidas


# ------------------------------
# CLASE PRODUCTO
# ------------------------------
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Setters
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self._cantidad = cantidad
        else:
            print("La cantidad no puede ser negativa.")

    def set_precio(self, precio):
        if precio >= 0:
            self._precio = precio
        else:
            print("El precio no puede ser negativo.")

    # Formato para guardar en archivo
    def to_file_format(self):
        return f"{self._id},{self._nombre},{self._cantidad},{self._precio}\n"

    # Representación del producto
    def __str__(self):
        return f"ID: {self._id} | Nombre: {self._nombre} | Cantidad: {self._cantidad} | Precio: ${self._precio:.2f}"


# ------------------------------
# CLASE INVENTARIO
# ------------------------------
class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_desde_archivo()

    # --------------------------
    # CARGAR INVENTARIO DESDE ARCHIVO
    # --------------------------
    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, "r") as f:
                for linea in f:
                    id_producto, nombre, cantidad, precio = linea.strip().split(",")
                    producto = Producto(id_producto, nombre, int(cantidad), float(precio))
                    self.productos.append(producto)
            print("Inventario cargado correctamente desde archivo.")
        except FileNotFoundError:
            # Si el archivo no existe, lo crea vacío
            print("Archivo no encontrado. Se creará uno nuevo.")
            try:
                open(self.archivo, "w").close()
            except PermissionError:
                print("Error: No se tienen permisos para crear el archivo.")
        except PermissionError:
            print("Error: No se tienen permisos para leer el archivo.")
        except Exception as e:
            print(f"Error inesperado al cargar archivo: {e}")

    # --------------------------
    # GUARDAR INVENTARIO EN ARCHIVO
    # --------------------------
    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as f:
                for producto in self.productos:
                    f.write(producto.to_file_format())
            print("Inventario guardado correctamente en archivo.")
        except PermissionError:
            print("Error: No se tienen permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error inesperado al guardar archivo: {e}")

    # --------------------------
    # MÉTODOS DE INVENTARIO
    # --------------------------
    def _buscar_por_id(self, id_producto):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                return producto
        return None

    def agregar_producto(self, producto):
        if self._buscar_por_id(producto.get_id()) is None:
            self.productos.append(producto)
            self.guardar_en_archivo()
            print("Producto agregado correctamente y guardado en archivo.")
        else:
            print("Error: Ya existe un producto con ese ID.")

    def eliminar_producto(self, id_producto):
        producto = self._buscar_por_id(id_producto)
        if producto:
            self.productos.remove(producto)
            self.guardar_en_archivo()
            print("Producto eliminado correctamente y archivo actualizado.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        producto = self._buscar_por_id(id_producto)
        if producto:
            if nueva_cantidad is not None:
                producto.set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                producto.set_precio(nuevo_precio)
            self.guardar_en_archivo()
            print("Producto actualizado correctamente y archivo guardado.")
        else:
            print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        encontrados = []
        nombre = nombre.lower()
        for producto in self.productos:
            if nombre in producto.get_nombre().lower():
                encontrados.append(producto)
        return encontrados

    def mostrar_inventario(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            print("\n===== INVENTARIO =====")
            for producto in self.productos:
                print(producto)
            print("======================\n")


# ------------------------------
# INTERFAZ DE CONSOLA
# ------------------------------
def menu():
    inventario = Inventario()

    while True:
        print("""
========= MENU =========
1. Añadir producto
2. Eliminar producto
3. Actualizar producto
4. Buscar producto por nombre
5. Mostrar inventario
0. Salir
========================
""")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_producto = input("Ingrese ID: ")
                nombre = input("Ingrese nombre: ")
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))

                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print("Error: Datos inválidos.")

        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese ID del producto: ")
            print("Dejar vacío si no desea cambiar un valor")

            cantidad = input("Nueva cantidad: ")
            precio = input("Nuevo precio: ")

            try:
                nueva_cantidad = int(cantidad) if cantidad != "" else None
                nuevo_precio = float(precio) if precio != "" else None
                inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)
            except ValueError:
                print("Error: Datos inválidos.")

        elif opcion == "4":
            nombre = input("Ingrese nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)

            if resultados:
                print("\nResultados encontrados:")
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos.")

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


# Ejecutar programa
if __name__ == "__main__":
    menu()