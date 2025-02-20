
# crear diccionario
celularx={
    "color": "negro",
    "cargador": "si",
    "stock": 50,
    "funda": "no",
    "audifonos": "bloutube",
    "camara":"uhd",
    "simcard":"si"
         
}
#acceder al diccionario
print("Los accesorios del celular son:",celularx)

#modificar datos y mostrar por consola
celularx ["cargador"]= "no venta"
celularx ["audifonos"]="cableados"

print("El nuevo equipo contiene:",celularx)

#agregar clave y mostrar el nuevo valor

celularx["manual"]="cuenta con manual"

print(celularx)

del celularx ["stock"]
print(celularx)
