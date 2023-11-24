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

    # TODO: Pedir o resto dos dados do veiculo, e não esquecer de os guardar no dicionario
    # ...

    veiculo = {"marca": marca,
               "modelo": modelo,
               "matricula": matricula,
               "ano": ano,
               "classe": classe,
               "lugares": lugares
               }

    return veiculo

def imprime_lista_de_veiculos(lista_de_veiculos):
    """TODO: documentação"""

    imprime_lista(cabecalho="Lista de Veiculos", lista=lista_de_veiculos)
