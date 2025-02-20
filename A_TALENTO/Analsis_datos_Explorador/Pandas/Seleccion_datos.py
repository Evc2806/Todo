
import os
import pandas as pd

file_path = '../Pandas/data4.csv'

df = pd.read_csv(file_path)
print(df.head())



nombre_columna = df['Nombre']
apellido1_columna = df['Apellido1']
apellido2_columna = df['Apellido2']
cedula_columna = df['Cedula']

print(nombre_columna)
"""
print(apellido1_columna)
print(apellido2_columna)
print(cedula_columna)
"""