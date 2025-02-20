import numpy as np
import sys


lista=[1,4,90,5,6,9]

#arreglo = np.array([lista])

arreglo = np.array([1,4,90,5,6,9])

#arreglo=np.arange(1,4,90) espera solo 2 o 3 valores

# Calcular el tamaño en bytes de la lista
memoria_lista = sys.getsizeof(lista) + sum(sys.getsizeof(elemento) for elemento in lista)

# Calcular el tamaño en bytes del arreglo de NumPy
memoria_arreglo = arreglo.nbytes

# Mostrar la diferencia de ocupación de memoria
print(f"Tamaño de la lista en bytes: {memoria_lista}")
print(f"Tamaño del arreglo de NumPy en bytes: {memoria_arreglo}")
print(f"Diferencia de ocupación de memoria: {memoria_lista - memoria_arreglo} bytes")