import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor

# Datos de ejemplo (puedes reemplazar estos con tus propios datos)
superficie = np.array([100, 150, 200, 250, 300, 350, 400, 450, 500]).reshape(-1, 1)
costo = np.array([150, 200, 300, 400, 550, 700, 850, 1000, 1200])

# Crear y entrenar el modelo de red neuronal
modelo_red_neuronal = MLPRegressor(hidden_layer_sizes=(100, 50),  # Estructura de la red (capas ocultas)
                                   activation='relu',             # Función de activación
                                   solver='adam',                 # Algoritmo de optimización
                                   max_iter=10000,                # Número máximo de iteraciones
                                   random_state=42)                # Semilla aleatoria para reproducibilidad
modelo_red_neuronal.fit(superficie, costo)


# Realizar predicciones
superficie_nueva = np.linspace(min(superficie), max(superficie), 100).reshape(-1, 1)
costo_predicho = modelo_red_neuronal.predict(superficie_nueva)

# Visualizar los resultados
plt.scatter(superficie, costo, color='blue', label='Datos reales')
plt.plot(superficie_nueva, costo_predicho, color='red', label='Red Neuronal')
plt.xlabel('Superficie (m^2)')
plt.ylabel('Costo (miles de $)')
plt.title('Modelo de Red Neuronal para Estimar Costos')
plt.legend()
plt.grid(True)
plt.show()

# Ejemplo de predicción para una superficie específica
superficie_a_predecir = np.array([[280]])
costo_estimado = modelo_red_neuronal.predict(superficie_a_predecir)

print(f"El costo estimado para una superficie de {superficie_a_predecir[0][0]} m^2 es de {costo_estimado[0]:.2f} miles de $.")