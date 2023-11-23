from io_terminal import imprime_lista

nome_ficheiro_lista_de_veiculos = "lista_de_veiculos.pk"


# TODO: Copie para aqui o código de cada uma das funções nos
# ficheiros com o nome veiculos-*.py e faça um commit de cada vez
# Quando este ficheiro estiver completo com todas as suas funções,
# deve ser o unico ficheiro veiculos.py existente, deve apagar
# todos os outros ficheiros veiculos-*.py, e inclusive estes comentários

# ...

def cria_novo_veiculo():
    """Pede ao utilizador para introduzir um novo veiculo

    :return: dicionario com um veiculo na forma
        {"marca": <<marca>>, "matricula": <<matricula>>, ...}
    """

    marca = input("marca? ")
    matricula = input("matricula? ").upper()
    # TODO: Pedir o resto dos dados do veiculo, e não esquecer de os guardar no dicionario
    # ...

    veiculo = {"marca": marca,
               "matricula": matricula}

    return veiculo
