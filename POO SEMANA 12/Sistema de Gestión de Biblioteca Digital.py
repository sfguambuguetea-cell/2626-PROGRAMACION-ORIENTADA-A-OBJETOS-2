# POO SEMANA 13 FABIAN GUAMBUGUETE

# ============================================
# SISTEMA DE GESTIÓN DE BIBLIOTECA DIGITAL
# ============================================
# Este programa permite gestionar una biblioteca digital
# utilizando Programación Orientada a Objetos (POO).
# Se administran libros, usuarios y préstamos.

# ============================================
# CLASE LIBRO
# ============================================
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Tupla para almacenar título y autor (datos inmutables)
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn
        self.disponible = True

    def obtener_titulo(self):
        return self.info[0]

    def obtener_autor(self):
        return self.info[1]

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"Título: {self.info[0]}, Autor: {self.info[1]}, Categoría: {self.categoria}, ISBN: {self.isbn}, Estado: {estado}"


# ============================================
# CLASE USUARIO
# ============================================
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        # Lista para almacenar libros prestados
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def listar_libros(self):
        if not self.libros_prestados:
            print("No tiene libros prestados.")
        else:
            for libro in self.libros_prestados:
                print(libro)

    def __str__(self):
        return f"Usuario: {self.nombre} | ID: {self.id_usuario}"


# ============================================
# CLASE BIBLIOTECA
# ============================================
class Biblioteca:
    def __init__(self):
        # Diccionario de libros (ISBN -> objeto Libro)
        self.libros = {}
        # Diccionario de usuarios
        self.usuarios = {}
        # Conjunto para asegurar IDs únicos
        self.ids_usuarios = set()

    # -------------------------------
    # AÑADIR LIBRO
    # -------------------------------
    def añadir_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print("Libro añadido correctamente.")
        else:
            print("El libro ya existe.")

    # -------------------------------
    # QUITAR LIBRO
    # -------------------------------
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado.")
        else:
            print("Libro no encontrado.")

    # -------------------------------
    # REGISTRAR USUARIO
    # -------------------------------
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print("Usuario registrado correctamente.")
        else:
            print("El ID de usuario ya existe.")

    # -------------------------------
    # ELIMINAR USUARIO
    # -------------------------------
    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario eliminado.")
        else:
            print("Usuario no encontrado.")

    # -------------------------------
    # PRESTAR LIBRO
    # -------------------------------
    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]

            if libro.disponible:
                libro.disponible = False
                usuario.prestar_libro(libro)
                print("Libro prestado correctamente.")
            else:
                print("El libro ya está prestado.")
        else:
            print("Libro o usuario no encontrado.")

    # -------------------------------
    # DEVOLVER LIBRO
    # -------------------------------
    def devolver_libro(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]

            libro.disponible = True
            usuario.devolver_libro(libro)
            print("Libro devuelto correctamente.")
        else:
            print("Libro o usuario no encontrado.")

    # -------------------------------
    # BUSCAR LIBROS
    # -------------------------------
    def buscar_por_titulo(self, titulo):
        for libro in self.libros.values():
            if titulo.lower() in libro.obtener_titulo().lower():
                print(libro)

    def buscar_por_autor(self, autor):
        for libro in self.libros.values():
            if autor.lower() in libro.obtener_autor().lower():
                print(libro)

    def buscar_por_categoria(self, categoria):
        for libro in self.libros.values():
            if categoria.lower() in libro.categoria.lower():
                print(libro)

    # -------------------------------
    # LISTAR LIBROS DE UN USUARIO
    # -------------------------------
    def listar_libros_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            self.usuarios[id_usuario].listar_libros()
        else:
            print("Usuario no encontrado.")


# ============================================
# PRUEBA DEL SISTEMA
# ============================================
if __name__ == "__main__":

    biblioteca = Biblioteca()

    # Crear libros
    libro1 = Libro("Cien Años de Soledad", "Gabriel Garcia Marquez", "Novela", "111")
    libro2 = Libro("Don Quijote", "Miguel de Cervantes", "Clásico", "222")
    libro3 = Libro("Python para Todos", "Charles Severance", "Programación", "333")

    # Añadir libros
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)
    biblioteca.añadir_libro(libro3)

    # Crear usuarios
    usuario1 = Usuario("Alison", 1)
    usuario2 = Usuario("Fabian", 2)

    # Registrar usuarios
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestar libro
    biblioteca.prestar_libro("111", 1)

    # Listar libros prestados
    print("\nLibros prestados a Ana:")
    biblioteca.listar_libros_usuario(1)

    # Devolver libro
    biblioteca.devolver_libro("111", 1)

    # Buscar libro por autor
    print("\nBuscar libros por autor 'Cervantes':")
    biblioteca.buscar_por_autor("Cervantes")

    # Buscar por categoría
    print("\nBuscar libros de programación:")
    biblioteca.buscar_por_categoria("Programación")