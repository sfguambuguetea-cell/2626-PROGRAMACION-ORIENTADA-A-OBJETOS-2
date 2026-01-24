
# Sistema de Facturación Mensual de Movistar Fabian Guambuguete
# Se utilizan clases, constructores (__init__) y destructores (__del__)

class ClienteMovistar:
    """
    Clase que representa a un cliente de Movistar.
    """

    def __init__(self, nombre, numero, plan, consumo_gb):
        """
        CONSTRUCTOR
        Este método se ejecuta automáticamente cuando se crea un objeto.
        Inicializa los atributos del cliente.
        """
        self.nombre = nombre
        self.numero = numero
        self.plan = plan
        self.consumo_gb = consumo_gb
        print(f"Cliente {self.nombre} registrado correctamente.")

    def __del__(self):
        """
        DESTRUCTOR
        Este método se ejecuta automáticamente cuando el objeto es eliminado
        o el programa finaliza. Se usa para liberar recursos o mostrar mensajes.
        """
        print(f"Cliente {self.nombre} eliminado del sistema.")

    def calcular_factura(self):
        """
        Calcula el valor de la factura mensual según el plan contratado.
        """
        if self.plan == "Básico":
            costo_base = 15
            limite_gb = 5
        elif self.plan == "Intermedio":
            costo_base = 25
            limite_gb = 10
        elif self.plan == "Premium":
            costo_base = 40
            limite_gb = 20
        else:
            print("Plan no válido")
            return 0

        # Costo adicional si excede el consumo de datos
        if self.consumo_gb > limite_gb:
            extra = (self.consumo_gb - limite_gb) * 2
        else:
            extra = 0

        return costo_base + extra

    def mostrar_factura(self):
        """
        Muestra el detalle de la factura mensual del cliente.
        """
        total = self.calcular_factura()
        print("\n--- FACTURA MENSUAL MOVISTAR ---")
        print(f"Cliente: {self.nombre}")
        print(f"Número: {self.numero}")
        print(f"Plan: {self.plan}")
        print(f"Consumo: {self.consumo_gb} GB")
        print(f"Total a pagar: ${total}")
        print("--------------------------------")


# PROGRAMA PRINCIPAL
# Aquí se crean y utilizan los objetos

cliente1 = ClienteMovistar("Fabian Guambuguete Fuentes ", "0990947613", "Intermedio", 12)
cliente1.mostrar_factura()

# Eliminación manual del objeto para activar el destructor
del cliente1
