
lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Iterar sobre cada lista interna
for lista_interna in lista_anidada:
    # Iterar sobre cada elemento dentro de la lista interna
    for elemento in lista_interna:
        print(elemento, end=" ")  # Imprimir el elemento
    print()  # Salto de línea después de imprimir cada lista interna