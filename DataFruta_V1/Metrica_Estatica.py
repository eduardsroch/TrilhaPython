from abc import ABC, abstractmethod
import math

class Data:
    def __init__(self, dia=1, mes=1, ano=2000):
        self.dia = dia
        self.mes = mes
        self.ano = ano

class AnaliseDados(ABC):
    @abstractmethod
    def entrada_de_dados(self, dados):
        pass

    @abstractmethod
    def mostra_mediana(self):
        pass

    @abstractmethod
    def mostra_menor(self):
        pass

    @abstractmethod
    def mostra_maior(self):
        pass

    @abstractmethod
    def listar_em_ordem(self):
        pass

    @abstractmethod
    def calcula_media(self):
        pass

    @abstractmethod
    def calcula_desvio_padrao(self):
        pass

    @abstractmethod
    def calcula_variancia(self):
        pass

    @abstractmethod
    def __iter__(self):
        pass

class ListaNomes(AnaliseDados):
    def __init__(self):
        self.lista = []

    def entrada_de_dados(self, nomes):
        self.lista.extend(nomes)

    def mostra_mediana(self):
        sorted_lista = sorted(self.lista)
        tamanho = len(sorted_lista)
        if tamanho % 2 == 0:
            indice1 = tamanho // 2 - 1
            indice2 = tamanho // 2
            mediana = sorted_lista[indice1]  # Retorna o primeiro nome entre os dois no meio
        else:
            indice = tamanho // 2
            mediana = sorted_lista[indice]  # Retorna o nome do meio
        return mediana

    def mostra_menor(self):
        return min(self.lista)

    def mostra_maior(self):
        return max(self.lista)

    def listar_em_ordem(self):
        return sorted(self.lista)

    def calcula_media(self):
        return sum(len(nome) for nome in self.lista) / len(self.lista) if len(self.lista) > 0 else 0

    def calcula_desvio_padrao(self):
        media = self.calcula_media()
        variancia = sum((len(nome) - media) ** 2 for nome in self.lista) / len(self.lista) if len(self.lista) > 0 else 0
        return math.sqrt(variancia)

    def calcula_variancia(self):
        media = self.calcula_media()
        return sum((len(nome) - media) ** 2 for nome in self.lista) / len(self.lista) if len(self.lista) > 0 else 0

    def __iter__(self):
        return iter(self.lista)

class ListaDatas(AnaliseDados):
    def __init__(self):
        self.lista = []

    def entrada_de_dados(self, datas):
        self.lista.extend(datas)

    def mostra_mediana(self):
        sorted_lista = sorted(self.lista, key=lambda x: (x.ano, x.mes, x.dia))
        tamanho = len(sorted_lista)
        if tamanho % 2 == 0:
            indice1 = tamanho // 2 - 1
            indice2 = tamanho // 2
            mediana = sorted_lista[indice1]  # Retorna a primeira data entre as duas no meio
        else:
            indice = tamanho // 2
            mediana = sorted_lista[indice]  # Retorna a data do meio
        return mediana

    def mostra_menor(self):
        return min(self.lista, key=lambda x: (x.ano, x.mes, x.dia))

    def mostra_maior(self):
        return max(self.lista)

    def listar_em_ordem(self):
        return sorted(self.lista)

    def calcula_media(self):
        total_dias = sum(data.dia for data in self.lista)
        total_meses = sum(data.mes for data in self.lista)
        total_anos = sum(data.ano for data in self.lista)

        media_dia = total_dias / len(self.lista) if len(self.lista) > 0 else 0
        media_mes = total_meses / len(self.lista) if len(self.lista) > 0 else 0
        media_ano = total_anos / len(self.lista) if len(self.lista) > 0 else 0

        return Data(int(media_dia), int(media_mes), int(media_ano))

    def calcula_desvio_padrao(self):
        media = self.calcula_media()

        variancia_dia = sum((data.dia - media.dia) ** 2 for data in self.lista) / len(self.lista) if len(self.lista) > 0 else 0
        variancia_mes = sum((data.mes - media.mes) ** 2 for data in self.lista) / len(self.lista) if len(self.lista) > 0 else 0
        variancia_ano = sum((data.ano - media.ano) ** 2 for data in self.lista) / len(self.lista) if len(self.lista) > 0 else 0

        desvio_dia = math.sqrt(variancia_dia)
        desvio_mes = math.sqrt(variancia_mes)
        desvio_ano = math.sqrt(variancia_ano)

        return Data(int(desvio_dia), int(desvio_mes), int(desvio_ano))

    def calcula_variancia(self):
        media = self.calcula_media()

        variancia_dia = sum((data.dia - media.dia) ** 2 for data in self.lista) / len(self.lista) if len(self.lista) > 0 else 0
        variancia_mes = sum((data.mes - media.mes) ** 2 for data in self.lista) / len(self.lista) if len(self.lista) > 0 else 0
        variancia_ano = sum((data.ano - media.ano) ** 2 for data in self.lista) / len(self.lista) if len(self.lista) > 0 else 0

        return Data(int(variancia_dia), int(variancia_mes), int(variancia_ano))

    def __iter__(self):
        return iter(self.lista)

class ListaSalarios(AnaliseDados):
    def __init__(self):
        self.lista = []

    def entrada_de_dados(self, salarios):
        self.lista.extend(salarios)

    def mostra_mediana(self):
        return sorted(self.lista)[len(self.lista) // 2]

    def mostra_menor(self):
        return min(self.lista)

    def mostra_maior(self):
        return max(self.lista)

    def listar_em_ordem(self):
        return sorted(self.lista)

    def calcula_media(self):
        return sum(self.lista) / len(self.lista) if len(self.lista) > 0 else 0

    def calcula_desvio_padrao(self):
        media = self.calcula_media()
        variancia = sum((salario - media) ** 2 for salario in self.lista) / len(self.lista) if len(self.lista) > 0 else 0
        return math.sqrt(variancia)

    def calcula_variancia(self):
        media = self.calcula_media()
        return sum((salario - media) ** 2 for salario in self.lista) / len(self.lista) if len(self.lista) > 0 else 0

    def __iter__(self):
        return iter(self.lista)

class ListaIdades(AnaliseDados):
    def __init__(self):
        self.lista = []

    def entrada_de_dados(self, idades):
        self.lista.extend(idades)

    def mostra_mediana(self):
        return sorted(self.lista)[len(self.lista) // 2]

    def mostra_menor(self):
        return min(self.lista)

    def mostra_maior(self):
        return max(self.lista)

    def listar_em_ordem(self):
        return sorted(self.lista)

    def calcula_media(self):
        return sum(self.lista) / len(self.lista) if len(self.lista) > 0 else 0

    def calcula_desvio_padrao(self):
        media = self.calcula_media()
        variancia = sum((idade - media) ** 2 for idade in self.lista) / len(self.lista) if len(self.lista) > 0 else 0
        return math.sqrt(variancia)

    def calcula_variancia(self):
        media = self.calcula_media()
        return sum((idade - media) ** 2 for idade in self.lista) / len(self.lista) if len(self.lista) > 0 else 0

    def __iter__(self):
        return iter(self.lista)
#1 
    # Restante do código...

def percorrer_listas_com_zip(lista_nomes, lista_salarios):
    for nome, salario in zip(lista_nomes, lista_salarios):
        print(f"{nome}: R${salario}")

def calcular_folha_com_reajuste(lista_salarios):
    for salario in lista_salarios:
        print(f"Novo salario com reajuste de 10%: R${salario * 1.1:.2f}")

def modificar_datas_anteriores_a_2019(lista_datas):
    for data in lista_datas:
        if data < Data(1, 1, 2019):
            data.dia = 1
    print("Datas modificadas com sucesso!")

def iterador_zip(lista_nomes, lista_salarios):
    percorrer_listas_com_zip(lista_nomes, lista_salarios)

def iterador_map(lista_salarios):
    calcular_folha_com_reajuste(lista_salarios)

def iterador_filter(lista_datas):
    modificar_datas_anteriores_a_2019(lista_datas)

def mostrar_codigo_desempenho():
    print("\nCodigo de Desempenho:")
    with open("Metrica_Estatica.py", "r") as file:
        print(file.read())

def calcular_metricas_estatisticas(nomes, datas, salarios, idades):
    print("\nMetricas Estatisticas:")
    print(f"Lista de Nomes: Media = {nomes.calcula_media()}, Desvio Padrão = {nomes.calcula_desvio_padrao()}, Variância = {nomes.calcula_variancia()}")
    print(f"Lista de Datas: Media = {datas.calcula_media()}, Desvio Padrão = {datas.calcula_desvio_padrao()}, Variância = {datas.calcula_variancia()}")
    print(f"Lista de Salarios: Media = {salarios.calcula_media()}, Desvio Padrao = {salarios.calcula_desvio_padrao()}, Variância = {salarios.calcula_variancia()}")
    print(f"Lista de Idades: Media = {idades.calcula_media()}, Desvio Padrao = {idades.calcula_desvio_padrao()}, Variancia = {idades.calcula_variancia()}")

def menu():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    while True:
        print("\n Menu Principal \n")
        print("1. Incluir um nome na lista de nomes")
        print("2. Incluir um salario na lista de salarios")
        print("3. Incluir uma data na lista de datas")
        print("4. Incluir uma idade na lista de idades")
        print("5. Percorrer as listas de nomes e salarios")
        print("6. Calcular o valor da folha com um reajuste de 10%")
        print("7. Modificar o dia das datas anteriores a 2019")
        print("8. Mostrar desempenho")
        print("9. Calcular metricas estatisticas")
        print("10. Sair")

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            nome = input("Digite o nome: ")
            nomes.entrada_de_dados([nome])
        elif opcao == "2":
            salario = float(input("Digite o salario: "))
            salarios.entrada_de_dados([salario])
        elif opcao == "3":
            while True:
                try:
                    data_input = input("Digite a data no formato dd/mm/aaaa: ")
                    dia, mes, ano = map(int, data_input.split('/'))
                    data = Data(dia, mes, ano)
                    datas.entrada_de_dados([data])
                    break
                except ValueError:
                    print("Erro: Insira uma data valida no formato dd/mm/aaaa.")
        elif opcao == "4":
            idade = int(input("Digite a idade: "))
            idades.entrada_de_dados([idade])
        elif opcao == "5":
            iterador_zip(nomes, salarios)
        elif opcao == "6":
            iterador_map(salarios)
        elif opcao == "7":
            iterador_filter(datas)
        elif opcao == "8":
            mostrar_codigo_desempenho()
        elif opcao == "9":
            calcular_metricas_estatisticas(nomes, datas, salarios, idades)
        elif opcao == "10":
            print("Saindo...")
            break
        else:
            print("Opção invalida. Tente novamente.")

if __name__ == "__main__":
    menu()





