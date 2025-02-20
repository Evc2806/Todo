
import os
import pandas as pd

""""

# Especifica la ruta del archivo CSV
file_path ="https://docs.google.com/spreadsheets/d/12MHNWZnbekh6RClFcxRcixMB90ooPsUsg3Tt9L7OllM/export?format=csv"

# Verifica si el archivo existe
if os.path.exists(file_path):
    # Lee el archivo CSV y conviértelo en un DataFrame
    df = pd.read_csv(file_path)
    print(df.head())  # Muestra las primeras filas del DataFrame
else:
    print(f"El archivo {file_path} no existe.")

"""
# Especifica la ruta relativa al archivo CSV
#file_path = 'pd.read_csv("https://docs.google.com/spreadsheets/d/12MHNWZnbekh6RClFcxRcixMB90ooPsUsg3Tt9L7OllM/export?format=csv")
#df2'



# Lee el archivo CSV y conviértelo en un DataFrame
df = pd.read_csv("https://docs.google.com/spreadsheets/d/12MHNWZnbekh6RClFcxRcixMB90ooPsUsg3Tt9L7OllM/export?format=csv")


# Muestra las primeras filas del DataFrame
print(df.head())




#enlaces
#https://www.youtube.com/watch?v=asOnjdw5oXI
#https://colab.research.google.com/drive/1teV61nKFoWTYI9byxWwX8BU3111ISWap?usp=sharing#scrollTo=QX0uP9Dnc-g5
