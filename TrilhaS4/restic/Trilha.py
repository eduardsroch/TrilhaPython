import pandas as pd

class Trilha:

    def __init__(self, residente, nome):
        self.nome = nome
        self.residente = residente
        self.df = pd.DataFrame(columns=['identificador', 'idade', 'formacao','formacao geral','formacao especifica', 'porcentagem', 'tempo de formado', 'experiencia'])

    def adicionaAluno(self, identificador, idade, formacao, formacao_geral, formacao_especifica, porcentagem, tempo_de_formado, experiencia):
        if identificador not in self.df['identificador'].values:
            self.df.loc[len(self.df)] = [identificador, idade, formacao, formacao_geral, formacao_especifica, porcentagem, tempo_de_formado, experiencia]
