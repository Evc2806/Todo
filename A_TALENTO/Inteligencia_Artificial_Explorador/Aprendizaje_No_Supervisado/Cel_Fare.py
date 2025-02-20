# 1. Importar las bibliotecas necesarias
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 2. Pedir las temperaturas al usuario
print("Ingrese las temperaturas en Celsius separadas por comas:")
celsius_input = input()  # Ejemplo: "15,20,25,30,35"
celsius_temps = np.array([float(temp.strip()) for temp in celsius_input.split(",")])

# Verificar si hay suficientes datos para clustering
if len(celsius_temps) < 3:
    print("\nError: Debes ingresar al menos 3 temperaturas para realizar clustering.")
else:
    # 3. Convertir los datos en un formato adecuado
    data = pd.DataFrame({
        "Celsius": celsius_temps
    })

    # 4. Aplicar K-means clustering
    kmeans = KMeans(n_clusters=3, random_state=42)  # Se agrupan en 3 clusters
    clusters = kmeans.fit_predict(data)

    # Agregar los resultados al DataFrame
    data["Cluster"] = clusters

    # 5. Mostrar los resultados
    print("\nTemperaturas agrupadas:")
    print(data)

    # 6. Visualizar los clusters
    plt.scatter(data.index, data["Celsius"], c=data["Cluster"], cmap="viridis", s=100)
    plt.title("Clustering de Temperaturas")
    plt.xlabel("Índice de la Temperatura")
    plt.ylabel("Celsius")
    plt.colorbar(label="Cluster")
    plt.grid()
    plt.show()
