def mostrar_menu():
    print("---- Menú del Restaurante ----")
    print("1. Hamburguesa - $10")
    print("2. Pizza - $8")
    print("3. Ensalada - $6")
    print("4. Bebida - $2")
    print("5. Salir")

def obtener_precio(opcion):
    if opcion == 1:
        return 10
    elif opcion == 2:
        return 8
    elif opcion == 3:
        return 6
    elif opcion == 4:
        return 2
    else:
        return 0

def menu_restaurante():
    total = 0
    opcion = 0
    
    while opcion != 5:
        mostrar_menu()
        opcion = int(input("Seleccione una opción del menú (1-5): "))
        
        if 1 <= opcion <= 4:
            precio = obtener_precio(opcion)
            total += precio
            print(f"Has agregado un producto por ${precio}. Total acumulado: ${total}")
        elif opcion == 5:
            print("Gracias por su visita.")
        else:
            print("Opción no válida, intente de nuevo.")
    
    print(f"El total a pagar es: ${total}")

menu_restaurante()
