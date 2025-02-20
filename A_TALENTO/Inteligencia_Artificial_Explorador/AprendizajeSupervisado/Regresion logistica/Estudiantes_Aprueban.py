# Importamos la librería necesaria
from sklearn.linear_model import LogisticRegression

# Datos de ejemplo
X = [[2], [3], [5], [7], [10]]  # Horas de estudio
y = [0, 0, 1, 1, 1]  # Aprobado (1) o Reprobado (0)

# Creamos un modelo de regresión logística
modelo = LogisticRegression()

# Entrenamos el modelo con los datos
modelo.fit(X, y)

# Hacemos una predicción para un nuevo valor de horas de estudio
nuevo_valor = [[4]]
prediccion = modelo.predict(nuevo_valor)

# Mostramos la predicción
print("Predicción para un estudiante que estudió", nuevo_valor[0][0], "horas:", "Aprobado" if prediccion[0] == 1 else "Reprobado")
