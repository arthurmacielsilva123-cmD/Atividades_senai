# TODO: atividade

# biblioteca
import os

# entrada de dados
nome = input("Informe o nome: ").strip().title() # string
email = input("Informe o e-mail: ").strip().lower() # string
cpf = input("Informe o CPF: ").strip() # string
telefone = input("Informe o telefone:").strip() # string

# limpa console
os.system("cls")

# saída de dados
print(f"Nome: {nome}")
print(f"E-mail: {email}")
print(f"CPF: {cpf}")
print(f"Telefone: {telefone}")


"""
Crie um programa que receba do usuário o nome, e-mail, cpf e telefone, limpe o console, e em seguida, exiba as informações do usuário na tela.
"""