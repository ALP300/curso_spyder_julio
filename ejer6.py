class Coche:
    def __init__(self,marca, modelo):
        self.marca= marca
        self.modelo= modelo
        self.velocidad=0
        
    def acelerar(self,incremento):
        self.velocidad+=incremento
        return f"La velocidad es: {self.velocidad} km/h"
    
    def frenar(self):
        self.velocidad=0
        return f"El coche se ha detenido"

mi_coche= Coche("Toyota","Corolla")
print(mi_coche.acelerar(100))
    