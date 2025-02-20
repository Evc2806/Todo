import pandas as pd

# Cargar el DataFrame desde el archivo CSV
file_path = '../Pandas/data_operaciones.csv'
df = pd.read_csv(file_path)

""""
#calcular para todas las columnas numéricas pero el archivo debe tener todas las columnas numéricas
# Calcular la media, mediana y desviación estándar de las columnas numéricas
media = df.mean()
mediana = df.median()
desviacion_estandar = df.std()

# Calcular la suma, el mínimo y el máximo de las columnas numéricas
suma = df.sum()
minimo = df.min()
maximo = df.max()

# Imprimir los resultados
print("Media de las columnas numéricas:")
print(media)
print("\nMediana de las columnas numéricas:")
print(mediana)
print("\nDesviación estándar de las columnas numéricas:")
print(desviacion_estandar)
print("\nSuma de las columnas numéricas:")
print(suma)
print("\nValor mínimo de las columnas numéricas:")
print(minimo)
print("\nValor máximo de las columnas numéricas:")
print(maximo)
"""

"""

# Calcular la media solo para columnas numéricas
media = df.mean(numeric_only=True)

# Calcular la mediana solo para columnas numéricas
mediana = df.median(numeric_only=True)

# Calcular la desviación estándar solo para columnas numéricas
desviacion_estandar = df.std(numeric_only=True)

# Calcular la suma solo para columnas numéricas
suma = df.sum(numeric_only=True)

# Calcular el mínimo solo para columnas numéricas
minimo = df.min(numeric_only=True)

# Calcular el máximo solo para columnas numéricas
maximo = df.max(numeric_only=True)

# Imprimir resultados
print("Media:\n", media)
print("\nMediana:\n", mediana)
print("\nDesviación estándar:\n", desviacion_estandar)
print("\nSuma:\n", suma)
print("\nMínimo:\n", minimo)
print("\nMáximo:\n", maximo)
"""




#Si se cual es la columna numérica

file_path = '../Pandas/data_operaciones.csv'

# Leer el archivo CSV en un DataFrame
df = pd.read_csv(file_path)

# Calcular la media de la columna 'numeros'
media = df['numeros'].mean()

# Imprimir la media
print("La media de la columna 'numeros' es:", media)
