import os


def validar_number(numero):
    if not numero.isdigit():
        return numero
    else:
        return int(numero)


def limpar_tela():
    os.system("clear")


def message_menu_erro(opcao=''):
    print(
        f"\n{'#'*35}\n{' '*3}Opção [ {opcao} ] inválido!\n{'#'*35}\n")
