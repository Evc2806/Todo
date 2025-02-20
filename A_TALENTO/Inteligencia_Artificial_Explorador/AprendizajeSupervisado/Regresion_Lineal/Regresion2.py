from sklearn.linear_model import LinearRegression

# Datos de ejemplo: tamaño de la casa (en metros cuadrados)
X = [[50], [75], [100], [125], [150]]  # Tamaño en m²
# Precios de las casas correspondientes (en miles de dólares)
y = [150, 200, 250, 300, 350]

# Crear el modelo de regresión lineal
modelo = LinearRegression()

# Entrenar el modelo con los datos
modelo.fit(X, y)

# Predecir el precio de una casa de 110 metros cuadrados
nuevo_valor = [[110]]
prediccion = modelo.predict(nuevo_valor)

# Mostrar la predicción
print("Predicción para una casa de", nuevo_valor[0][0], "m²:", prediccion[0], "mil dólares")
