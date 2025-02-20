"""Escribe un programa en Python que le pida al usuario 5 números y luego muestre 
la suma de esos números utilizando un bucle for.
"""

suma = 0

for i in range(3):
    numero = int(input("Ingrese el número "))
    i=i+1
    suma= suma+numero

print("La suma de los 3 números es:",suma)