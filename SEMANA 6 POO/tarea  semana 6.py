

#Programa: Sistema de Cuenta Bancaria
# Autor: Segundo Fabian Gambuguete
# Descripción: Aplicación de Programación Orientada
# a Objetos en Python



# Clase Base: CuentaBancaria

class CuentaBancaria:
    """
    Clase que representa una cuenta bancaria general.
    Aplica Encapsulación al proteger el saldo.
    """

    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial  # Atributo encapsulado

    def depositar(self, monto):
        """Permite depositar dinero en la cuenta"""
        if monto > 0:
            self.__saldo += monto
            print(f"Depósito realizado. Saldo actual: ${self.__saldo}")
        else:
            print("El monto a depositar debe ser mayor que cero.")

    def retirar(self, monto):
        """Permite retirar dinero si hay fondos suficientes"""
        if monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Retiro exitoso. Saldo actual: ${self.__saldo}")
        else:
            print("Fondos insuficientes para el retiro.")

    def get_saldo(self):
        """Método getter para acceder al saldo"""
        return self.__saldo

    def mostrar_informacion(self):
        """
        Método que muestra la información básica
        Este método será  (polimorfismo)
        """
        print("=== Información de la Cuenta ===")
        print(f"Titular: {self.titular}")
        print(f"Saldo: ${self.__saldo}")


# HERENCIA
# Clase Derivada: CuentaAhorro

class CuentaAhorro(CuentaBancaria):
    """
    Clase que representa una cuenta de ahorro.
    Hereda de CuentaBancaria.
    """

    def __init__(self, titular, saldo_inicial, tasa_interes):
        super().__init__(titular, saldo_inicial)
        self.tasa_interes = tasa_interes

    def mostrar_informacion(self):
        """
        Método sobrescrito que demuestra polimorfismo
        """
        print("=== Información de la Cuenta de Ahorro ===")
        print(f"Titular: {self.titular}")
        print(f"Saldo: ${self.get_saldo()}")
        print(f"Tasa de interés: {self.tasa_interes}%")



# Programa Principal


# Creación de un objeto de la clase base
cuenta_normal = CuentaBancaria(" Agustin Gomez", 1000)
cuenta_normal.depositar(500)
cuenta_normal.retirar(200)
cuenta_normal.mostrar_informacion()

print(" ")

# Creación de un objeto de la clase derivada
cuenta_ahorro = CuentaAhorro("Fabian Guambuguete", 2000, 4.5)
cuenta_ahorro.depositar(800)
cuenta_ahorro.mostrar_informacion()
