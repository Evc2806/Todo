# Importar NumPy para los cálculos
import numpy as np

# Función sigmoide para la activación
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Definir la red neuronal de una capa (perceptrón simple)
def perceptron_simple(X1, X2, W1, W2, b):
    # Cálculo del valor Z = X1*W1 + X2*W2 + b
    Z = (X1 * W1) + (X2 * W2) + b
    # Pasar Z a través de la función sigmoide para obtener la salida
    Y = sigmoid(Z)
    return Y

# Definir los pesos y el sesgo
W1 = -0.7  # Peso para X1 (precio del producto)
W2 = 1.2   # Peso para X2 (calificación del producto)
b = 1.5    # Sesgo

# Ejemplo de entradas: X1 (precio), X2 (calificación)
X1 = 3  # Precio del producto (en una escala de 1 a 10)
X2 = 8  # Calificación del producto (en una escala de 1 a 10)

# Calcular la salida
Y = perceptron_simple(X1, X2, W1, W2, b)

# Determinar si compra o no compra (clasificación binaria)
if Y > 0.5:
    print("Resultado: Compra el producto (Y = {:.2f})".format(Y))
else:
    print("Resultado: No compra el producto (Y = {:.2f})".format(Y))
