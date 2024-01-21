import pandas as pd

class Trilha:
    def __init__(self, nome):
        self.__nome = nome
        self.__residentes = []
        self.__df = pd.DataFrame(columns=['identificador', 'idade', 'formacao', 'formacao_geral', 'formacao_especifica', 'porcentagem', 'tempo_formado', 'experiencia'])

        # carregar dados do arquivo CSV ao criar uma nova instância
        self.carregar_dados()

    def adiciona_residente(self, residente):
        try:
            if residente.get_identificador() not in self.__df['identificador'].values:
                self.__df = self.__df.append(residente.to_dict(), ignore_index=True)
                self.__residentes.append(residente)
                self.salvar_dados()  # salvar dados ao adicionar residente
        except Exception as e:
            print(f"Erro ao adicionar residente: {e}")

    def get_residentes(self):
        return self.__residentes

    def get_dataframe(self):
        return self.__df

    def salvar_dados(self):
        self.__df.to_csv(f'{self.__nome}_dados.csv', index=False)

    def carregar_dados(self):
        try:
            self.__df = pd.read_csv(f'{self.__nome}_dados.csv')
        except FileNotFoundError:
            pass  # ignorar se o arquivo não existir ainda
