# Clase Motor
class Motor:
    def arrancar(self):
        print("El motor ha arrancado.")

# Clase Coche que tiene un Motor
class Coche:
    def __init__(self):
        self.motor = Motor()  # Python está creando una nueva instancia de la clase motor

    def conducir(self):
        print("El coche está conduciendo.")
        self.motor.arrancar()  # Usamos el motor del coche

# Crear una instancia de Coche
mi_coche = Coche()
mi_coche.conducir()  # Imprime: "El coche está conduciendo." y "El motor ha arrancado."
