import os
from classe import conta


def limpar():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    limpar()

    cc = conta(titular="", cpf="", agencia="4002", n_conta="12345", saldo=0)

    cc.titular = input("Informe o nome do titular: ").strip().title()
    cc.cpf = input("Informe o CPF do titular: ").strip()
    limpar()

    while True:
        # MENU
        print("1 - Consultar dados")
        print("2 - Depositar valor")
        print("3 - Sacar valor")
        print("4 - Sair do programa")

        opcao = input("Opção desejada: ").strip()

        match opcao:
            case "1":
                cc.consultar_dados()
                continue

            case "2":
                valor = float(input("Informe o valor do depósito: R$").strip().replace(",", "."))
                print(f"Depósito efetuado com sucesso. Saldo atual: R${cc.depositar(valor):.2f}")
                continue

            case "3":
                valor = float(input("Informe o valor do saque: R$").strip().replace(",", "."))
                print(f"Valor sacado: R${cc.sacar(valor):.2f}")
                continue

            case "4":
                print("Programa encerrado.")
                break

            case _:
                print("Opção inválida.")
                continue


if __name__ == "__main__":
    main()
