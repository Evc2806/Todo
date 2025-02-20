# Enunciado:
# Desarrollamos una red neuronal de una capa para predecir si un cliente renovará su suscripción
# basada en dos características: la Duración de la Suscripción y el Uso del Servicio.
# La red neuronal devolverá 1 si el cliente renovará su suscripción y 0 si no lo hará.

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
W1 = 0.4  # Peso para X1 (Duración de la Suscripción)
W2 = 0.6  # Peso para X2 (Uso del Servicio)
b = -2.5  # Sesgo que ajusta la predicción

# Ejemplo de entradas: X1 (Duración de la Suscripción), X2 (Uso del Servicio)
X1 = 12.0  # Duración de la suscripción en meses
X2 = 10.0  # Uso promedio del servicio por mes

# Calcular la salida utilizando la función del perceptrón
Y = perceptron_simple(X1, X2, W1, W2, b)

# Determinar si el cliente renovará la suscripción o no (clasificación binaria)
if Y > 0.5:
    print("Resultado: Renovará la Suscripción (Y = {:.2f})".format(Y))
else:
    print("Resultado: No Renovará la Suscripción (Y = {:.2f})".format(Y))
