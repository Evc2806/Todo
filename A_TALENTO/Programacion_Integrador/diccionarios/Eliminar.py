# Crear un diccionario con información sobre una persona
persona = {
    "nombre": "Ana",
    "edad": 28,
    "ciudad": "Bogotá",
     
 
}

# Acceder a los valores del diccionario usando las claves
print("Nombre:", persona["nombre"])
print("Edad:", persona["edad"])
print("Ciudad:", persona["ciudad"])

# Modificar un valor en el diccionario
persona["edad"] = 29
print("Edad actualizada:", persona["edad"])

# Agregar una nueva clave y valor al diccionario
persona["profesión"] = "Ingeniera"
print("Profesión añadida:", persona["profesión"])

# Eliminar un elemento del diccionario
del persona["ciudad"]
print("Ciudad eliminada:", persona)