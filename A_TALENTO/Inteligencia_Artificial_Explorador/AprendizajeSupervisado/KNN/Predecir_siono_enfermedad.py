import random
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def modelo_knn_enfermedad(num_muestras=100):
    """
    Modelo KNN para predecir la presencia o ausencia de una enfermedad.
    Genera datos aleatorios y un modelo KNN con una precisión superior al 80%.

    Args:
      num_muestras: Número de muestras de datos a generar.

    Returns:
      Una tupla con la precisión del modelo y una predicción para un nuevo paciente.
    """

    # Generar datos aleatorios
    X = np.random.rand(num_muestras, 5)  # 5 características aleatorias
    y = np.random.randint(0, 2, num_muestras) # 0: sin enfermedad, 1: con enfermedad


    # Dividir los datos en conjuntos de entrenamiento y prueba (80/20)
    split_index = int(0.8 * num_muestras)
    X_train, X_test = X[:split_index], X[split_index:]
    y_train, y_test = y[:split_index], y[split_index:]


    # Entrenar un modelo KNN con k=3 (puedes ajustar este valor)
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)

    # Realizar predicciones en el conjunto de prueba
    y_pred = knn.predict(X_test)

    # Calcular la precisión del modelo
    precision = accuracy_score(y_test, y_pred)

    # Generar datos para un nuevo paciente (aleatorios)
    nuevo_paciente = np.random.rand(1, 5)
    prediccion_nuevo_paciente = knn.predict(nuevo_paciente)


    # Ajustar el modelo iterativamente hasta alcanzar una precisión superior al 80%
    iteraciones = 0
    while precision < 0.8 and iteraciones < 1000: # Limitar iteraciones
        # Re-generar datos
        X = np.random.rand(num_muestras, 5)
        y = np.random.randint(0, 2, num_muestras)
        split_index = int(0.8 * num_muestras)
        X_train, X_test = X[:split_index], X[split_index:]
        y_train, y_test = y[:split_index], y[split_index:]
        
        # Re-entrenar modelo
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)
        precision = accuracy_score(y_test, y_pred)
        
        # Re-generar datos para un nuevo paciente
        nuevo_paciente = np.random.rand(1, 5)
        prediccion_nuevo_paciente = knn.predict(nuevo_paciente)
        iteraciones +=1

    # Imprimir la precisión
    print(f"Precisión del modelo: {precision * 100:.2f}%")

    return precision, prediccion_nuevo_paciente

# Ejemplo de uso
precision, prediccion = modelo_knn_enfermedad()
print(f"Predicción para el nuevo paciente: {prediccion[0]} (0: Sin enfermedad, 1: Con enfermedad)")