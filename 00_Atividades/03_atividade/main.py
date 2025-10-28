# TODO: atividade

# tratamento de exceção
try:
    # entrada de dados
    nome = input("Informe o nome: ").strip().title()
    peso = float(input("Informe o peso em kg: ").strip().replace(",","."))
    altura = float(input("Informe a altura em metros: ").strip().replace(",","."))

    # cálculo do IMC
    imc = peso/(altura**2)

    # exibe o imc do usuário
    print(f"{nome}, seu IMC é {imc:.2f}")

    # diagnóstico do IMC
    if imc < 18.5:
        print(f"{nome} está abaixo do peso.")
    elif imc < 25:
        print(f"{nome} está no peso ideal.")
    elif imc < 30:
        print(f"{nome} está acima do peso.")
    elif imc < 35:
        print(f"{nome} está obeso.")
    elif imc < 40:
        print(f"{nome} está com obesidade nível II.")
    else:
        print(f"{nome} está com obesidade mórbida.")
except Exception as e:
    print(f"Deu ruim! {e}")

"""
Crie um programa que receba do usuário o nome, peso (em kg) e altura (em metros), calcule o IMC do usuário (arredondado para 2 casas decimais), e exiba o diagnóstico do usuário com base na tabela do IMC.
"""