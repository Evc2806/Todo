class Perro:
    def __init__(self,nombre):
        self.__nombre=nombre
        
    def obtener_nombre(self):
            return  self.__nombre
        
    def cambiar_nombre(self,nuevo_nombre):
        self.__nombre=nuevo_nombre
    
mi_perro=Perro("maxi")

print(mi_perro.obtener_nombre())

mi_perro.cambiar_nombre("simon")

print(mi_perro.obtener_nombre())


nombre=int(input("ingrese nombre"))
nombre="edwin"








        