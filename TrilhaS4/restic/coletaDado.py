import pandas as pd


def gerar_identificador(nome, cpf, ano_nascimento):
    """
    Gera um identificador para o residente.

    Args:
        nome: Nome do residente.
        cpf: CPF do residente.
        ano_nascimento: Ano de nascimento do residente.

    Returns:
        O identificador do residente.
    """

    if not nome:
        raise ValueError("O nome do residente deve ser informado")
    if not cpf:
        raise ValueError("O CPF do residente deve ser informado")
    if not ano_nascimento:
        raise ValueError("O ano de nascimento do residente deve ser informado")

    trilha = "tic18Py" if nome.startswith("tic18Py") else "tic18Net" if nome.startswith("tic18Net") else "tic18Jav"
    return f"{trilha}{cpf[:3]}{ano_nascimento[2:]}"


def coletar_dados():
    """
    Coleta os dados do residente.

    Returns:
        Um objeto `Residente` com os dados do residente.
    """

    nome = input("Nome: ")
    cpf = input("CPF: ")
    ano_nascimento = input("Ano de nascimento: ")

    try:
        identificador = gerar_identificador(nome, cpf, ano_nascimento)
    except ValueError as e:
        print(e)
        return None

    idade = int(input("Idade: "))

    formação = input("Formação: ")
    if formação == "Ensino Médio":
        formação = 1
    elif formação == "Graduação":
        formação = 2
    elif formação == "Pós-Graduação":
        formação = 3
    else:
        raise ValueError("Formação inválida")

    formação_geral = formação >= 2

    formação_específica = input("Formação Específica: ")

    andamento_graduação = float(input("Andamento Graduação (0 a 100): "))

    tempo_formado = float(input("Tempo Formado (anos): "))

    experiência_prévia = input("Experiência Prévia: ") == "True"

    return Residente(nome, idade, formação, formação_específica, andamento_graduação, tempo_formado, experiência_prévia, identificador)


def main():
    residente = coletar_dados()
    if residente is not None:
        print(residente)


if __name__ == "__main__":
    main()
