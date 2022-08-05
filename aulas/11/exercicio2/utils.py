import os
import re


def validar_number(numero):
    if not numero.isdigit():
        return numero
    else:
        return int(numero)


def obter_numero():
    try:
        valor = input('Digite a opção: ')
        if valor.isnumeric() == False:
            raise TypeError("Opção inválida.")

        valor_convertido = int(valor)
        if valor_convertido == 0:
            return 0
        elif valor_convertido >> 0:
            return valor_convertido
        else:
            raise TypeError("Opção inválida.")
    except TypeError as e:
        print(f"Alerta: {e}")
        return obter_numero()


def limpar_tela():
    os.system("clear")


def message_menu_erro(opcao=''):
    print(
        f"\n{'#'*35}\n{' '*3}Opção [ {opcao} ] inválido!\n{'#'*35}\n")


def gerador_id(lista):
    numero = len(lista)
    return numero + 1


def obtem_opcao_menu(incial, final):
    try:
        valor_entrada = input('Digite a opção: ')

        if valor_entrada.isnumeric() == False:
            raise TypeError("Opção inválida.")

        valor_convertido = int(valor_entrada)
        if valor_convertido == 0:
            return 0
        elif valor_convertido >= incial and valor_convertido <= final:
            return valor_convertido
        else:
            raise TypeError("Opção inválida.")
    except TypeError as e:
        print(f"Alerta: {e}")
        return obtem_opcao_menu(incial, final)


def validar_email(email):
    regex = re.compile(
        r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        return True
    else:
        return False
