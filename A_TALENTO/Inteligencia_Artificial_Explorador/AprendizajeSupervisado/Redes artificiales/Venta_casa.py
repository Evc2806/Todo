# Enunciado:
# Desarrollamos una red neuronal de una capa para predecir si una casa será vendida
# basada en dos características: el Tamaño de la Casa y el Número de Habitaciones.
# La red neuronal devolverá 1 si la casa será vendida y 0 si no lo será.

import numpy as np  # Importar la librería NumPy para cálculos numéricos

# Definir la función sigmoide que actúa como función de activación
def sigmoid(z):
    # La función sigmoide transforma el valor de entrada en un rango entre 0 y 1
    return 1 / (1 + np.exp(-z))

# Definir la función para el perceptrón simple
def perceptron_simple(X1, X2, W1, W2, b):
    # Calcular la suma ponderada de las entradas más el sesgo
    Z = (X1 * W1) + (X2 * W2) + b
    # Aplicar la función sigmoide para obtener la probabilidad
    Y = sigmoid(Z)
    return Y  # Retornar el valor de salida

# Definir los pesos y el sesgo
W1 = 0.5  # Peso para X1 (Tamaño de la Casa)
W2 = 0.7  # Peso para X2 (Número de Habitaciones)
b = -6.0  # Sesgo que ajusta la predicción

# Ejemplo de entradas: X1 (Tamaño de la Casa), X2 (Número de Habitaciones)
X1 = 100.0  # Tamaño de la casa en metros cuadrados
X2 = 3.0    # Número de habitaciones en la casa

# Calcular la salida utilizando la función del perceptrón
Y = perceptron_simple(X1, X2, W1, W2, b)

# Determinar si la casa será vendida o no (clasificación binaria)
if Y > 0.5:
    print("Resultado: La Casa Será Vendida (Y = {:.2f})".format(Y))
else:
    print("Resultado: La Casa No Será Vendida (Y = {:.2f})".format(Y))
