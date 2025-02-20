import pandas as pd

# Cargar el DataFrame desde el archivo CSV
file_path = '../Pandas/mediana.csv'
df = pd.read_csv(file_path)

media = df.median()
print(media)