
# Ejemplo una tienda     Fabian Guambuguete

# Clase Producto
# Representa un producto que se vende en la tienda
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre      # Nombre del producto
        self.precio = precio      # Precio unitario
        self.stock = stock        # Cantidad disponible

    def vender(self, cantidad):
        """
        Reduce el stock del producto si hay suficiente cantidad
        """
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        else:
            print(f"No hay suficiente stock de {self.nombre}")
            return False


# Clase Cliente
# Representa a un cliente de la tienda
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = []  # Lista de productos comprados

    def agregar_al_carrito(self, producto, cantidad):
        """
        Agrega un producto al carrito del cliente
        """
        if producto.vender(cantidad):
            self.carrito.append((producto.nombre, cantidad, producto.precio))
            print(f"{self.nombre} agregó {cantidad} {producto.nombre}(s) al carrito")


# Clase Tienda
# Representa la tienda y sus operaciones
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []  # Lista de productos disponibles

    def agregar_producto(self, producto):
        """
        Agrega un producto al inventario de la tienda
        """
        self.productos.append(producto)

    def mostrar_productos(self):
        """
        Muestra los productos disponibles en la tienda
        """
        print(f"\nProductos disponibles en {self.nombre}:")
        for producto in self.productos:
            print(f"- {producto.nombre}: ${producto.precio} | Stock: {producto.stock}")


# =========================
# Ejemplo de uso del sistema
# =========================

# Crear una tienda
mi_tienda = Tienda("Tienda Central")

# Crear productos
producto1 = Producto("Arroz", 1.50, 20)
producto2 = Producto("Leche", 0.90, 15)

# Agregar productos a la tienda
mi_tienda.agregar_producto(producto1)
mi_tienda.agregar_producto(producto2)

# Mostrar productos disponibles
mi_tienda.mostrar_productos()

# Crear un cliente
cliente1 = Cliente("Fabian Guambuguete")

# Cliente compra productos
cliente1.agregar_al_carrito(producto1, 5)
cliente1.agregar_al_carrito(producto2, 3)

# Mostrar productos después de la compra
mi_tienda.mostrar_productos()