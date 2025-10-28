# TODO: atividade

# tratamento de exceção
try:
    # entrada de dados
    nome = input("Informe seu nome: ").strip().title()
    idade = int(input("Informe sua idade: ").strip())

    # lista de filmes
    sala_1 = "A Roda Quadrada"
    sala_2 = "A Volta dos Que Não Foram"
    sala_3 = "Poeira em Alto Mar"
    sala_4 = "As Tranças do Rei Careca"
    sala_5 = "A Vingança do Frango Assado"

    # loop
    while True:
        # menu de filmes
        print(f"Sala 1 - {sala_1} - Livre")
        print(f"Sala 2 - {sala_2} - 12 anos")
        print(f"Sala 3 - {sala_3} - 14 anos")
        print(f"Sala 4 - {sala_4} - 16 anos")
        print(f"Sala 5 - {sala_5} - 18 anos")
        sala = input("Informe a sala desejada: ").strip()

        # verifica a sala selecionada
        match sala:
            case "1":
                filme = sala_1
                idade_minima = 0
            case "2":
                filme = sala_2
                idade_minima = 12
            case "3":
                filme = sala_3
                idade_minima = 14
            case "4":
                filme = sala_4
                idade_minima = 16
            case "5":
                filme = sala_5
                idade_minima = 18
            case _:
                print("Sala inexistente.")
        if idade >= idade_minima:
            print(f"{nome} escolheu {filme}. Tenha um bom filme!")
            break
        else:
            print(f"{nome} não foi autorizado a ver {filme}.")
            continue
except Exception as e:
    print(f"Erro no programa. {e}")

"""
Crie um programa que recebe do usuário o nome e a idade, e em seguida, exiba na tela uma lista de filmes, suas respectivas salas e classificações indicativas:
Sala 1 - A Roda Quadrada - Livre
Sala 2 - A Volta dos Que Não Foram - 12 anos
Sala 3 - Poeira em Alto Mar - 14 anos
Sala 4 - As Tranças do Rei Careca - 16 anos
Sala 5 - A Vingança do Frango Assado - 18 anos
O usuário deverá escolher o filme, e caso ele tiver a idade mínima para ver o filme, imprime o ingresso e encerra o programa. Caso o usuário não tenha a idade mínima, o programa impede a entrada do usuário e re-exibe a lista de filmes para que o mesmo escolha outro filme.
"""