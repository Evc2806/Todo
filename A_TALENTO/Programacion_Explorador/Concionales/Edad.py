

"""
Escribe un programa que solicite la edad de una persona y determine si la persona es un niño (0-12
años), un adolescente (13-17 años), un adulto (18-64 años), o un adulto mayor (65 años o más).
"""

# Solicitar al usuario que ingrese su edad
edad = int(input("Ingresa tu edad: "))

# Clasificar la edad en una categoría
if edad < 0:
    print("La edad no puede ser negativa.")
elif edad <= 12:
    print("Eres un niño.")
elif edad <= 17:
    print("Eres un adolescente.")
elif edad <= 64:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")
