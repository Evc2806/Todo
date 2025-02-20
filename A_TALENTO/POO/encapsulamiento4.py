class Perro:
    def __init__(self,nombre):
        self.__nombre=nombre
        
    def obtener_noombre(self):
        return self.__nombre
    
    def cambiar_nombre(self,nuevo_nombre):
        self.__nombre=nuevo_nombre
        
mi_perro= Perro("max")

print(mi_perro.obtener_noombre())

mi_perro.cambiar_nombre("ruby")

print(mi_perro.obtener_noombre())


        