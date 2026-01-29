

# Clase base
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        return f"Vehículo {self.marca} {self.modelo}"


# Subclase: Auto
class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def descripcion(self):
        return f"Auto {self.marca} {self.modelo} - Puertas: {self.puertas}"


# Subclase: Moto
class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def descripcion(self):
        return f"Moto {self.marca} {self.modelo} - Cilindraje: {self.cilindrada}cc"


# Subclase: Camion
class Camion(Vehiculo):
    def __init__(self, marca, modelo, capacidad):
        super().__init__(marca, modelo)
        self.capacidad = capacidad

    def descripcion(self):
        return f"Camión {self.marca} {self.modelo} - Capacidad: {self.capacidad} toneladas"


# Polimorfismo en acción
vehiculos = [
    Auto("Toyota", "Corolla", 4),
    Moto("Yamaha", "R3", 321),
    Camion("Volvo", "FH16", 25)
]

for v in vehiculos:
    print(v.descripcion())