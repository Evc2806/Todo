
class Perro:
    def __init__(self, nombre):
        self.__nombre = nombre  # Atributo privado

    # Método para obtener el nombre
    def obtener_nombre(self):
        return self.__nombre

    # Método para cambiar el nombre
    def cambiar_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

# Crear una instancia de Perro
mi_perro = Perro("Rex")

# Obtener el nombre usando el método público
print(mi_perro.obtener_nombre())  # Imprime: Rex

# Cambiar el nombre usando el método público
mi_perro.cambiar_nombre("Max")

# Verificar el nuevo nombre
print(mi_perro.obtener_nombre())  # Imprime: Max
