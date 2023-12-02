from io_terminal import imprime_lista

nome_ficheiro_lista_de_clientes = "lista_de_clientes.pk"

def cria_novo_cliente():
    """
    Pedir os dados de um novo cliente.

    Esta função solicita ao usuário que forneça os dados de um novo cliente,
    incluindo nome, idade, NIF, endereço e e-mail. Os dados são lidos a partir
    da entrada padrão.

    :return: Um dicionário representando o novo cliente, com as seguintes chaves:
             - "nome": Nome do cliente.
             - "idade": Idade do cliente.
             - "nif": Número de Identificação Fiscal (NIF) do cliente.
             - "endereco": Endereço do cliente.
             - "email": Endereço de e-mail do cliente.
    :rtype: dict

    Exemplo de uso:

    >>> novo_cliente = cria_novo_cliente()
    Introduza os dados do novo cliente:
    Nome: Simão Marcos
    Idade: 65
    NIF: 123456789
    Endereço: 8125 Rua dos Furados
    E-mail: simao.marcos@exemplo.com

    >>> print(novo_cliente)
    {'nome': 'Simão Marcos', 'idade': '65', 'nif': '123456789', 'endereco': '8125 Rua dos Furados', 'email': 'simao.marcos@exemplo.com'}
    """
    
    print("Introduza os dados do novo cliente:")

    nome = input("Nome: ")
    idade = input("Idade: ")
    nif = input("NIF: ")
    endereco = input("Endereço: ")
    email = input("E-mail: ")

    novo_cliente = {
        "nome": nome,
        "idade": idade,
        "nif": nif,
        "endereco": endereco,
        "email": email
    }
    return novo_cliente

def imprime_lista_de_clientes(lista_de_clientes):
    """Imprime os detalhes dos clientes na lista.

    Esta função recebe uma lista de clientes e imprime as informações
    relevantes de cada cliente, incluindo nome, idade, NIF, endereço e e-mail.

    :param lista_de_clientes: Uma lista contendo dicionários com informações
                              dos clientes.
    :type lista_de_clientes: list

    :return: Nenhum valor é retornado.
    :rtype: None
    """
    
    if not lista_de_clientes:
        print("Nenhum cliente na lista.")
    else:
        for cliente in lista_de_clientes:
            print("\nNome: ", cliente["nome"])
            print("Idade: ", cliente["idade"])
            print("NIF: ", cliente["nif"])
            print("Endereço: ", cliente["endereco"])
            print("E-mail: ", cliente["email"])
