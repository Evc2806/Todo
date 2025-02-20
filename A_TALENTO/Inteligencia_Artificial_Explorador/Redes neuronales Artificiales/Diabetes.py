# Enunciado:
# Desarrollamos una red neuronal de una capa para predecir si un paciente tiene diabetes
# basada en dos características: el Índice de Masa Corporal (BMI) y la Edad del paciente.
# La red neuronal devolverá 1 si el paciente tiene diabetes y 0 si no la tiene.

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
W1 = 0.5  # Peso para X1 (BMI)
W2 = 1.2  # Peso para X2 (Edad)
b = -4.0  # Sesgo que ajusta la predicción

# Ejemplo de entradas: X1 (BMI), X2 (Edad)
X1 = 28.0  # Índice de Masa Corporal del paciente
X2 = 45.0  # Edad del paciente

# Calcular la salida utilizando la función del perceptrón
Y = perceptron_simple(X1, X2, W1, W2, b)

# Determinar si el paciente tiene diabetes o no (clasificación binaria)
if Y > 0.5:
    print("Resultado: Tiene Diabetes (Y = {:.2f})".format(Y))
else:
    print("Resultado: No Tiene Diabetes (Y = {:.2f})".format(Y))
