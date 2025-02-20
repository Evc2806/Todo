"""
Enunciado: Desarrolla un algoritmo de regresión lineal simple que permita predecir valores en
función de un conjunto de datos de entrenamiento. El algoritmo deberá utilizar la biblioteca
scikit-learn para ajustar un modelo de regresión lineal a los datos de entrada y predecir un valor
de salida basado en un nuevo dato de entrada.
"""

# Se importa la clase LinearRegression de la biblioteca scikit-learn. 
#Esta clase se utiliza para crear un modelo de regresión lineal que será entrenado con los datos.
from sklearn.linear_model import LinearRegression

# Datos de ejemplo (puedes usar tus propios datos)
X = [[1], [2], [3], [4], [5]]  # Valores de entrada
y = [2, 4, 5, 4, 5]  # Valores de salida correspondientes

# Creamos un modelo de regresión lineal
modelo = LinearRegression()

# Entrenamos el modelo con los datos
modelo.fit(X, y)

# Hacemos una predicción para un nuevo valor de entrada
nuevo_valor = [[6]]
prediccion = modelo.predict(nuevo_valor)

# Mostramos la predicción
print("Predicción para el valor", nuevo_valor[0][0], ":", prediccion[0])

