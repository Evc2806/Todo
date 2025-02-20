import pandas as pd

# Cargar el DataFrame desde el archivo CSV
file_path = '../Pandas/media.csv'
df = pd.read_csv(file_path)




media = df.mean()
print(media)