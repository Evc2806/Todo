import array

# Definir un arreglo de enteros
numeros = array.array('i', [1, 2, 3, 4, 5])

# Calcular la resta de todos los elementos
resta_total = numeros[0] - sum(numeros[1:])

# Imprimir la resta
print("La resta de todos los elementos es:", resta_total)