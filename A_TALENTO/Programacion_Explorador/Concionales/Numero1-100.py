#Escribe un programa en Python que verifique si un número ingresado por el usuario está entre 1 y 100.

numero = int(input("Ingresa un número: "))

if numero >= 1 and numero <= 100:
    print("El número", numero,"está en el rango de 1 a 100.")
else:
    print("El número", numero,"está fuera del rango")
