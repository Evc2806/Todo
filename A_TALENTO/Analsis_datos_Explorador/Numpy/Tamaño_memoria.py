import numpy as np
import sys

#numpy como np para manejar los arreglos de numpy.
#sys para obtener el tamaño en bytes de los objetos.

# Definir el tamaño de los arreglos
tamaño = 100

# Crear una lista de Python
lista = list(range(tamaño))

# Crear un arreglo de NumPy
arreglo = np.arange(tamaño)

# Calcular el tamaño en bytes de la lista
memoria_lista = sys.getsizeof(lista) + sum(sys.getsizeof(elemento) for elemento in lista)

# Calcular el tamaño en bytes del arreglo de NumPy
memoria_arreglo = arreglo.nbytes

# Mostrar la diferencia de ocupación de memoria
print(f"Tamaño de la lista en bytes: {memoria_lista}")
print(f"Tamaño del arreglo de NumPy en bytes: {memoria_arreglo}")
print(f"Diferencia de ocupación de memoria: {memoria_lista - memoria_arreglo} bytes")