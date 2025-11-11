# classe
class conta:
    def __init__(self, titular, cpf, agencia, n_conta, saldo):
         self.agencia = agencia
         self.n_conta = n_conta
         self.cpf = cpf
         self.saldo = saldo
         self.titular = titular
         
    
    def consultar_dados(self,):
        
        print(f"nome do titular da conta: {self.titular}")
        print(f"cpf do titular da conta: {self.cpf}")
        print(f"agencia da conta: {self.agencia}")
        print(f"Número da conta: {self.n_conta}")
        print(f"saldo da conta: R$ {self.saldo:.2f}")

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo
    
    def sacar(self, valor):
        # Continuação do seu código:
        if self.saldo >= valor: 
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado.")
            return True
        else:
            print("Saldo insuficiente.")
            return False
            
        
