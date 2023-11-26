from io_terminal import imprime_lista

nome_ficheiro_lista_de_clientes = "lista_de_clientes.pk"

def cria_novo_cliente():
    """Pedir os dados de um novo cliente

    :return: dicionario com o novo cliente, {"nome": <<nome>>, "nif": <<nif>>, ...}
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
