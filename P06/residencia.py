from trilha import Trilha

class Residencia:
    def __init__(self):
        self.__trilhas = {}

    def adiciona_trilha(self, nome_trilha):
        # verifica se a trilha já existe no dicionário de trilhas
        if nome_trilha not in self.__trilhas:
            # se não existir, cria uma nova instância de Trilha e adiciona ao dicionário
            self.__trilhas[nome_trilha] = Trilha(nome_trilha)

    def adiciona_residente_na_trilha(self, nome_trilha, residente):
        # verifica se a trilha existe no dicionário de trilhas
        if nome_trilha in self.__trilhas:
            # se existir, chama o método adiciona_residente da trilha correspondente
            self.__trilhas[nome_trilha].adiciona_residente(residente)

    def get_trilhas(self):
        # retorna o dicionário de trilhas
        return self.__trilhas

    def salvar_dados(self):
        # percorre o dicionário de trilhas
        for nome_trilha, trilha in self.__trilhas.items():
            # chama o método salvar_dados da trilha correspondente
            trilha.salvar_dados()

    def carregar_dados(self):
        # percorre o dicionário de trilhas
        for nome_trilha, trilha in self.__trilhas.items():
            # chama o método carregar_dados da trilha correspondente
            trilha.carregar_dados()
