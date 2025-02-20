class Animal:
    def hacer_sonido(self):
        pass  # Método que será sobrescrito en las clases derivadas

class Perro(Animal):
    def hacer_sonido(self):
        print("¡Guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print("¡Miau!")

# Usando el polimorfismo(lista de instancias)
animales = [Perro(), Gato()]

for animal in animales:
    animal.hacer_sonido()
