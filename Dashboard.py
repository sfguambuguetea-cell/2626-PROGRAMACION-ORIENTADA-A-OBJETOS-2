import os
import subprocess


# ==================================================
# SE MANTIENEN TUS FUNCIONES ORIGINALES
# ==================================================

def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)

    try:
        with open(ruta_script_absoluta, 'r', encoding="utf-8") as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo

    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None

    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None


def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")


# ==================================================
# MENÚ POR SEMANAS (YA NO POR CARPETAS)
# ==================================================

def mostrar_menu():

    # Diccionario semana → tareas (NO carpetas)
    semanas = {
        "2": [
            "Método Polimorfismo",
            "Método Abstracción",
            "Herencia",
            "Encapsulamiento"
        ],
        "3": ["Ejemplo del Clima"],
        "4": ["Ejemplos del Mundo Real"],
        "5": ["Tipos de Datos"],
        "6": ["Cuenta Bancaria"],
        "7": ["Implementación de Constructores y Destructores"]
    }

    while True:

        print("\n===== DASHBOARD POO =====")
        print("Ingrese número de semana (2 a 7)")
        print("0 - Salir")

        semana = input("\nSemana: ")

        if semana == "0":
            print("Saliendo del programa...")
            break

        elif semana in semanas:

            print(f"\n📘 TAREAS DE LA SEMANA {semana}:\n")

            for tarea in semanas[semana]:
                print("•", tarea)

        else:
            print("⚠ Semana incorrecta. Intente otra vez.")


# ==================================================
# EJECUCIÓN
# ==================================================

if __name__ == "__main__":
    mostrar_menu()

