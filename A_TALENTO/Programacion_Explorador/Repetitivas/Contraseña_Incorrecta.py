"""Escribe un programa en Python que siga pidiendo 
al usuario una contraseña hasta que ingrese la correcta ("12345").
"""

contraseña = ""
while contraseña != "12345" :
     contraseña = input("Contraseña incorrecta, ingrese nuevamente su contraseña: ")

print("Contraseña correcta, acceso concedido.")
