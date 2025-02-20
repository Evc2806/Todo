class Vehiculo:
    def __init__(self, marca):
        self.marca = marca
    
    def mostrar_info(self):
        print(f"Vehículo de la marca {self.marca}")

class Coche(Vehiculo):
    def mostrar_info(self):
        print(f"Coche de la marca {self.marca}")

class Moto(Vehiculo):
    def mostrar_info(self):
        print(f"Moto de la marca {self.marca}")

# Usando polimorfismo
vehiculos = [Coche("Toyota"), Moto("Yamaha")]

for vehiculo in vehiculos:
    vehiculo.mostrar_info()
