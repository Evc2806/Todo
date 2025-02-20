class Animal: 
    def hacer_sonido(self):
        pass
    
class Perro(Animal):
    def hacer_sonido(self):
        print("guau")
        
        
class Gato(Animal):
    def hacer_sonido(self):
        print("miau")
        
animales=[Perro(),Gato()]

for animal in animales:
    animal.hacer_sonido()
        
        
       
        
