# Importar las librerías necesarias
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
W1 = 0.6  # Peso para X1 (horas de estudio)
W2 = 0.9  # Peso para X2 (nivel de atención)
b = -5    # Sesgo

# Ejemplo de entradas: X1 (horas de estudio), X2 (nivel de atención)
X1 = 5  # Horas de estudio
X2 = 7  # Nivel de atención en clase

# Calcular la salida
Y = perceptron_simple(X1, X2, W1, W2, b)

# Determinar si aprobó o no aprobó (clasificación binaria)
if Y > 0.5:
    print("Resultado: Aprobado (Y = {:.2f})".format(Y))
else:
    print("Resultado: No Aprobado (Y = {:.2f})".format(Y))

# Explicación del proceso en comentarios:

# Una red neuronal de una capa (también conocida como perceptrón simple) es el tipo más básico de red neuronal.
# Tiene una capa de entrada y una capa de salida, sin capas ocultas. Puede resolver problemas de clasificación lineales,
# donde los datos se pueden separar con una línea recta.

# Paso 1: Definir la entrada y la salida.
# Las entradas son dos características, X1 (horas de estudio) y X2 (nivel de atención), mientras que la salida será
# un valor binario (0 o 1) indicando si el estudiante aprobó o no.

# Paso 2: Pesos y sesgo (bias).
# Los pesos W1 y W2 definen la importancia de cada entrada para la predicción. El sesgo b ajusta la función para
# mejorar la predicción.

# Paso 3: La función de activación.
# Usamos la función sigmoide para convertir la suma ponderada en una probabilidad entre 0 y 1.

# Paso 4: Evaluar el modelo.
# Si la salida Y es mayor que 0.5, se considera que el estudiante aprobó el examen, de lo contrario, no aprobó.
