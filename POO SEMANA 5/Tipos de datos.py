
# Tarea: Tipos de datos, Identificadores. Implementación y Publicación de Código en Python
# Fabian Guambuguete

"""
Programa: Cálculo del área de un rectángulo
Descripción: Este programa solicita al usuario el largo y el ancho de un rectángulo,
verifica si los valores son válidos y calcula el área correspondiente.
"""

# Función que calcula el área de un rectángulo
def calcular_area_rectangulo(largo, ancho):
    """
    Calcula el área de un rectángulo.
    Parámetros:
        largo (float): longitud del rectángulo
        ancho (float): ancho del rectángulo
    Retorna:
        float: área del rectángulo
    """
    area = largo * ancho
    return area


# Solicitar datos al usuario (tipo string)
nombre_usuario = input("Ingrese su nombre: ")

# Solicitar dimensiones del rectángulo (tipo float)
largo_rectangulo = float(input("Ingrese el largo del rectángulo: "))
ancho_rectangulo = float(input("Ingrese el ancho del rectángulo: "))

# Validar si las dimensiones son positivas (tipo boolean)
datos_validos = largo_rectangulo > 0 and ancho_rectangulo > 0

# Condicional para verificar los datos
if datos_validos:
    # Calcular el área
    area_rectangulo = calcular_area_rectangulo(largo_rectangulo, ancho_rectangulo)

    # Mostrar el resultado
    print(f"\nHola {nombre_usuario}, el área del rectángulo es: {area_rectangulo} unidades cuadradas.")
else:
    # Mensaje de error si los datos no son válidos
    print("\nError: El largo y el ancho deben ser valores positivos.")