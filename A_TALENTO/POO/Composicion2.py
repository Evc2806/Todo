# Clase base
class Componente:
    def mostrar(self):
        raise NotImplementedError("El método mostrar debe ser implementado.")

# Clase Hoja: representa objetos simples que no contienen otros componentes
class Hoja(Componente):
    def __init__(self, nombre):
        self.nombre = nombre
    
    def mostrar(self):
        print(f"Hoja: {self.nombre}")

# Clase ComponenteCompuesto: puede contener otros objetos Componente
class ComponenteCompuesto(Componente):
    def __init__(self, nombre):
        self.nombre = nombre
        self.componentes = []
    
    def agregar_componente(self, componente):
        self.componentes.append(componente)
    
    def eliminar_componente(self, componente):
        self.componentes.remove(componente)
    
    def mostrar(self):
        print(f"Componente compuesto: {self.nombre}")
        for componente in self.componentes:
            componente.mostrar()

# Crear una estructura jerárquica de componentes
hoja1 = Hoja("Hoja 1")
hoja2 = Hoja("Hoja 2")
hoja3 = Hoja("Hoja 3")

componente_compuesto1 = ComponenteCompuesto("Componente 1")
componente_compuesto1.agregar_componente(hoja1)
componente_compuesto1.agregar_componente(hoja2)

componente_compuesto2 = ComponenteCompuesto("Componente 2")
componente_compuesto2.agregar_componente(hoja3)

componente_principal = ComponenteCompuesto("Componente Principal")
componente_principal.agregar_componente(componente_compuesto1)
componente_principal.agregar_componente(componente_compuesto2)

# Mostrar la estructura jerárquica
componente_principal.mostrar()
