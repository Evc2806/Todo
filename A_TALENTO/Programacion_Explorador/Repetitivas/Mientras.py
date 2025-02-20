# Inicializamos la variable para la suma total
total = 0

# Pedimos al usuario que ingrese la cantidad de artículos
cantidad_articulos = int(input("¿Cuántos artículos tienes?: "))

# Inicializamos un contador
contador = 0

# Usamos un bucle while para sumar el precio de cada artículo
while contador < cantidad_articulos:
    precio = float(input(f"Ingrese el precio del artículo {contador + 1}: "))
    total += precio
    contador += 1  # Aumentamos el contador

# Mostramos el total
print(f"El total a pagar por los {cantidad_articulos} artículos es: {total}")
