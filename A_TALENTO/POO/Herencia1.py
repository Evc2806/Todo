class Animal:
    def __init__(self, nombre, edad):
    
        self.nombre = nombre
        self.edad = edad

    def hablar(self):
 
        print("El animal hace un sonido.")

    def informacion(self):
      
        print(f"Nombre: {self.nombre}, Edad: {self.edad} años.")



class Gato(Animal):
    def __init__(self, nombre, edad, raza):
      
        super().__init__(nombre, edad)
        
        self.raza = raza

    def hablar(self):
        # Sobrescribimos el método hablar para los gatos
        print(f"{self.nombre} maúlla.")

    def ronronear(self):
        
        print(f"{self.nombre} está ronroneando.")

    def informacion(self):
        # Sobrescribimos el método de información para añadir la raza
        super().informacion()  # Llamamos al método de la superclase
        print(f"Raza: {self.raza}")


# Crear un objeto de la clase Gato
mi_gato = Gato("Whiskers", 2, "Persa")

# Mostrar la información del gato
print("Información del Gato:")
mi_gato.informacion()  # Imprime: Nombre, Edad, Raza

# Llamar al método sobrescrito hablar()
print("\nEl gato habla:")
mi_gato.hablar()  # Imprime: Whiskers maúlla.

# Hacer que el gato ronronee
print("\nEl gato ronronea:")
mi_gato.ronronear()  # Imprime: Whiskers está ronroneando.

# Llamar al método hablar de la superclase (Animal)
print("\nEl método de la superclase hablar:")
super(Gato, mi_gato).hablar()  # Esto ejecuta el método hablar de Animal
