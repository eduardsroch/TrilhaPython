import ListaNotas

notas = ListaNotas.NotasTurma()
notas.leNotas()
print (notas.quantAprovados())
print (notas.quantReprovados())
print(notas.mediaTurma())
print(notas.mediaAluno(9))
print(notas.mediaAvaliaçao(0))
print(notas.maiorNota())
print(notas.menorNota())