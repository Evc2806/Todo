# Definir la clase Persona
class Persona:
    # Método constructor
    def __init__(self, nombre, edad):
        self.nombre2 = nombre
        self.edad2 = edad
    
    # Método para saludar
    def saludar(self):
        # Imprimir usando comas
        print("¡Hola! Mi nombre es", self.nombre2, "y tengo", self.edad2, "años.")

# Crear un objeto de la clase Persona
persona1 = Persona("Camilo", 30)

# Usar el método del objeto
persona1.saludar()

