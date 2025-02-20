import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Conjunto de datos: Promedio del estudiante, Puntaje de examen y Resultado de admisión
# Los valores de la última columna (admitido) son 1 para admitido y 0 para no admitido
X = np.array([[4.0, 6.0],   # Promedio y Puntaje de examen
              [5.5, 7.5],
              [3.0, 5.0],
              [6.0, 8.0],
              [2.5, 4.5],
              [7.0, 9.0],
              [4.5, 6.5]])

# Etiquetas: 1 = Admitido, 0 = No admitido
y = np.array([0, 1, 0, 1, 0, 1, 1])

# Dividir los datos en un conjunto de entrenamiento y uno de prueba (70% entrenamiento, 30% prueba)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear el modelo de regresión logística
model = LogisticRegression()

# Entrenar el modelo con los datos de entrenamiento
model.fit(X_train, y_train)

# Hacer predicciones con los datos de prueba
y_pred = model.predict(X_test)

# Evaluar el modelo usando la precisión (accuracy)
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {accuracy * 100:.2f}%")

# Hacer una predicción para un nuevo estudiante (promedio = 4.0, puntaje de examen = 6.0)
new_data = np.array([[4.0, 6.0]])
prediction = model.predict(new_data)

if prediction == 1:
    print("Resultado: Admitido")
else:
    print("Resultado: No Admitido")
