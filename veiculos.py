from io_terminal import imprime_lista

nome_ficheiro_lista_de_veiculos = "lista_de_veiculos.pk"

def cria_novo_veiculo():
    """Pede ao utilizador para introduzir um novo veiculo

    :return: dicionario com um veiculo na forma
        {"marca": <<marca>>, "matricula": <<matricula>>, ...}
    """

    marca = input("marca? ")
    modelo = input("modelo? ")
    matricula = input("matricula? ").upper()
    ano = input("ano de compra? ")
    classe = input("classe (1-5)? ") #classe do veiculo de acordo com a via verde (1-5)
    lugares = input("lugares? ")
    cor = input("cor? ")
    comprimento = input("comprimento? ")
    cilindrada = input("cilindrada? ")

    veiculo = {"marca": marca,
               "modelo": modelo,
               "matricula": matricula,
               "ano": ano,
               "classe": classe,
               "lugares": lugares,
               "cor": cor,
               "comprimento": comprimento,
               "cilindrada": cilindrada
               }

    return veiculo

def imprime_lista_de_veiculos(lista_de_veiculos):
    """
    Imprime uma lista de veículos formatada.

    Esta função recebe uma lista de veículos e imprime suas informações de maneira formatada.
    
    :param lista_de_veiculos: Uma lista de dicionários, onde cada dicionário representa um veículo.
    :type lista_de_veiculos: list[dict]
    
    :return: None
    :rtype: None

    :Example:

    >>> veiculos = [
    ...     {"marca": "Toyota", "modelo": "Corolla", "matricula": "AB-123-CD", "ano": "2020", "classe": "3", "lugares": "5", "cor": "azul", "comprimento": "4.5", "cilindrada": "2000"},
    ...     {"marca": "Honda", "modelo": "Civic", "matricula": "XY-789-ZW", "ano": "2019", "classe": "2", "lugares": "4", "cor": "vermelho", "comprimento": "4.2", "cilindrada": "1800"},
    ...     # Adicione mais veículos conforme necessário
    ... ]

    >>> imprime_lista_de_veiculos(veiculos)
    Lista de Veículos
    -----------------
    Marca: Toyota, Modelo: Corolla, Matrícula: AB-123-CD, Ano: 2020, Classe: 3, Lugares: 5, Cor: azul, Comprimento: 4.5, Cilindrada: 2000
    Marca: Honda, Modelo: Civic, Matrícula: XY-789-ZW, Ano: 2019, Classe: 2, Lugares: 4, Cor: vermelho, Comprimento: 4.2, Cilindrada: 1800
    ...
    """

    imprime_lista(cabecalho="Lista de Veiculos", lista=lista_de_veiculos)
