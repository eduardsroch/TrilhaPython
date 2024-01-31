import pandas as pd

class Residente:
    def __init__(self, nome, cpf, ano_nascimento, turma, idade=None, formacao=None, formacao_geral=False, andamento_graduacao=None, tempo_formacao=None, experiencia_programacao=False):
        self._nome = nome
        self._cpf = cpf
        self._ano_nascimento = ano_nascimento
        self._turma = turma
        self._idade = idade
        self._formacao = formacao
        self._formacao_geral = formacao_geral
        self._andamento_graduacao = andamento_graduacao
        self._tempo_formacao = tempo_formacao
        self._experiencia_programacao = experiencia_programacao

    def calcular_idade(self, ano_atual):
        self._idade = ano_atual - self._ano_nascimento

    def get_nome(self):
        return self._nome

    def get_cpf(self):
        return self._cpf

    def get_ano_nascimento(self):
        return self._ano_nascimento

    def get_turma(self):
        return self._turma

    def get_idade(self):
        return self._idade

    def set_formacao(self, formacao):
        # Mapear opções de formação para códigos numéricos
        formacoes = {'Bacharelado': 1, 'Licenciatura': 2, 'Tecnólogo': 3}
        self._formacao = formacoes.get(formacao)

    def get_formacao(self):
        return self._formacao

    def set_formacao_geral(self, formacao_geral):
        self._formacao_geral = formacao_geral

    def get_formacao_geral(self):
        return self._formacao_geral

    def set_andamento_graduacao(self, andamento_graduacao):
        self._andamento_graduacao = andamento_graduacao

    def get_andamento_graduacao(self):
        return self._andamento_graduacao

    def set_tempo_formacao(self, tempo_formacao):
        self._tempo_formacao = tempo_formacao

    def get_tempo_formacao(self):
        return self._tempo_formacao

    def adicionar_experiencia_programacao(self):
        # Lógica de determinar experiência em programação
        self._experiencia_programacao = True

    def tem_experiencia_programacao(self):
        return self._experiencia_programacao


class Trilha:
    def __init__(self, identificador):
        self._identificador = identificador
        self._dados_entrevistados = pd.DataFrame(columns=['Nome', 'CPF', 'Ano Nascimento', 'Turma', 'Idade', 'Formação', 'Formação Geral', 'Andamento Graduação', 'Tempo Formação', 'Experiência Programação'])

    def adicionar_residente(self, residente):
        # Adicione lógica para garantir identificadores únicos
        cpf_residente = getattr(residente, '_cpf', None)  # Pode não ter atributo _cpf
        if cpf_residente is not None and cpf_residente not in self._dados_entrevistados['CPF'].values:
            residente.calcular_idade(2024)  # Assumindo que a coleta é feita em 2024
            residente.set_formacao('Bacharelado')  # Exemplo, ajuste conforme a coleta real

            dados_residente = {
                'Nome': residente.get_nome(),
                'CPF': cpf_residente,
                'Ano Nascimento': residente.get_ano_nascimento(),
                'Turma': residente.get_turma(),
                'Idade': residente.get_idade(),
                'Formação': residente.get_formacao(),
                'Formação Geral': residente.get_formacao_geral(),
                'Andamento Graduação': residente.get_andamento_graduacao(),
                'Tempo Formação': residente.get_tempo_formacao(),
                'Experiência Programação': residente.tem_experiencia_programacao()
            }

            self._dados_entrevistados = self._dados_entrevistados.append(dados_residente, ignore_index=True)
        else:
            if cpf_residente is not None:
                print(f"CPF {cpf_residente} já entrevistado nesta trilha.")
            else:
                print("Residente sem CPF não pode ser adicionado à trilha.")


class Residencia:
    def __init__(self, nome_residencia):
        self._nome_residencia = nome_residencia
        self._trilhas = {}

    def adicionar_trilha(self, identificador_trilha):
        if identificador_trilha not in self._trilhas:
            self._trilhas[identificador_trilha] = Trilha(identificador_trilha)
        else:
            print(f"Trilha {identificador_trilha} já existe nesta residência.")

    def obter_trilha(self, identificador_trilha):
        return self._trilhas.get(identificador_trilha)


def menu():
    print("----- Menu -----")
    print("1. Adicionar residente")
    print("2. Exibir dados da turma Python")
    print("3. Sair")


# Exemplo de utilização do menu:

# Criar uma residência
residencia = Residencia("Minha Residência")

# Adicionar trilhas
residencia.adicionar_trilha("tic18Py")
residencia.adicionar_trilha("tic18Net")
residencia.adicionar_trilha("tic18Jav")

opcao = 0

while opcao != 3:
    menu()

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Opção inválida. Digite um número.")

    if opcao == 1:
        nome = input("Digite o nome do residente: ")
        cpf = input("Digite o CPF do residente: ")
        ano_nascimento = int(input("Digite o ano de nascimento do residente: "))
        turma = input("Digite a turma do residente (tic18Py, tic18Net, tic18Jav): ")

        residente = Residente(nome, cpf, ano_nascimento, turma)
        residencia.obter_trilha(turma).adicionar_residente(residente)

        print(f"Residente {nome} adicionado com sucesso!")

    elif opcao == 2:
        dados_turma_python = residencia.obter_trilha("tic18Py")._dados_entrevistados
        print("Dados da turma Python:")
        print(dados_turma_python)

    elif opcao == 3:
        print("Saindo do programa.")

    else:
        print("Opção inválida. Digite um número de 1 a 3.")
