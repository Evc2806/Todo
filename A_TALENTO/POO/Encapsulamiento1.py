class Perro:
    def __init__(self, nombre, edad, raza):
        # Atributos privados
        self.__nombre = nombre
        self.__edad = edad
        self.__raza = raza

    # Método getter para obtener el nombre del perro
    def obtener_nombre(self):
        return self.__nombre

    # Método getter para obtener la edad del perro
    def obtener_edad(self):
        return self.__edad

    # Método getter para obtener la raza del perro
    def obtener_raza(self):
        return self.__raza

    # Método setter para cambiar el nombre del perro
    def cambiar_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    # Método para aumentar la edad del perro
    def cumplir_edad(self):
        self.__edad=self.__edad+1

    # Método para saludar
    def saludar(self):
        print(f"Hola, soy un {self.__raza} llamado {self.__nombre}, tengo {self.__edad} años.")

# Crear un objeto de la clase Perro
mi_perro = Perro("Max", 5, "Labrador")

# Saludar (se imprimirá el saludo con el nombre, edad y raza)
mi_perro.saludar()  # "Hola, soy un Labrador llamado Max, tengo 5 años."

# Obtener y mostrar el nombre, edad y raza del perro
print("Nombre:", mi_perro.obtener_nombre())  # "Max"
print("Edad:", mi_perro.obtener_edad())  # 5
print("Raza:", mi_perro.obtener_raza())  # "Labrador"

# Cambiar el nombre del perro
mi_perro.cambiar_nombre("Ruby")
print("\nDespués de cambiar el nombre...")
print("Nombre:", mi_perro.obtener_nombre())  # "Ruby"

# Cumplir un año más
mi_perro.cumplir_edad()
print("\nDespués de cumplir años...")
print("Edad:", mi_perro.obtener_edad())  # 6

# Saludar de nuevo con los nuevos valores
mi_perro.saludar()  # "Hola, soy un Labrador llamado Ruby, tengo 6 años."
