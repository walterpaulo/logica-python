import os
import re
from ..styles.cores import Cores as cor
import json


class Utils():

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
            Utils.messagem_error(e=e)
            return Utils.obtem_opcao_menu(incial, final)

    def validar_email(email):
        regex = re.compile(
            r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, email):
            return True
        else:
            return False

    def number_float(numero):
        if numero.replace('.', '', 1).isdigit():
            return True
        else:
            return False

    def limpar_tela():
        os.system("cls||clear")

    def titulo(texto):
        print(f"{cor.CTEXTINFO}{'-'*10}{cor.CEND}{cor.BINFO} {texto} {cor.CEND}{cor.CTEXTINFO}{'-'*10}{cor.CEND}")

    def messagem_error(texto="Alerta", e=''):
        print(f"{cor.BERROR} {texto} {cor.BEND} {e}")

    def messagem_success(texto):
        print(f"{cor.BSUCCESS} {texto} {cor.BEND}")

    def obter_numero(texto="Digite a opção"):
        try:
            valor = input(f"{texto}:")
            if valor.isnumeric() == False:
                raise TypeError("Valor inválida")

            valor_convertido = int(valor)
            if valor_convertido == 0:
                return 0
            elif valor_convertido >> 0:
                return valor_convertido
            else:
                raise TypeError("Valor inválida")
        except TypeError as e:
            Utils.messagem_error(e=e)
            return Utils.obter_numero()

    def para_dict(obj):
        # Se for um objeto, transforma num dict
        if hasattr(obj, '__dict__'):
            obj = obj.__dict__

        # Se for um dict, lê chaves e valores; converte valores
        if isinstance(obj, dict):
            return {k: Utils.para_dict(v) for k, v in obj.items()}
        # Se for uma lista ou tupla, lê elementos; também converte
        elif isinstance(obj, list) or isinstance(obj, tuple):
            return [Utils.para_dict(e) for e in obj]
        # Se for qualquer outra coisa, usa sem conversão
        else:
            return obj
