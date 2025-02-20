#Escribe un programa en Python que verifique si una persona es menor de edad, 
# mayor de edad, o si es muy mayor para votar.

edad = int(input("Ingresa tu edad: "))




if edad < 18:
    print("Eres menor de edad y no puedes votar.")
elif edad >= 18 and edad <= 70:
    print("Eres mayor de edad y puedes votar.")
else:
    print("Eres mayor de 70 años, votar es opcional para ti.")
