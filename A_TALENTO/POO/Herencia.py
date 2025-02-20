
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hablar(self):
        print("El animal hace un sonido.")


class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        
        super().__init__(nombre, edad)
        self.raza = raza

    def hablar(self):
        # Sobreescribimos el método "hablar" de la clase base
        print(f"{self.nombre} dice: ¡Guau!")

# Crear un objeto de la clase Perro
mi_perro = Perro("Rex", 3, "Labrador")

# Acceder a los atributos y métodos heredados de la clase Animal
print(mi_perro.nombre)  # Imprime: Rex
print(mi_perro.edad)    # Imprime: 3
print(mi_perro.raza)    # Imprime: Labrador

# Llamar al método sobrescrito "hablar"
mi_perro.hablar()  # Imprime: Rex dice: ¡Guau!
