class Perro:
    def __init__(self, nombre, edad):
        self.nombre= nombre
        self.edad= edad
    def ladrar(self):
        return f"{self.nombre} tiene {self.edad} años"

mi_perro= Perro("Poncio",3)
print(mi_perro.ladrar())