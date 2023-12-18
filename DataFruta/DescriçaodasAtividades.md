# P001 Manipulação Dinâmica de Dados e Análise Estatística

O código descrito implementa um programa que manipula `dados` relacionados a `nomes`, `salários`, `datas` e `idades` usando `classes` em Python. 

O programa oferece funcionalidades como `adição de elementos` às listas, `ordenação dos dados`, `cálculos de folha de pagamento com reajuste salarial`, e `modificações condicionais nas datas`. 

Além disso, o código propõe a criação de um aplicativo interativo com um menu de opções, permitindo ao usuário escolher entre várias operações para interagir com os dados de forma dinâmica.

<a href="./P001/">Primeira etapa</a>

# P002 Avaliação de Desempenho para Manipulação de Dados

O código proposto envolve a implementação e avaliação do desempenho de classes em Python para armazenar dados (idades e salários) em listas, comparando essa abordagem com o uso de `ndarrays` do pacote `NumPy`.

**Parte 1:** Avaliação do desempenho das listas

São implementadas funções para gerar objetos das classes `ListaIdade` e `ListaSalario` com dados aleatórios. O desempenho das classes é testado com 5000 itens, medindo o tempo de execução dos métodos `mostraMediana`, `mostraMenor` e `mostraMaior`.

**Parte 2:** Utilização do NumPy

É explorado o pacote `NumPy` para gerar ndarrays com valores aleatórios (`inteiros` e `ponto flutuante`) em intervalos específicos. São criados ndarrays a partir das listas geradas no exercício anterior utilizando as funcionalidades do `NumPy`. Além disso, são pesquisados recursos do `NumPy` para calcular a `mediana`, o valor `mínimo` e `máximo` de um ndarray. O desempenho dessas operações é comparado com os métodos utilizados no exercício anterior.

<a href="./P002/">Segunda etapa</a>