# Definir la clase Libro
class Libro:
    # Método constructor
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo  # Atributo: título del libro
        self.autor = autor    # Atributo: autor del libro
        self.paginas = paginas  # Atributo: número de páginas

    # Método para imprimir la descripción del libro
    def descripcion(self):
        print(f"El libro '{self.titulo}' fue escrito por {self.autor} y tiene {self.paginas} páginas.")

# Crear un objeto de la clase Libro
libro1 = Libro("Python para Todos", "Juan Pérez", 250)

# Acceder a los atributos
print(f"Título: {libro1.titulo}")
print(f"Autor: {libro1.autor}")
print(f"Páginas: {libro1.paginas}")

# Llamar al método descripcion
libro1.descripcion()
