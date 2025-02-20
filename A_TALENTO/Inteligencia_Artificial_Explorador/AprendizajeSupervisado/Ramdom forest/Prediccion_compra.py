# Importación de librerías necesarias
import pandas as pd  # Librería para manejar datos en formato DataFrame
from sklearn.model_selection import train_test_split  # Para dividir los datos en entrenamiento y prueba
from sklearn.ensemble import RandomForestClassifier  # Algoritmo Random Forest para clasificación
from sklearn.metrics import classification_report, accuracy_score  # Para evaluar el desempeño del modelo
from sklearn.preprocessing import LabelEncoder  # Para convertir etiquetas categóricas en valores numéricos

# Simulación de datos (reemplaza esto con tus datos reales)
# Creamos un DataFrame con la información de los clientes
data = {
    'edad': [25, 30, 45, 22, 50, 35, 28, 40, 60, 20],  # Edad del cliente
    'ingresos': [50000, 60000, 100000, 40000, 120000, 70000, 55000, 80000, 150000, 30000],  # Ingresos del cliente
    'compras_anteriores': [2, 5, 10, 1, 15, 6, 3, 8, 20, 0],  # Número de compras previas realizadas
    'valor_cliente': ['alto', 'medio', 'alto', 'bajo', 'alto', 'medio', 'medio', 'alto', 'alto', 'bajo'],  # Etiqueta categórica sobre el valor del cliente
    'compra_realizada': [1, 0, 1, 0, 1, 1, 0, 1, 1, 0]  # 1 = Compró, 0 = No compró (variable objetivo)
}

# Creamos el DataFrame con los datos proporcionados
df = pd.DataFrame(data)

# **Codificación de la variable categórica 'valor_cliente'**
# Convertimos las categorías 'alto', 'medio', 'bajo' a números usando LabelEncoder.
le = LabelEncoder()
df['valor_cliente'] = le.fit_transform(df['valor_cliente'])  # 'alto' -> 2, 'medio' -> 1, 'bajo' -> 0

# **Definición de las características (X) y la variable objetivo (y)**
# X son las características que el modelo usará para hacer la predicción
X = df[['edad', 'ingresos', 'compras_anteriores', 'valor_cliente']]
# y es la variable objetivo que queremos predecir (si el cliente compró o no)
y = df['compra_realizada']

# **División de los datos en conjuntos de entrenamiento y prueba**
# train_test_split divide el conjunto de datos en dos partes: 80% para entrenamiento y 20% para prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# **Creación y entrenamiento del modelo Random Forest**
# RandomForestClassifier crea un conjunto de árboles de decisión. n_estimators=100 indica que queremos 100 árboles
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)  # Entrenamos el modelo con los datos de entrenamiento

# **Hacer predicciones con el conjunto de prueba**
# Usamos el modelo entrenado para predecir la variable objetivo (si el cliente compró o no) en el conjunto de prueba
y_pred = rf_model.predict(X_test)

# **Evaluación del modelo**
# El classification_report nos muestra métricas como precision, recall, f1-score para cada clase (0 y 1)
print("Reporte de Clasificación:")
print(classification_report(y_test, y_pred))

# La exactitud (accuracy) muestra qué porcentaje de las predicciones fueron correctas
print("Exactitud:", accuracy_score(y_test, y_pred))

# **Ejemplo de predicción para un nuevo cliente**
# Creamos un DataFrame con las características del nuevo cliente. 'valor_cliente' = 1 significa "medio"
# Cambia estos valores según el nuevo cliente que quieras predecir
nuevo_cliente = pd.DataFrame({'edad': [27], 'ingresos': [65000], 'compras_anteriores': [4], 'valor_cliente': [1]})

# Realizamos la predicción para el nuevo cliente
# El modelo predice 1 (compró) o 0 (no compró) según las características del cliente
prediccion = rf_model.predict(nuevo_cliente)

# Imprimimos la predicción: 1 significa que el cliente realizará la compra, 0 significa que no
print("Predicción para el nuevo cliente (1 = compra, 0 = no compra):", prediccion[0])


