import pandas as pd
# Crear un DataFrame simple
a = {
    'Nombre': ['Alice', 'Bob', 'Charlie'],
    'Edad': [25, 30, 35],
    'Ciudad': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(a)

# Mostrar el DataFrame
print(df)