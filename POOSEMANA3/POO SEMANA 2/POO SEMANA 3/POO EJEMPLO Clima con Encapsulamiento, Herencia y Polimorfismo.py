
#Diseña una solución utilizando el paradigma de POO.
#Crea una clase que represente la información diaria del clima.
#Utiliza métodos de la clase para ingresar datos y calcular el promedio semanal.
#Asegúrate de aplicar conceptos como encapsulamiento, herencia o polimorfismo


# ----------------------------
# 1. Encapsulamiento
# ----------------------------
class DiaClima:
    def __init__(self, dia, temperatura):
        self._dia = dia               # Atributos encapsulados (protegidos)
        self._temperatura = temperatura

    def obtener_info(self):
        return f"{self._dia}: {self._temperatura}°C"

    # Encapsulamiento: control para cambiar temperatura
    def set_temperatura(self, nueva_temp):
        if nueva_temp < -50 or nueva_temp > 60:
            print("Temperatura fuera de rango.")
        else:
            self._temperatura = nueva_temp

    def get_temperatura(self):
        return self._temperatura


# ----------------------------
# 2. Herencia
# ----------------------------
class SemanaClima(DiaClima):
    def __init__(self):
        self.dias = []  # lista de objetos DiaClima

    def agregar_dia(self, dia_clima):
        self.dias.append(dia_clima)

    def promedio(self):
        total = sum(d.get_temperatura() for d in self.dias)
        return total / len(self.dias)


# ----------------------------
# 3. Polimorfismo
# ----------------------------
class DiaClimaSensacion(DiaClima):
    # Redefine (sobrescribe) método obtener_info → POLIMORFISMO
    def obtener_info(self):
        sensacion = "Frío" if self._temperatura < 18 else "Cálido"
        return f"{self._dia}: {self._temperatura}°C - Sensación: {sensacion}"


# ----------------------------
# Ejecución del ejemplo
# ----------------------------
# Crear semana
semana = SemanaClima()

# Crear objetos días (algunos normales, uno con polimorfismo)
semana.agregar_dia(DiaClima("Lunes", 22))
semana.agregar_dia(DiaClima("Martes", 19))
semana.agregar_dia(DiaClimaSensacion("Miércoles", 15))  # polimorfismo
semana.agregar_dia(DiaClima("Jueves", 25))
semana.agregar_dia(DiaClimaSensacion("Viernes", 28))   # polimorfismo

# Mostrar días
print("=== Datos del clima semanal ===")
for dia in semana.dias:
    print(dia.obtener_info())  # Usa polimorfismo si aplica

# Promedio semanal
print("\nPromedio semanal:", semana.promedio(), "°C")