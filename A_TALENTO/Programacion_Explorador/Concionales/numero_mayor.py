#Calcular el mayor de tres números:

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

if num1 >= num2 and num1 >= num3:
    print("El primer número es el mayor.")
elif num2 >= num1 and num2 >= num3:
    print("El segundo número es el mayor.")
else:
    print("El tercer número es el mayor.")
    
    
