# Clase base
class Persona:
    def __init__(self, nombre, edad):
        # Atributos protegidos
        self._nombre = nombre
        self._edad = edad

    def mostrar_informacion(self):
        # Método para mostrar la información
        print(f"Nombre: {self._nombre}, Edad: {self._edad}")


# Crear un objeto de la clase Persona
persona = Persona("Carlos", 25)

# Mostrar la información de la persona
persona.mostrar_informacion()
