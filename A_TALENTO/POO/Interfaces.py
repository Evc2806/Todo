from abc import ABC, abstractmethod  ## Importamos la librería ABC y el decorador abstractmethod modifica o extiende el comportamiento de otras funciones o métodos.

# Definiendo la "interfaz" con una clase abstracta
class VehiculoInterface(ABC):  # La clase VehiculoInterface es una clase abstracta que hereda de ABC
    @abstractmethod  # Indicamos que este método es abstracto y debe ser implementado en las subclases
    def mover(self):  # Este método no tiene implementación en la clase base, debe implementarse en las subclases
        pass  # 'pass' indica que no hay implementación en esta clase abstracta


# Clase Coche implementando la interfaz
class Coche(VehiculoInterface):  # La clase Coche hereda de VehiculoInterface, por lo tanto debe implementar 'mover'
    def mover(self):  # Implementación del método 'mover' específico para la clase Coche
        print("El coche está conduciendo por la carretera.")  # Lo que se imprime cuando el coche se mueve


# Clase Bicicleta implementando la interfaz
class Bicicleta(VehiculoInterface):  # La clase Bicicleta también hereda de VehiculoInterface
    def mover(self):  # Implementación del método 'mover' específico para la clase Bicicleta
        print("La bicicleta está siendo pedaleada por el ciclista.")  # Lo que se imprime cuando la bicicleta se mueve


# Lista de vehículos
vehiculos = [Coche(), Bicicleta()]  # Creamos una lista con instancias de las clases Coche y Bicicleta


# Usando polimorfismo: llamando al método 'mover' en la lista
for vehiculo in vehiculos:  # Iteramos sobre cada objeto en la lista 'vehiculos'
    vehiculo.mover()  # Llamamos al método 'mover' de cada objeto en la lista. El método específico depende del tipo de objeto
