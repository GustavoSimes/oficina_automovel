from tabulate import tabulate


def imprime_lista(cabecalho, lista):
    """Imprime a :attr:`lista` na forma de uma tabela com um cabeçalho

    Recebe uma lista na forma [{"atrib1": valor1, "atrib2": valor2, ...},
    {"atrib1": valor1, "atrib2": valor2, ...}, ...] e imprime no terminal uma tabela
    na forma

    ==  ======  ======
    id  atrib1  atrib2
    ==  ======  ======
    0   valor1  valor2
    1   ...      ...
    ==  ======  ======

    :param cabecalho: Cabecalho para a listagem
    :param lista: Lista a ser impressa
    """

    print(cabecalho)

    if (len(lista) == 0):
        print("Lista vazia")
    else:
        # cabecalho da tabela
        lista_a_imprimir = [["id"] + list(lista[0].keys())]
        # dados
        lista_a_imprimir.extend([[id] + list(d.values()) for id, d in enumerate(lista)])

        print(tabulate(lista_a_imprimir, headers="firstrow", tablefmt='psql'))

def pause():
    """Faz uma pausa no programa e espera que o utilizador pressione ENTER"""

    input("Pressione ENTER para continuar...")

def pergunta_id(questao, lista, mostra_lista=False):
    """
    Pede ao utilizador para selecionar um índice com base numa lista fornecida.

    :param questao: Uma string que representa a pergunta apresentada.
    :param lista: Uma lista de dicionários para escolher.
    :param mostra_lista: Um booleano que indica se deve mostrar a lista antes de pedir ao utilizador. O padrão é Falso.

    :return: O índice selecionado (id) da lista.

    Esta função pede ao utilizador para escolher um índice correspondente à lista fornecida.
    Se `mostra_lista` for Verdadeiro, exibe a lista como uma tabela usando a função `imprime_lista` antes de pedir ao utilizador.

    Exemplo de Utilização:

    >>> pergunta_id("Selecione um item: ", [{"atrib1": valor1, "atrib2": valor2}, {"atrib1": valor3, "atrib2": valor4}])

    :raises ValueError: Se o índice inserido estiver fora do intervalo válido.
    """
    if mostra_lista:
        imprime_lista(cabecalho="", lista=lista)

    while True:
        id = int(input(questao))
        if 0 <= id < len(lista):
            return id
        else:
            print(f"id inexistente. Tente de novo. Valores admitidos {0} - {len(lista)}")
