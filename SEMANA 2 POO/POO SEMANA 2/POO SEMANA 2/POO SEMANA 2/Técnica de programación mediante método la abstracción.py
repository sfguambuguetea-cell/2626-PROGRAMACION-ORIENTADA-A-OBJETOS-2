

class Persona:
    def __init__(self, nombre, apellido, genero, edad):
        # Atributos "privados" mediante abstracción
        self._nombre = nombre
        self._apellido = apellido
        self._genero = genero
        self._edad = edad

    # Método que muestra la información usando abstracción
    def mostrar_info(self):
        return f"{self._nombre} {self._apellido} ({self._genero}), {self._edad} años"


# Crear un objeto con los datos solicitados
persona1 = Persona("Fabian", "Guambuguete", "Masculino", 38)

# Imprimir información
print(persona1.mostrar_info())