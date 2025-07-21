class Animal:
    def __init__(self, nombre):
        self.nombre= nombre
    
    def moverse(self):
        return f"{self.nombre} está moviéndose"

class Perro(Animal):
    def maullar(self):
        return f"{self.nombre} está ladrando"


mi_gato= Perro("Shadow")
print(mi_gato.moverse())
print(mi_gato.maullar())