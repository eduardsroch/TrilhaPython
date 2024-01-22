from trilha import Trilha

class Residencia:
    def __init__(self):
        # inicializa a residência com um dicionário vazio para armazenar as trilhas
        self.__trilhas = {}

    def adiciona_trilha(self, nome_trilha):
        # adiciona uma nova trilha à residência se ela não existir
        if nome_trilha not in self.__trilhas:
            self.__trilhas[nome_trilha] = Trilha(nome_trilha)

    def adiciona_residente_na_trilha(self, nome_trilha, residente):
        # adiciona um residente a uma trilha específica
        if nome_trilha in self.__trilhas:
            self.__trilhas[nome_trilha].adiciona_residente(residente)

    def mostrar_dataframe_trilha(self, nome_trilha):
        # mostra o DataFrame de uma trilha específica
        if nome_trilha in self.__trilhas:
            self.__trilhas[nome_trilha].mostrar_dataframe()

    def salvar_dados(self):
        # salva os dados de todas as trilhas
        for nome_trilha, trilha in self.__trilhas.items():
            trilha.salvar_dados()

    def carregar_dados(self):
        # carrega os dados de todas as trilhas
        for nome_trilha, trilha in self.__trilhas.items():
            trilha.carregar_dados()

    def get_trilhas(self):
        # retorna o dicionário de trilhas
        return self.__trilhas
