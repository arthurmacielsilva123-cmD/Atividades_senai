# TODO: 
# banco virtual


#biblotecas
import random
import time


#classe
class Conta:
    """
    Classe que representa uma Conta bancária.
    """
    
    def __init__(self, titular, cpf):
        """
        Inicializa uma nova conta.
        O saldo inicial é 0.
        Agência e Conta são gerados automaticamente para este exemplo.
        """
        self.titular = titular
        self.cpf = cpf
        # Define uma agência fixa para simplificar
        self.numero_agencia = "0001" 
        # Gera um número de conta aleatório
        self.numero_conta = f"{random.randint(10000, 99999)}-{random.randint(0, 9)}"
        self.saldo = 0.0
        print(f"Conta criada com sucesso para {self.titular}!")
        print(f"Agência: {self.numero_agencia} | Conta: {self.numero_conta}")

    def consultar_dados(self):
        """
        Exibe os dados formatados da conta e o saldo atual.
        """
        print("\n--- Consulta de Dados da Conta ---")
        print(f"Titular: {self.titular}")
        print(f"CPF: {self.cpf}")
        print(f"Agência: {self.numero_agencia}")
        print(f"Conta: {self.numero_conta}")
        # Formata o saldo para exibir como moeda (R$)
        print(f"Saldo Atual: R$ {self.saldo:.2f}")
        print("------------------------------------")

    def depositar(self, valor):
        """
        Adiciona um valor ao saldo da conta.
        O valor deve ser positivo.
        """
        if valor > 0:
            self.saldo += valor
            print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso.")
            print(f"Novo saldo: R$ {self.saldo:.2f}")
        else:
            print("\nErro: O valor do depósito deve ser maior que zero.")

    def sacar(self, valor):
        """
        Retira um valor do saldo da conta.
        O valor deve ser positivo e não pode ser maior que o saldo disponível.
        """
        if valor <= 0:
            print("\nErro: O valor do saque deve ser maior que zero.")
        elif valor > self.saldo:
            print("\nErro: Saldo insuficiente para este saque.")
            print(f"Seu saldo atual é: R$ {self.saldo:.2f}")
        else:
            self.saldo -= valor
            print(f"\nSaque de R$ {valor:.2f} realizado com sucesso.")
            print(f"Novo saldo: R$ {self.saldo:.2f}")

def exibir_menu():
    """
    Função auxiliar para mostrar o menu de opções.
    """
    print("\n--- Banco Virtual - Menu ---")
    print("[1] Consultar dados da conta")
    print("[2] Depositar valor")
    print("[3] Sacar valor")
    print("[4] Sair do programa")
    print("------------------------------")

def main():
    """
    Função principal que executa o aplicativo do banco.
    """
    print("--- Bem-vindo ao Banco Virtual ---")
    print("Por favor, crie sua conta para começar.")
    
    # Coleta os dados iniciais do usuário
    titular = input("Digite o nome completo do titular: ")
    cpf = input("Digite o CPF do titular (apenas números): ")
    
    # Cria o objeto da conta
    minha_conta = Conta(titular, cpf)
    
    time.sleep(1) # Pequena pausa

    # Loop principal do menu
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            # 1. Consultar dados
            minha_conta.consultar_dados()
            
        elif opcao == '2':
            # 2. Depositar
            try:
                # Tenta converter a entrada para float
                valor_deposito = float(input("Digite o valor a depositar: R$ "))
                minha_conta.depositar(valor_deposito)
            except ValueError:
                print("\nErro: Valor inválido. Por favor, digite um número (ex: 150.50).")
                
        elif opcao == '3':
            # 3. Sacar
            try:
                # Tenta converter a entrada para float
                valor_saque = float(input("Digite o valor a sacar: R$ "))
                minha_conta.sacar(valor_saque)
            except ValueError:
                print("\nErro: Valor inválido. Por favor, digite um número (ex: 100.00).")

        elif opcao == '4':
            # 4. Sair
            print("\nObrigado por usar o Banco Virtual. Volte sempre!")
            break # Encerra o loop while
            
        else:
            # Opção inválida
            print("\nOpção inválida. Por favor, escolha um número de 1 a 4.")
            
        time.sleep(1.5) # Pausa para o usuário ler a saída

# Executa a função principal quando o script é rodado
if __name__ == "__main__":
    main()




"""
 crie um app de banco. O programa devera ter a classe conta, com os atributos:
 - titular da conta(nome)
 - cpf do titular
 - número da agencia
 -  Número da agencia 
 - numero da conta
 - saldo
 o usuario irá inserir os dados titular da conta e cpf, e poderá escolher
 entre as seguites opções:
 - Consultar dados da conta
 - depositar valor
 - sacar valor
 - sair do programa 
 
 """