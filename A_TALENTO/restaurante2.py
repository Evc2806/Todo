total = 0

print("---- Menú del Restaurante ----")
print("1. Hamburguesa - $10")
print("2. Pizza - $8")
print("3. Ensalada - $6")
print("4. Bebida - $2")
print("5. No pedir más platos")

# Primer pedido
opcion = int(input("Seleccione una opción del menú (1-5): "))

if opcion == 1:
    total += 10
    print(f"Has añadido una Hamburguesa por $10. Total actual: ${total}")
elif opcion == 2:
    total += 8
    print(f"Has añadido una Pizza por $8. Total actual: ${total}")
elif opcion == 3:
    total += 6
    print(f"Has añadido una Ensalada por $6. Total actual: ${total}")
elif opcion == 4:
    total += 2
    print(f"Has añadido una Bebida por $2. Total actual: ${total}")
elif opcion == 5:
    print("No has pedido más platos.")
else:
    print("Opción no válida.")

# Permitir múltiples pedidos
otra_opcion = "si"  # Inicializamos la variable

while otra_opcion == "si":
    otra_opcion = input("¿Desea pedir otro plato? (si/no): ").lower()
    
    if otra_opcion == "si":
        opcion = int(input("Seleccione otra opción del menú (1-5): "))
        
        if opcion == 1:
            total += 10
            print(f"Has añadido una Hamburguesa por $10. Total actual: ${total}")
        elif opcion == 2:
            total += 8
            print(f"Has añadido una Pizza por $8. Total actual: ${total}")
        elif opcion == 3:
            total += 6
            print(f"Has añadido una Ensalada por $6. Total actual: ${total}")
        elif opcion == 4:
            total += 2
            print(f"Has añadido una Bebida por $2. Total actual: ${total}")
        elif opcion == 5:
            print("No has pedido más platos.")
        else:
            print("Opción no válida.")
    elif otra_opcion == "no":
        print("Gracias por tu compra.")
    else:
        print("Opción no válida.")

print(f"Total a pagar: ${total}")
