# Pedir al usuario que ingrese un número
numero = int(input("Ingresa un número para calcular su factorial: "))

# Inicializar el resultado y el contador
resultado = 1
contador = 1

# Mientras el contador sea menor o igual al número ingresado
while contador <= numero:
    resultado=resultado*contador  # Multiplicar el resultado por el contador
    contador=contador+1        # Incrementar el contador en 1

# Mostrar el resultado
print("El factorial de ",numero,"es: ",resultado)