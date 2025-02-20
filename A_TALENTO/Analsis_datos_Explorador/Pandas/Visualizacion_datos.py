import os
import pandas as pd

file_path = '../Pandas/data3.csv'

# FUNCIÓN MUESTRA LOS PRIMEROS DATOS DE UN DATA FRAME
df = pd.read_csv(file_path)
print(df.head())



# FUNCIÓN MUESTRA LOS PRIMEROS DATOS DE UN DATA FRAME

#print(df.head()) #Muestra las primeras filas del DataFrame.
#print(df.tail(2)) #Muestra las últimas filas del DataFrame.
#print(df.info()) #Proporciona información sobre el DataFrame, como el tipo de datos y la cantidad de valores no nulos.
#print(df.describe()) #Genera estadísticas descriptivas para columnas numéric
