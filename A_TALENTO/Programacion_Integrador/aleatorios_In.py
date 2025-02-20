import random

# número entero
numero_entero = random.randint(1, 5)
print("Número entero aleatorio:", numero_entero)


# Generar un número decimal aleatorio entre 0 y 1
numero_decimal = random.random()
print("Número decimal aleatorio:", numero_decimal)


# Generar un número decimal aleatorio en un rango específico, por ejemplo, entre 0 y 10
numero_decimal_rango = random.uniform(0, 3)
print("Número decimal aleatorio en un rango específico:", numero_decimal_rango)

#lista aleatoria de números
lista_enteros = [random.randint(1, 100) for _ in range(10)]
print("Lista aleatoria de números enteros:", lista_enteros)