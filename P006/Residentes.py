import pandas as pd
import numpy as np

class Residente:
    def __init__(self, nome, ano_nascimento, genero, endereco, turma, cpf):
        self._nome = nome
        self._ano_nascimento = ano_nascimento
        self._genero = genero
        self._endereco = endereco
        self._turma = turma
        self._cpf = cpf
        self._identificador = f"tic18{turma}{cpf[:3]}{str(ano_nascimento)[-2:]}"

    def get_nome(self):
        return self._nome

    def get_idade(self, ano_atual):
        return ano_atual - self._ano_nascimento

    def get_genero(self):
        return self._genero

    def get_endereco(self):
        return self._endereco

    def get_turma(self):
        return self._turma

    def get_cpf(self):
        return self._cpf

    def get_identificador(self):
        return self._identificador

    def __str__(self):
        return f"Residente(nome={self._nome}, identificador={self._identificador}, turma={self._turma})"


class Trilha:
    def __init__(self):
        self._entrevistados = pd.DataFrame(columns=['Nome', 'Identificador', 'Idade', 'Gênero', 'Endereço',
                                                    'Turma', 'CPF', 'Formação', 'Formação_Especifica',
                                                    'Formação_Geral', 'Andamento_Graduação', 'Tempo_Formação',
                                                    'Experiencia_Previa'])

    def adicionar_residente(self, residente, formacao_especifica=None, formacao_geral=False,
                            andamento_graduacao=None, tempo_formacao=None, experiencia_previa=False):
        if residente.get_identificador() not in self._entrevistados['Identificador'].values:
            dados_residente = {
                'Nome': residente.get_nome(),
                'Identificador': residente.get_identificador(),
                'Idade': residente.get_idade(2024),  # Assume-se que a coleta de dados ocorre em 2024
                'Gênero': residente.get_genero(),
                'Endereço': residente.get_endereco(),
                'Turma': residente.get_turma(),
                'CPF': residente.get_cpf(),
                'Formação': None,
                'Formação_Especifica': formacao_especifica,
                'Formação_Geral': formacao_geral,
                'Andamento_Graduação': andamento_graduacao,
                'Tempo_Formação': tempo_formacao,
                'Experiencia_Previa': experiencia_previa
            }
            self._entrevistados = self._entrevistados.append(dados_residente, ignore_index=True)
        else:
            print(f"Entrevistado {residente.get_nome()} já existe na trilha.")

    def obter_entrevistados(self):
        return self._entrevistados

    def __str__(self):
        return f"Trilha(entrevistados=\n{self._entrevistados})"


class Residencia:
    def __init__(self):
        self._trilhas = {}

    def adicionar_trilha(self, nome_trilha, trilha):
        if nome_trilha not in self._trilhas:
            self._trilhas[nome_trilha] = trilha
        else:
            print(f"A trilha {nome_trilha} já existe na residência.")

    def obter_trilhas(self):
        return self._trilhas

    def __str__(self):
        return f"Residencia(trilhas=\n{self._trilhas})"


# Exemplo de uso:

# Criar residentes
residente1 = Residente("João", 1990, "Masculino", "Rua A", "Py", "123456789")
residente2 = Residente("Maria", 1995, "Feminino", "Rua B", "Net", "987654321")

# Criar trilhas
trilha_py = Trilha()
trilha_net = Trilha()

# Adicionar residentes às trilhas
trilha_py.adicionar_residente(residente1, formacao_especifica="Engenharia", experiencia_previa=True)
trilha_net.adicionar_residente(residente2, formacao_geral=True, andamento_graduacao="Em andamento")

# Criar residência e adicionar trilhas
residencia = Residencia()
residencia.adicionar_trilha("Trilha Python", trilha_py)
residencia.adicionar_trilha("Trilha .NET", trilha_net)

# Exibir informações
print(residencia)

# Persistência usando Pandas
entrevistados_df = trilha_py.obter_entrevistados()
entrevistados_df.to_csv('entrevistados.csv', index=False)
# Para carregar novamente os dados
entrevistados_carregados = pd.read_csv('entrevistados.csv')
print(entrevistados_carregados)
