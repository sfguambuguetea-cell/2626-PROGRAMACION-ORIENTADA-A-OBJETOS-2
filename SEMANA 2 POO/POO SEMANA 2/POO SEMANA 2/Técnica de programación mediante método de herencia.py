

# Clase base (superclase)
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        return "Este animal hace un sonido."

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad} años"


# Clase derivada (subclase) que hereda de Animal
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        # Llamar al constructor de Animal
        super().__init__(nombre, edad)
        self.raza = raza

    # Sobrescribir método
    def hacer_sonido(self):
        return "El perro ladra: ¡Guau guau!"

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Raza: {self.raza}"


# Crear un objeto de la clase Perro
mi_perro = Perro("Firulais", 4, "Pastor Alemán")

print(mi_perro.mostrar_info())
print(mi_perro.hacer_sonido())