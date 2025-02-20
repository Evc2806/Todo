# 1. Importar las bibliotecas necesarias
import pandas as pd  # Para manejar los datos en formato de tablas
import numpy as np  # Para operaciones matemáticas
from sklearn.model_selection import train_test_split  # Para dividir los datos en entrenamiento y prueba
from sklearn.linear_model import LinearRegression  # Para implementar la regresión lineal
from sklearn.metrics import mean_squared_error, r2_score  # Para evaluar el modelo

# 2. Crear o cargar el conjunto de datos
# Ejemplo de datos simulados
data = {
    "ubicacion": [1, 2, 1, 3, 2],  # Codificación de ubicaciones geográficas
    "costo_kwh": [0.12, 0.15, 0.11, 0.20, 0.14],  # Costo del kWh con paneles solares
    "temperatura_promedio": [25, 30, 20, 35, 28],  # Temperatura promedio anual
    "horas_solares_dia": [5, 6, 4, 8, 7],  # Promedio de horas solares diarias
    "costo_ahorro": [300, 450, 280, 520, 400]  # Ahorro energético (variable objetivo)
}
df = pd.DataFrame(data)  # Convertir los datos en un DataFrame de pandas

# 3. Separar las características (X) y la variable objetivo (y)
X = df[["ubicacion", "costo_kwh", "temperatura_promedio", "horas_solares_dia"]]  # Variables predictoras
y = df["costo_ahorro"]  # Variable objetivo

# 4. Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# test_size=0.2 significa que el 20% de los datos se usará para pruebas
# random_state asegura que los resultados sean reproducibles

# 5. Crear un modelo de regresión lineal
model = LinearRegression()  # Inicializar el modelo

# 6. Entrenar el modelo con los datos de entrenamiento
model.fit(X_train, y_train)
# El modelo aprende los pesos (coeficientes) que relacionan las variables predictoras con la variable objetivo

# 7. Realizar predicciones sobre el conjunto de prueba
y_pred = model.predict(X_test)
# Usamos el modelo entrenado para predecir el ahorro energético en los datos de prueba

# 8. Evaluar el modelo
mse = mean_squared_error(y_test, y_pred)  # Calcula el error cuadrático medio
r2 = r2_score(y_test, y_pred)  # Calcula el coeficiente de determinación (R²)

print("Error cuadrático medio (MSE):", mse)
print("Coeficiente de determinación (R²):", r2)

# 9. Mostrar los coeficientes del modelo
print("Coeficientes del modelo:", model.coef_)
print("Intersección del modelo (bias):", model.intercept_)

# 10. Hacer una predicción con nuevos datos
nueva_prediccion = model.predict([[2, 0.13, 27, 6]])
# Ejemplo: Ubicación = 2, costo_kwh = 0.13, temperatura = 27°C, horas solares = 6
print("Predicción de ahorro energético:", nueva_prediccion[0])
 