from __init__ import ListaIdades, ListaSalarios
import time
import random
import numpy as np

def geraListaIdades(quantidade, idade_minimo=18, idade_maximo=65):
    idades = []
    for _ in range(quantidade):
        idades = [random.randint(idade_minimo, idade_maximo) for _ in range(quantidade)]
    return idades

def geraListaSalarios(quantidade, salario_minimo = 1320, salario_maximo = 13200):
        salarios = []
        for _ in range(quantidade):
            salario = round(random.uniform(salario_minimo, salario_maximo), 2)
            salarios.append(salario)
        return salarios
x = 20000

lista_idades = geraListaIdades(x)
idades_obj = ListaIdades(lista_idades)

 
print("metodos tradicionais:")

start_time = time.time()
mediana = idades_obj.mostra_mediana()
elapsed_time = time.time() - start_time
print("Tempo para executar mostra_mediana: {elapsed_time} segundos")

start_time = time.time()
idades_obj.mostra_menor()
elapsed_time = time.time() - start_time
print(f"Tempo para executar mostra_menor: {elapsed_time} segundos")

start_time = time.time()
idades_obj.mostra_maior()
elapsed_time = time.time() - start_time
print(f"Tempo para executar mostra_maior: {elapsed_time} segundos")

lista_salarios = geraListaSalarios(x)
salarios_obj = ListaSalarios(lista_salarios)

start_time = time.time()
salarios_obj.mostra_mediana()
elapsed_time = time.time() - start_time
print(f"Tempo para executar mostra_mediana: {elapsed_time} segundos")

start_time = time.time()
salarios_obj.mostra_menor()
elapsed_time = time.time() - start_time
print(f"Tempo para executar mostra_menor: {elapsed_time} segundos")

start_time = time.time()
salarios_obj.mostra_maior()
elapsed_time = time.time() - start_time
print(f"Tempo para executar mostra_maior: {elapsed_time} segundos")

print("_____________________________________________")
print ("metodos numpy:")

def gera_idades_aleatorias(quantidade, idade_minima=18, idade_maxima=65):
    idades = np.random.randint(idade_minima, idade_maxima + 1, quantidade)
    return idades

quantidade_de_idades = x
idades_ = gera_idades_aleatorias(quantidade_de_idades)


start_time = time.time()
mediana = np.median(np.sort(idades_))
elapsed_time = time.time() - start_time
print(f"Tempo para executar mostra_mediana: {elapsed_time} segundos")

start_time = time.time()
menor_ = np.min(idades_)
elapsed_time = time.time() - start_time
print(f"Tempo para executar mostra_menor: {elapsed_time} segundos")

start_time = time.time()
maior_ = np.max(idades_)
elapsed_time = time.time() - start_time
print(f"Tempo para executar mostra_maior: {elapsed_time} segundos")

def gera_idades_aleatorias(quantidade, salario_minimo = 1320, salario_maximo = 13200):
    salario = np.random.uniform(salario_minimo, salario_maximo + 1, quantidade)
    return salario

quantidade_de_salarios = x
salarios_ = gera_idades_aleatorias(quantidade_de_idades)

start_time = time.time()
mediana_ = np.median(salarios_)
elapsed_time = time.time() - start_time
print(f"Tempo para executar mostra_mediana: {elapsed_time} segundos")

start_time = time.time()
menor_ = np.min(salarios_)
elapsed_time = time.time() - start_time
print(f"Tempo para executar mostra_menor: {elapsed_time} segundos")

start_time = time.time()
maior_ = np.max(salarios_)
elapsed_time = time.time() - start_time
print(f"Tempo para executar mostra_maior: {elapsed_time} segundos")