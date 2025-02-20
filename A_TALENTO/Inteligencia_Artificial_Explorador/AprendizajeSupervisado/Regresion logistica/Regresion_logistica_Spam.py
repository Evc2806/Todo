from sklearn.linear_model import LogisticRegression

# Datos de ejemplo: [contiene 'oferta', contiene 'gratis', contiene 'urgente']
X = [
    [1, 1, 0],  # spam
    [0, 1, 1],  # spam
    [1, 0, 1],  # spam
    [0, 0, 0],  # no spam
    [0, 1, 0],  # no spam
    [1, 0, 0]   # no spam
]

# Etiquetas: 1 = spam, 0 = no spam
y = [1, 1, 1, 0, 0, 0]

# Crear el modelo de regresión logística
modelo = LogisticRegression()

# Entrenar el modelo con los datos
modelo.fit(X, y)

# Nuevo correo para clasificar: contiene 'oferta' y 'gratis'
nuevo_correo = [[1, 1, 0]]

# Predecir si el nuevo correo es spam o no
prediccion = modelo.predict(nuevo_correo)

# Mostrar la predicción
print("Predicción (1 = spam, 0 = no spam):", prediccion[0])
