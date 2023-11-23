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

    novo_cliente = {
        "nome": nome,
        "idade": idade,
        "nif": nif,
        "endereco": endereco,
    }
    return novo_cliente

def imprime_lista_de_clientes(lista_de_clientes):
    """TODO: documentação"""

    #TODO: Implementar esta função
    # ...
