class Singleton:
    # Variable de clase que almacenará la única instancia de la clase
    _instancia = None

    @staticmethod  #decorador me define un método estático(no creo unaa instancia d ela clase)
    def obtener_instancia():
        # Si no existe una instancia creada, la creamos
        if Singleton._instancia is None:
            Singleton._instancia = Singleton()
        # Devolvemos la instancia única
        return Singleton._instancia

    def __init__(self):
        # Si ya existe una instancia, evitamos crear una nueva
        if Singleton._instancia is not None:
            # Si alguien intenta crear una instancia directamente, lanzamos una excepción
            raise Exception("Ya existe una instancia de Singleton. Usa obtener_instancia() para acceder a ella.")

# Usando el Singleton:
# Obtenemos la instancia del Singleton (la primera vez, la creamos)
obj1 = Singleton.obtener_instancia()
# Obtenemos la misma instancia de Singleton (no se crea una nueva)
obj2 = Singleton.obtener_instancia()

# Comprobamos si ambas variables apuntan a la misma instancia
print(obj1 is obj2)  # Imprime 'True', porque ambas referencias apuntan al mismo objeto

# Intentar crear una instancia directamente generaría una excepción,
# pero no usamos try/except para capturarla, así que se lanzaría la excepción automáticamente
# obj3 = Singleton()  # Esto lanzaría una excepción debido a que ya existe una instancia

