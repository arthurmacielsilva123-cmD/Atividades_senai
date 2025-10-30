# TODO: ATIVIDADE"
#CRIE UM PROGRAMA que receba do usuario os seguintes dados: nome, email,telefone,cpf,genero
#apos isso, o programa deve armazenar esses dados em um dicionario exibir os dados desse dicionario no terminal

def coletar_e_exibir_dados():
    """
    Coleta nome, email, telefone, CPF e gênero do usuário,
    armazena em um dicionário e exibe o resultado.
    """
    print("--- 📝 Coleta de Dados do Usuário ---")

    # 1. Coletando os dados
    nome = input("Digite seu Nome: ")
    email = input("Digite seu E-mail: ")
    telefone = input("Digite seu Telefone (com DDD): ")
    cpf = input("Digite seu CPF: ")
    genero = input("Digite seu Gênero: ")

    # 2. Armazenando os dados em um dicionário
    dados_usuario = {
        "Nome": nome,
        "Email": email,
        "Telefone": telefone,
        "CPF": cpf,
        "Gênero": genero
    }

    # 3. Exibindo os dados do dicionário
    print("\n--- ✅ Dados Cadastrados ---")
    
    # Percorrendo o dicionário para exibir os pares chave-valor
    for chave, valor in dados_usuario.items():
        print(f"**{chave}**: {valor}")
    
    # Exibe o dicionário completo (opcional)
    print("\n--- 💾 Dicionário Completo ---")
    print(dados_usuario)

# Chamada da função para executar o programa
if __name__ == "__main__":
    coletar_e_exibir_dados()
