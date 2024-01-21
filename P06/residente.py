from datetime import datetime

class Residente:
    def __init__(self, identificador, idade, formacao, formacao_geral, formacao_especifica, porcentagem, tempo_formado, experiencia):

        self.__identificador = identificador
        self.__idade = idade
        self.__formacao = formacao
        self.__formacao_geral = formacao_geral
        self.__formacao_especifica = formacao_especifica
        self.__porcentagem = porcentagem
        self.__tempo_formado = tempo_formado
        self.__experiencia = experiencia

        # adiciona_residente para garantir consistência nos dados
        self.adiciona_residente(identificador, idade, formacao, formacao_geral, formacao_especifica, porcentagem, tempo_formado, experiencia)

    # acessar os atributos privados
    def get_identificador(self):
        return self.__identificador

    def get_formacao(self):
        return self.__formacao

    def get_tempo_formado(self):
        return self.__tempo_formado

    def get_experiencia(self):
        return self.__experiencia

    # atualizar atributos com novos dados do residente
    def adiciona_residente(self, identificador, idade, formacao, formacao_geral, formacao_especifica, porcentagem, tempo_formado, experiencia):
        self.__idade = idade  
        self.__formacao_especifica = formacao_especifica
        self.__porcentagem = porcentagem
        self.__tempo_formado = tempo_formado
        self.__experiencia = experiencia

        # validar e atualizar alguns atributos com base na formação
        if formacao >= 0 and formacao <= 3:
            self.__formacao = formacao
        if formacao_geral >= 0 and formacao_geral <= 1:
            self.__formacao_geral = formacao_geral
        nascimento = datetime.now().year - idade
        nascimento1 = datetime.now().year - idade - 1
        if identificador[-2:] == str(nascimento)[-2:] or identificador[-2:] == str(nascimento1)[-2:]:
            self.__identificador = identificador   
        if formacao == 0:
            self.__formacao_geral = None
            self.__formacao_especifica = None
        if formacao == 0 or formacao == 3:
            self.__porcentagem = None
        if formacao == 0 or formacao == 1 or formacao == 2:
            self.__tempo_formado = None

    # validar o identificador
    def valida_identificador(self):
        nascimento = datetime.now().year - self.__idade
        nascimento1 = datetime.now().year - self.__idade - 1
        return self.__identificador[-2:] == str(nascimento)[-2:] or self.__identificador[-2:] == str(nascimento1)[-2:]

    # verificar se o residente é um graduando
    def is_graduando(self):
        return self.__formacao == 2

    # verificar a validade do tempo formado
    def is_tempo_formado_valido(self):
        return self.__formacao != 2 or self.__tempo_formado is not None

    # verificar a validade da experiência
    def is_experiencia_valida(self):
        return self.__experiencia in ["Sim", "Não"]

    # converter os dados do residente em um dicionário
    def to_dict(self):
        return {
            "identificador": self.__identificador,
            "idade": self.__idade,
            "formacao": self.__formacao,
            "formacao_geral": self.__formacao_geral,
            "formacao_especifica": self.__formacao_especifica,
            "porcentagem": self.__porcentagem,
            "tempo_formado": self.__tempo_formado,
            "experiencia": self.__experiencia
        }

    # representação em string do objeto
    def __str__(self):
        return f"Residente(identificador={self.__identificador}, idade={self.__idade}, formacao={self.__formacao}, formacao_geral={self.__formacao_geral}, formacao_especifica={self.__formacao_especifica}, porcentagem={self.__porcentagem}, tempo_formado={self.__tempo_formado}, experiencia={self.__experiencia})"
