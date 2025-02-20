
import pandas as pd

# Cargar el DataFrame desde el archivo CSV
file_path = '../Pandas/suma_max_min.csv'
df = pd.read_csv(file_path)



# Calcular la suma, el mínimo y el máximo de las columnas numéricas
suma = df.sum()
minimo = df.min()
maximo = df.max()

print("El resltado de la suma es:",suma)
print("El mínimo es:",minimo)
print("El máximo es:",maximo)