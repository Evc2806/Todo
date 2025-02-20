import array

# Definir un arreglo de enteros
numeros = array.array('i', [1, 2, 3, 4, 5])

# Inicializar el producto
producto_total = 1

# Calcular la multiplicación de todos los elementos
for numero in numeros:
    producto_total=   producto_total*numero

# Imprimir el producto
print("La multiplicación de todos los elementos es:", producto_total)