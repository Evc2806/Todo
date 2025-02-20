class Vehiculo:
    def __init__(self, marca, año):
        self.marca = marca
        self.año = año
    
    def mostrar_info(self):
        print(f"Vehículo de la marca {self.marca}, año {self.año}")

class Coche(Vehiculo):
    def __init__(self, marca, año, puertas):
        super().__init__(marca, año)
        self.puertas = puertas
    
    def mostrar_info(self):
        print(f"Coche de la marca {self.marca}, año {self.año}, con {self.puertas} puertas")

class Moto(Vehiculo):
    def __init__(self, marca, año, cilindrada):
        super().__init__(marca, año)
        self.cilindrada = cilindrada
    
    def mostrar_info(self):
        print(f"Moto de la marca {self.marca}, año {self.año}, con {self.cilindrada} cilindrada")

class Camion(Vehiculo):
    def __init__(self, marca, año, capacidad):
        super().__init__(marca, año)
        self.capacidad = capacidad
    
    def mostrar_info(self):
        print(f"Camión de la marca {self.marca}, año {self.año}, con {self.capacidad} toneladas de capacidad")

class Bicicleta(Vehiculo):
    def __init__(self, marca, año, tipo):
        super().__init__(marca, año)
        self.tipo = tipo
    
    def mostrar_info(self):
        print(f"Bicicleta de la marca {self.marca}, año {self.año}, tipo {self.tipo}")

# Lista de vehículos
vehiculos = [
    Coche("Toyota", 2020, 4),
    Moto("Yamaha", 2019, 600),
    Camion("Mercedes", 2018, 12),
    Bicicleta("Giant", 2022, "de montaña")
]

# Usando polimorfismo
for vehiculo in vehiculos:
    vehiculo.mostrar_info()
