# contraseña 3 intentos

contraseña = "1234"  # Contraseña predefinida
intentos = 3

while intentos > 0:
    intento = input("Ingrese la contraseña: ")
    if intento == contraseña:
        print("Contraseña correcta. Bienvenido.")
        break
    else:
        print("Contraseña incorrecta. Intente de nuevo.")
        intentos=intentos-1

if intentos == 0:
    print("Se acabaron los intentos. Acceso denegado.")