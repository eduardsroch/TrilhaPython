import numpy as np
class NotasTurma:

    def __init__(self, nAlunos = 30, nCreditos = 3):
        self.listaNotas = np.zeros((nAlunos,nCreditos))
        self.nAlunos = nAlunos
        self.nCreditos = nCreditos
        pass
    def leNotas(self):
        self.listaNotas = np.round(np.random.uniform(low = 0, high = 10, size = (self.nAlunos, self.nCreditos)),2)
        print (self.listaNotas)
    def mediaTurma(self):
        mediaTurma = np.mean(self.listaNotas)
        return mediaTurma
    def mediaAluno(self, index = 0):
        if index > self.nAlunos:
            print("Aluno inexistente")
            return
        mediaAluno = np.mean(self.listaNotas[index,:])
        return mediaAluno
    def mediaAvaliaçao(self, index = 0):
        if index > self.nCreditos:
            print("Avaliação inexistente")
            return
        mediaAvaliaçao = np.mean(self.listaNotas[:,index])
        return mediaAvaliaçao
    def quantAprovados(self): 
        media = np.mean(self.listaNotas[:,:3], axis = 1)>=6
        media = np.count_nonzero(media)
        #print (media)
        return media
    def quantReprovados(self):
        media = np.mean(self.listaNotas[:,:3], axis = 1) < 6
        reprovados = np.count_nonzero(media)
        #print (media)
        return reprovados
        
    def menorNota(self):
        listaDeNotasRuins = np.zeros(4)
        listaDeNotasRuins[0]= np.min(self.listaNotas[:,0])
        listaDeNotasRuins[1]= np.min(self.listaNotas[:,1])
        listaDeNotasRuins[2]= np.min(self.listaNotas[:,2])
        listaDeNotasRuins[3]= np.min(np.mean(self.listaNotas[:,:3], axis = 1))
        return listaDeNotasRuins
    def maiorNota(self):
        listaDeNotasBoas = np.zeros(4)
        listaDeNotasBoas[0]= np.max(self.listaNotas[:,0])
        listaDeNotasBoas[1]= np.max(self.listaNotas[:,1])
        listaDeNotasBoas[2]= np.max(self.listaNotas[:,2])
        listaDeNotasBoas[3]= np.max(np.mean(self.listaNotas[:,:3], axis = 1))
        return listaDeNotasBoas

    def __str__(self):
        
        pass