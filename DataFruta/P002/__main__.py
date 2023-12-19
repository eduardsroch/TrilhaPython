from __init__ import *

def percorrer_listas_com_zip(lista_nomes, lista_salarios):
    for nome, salario in zip(lista_nomes, lista_salarios):
        print(f"{nome}: R${salario}")

def calcular_folha_com_reajuste(lista_salarios):
    for salario in lista_salarios:
        print(f"Novo salário com reajuste de 10%: R${salario * 1.1:.2f}")

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
    print("\nCódigo de Desempenho:")
    with open("teste_tempo.py", "r") as file:
        print(file.read())    

def iterador_zip(lista_nomes, lista_salarios):
    percorrer_listas_com_zip(lista_nomes, lista_salarios)

def iterador_map(lista_salarios):
    calcular_folha_com_reajuste(lista_salarios)

def iterador_filter(lista_datas):
    modificar_datas_anteriores_a_2019(lista_datas)

def menu():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    while True:
        print("\n Menu Principal \n")
        print("1. Incluir um nome na lista de nomes")
        print("2. Incluir um salário na lista de salários")
        print("3. Incluir uma data na lista de datas")
        print("4. Incluir uma idade na lista de idades")
        print("5. Percorrer as listas de nomes e salários")
        print("6. Calcular o valor da folha com um reajuste de 10%")
        print("7. Modificar o dia das datas anteriores a 2019")
        print("8. Mostrar desempenho")
        print("9. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome: ")
            nomes.entrada_de_dados([nome])  
        elif opcao == "2":
            salario = float(input("Digite o salário: "))
            salarios.entrada_de_dados(salario)
        elif opcao == "3":
            while True:
                try:
                    data_input = input("Digite a data no formato dd/mm/aaaa: ")
                    dia, mes, ano = map(int, data_input.split('/'))
                    data = Data(dia, mes, ano)
                    datas.entrada_de_dados(data)
                    break
                except ValueError:
                    print("Erro: Insira uma data válida no formato dd/mm/aaaa.")
        elif opcao == "4":
            idade = int(input("Digite a idade: "))
            idades.entrada_de_dados(idade)
        elif opcao == "5":
            iterador_zip(nomes, salarios)
        elif opcao == "6":
            iterador_map(salarios)
        elif opcao == "7":
            iterador_filter(datas)
        elif opcao == "8":
            mostrar_codigo_desempenho()
        elif opcao == "9":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()