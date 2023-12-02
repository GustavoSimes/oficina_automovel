from datetime import date

from io_terminal import imprime_lista, pergunta_id

nome_ficheiro_lista_de_faturas = "lista_de_faturas.pk"

def imprime_lista_de_faturas(lista_de_faturas):
    """
    Imprime uma lista de faturas.

    Esta função percorre a lista de faturas e imprime cada uma delas.

    :param lista_de_faturas: Uma lista de dicionários, onde cada dicionário representa uma fatura.
    :type lista_de_faturas: list[dict]

    :return: None
    :rtype: None

    :Example:

    >>> faturas = [
    ...     {"cliente": 1, "veiculo": 101, "data": date(2023, 12, 1), "descricao": "Reparo de motor", "deseja_email": True},
    ...     {"cliente": 2, "veiculo": 102, "data": date(2023, 12, 2), "descricao": "Troca de pneus", "deseja_email": False},
    ...     # Adicione mais faturas conforme necessário
    ... ]

    >>> imprime_lista_de_faturas(faturas)
    {'cliente': 1, 'veiculo': 101, 'data': datetime.date(2023, 12, 1), 'descricao': 'Reparo de motor', 'deseja_email': True}
    {'cliente': 2, 'veiculo': 102, 'data': datetime.date(2023, 12, 2), 'descricao': 'Troca de pneus', 'deseja_email': False}
    ...
    """

    for fatura in lista_de_faturas:
        print(fatura)
    pass

def cria_nova_fatura(lista_de_clientes, lista_de_veiculos):
    """
    Pede ao utilizador para introduzir os dados de uma nova fatura.

    Esta função interage com o utilizador para obter os dados necessários para criar
    uma nova fatura. Os dados incluem o ID do cliente, o ID do veículo, a descrição da
    fatura e se o cliente deseja receber a fatura por e-mail. A data da fatura é definida
    automaticamente como a data atual.

    :param lista_de_clientes: Uma lista de clientes, onde cada cliente é representado por um dicionário.
    :type lista_de_clientes: list[dict]

    :param lista_de_veiculos: Uma lista de veículos, onde cada veículo é representado por um dicionário.
    :type lista_de_veiculos: list[dict]

    :return: Um dicionário representando a nova fatura, com as seguintes chaves:
             - "cliente": ID do cliente.
             - "veiculo": ID do veículo.
             - "data": Data atual (objeto date).
             - "descricao": Descrição da fatura.
             - "deseja_email": Indica se o cliente deseja receber a fatura por e-mail (True/False).
    :rtype: dict

    :Example:

    >>> clientes = [
    ...     {"id": 1, "nome": "Abel Dias", "idade": 63, "nif": "123456789", "endereco": "Rua das Gaivotas", "email": "abel.dias@exemplo.com"},
    ...     {"id": 2, "nome": "Fernando Carvalho", "idade": 24, "nif": "987654321", "endereco": "Rua Caminho do Lago", "email": "nando.carvalho@exemplo.com"},
    ...     # Adicione mais clientes conforme necessário
    ... ]

    >>> veiculos = [
    ...     {"id": 101, "modelo": "Carro A", "ano": 2022, "cor": "Azul"},
    ...     {"id": 102, "modelo": "Carro B", "ano": 2021, "cor": "Vermelho"},
    ...     # Adicione mais veículos conforme necessário
    ... ]

    >>> nova_fatura = cria_nova_fatura(clientes, veiculos)
    Qual o id do cliente? (Mostrando lista de clientes)
    [1] Abel Dias
    [2] Fernando Carvalho
    Selecione o ID do cliente: 1

    Qual o id do veiculo? (Mostrando lista de veículos)
    [101] Carro A
    [102] Carro B
    Selecione o ID do veículo: 101

    Qual é a descrição? (Mostrando lista de veículos)
    [101] Carro A
    [102] Carro B
    Selecione o ID do veículo para obter a descrição: 101

    Deseja receber a fatura por email (S/N)? (Mostrando lista de veículos)
    [101] Carro A
    [102] Carro B
    Selecione o ID do veículo para confirmar a escolha: S

    >>> print(nova_fatura)
    {'cliente': 1, 'veiculo': 101, 'data': datetime.date(2023, 12, 1), 'descricao': 'Carro A', 'deseja_email': True}
    """
    
    id_cliente = pergunta_id(questao="Qual o id do cliente?", lista=lista_de_clientes, mostra_lista=True)
    id_veiculo = pergunta_id(questao="Qual o id do veiculo?", lista=lista_de_veiculos, mostra_lista=True)
    descricao = pergunta_id(questao="Qual é a descrição?", lista=lista_de_veiculos, mostra_lista=True)
    deseja_email = pergunta_id(questao="Deseja receber a fatura por email (S/N)?", lista=lista_de_veiculos, mostra_lista=True)

    fatura = {"cliente": id_cliente,
              "veiculo": id_veiculo,
              "data": date.today(),
              "descricao": descricao,
              "deseja_email": deseja_email}

    return fatura
