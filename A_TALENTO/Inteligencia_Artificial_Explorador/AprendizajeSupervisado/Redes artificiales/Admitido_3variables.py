# Enunciado:
# Desarrollamos una red neuronal de una capa para predecir si un estudiante será admitido
# en una universidad basada en tres características: la Calificación del Examen de Ingreso,
# el Promedio de Calificaciones y las Actividades Extracurriculares.
# La red neuronal devolverá 1 si el estudiante será admitido y 0 si no lo será.

import numpy as np  # Importar la librería NumPy para cálculos numéricos

# Definir la función sigmoide que actúa como función de activación
def sigmoid(z):
    # La función sigmoide transforma el valor de entrada en un rango entre 0 y 1
    return 1 / (1 + np.exp(-z))

# Definir la función para el perceptrón simple
def perceptron_simple(X1, X2, X3, W1, W2, W3, b):
    # Calcular la suma ponderada de las entradas más el sesgo
    Z = (X1 * W1) + (X2 * W2) + (X3 * W3) + b
    # Aplicar la función sigmoide para obtener la probabilidad
    Y = sigmoid(Z)
    return Y  # Retornar el valor de salida

# Definir los pesos y el sesgo
W1 = 0.5  # Peso para X1 (Calificación del Examen de Ingreso)
W2 = 0.3  # Peso para X2 (Promedio de Calificaciones)
W3 = 0.2  # Peso para X3 (Actividades Extracurriculares)
b = -4.0  # Sesgo que ajusta la predicción

# Ejemplo de entradas: X1 (Calificación), X2 (Promedio), X3 (Actividades)
X1 = 85.0  # Calificación del examen de ingreso
X2 = 90.0  # Promedio de calificaciones
X3 = 2.0   # Número de actividades extracurriculares

# Calcular la salida utilizando la función del perceptrón
Y = perceptron_simple(X1, X2, X3, W1, W2, W3, b)

# Determinar si el estudiante será admitido o no (clasificación binaria)
if Y > 0.5:
    print("Resultado: El Estudiante Será Admitido (Y = {:.2f})".format(Y))
else:
    print("Resultado: El Estudiante No Será Admitido (Y = {:.2f})".format(Y))
