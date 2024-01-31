import random

def geraListaIdades( quantidade, idade_minimo=18, idade_maximo=65):
    idades = [random.randint(idade_minimo, idade_maximo) for _ in range(quantidade)]
    return idades 

class ListaIdades:
    def __init__(self, idades=[]):
        self.idades = idades

 # Adiciona essa linha para retornar a lista gerada

# Agora você pode usar o código assim:
lista_idades = geraListaIdades(50)
idades_obj = ListaIdades(lista_idades)

print(type(lista_idades))
print(type(idades_obj))
print(lista_idades)
print(idades_obj)
