import pandas as pd

# Cargar el DataFrame desde el archivo CSV
file_path = '../Pandas/desviacion.csv'
df = pd.read_csv(file_path)

desviacion = df.std()
print(desviacion)