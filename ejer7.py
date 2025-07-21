class CuentaBancaria:
    def __init__(self,titular, saldo_inicial):
        self.titular= titular
        self.__saldo= saldo_inicial
        
    def depositar(self, cantidad):
        if cantidad >0:
            self.__saldo+=cantidad
            return f"Depósito realizado {self.__saldo}"
        
        return "Cantidad inválida"
    
    def retirar( self, cantidad):
         if 0<cantidad<=self.__saldo:
             self.__saldo-=cantidad
             return f"Retiro exitoso. Saldo actual {self.__saldo}"
    
    def consultar_saldo(self):
        return f"Saldo actual {self.__saldo}"

cuenta= CuentaBancaria("Hector", 2000)
print(cuenta.depositar(1200))
