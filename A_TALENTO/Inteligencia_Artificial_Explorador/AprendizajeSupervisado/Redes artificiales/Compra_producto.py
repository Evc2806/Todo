# Enunciado:
# Desarrollamos una red neuronal de una capa para predecir si un cliente comprará un producto
# basada en dos características: la Edad del cliente y su Salario.
# La red neuronal devolverá 1 si el cliente comprará el producto y 0 si no lo hará.

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
W1 = 0.3  # Peso para X1 (Edad)
W2 = 0.7  # Peso para X2 (Salario)
b = -5.0  # Sesgo que ajusta la predicción

# Ejemplo de entradas: X1 (Edad), X2 (Salario)
X1 = 30.0  # Edad del cliente
X2 = 55000.0  # Salario del cliente

# Calcular la salida utilizando la función del perceptrón
Y = perceptron_simple(X1, X2, W1, W2, b)

# Determinar si el cliente comprará el producto o no (clasificación binaria)
if Y > 0.5:
    print("Resultado: Comprará el Producto (Y = {:.2f})".format(Y))
else:
    print("Resultado: No Comprará el Producto (Y = {:.2f})".format(Y))
