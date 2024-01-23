import pandas as pd

class Trilha:
    def __init__(self, nome):
        # inicializa a classe Trilha com um nome e um DataFrame vazio
        self.__nome = nome
        self.__df = pd.DataFrame(columns=['identificador', 'idade', 'formacao', 'formacao_geral', 'formacao_especifica', 'porcentagem', 'tempo_formado', 'experiencia'])

    def adiciona_residente(self, residente):
        # adiciona um residente ao DataFrame
        self.__df.loc[len(self.__df)] = residente.to_dict()

    def mostrar_dataframe(self):
        # mostra o DataFrame
        print(self.__df)

    def salvar_dados(self):
        # salva o DataFrame em um arquivo CSV com o nome da trilha
        self.__df.to_csv(f"{self.__nome}_dados.csv", index=False)

    def carregar_dados(self):
        # carrega os dados de um arquivo CSV com o nome da trilha, se existir
        try:
            self.__df = pd.read_csv(f"{self.__nome}_dados.csv")
        except FileNotFoundError:
            print(f"Arquivo {self.__nome}_dados.csv não encontrado. Criando novo DataFrame.")
