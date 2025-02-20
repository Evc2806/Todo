class Perro:
    def hablar(self):
        return "Guau!"

class Gato:
    def hablar(self):
        return "Miau!"

class AnimalFactory:
    def crear_animal(self, tipo):
        if tipo == "perro":
            return Perro()
        elif tipo == "gato":
            return Gato()
        else:
            raise ValueError("Tipo de animal no reconocido")

# Usando la fábrica:
factory = AnimalFactory()

# Creamos un perro
animal1 = factory.crear_animal("perro")
print(animal1.hablar())  # Imprime 'Guau!'

# Creamos un gato
animal2 = factory.crear_animal("gato")
print(animal2.hablar())  # Imprime 'Miau!'
