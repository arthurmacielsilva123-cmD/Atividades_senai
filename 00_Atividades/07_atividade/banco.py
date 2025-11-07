# biblioteca padrão
import os

# ==========================
# CLASSE CONTA BANCÁRIA
# ==========================
class Conta:
    def __init__(self, titular, cpf, agencia, numero_conta, saldo=0.0):
        self.titular = titular
        self.cpf = cpf
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo

    # método para exibir informações da conta
    def exibir_dados(self):
        print("=== DADOS DA CONTA ===")
        print(f"Titular: {self.titular}")
        print(f"CPF: {self.cpf}")
        print(f"Agência: {self.agencia}")
        print(f"Número da Conta: {self.numero_conta}")
        print(f"Saldo: R${self.saldo:.2f}")

    # método para depositar valor
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito!")

    # método para sacar valor
    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido para saque!")
        elif valor > self.saldo:
            print("Saldo insuficiente!")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
