import os


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


def limpar_tela():
    os.system("clear")
