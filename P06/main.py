from residencia import Residencia
from trilha import Trilha
from residente import Residente

def adicionar_residente(trilha, nome_trilha):
    # solicita dados do residente ao usuário
    print("Informe os dados do residente:")
    identificador = input("Identificador: ")
    idade = int(input("Idade: "))
    formacao = int(input("Formação (0-3): "))
    formacao_geral = int(input("Formação Geral (0 ou 1): "))
    formacao_especifica = input("Formação Específica: ")
    porcentagem = float(input("Porcentagem : ")) if formacao == 3 else None
    tempo_formado = float(input("Tempo de Formado : ")) if formacao != 2 else None
    experiencia = input("Possui experiência (S/N): ").upper()

    # cria um objeto Residente com os dados fornecidos
    residente = Residente(identificador, idade, formacao, formacao_geral, formacao_especifica, porcentagem, tempo_formado, experiencia)

    # adiciona o residente à trilha especificada
    trilha.adiciona_residente(residente)
    print("Residente adicionado com sucesso!")

def main():
    # cria um objeto Residencia
    residencia = Residencia()

    while True:
        
        print("\nMenu Principal:")
        print("1. Adicionar Trilha")
        print("2. Adicionar Residente")
        print("3. Mostrar DataFrame da Trilha")
        print("4. Salvar Dados")
        print("5. Carregar Dados")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # adiciona uma nova trilha à residência
            nome_trilha = input("Informe o nome da trilha: ")
            residencia.adiciona_trilha(nome_trilha)
            print(f"Trilha '{nome_trilha}' adicionada com sucesso!")
        elif opcao == "2":
            # adiciona um residente a uma trilha existente
            nome_trilha = input("Informe o nome da trilha para adicionar o residente: ")
            trilha_atual = residencia.get_trilhas().get(nome_trilha)
            if trilha_atual:
                adicionar_residente(trilha_atual, nome_trilha)
            else:
                print(f"Trilha '{nome_trilha}' não encontrada.")
        elif opcao == "3":
            # mostra o DataFrame de uma trilha específica
            nome_trilha = input("Informe o nome da trilha para mostrar o DataFrame: ")
            trilha_atual = residencia.get_trilhas().get(nome_trilha)
            if trilha_atual:
                trilha_atual.mostrar_dataframe()
            else:
                print(f"Trilha '{nome_trilha}' não encontrada.")
        elif opcao == "4":
            # salva os dados da residência
            residencia.salvar_dados()
            print("Dados salvos com sucesso!")
        elif opcao == "5":
            # carrega os dados da residência
            residencia.carregar_dados()
            print("Dados carregados com sucesso!")
        elif opcao == "0":
            # sai do programa, salvando os dados antes
            residencia.salvar_dados()
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
