
"""
Escribe un programa en Python que clasifique una calificación (0 a 100) en las siguientes categorías:

"Excelente" si es 90 o más.
"Bueno" si está entre 70 y 89.
"Regular" si está entre 50 y 69.
"Insuficiente" si es menor de 50.

"""

calificacion = int(input("Ingresa tu calificación (0-100): "))

if calificacion >= 90:
    print("Excelente")
elif calificacion >= 70:
    print("Bueno")
elif calificacion >= 50:
    print("Regular")
else:
    print("Insuficiente")
