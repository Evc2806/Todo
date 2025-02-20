def obtener_datos_persona(nombre, edad, ciudad):
    return f"Hola, mi nombre es {nombre}, tengo {edad} años y vivo en {ciudad}."

def pedir_datos():
    nombre = input("Introduce tu nombre: ")
    edad = input("Introduce tu edad: ")
    ciudad = input("Introduce tu ciudad: ")
    mensaje = obtener_datos_persona(nombre, edad, ciudad)
    print(mensaje)
     
pedir_datos()