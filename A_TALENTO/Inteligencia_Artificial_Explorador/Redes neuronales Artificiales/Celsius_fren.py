import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Dense # type: ignore

# Datos de entrada y salida (relación Celsius -> Fahrenheit)
celsius = np.array([-40, -10, 0, 8, 15, 22, 38, 50, 100, 200], dtype=float)  # Temperaturas en Celsius (añadimos más datos)
fahrenheit = np.array([-40, 14, 32, 46.4, 59, 71.6, 100.4, 122, 212, 392], dtype=float)  # Temperaturas correspondientes en Fahrenheit

# Modelo de red neuronal con más capas (una capa adicional de 10 unidades)
model = Sequential([
    Dense(units=10, input_shape=[1], activation='relu'),  # Capa oculta con 10 unidades y función de activación ReLU
    Dense(units=1)  # Capa de salida con una unidad
])

# Compilación del modelo
model.compile(optimizer=tf.keras.optimizers.Adam(0.1), loss='mean_squared_error')

# Entrenamiento del modelo y guardar el historial
history = model.fit(celsius, fahrenheit, epochs=1000, verbose=False)  # Aumentamos las épocas para mejor aprendizaje

# Graficar la pérdida durante el entrenamiento
plt.plot(history.history['loss'])
plt.title('Pérdida durante el entrenamiento')
plt.xlabel('Épocas')
plt.ylabel('Pérdida')
plt.show()

# Pedir al usuario que ingrese una temperatura en Celsius
user_input = float(input("Ingrese una temperatura en Celsius: "))

# Predicción (convertir entrada a un array de numpy)
predicted_fahrenheit = model.predict(np.array([[user_input]]))[0][0]
print(f"La predicción para {user_input}°C es: {predicted_fahrenheit:.2f}°F")

# Graficar los resultados comparando datos reales y predicciones del modelo
predictions = model.predict(celsius)
plt.scatter(celsius, fahrenheit, color='blue', label='Datos reales')  # Datos reales
plt.plot(celsius, predictions, color='red', label='Predicciones del modelo')  # Predicciones
plt.title('Conversión de Celsius a Fahrenheit')
plt.xlabel('Temperatura en Celsius')
plt.ylabel('Temperatura en Fahrenheit')
plt.legend()
plt.show()

# Obtener el peso y el sesgo del modelo
weights, biases = model.layers[0].get_weights()
print("Peso (weights):", weights)
print("Sesgo (biases):", biases)

