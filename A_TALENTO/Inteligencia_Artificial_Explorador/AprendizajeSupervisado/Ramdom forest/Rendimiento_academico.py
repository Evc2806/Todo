# prompt: quiero un modelo utilizando random forest que me prediga el rendimiento academico de un estudiante teniendo en cuenta unas carcateristicas con comentarios en español pero sin cargar archivos y quiero que me dejes las lineas donde se pueden cargar con cometarios

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Aquí se cargarían los datos desde un archivo, por ejemplo un CSV
# data = pd.read_csv('datos_estudiantes.csv') 

# Simulamos algunos datos (reemplazar con tus datos reales)
data = pd.DataFrame({
    'horas_estudio': [2, 5, 3, 7, 1, 6, 4, 8, 2, 9],
    'asistencia': [90, 100, 80, 95, 70, 98, 85, 100, 75, 92],
    'puntuacion_examenes': [70, 85, 75, 92, 60, 90, 80, 95, 65, 98],
    'rendimiento': [75, 90, 80, 95, 65, 92, 82, 98, 70, 100] # Variable a predecir
})

# Definir características (X) y variable objetivo (y)
X = data[['horas_estudio', 'asistencia', 'puntuacion_examenes']]
y = data['rendimiento']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # test_size controla el porcentaje para test

# Inicializar y entrenar el modelo Random Forest
modelo_rf = RandomForestRegressor(n_estimators=100, random_state=42)  # n_estimators es el número de árboles
modelo_rf.fit(X_train, y_train)

# Realizar predicciones sobre el conjunto de prueba
y_pred = modelo_rf.predict(X_test)

# Evaluar el modelo (error cuadrático medio)
mse = mean_squared_error(y_test, y_pred)
print(f'Error cuadrático medio: {mse}')

# Ejemplo de predicción para un nuevo estudiante (reemplazar con nuevos datos)
nuevo_estudiante = pd.DataFrame({
    'horas_estudio': [4],
    'asistencia': [85],
    'puntuacion_examenes': [78]
})

prediccion = modelo_rf.predict(nuevo_estudiante)
print(f'Predicción del rendimiento académico: {prediccion[0]}')