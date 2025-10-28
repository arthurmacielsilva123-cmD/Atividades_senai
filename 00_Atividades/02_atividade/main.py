# TODO: atividade

# bibliotecas
import time
import os

try:
    n = int(input("Informe um número inteiro: ").strip())
    while n >= 0:
        os.system("cls")
        print(n)
        time.sleep(1)
        n -= 1
    print("BOOOOMMM!!!!")
except:
    print("Deu erro.")

"""
Crie um programa que receba um número inteiro do usuário, e mostre uma contagem regressiva em segundos, e ao terminar, exiba uma mensagem qualquer.
"""