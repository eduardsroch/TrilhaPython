from datetime import datetime
from residente import Residente
from trilha import Trilha
from residencia import Residencia

def exibir_menu():
    print("MENU:")
    print("1. Adicionar Residente à Trilha Python")
    print("2. Adicionar Residente à Trilha .NET")
    print("3. Adicionar Residente à Trilha Java")
    print("4. Voltar ao Menu Anterior")
    print("5. Sair")

# Fadicionar um residente a uma trilha
def adicionar_residente(trilha, nome_trilha):

    idade = int(input("Idade: "))
    formacao = int(input("Formação (0-3): "))
    formacao_geral = bool(int(input("Formação Geral (0/1): ")))
    formacao_especifica = input("Formação Específica: ")
    porcentagem = int(input("Porcentagem: "))
    tempo_formado = None
    if formacao != 2:
        tempo_formado = int(input("Tempo Formado: "))
    experiencia = input("Experiência (Sim/Não): ")

    # identificador do residente
    ano_nascimento = datetime.now().year - idade
    tipo_trilha = nome_trilha[:6]
    identificador = f"{tipo_trilha}{str(ano_nascimento)[-3:]}"

    # objeto Residente com as informações fornecidas
    residente = Residente(identificador, idade, formacao, formacao_geral, formacao_especifica, porcentagem, tempo_formado, experiencia)
    
    # adicionando o residente à trilha
    trilha.adiciona_residente(residente)
    print(f"Residente adicionado à Trilha {nome_trilha} com identificador: {identificador}")


def main():

    residencia = Residencia()
    residencia.carregar_dados()  # Carregar dados ao iniciar o programa
    trilha_atual = None

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome_trilha = "Python"
            residencia.adiciona_trilha(nome_trilha)
            trilha_atual = residencia.get_trilhas()[nome_trilha]
            adicionar_residente(trilha_atual, nome_trilha)
        elif opcao == "2":
            nome_trilha = ".NET"
            residencia.adiciona_trilha(nome_trilha)
            trilha_atual = residencia.get_trilhas()[nome_trilha]
            adicionar_residente(trilha_atual, nome_trilha)
        elif opcao == "3":
            nome_trilha = "Java"
            residencia.adiciona_trilha(nome_trilha)
            trilha_atual = residencia.get_trilhas()[nome_trilha]
            adicionar_residente(trilha_atual, nome_trilha)
        elif opcao == "4":
            trilha_atual = None
        elif opcao == "5":
            residencia.salvar_dados()  # salvar dados ao encerrar o programa
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
