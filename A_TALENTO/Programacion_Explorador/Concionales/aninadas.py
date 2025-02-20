# Solicitar al usuario que ingrese su edad
edad = int(input("Ingrese su edad: "))

# Comprobar si es mayor de edad y si es adulto mayor
if edad >= 18:
    print("Eres mayor de edad.")
    
    if edad >= 65:
        print("También eres un adulto mayor.")
else:
    print("Eres menor de edad.")
    
    
  