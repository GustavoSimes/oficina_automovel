from datetime import date

from io_terminal import imprime_lista, pergunta_id

nome_ficheiro_lista_de_faturas = "lista_de_faturas.pk"

def imprime_lista_de_faturas(lista_de_faturas):
    """TODO: documentação"""

    for fatura in lista_de_faturas:
        print(fatura)
    pass

def cria_nova_fatura(lista_de_clientes, lista_de_veiculos):
    """Pede ao utilizador para introduzir os dados de uma nova fatura

    :return: dicionario com uma fatura, na forma
        {"cliente": <<id_cliente>>, "veiculo": <<id_veiculo>>, "data": <<data>>, ...}
    """

    id_cliente = pergunta_id(questao="Qual o id do cliente?", lista=lista_de_clientes, mostra_lista=True)
    id_veiculo = pergunta_id(questao="Qual o id do veiculo?", lista=lista_de_veiculos, mostra_lista=True)
    descricao = pergunta_id(questao="Qual é a descrição?", lista=lista_de_veiculos, mostra_lista=True)
    deseja_email = pergunta_id(questao="Deseja receber a fatura por email (S/N)?", lista=lista_de_veiculos, mostra_lista=True)
    # TODO: Pedir o resto dos dados da fatura, e não esquecer de os guardar no dicionario
    # ...

    fatura = {"cliente": id_cliente,
              "veiculo": id_veiculo,
              "data": date.today(),
              "descrição": descricao,
              "deseja_email": deseja_email}

    return fatura
