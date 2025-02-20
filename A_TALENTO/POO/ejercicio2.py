# 1. Crear la clase Coche
class Automovil:
    def __init__(self, marca, modelo, año):
        # Atributos del coche
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    # 2. Método para mostrar la información del coche
    def informacion(self):
        print(f"El coche es un {self.marca} {self.modelo} del año {self.año}.")
        

# 3. Crear una instancia de la clase Coche con datos de ejemplo
mi_coche = Automovil("Toyota", "Corolla", 2020)

# 4. Acceder a los atributos del coche
print(f"Marca: {mi_coche.marca}")
print(f"Modelo: {mi_coche.modelo}")
print(f"Año: {mi_coche.año}")

# Llamar al método informacion()
mi_coche.informacion()
