# Definimos la función para sumar
def suma(a, b):
    print("Suma:", a + b)

# Definimos la función para restar
def resta(a, b):
    print("Resta:", a - b)

# Definimos la función para multiplicar
def multiplicacion(a, b):
    print("Multiplicación:", a * b)

# Pedimos al usuario que ingrese dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Llamamos a cada función con los números ingresados
suma(num1, num2)
resta(num1, num2)
multiplicacion(num1, num2)