import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score

# Generar datos de ejemplo (reemplazar con datos reales si están disponibles)
np.random.seed(0)
n_samples = 1000
monto = np.random.uniform(10, 10000, n_samples)
hora = np.random.randint(0, 24, n_samples)
ubicacion = np.random.randint(0, 10, n_samples) # 10 ubicaciones diferentes
tipo_transaccion = np.random.randint(0, 5, n_samples) # 5 tipos de transacciones
fraude = np.random.choice([0,1], n_samples, p=[0.95,0.05]) # 5% de fraude

# Crear DataFrame
data = pd.DataFrame({
    'Monto': monto,
    'Hora': hora,
    'Ubicacion': ubicacion,
    'Tipo_Transaccion': tipo_transaccion,
    'Fraude': fraude
})

# Convertir la columna 'Fraude' a texto (Sí/No)
data['Fraude'] = data['Fraude'].map({0: 'No', 1: 'Sí'})

# Dividir los datos en entrenamiento y prueba
X = data.drop('Fraude', axis=1)
y = data['Fraude']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo SVM
modelo_svm = SVC(kernel='linear') # Se puede cambiar el kernel si es necesario
modelo_svm.fit(X_train, y_train)

# Hacer predicciones
y_pred = modelo_svm.predict(X_test)

# Evaluar el modelo
print(classification_report(y_test, y_pred))
print("Precisión del modelo:", accuracy_score(y_test, y_pred))

# Ejemplo de predicción con nuevos datos
nuevos_datos = pd.DataFrame({
    'Monto': [5000],
    'Hora': [2],
    'Ubicacion': [3],
    'Tipo_Transaccion': [1]
})
prediccion = modelo_svm.predict(nuevos_datos)
print(f"Predicción para los nuevos datos: {prediccion[0]}")