from datetime import datetime

class Residente:
    def __init__(self, identificador, idade, formacao,formacao_geral, formacao_especifica, porcentagem, tempo_formado, experiencia):
        self.identificador = identificador
        self.idade = idade  
        self.formacao = formacao
        self.formacao_geral = formacao_geral
        self.formacao_especifica = formacao_especifica
        self.porcentagem = porcentagem
        self.tempo_formado = tempo_formado
        self.experiencia = experiencia

    

    def adicionaResidente(self, identificador, idade, formacao,formacao_geral, formacao_especifica, porcentagem, tempo_formado, experiencia):
        self.idade = idade  
        self.formacao_especifica = formacao_especifica
        self.porcentagem = porcentagem
        self.tempo_formado = tempo_formado
        self.experiencia = experiencia

        if formacao >= 0 and formacao <=3:
            self.formacao = formacao
        if formacao_geral >= 0 and formacao_geral <=1:
            self.formacao_geral = formacao_geral
        nascimento = datetime.now().year - idade
        nascimento1 = datetime.now().year - idade -1
        if identificador[-2:] == str(nascimento)[-2:] or identificador[-2:]== str(nascimento1)[-2:]:
            self.identificador = identificador   
        if formacao == 0:
            self.formacao_geral = None
            self.formacao_especifica = None
        if formacao == 0 or formacao == 3:
            self.porcentagem = None
        if formacao == 0 or formacao == 1 or formacao == 2:
            self.tempo_formado = None


    
