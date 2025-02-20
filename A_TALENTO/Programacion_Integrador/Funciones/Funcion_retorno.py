# Definimos la función para sumar
def suma(a, b):
    #return a + b
    c=a+b
    return c



# Definimos la función para restar
def resta(a, b):
    #return a - b
    c=a-b
    return c

# Definimos la función para multiplicar
def multiplicacion(a, b):
    return a * b

# Pedimos al usuario que ingrese dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Llamamos a cada función con los números ingresados y mostramos los resultados
print("Suma:", suma(num1, num2))
print("Resta:", resta(num1, num2))
print("Multiplicación:", multiplicacion(num1, num2))
