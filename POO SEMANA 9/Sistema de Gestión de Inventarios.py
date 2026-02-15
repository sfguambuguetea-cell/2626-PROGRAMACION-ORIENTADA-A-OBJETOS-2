
# Fabian Guambuguete semana 9 POO
# SISTEMA DE INVENTARIO - TIENDA

# Este programa implementa un sistema básico de gestión de inventarios
# usando Programación Orientada a Objetos (POO).
# Permite: añadir, eliminar, actualizar, buscar y listar productos.


# CLASE PRODUCTO

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Constructor: inicializa los atributos del producto
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

    # Representación del producto
    def __str__(self):
        return f"ID: {self._id} | Nombre: {self._nombre} | Cantidad: {self._cantidad} | Precio: ${self._precio:.2f}"



# CLASE INVENTARIO

class Inventario:
    def __init__(self):
        # Lista donde se almacenan los productos
        self.productos = []

    # Verificar si ID existe
    def _buscar_por_id(self, id_producto):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                return producto
        return None

    # Añadir producto asegurando ID único
    def agregar_producto(self, producto):
        if self._buscar_por_id(producto.get_id()) is None:
            self.productos.append(producto)
            print("Producto agregado correctamente.")
        else:
            print("Error: Ya existe un producto con ese ID.")

    # Eliminar producto
    def eliminar_producto(self, id_producto):
        producto = self._buscar_por_id(id_producto)
        if producto:
            self.productos.remove(producto)
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")

    # Actualizar cantidad o precio
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        producto = self._buscar_por_id(id_producto)
        if producto:
            if nueva_cantidad is not None:
                producto.set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                producto.set_precio(nuevo_precio)
            print("Producto actualizado correctamente.")
        else:
            print("Producto no encontrado.")

    # Buscar por nombre (coincidencia parcial)
    def buscar_por_nombre(self, nombre):
        encontrados = []
        nombre = nombre.lower()
        for producto in self.productos:
            if nombre in producto.get_nombre().lower():
                encontrados.append(producto)
        return encontrados

    # Mostrar inventario completo
    def mostrar_inventario(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            print("\n===== INVENTARIO =====")
            for producto in self.productos:
                print(producto)
            print("======================\n")

# INTERFAZ DE CONSOLA


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

        # Añadir producto
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

        # Eliminar producto
        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        # Actualizar producto
        elif opcion == "3":
            id_producto = input("Ingrese ID del producto: ")
            print("Dejar vacío si no desea cambiar un valor")

            cantidad = input("Nueva cantidad: ")
            precio = input("Nuevo precio: ")

            nueva_cantidad = int(cantidad) if cantidad != "" else None
            nuevo_precio = float(precio) if precio != "" else None

            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        # Buscar producto
        elif opcion == "4":
            nombre = input("Ingrese nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)

            if resultados:
                print("\nResultados encontrados:")
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos.")

        # Mostrar inventario
        elif opcion == "5":
            inventario.mostrar_inventario()

        # Salir
        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


# Ejecutar programa
if __name__ == "__main__":
    menu()
