#import os
import pandas as pd

file_path = '../Pandas/data3.csv'

df = pd.read_csv(file_path)
print(df.head(3))

""""
# Ruta relativa al archivo CSV SI EL ARCHIVO NO EXISTE VA A MOSTRAR ESE MENSAJE
file_path = '../Pandas/data3.csv'

#if os.path.exists(file_path):
df = pd.read_csv(file_path)
print(df.head())
#else:
  #  print(f"El archivo {file_path} no existe.")
  """
"""
    
  # Ruta relativa al archivo CSV  CONVIRTIENDO A COMAS CUANDO ESTA COM PUNTO Y COMA
file_path = '../Pandas/data1.csv'

if os.path.exists(file_path):
    # Lee el archivo CSV con punto y coma como delimitador
    try:
        df = pd.read_csv(file_path, sep=';', encoding='utf-8')
    except UnicodeDecodeError:
        # Si falla con utf-8, prueba con latin1
        df = pd.read_csv(file_path, sep=';', encoding='latin1')
    
    # Muestra las primeras 10 filas para verificar la estructura
    print(df.head(3))
else:
    print(f"El archivo {file_path} no existe.")
    
    """