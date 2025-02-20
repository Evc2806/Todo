# Definir una matriz (arreglo bidimensional)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Recorrer la matriz e imprimir todos los elementos
for fila in matriz:
    for elemento in fila:
      print(elemento, end=" ")  # Utilizamos end=" " para imprimir en la misma línea
    print()  # Agregamos una línea en blanco al final de cada fila