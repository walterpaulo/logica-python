"""
Dado que você aprendeu como fazer persistencia, cria um programa
para cadasto de cliente, com os campos:
Nome, email

Crie um menu para que vc possa orientar o cliente da criação e 
leitura dos clientes cadastrados no disco

1 - cadastrar
2 - listar
3 - sair

"""

import json
from os.path import exists
import os
import re
import time
import re


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def validar_email(email):
    regex = re.compile(
        r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        return True
    else:
        return False


def tempo_em_segundo(segundo):
    time.sleep(segundo)


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


def cadastro(nome="", email="", exibe_cabecalho=True, db=[]):
    if exibe_cabecalho == True:
        print(f"{'_'* 10}| Cadastro de Cliente |{'_'*10}")
    try:
        if nome.strip() == "":
            nome = input("Digite o nome:")
            if nome.strip() == "":
                raise TypeError("Digite o nome correto.")

        email = input("Digite o e-mail:")
        if email.strip() == "":
            raise TypeError("Email inválido.")
        if validar_email(email) == False:
            raise TypeError("Email inválido.")

        usuario = {
            "nome": nome,
            "email": email
        }

        db.append(usuario)
        salvar_dados("clientes.json", db)
        print('\nUsuário cadastrado!')
        tempo_em_segundo(3)
        limpar_tela()

        while True:
            print("Deseja cadastar novo usuário?")
            print("1 - Sim")
            print("2 - Não")
            print("0 - Retornar ao menu anterior")
            opcao_selecionado = obtem_opcao_menu(1, 2)
            if opcao_selecionado == 1:
                limpar_tela()
                nome = ""
                email = ""
                cadastro(nome, email, exibe_cabecalho=True, db=db)
            if opcao_selecionado == 2 or opcao_selecionado == 0:
                limpar_tela()
                break

    except Exception as e:
        print(f"Alerta: {e}")
        return cadastro(nome, email, exibe_cabecalho=False)


def ler():
    try:
        with open('clientes.json') as arquivo_clientes:
            clientes = arquivo_clientes.read()
        limpar_tela()
        cliente_json = json.loads(clientes)
        print(f"{'_'*10}| Lista de Usuários |{'_'*10}\n")
        for cliente in cliente_json:
            print(f"Nome: {cliente['nome']}")
            print(f"Email: {cliente['email']}\n")
    except json.decoder.JSONDecodeError:
        print("Lista vazia")
    except Exception as e:
        print(f"Alerta: {e}")


def salvar_dados(nomedojson, file):
    with open(nomedojson, "w", encoding="utf-8") as dados:
        salvando = json.dump(file, dados)
    return salvando


def carregar_dados(nomeJson):
    file_exists = exists(nomeJson)
    if file_exists:
        with open(nomeJson, "r", encoding="utf-8") as dados:
            return json.load(dados)
    else:
        with open(nomeJson, "w", encoding="utf-8") as dados:
            temporario = []
            json.dump(temporario, dados)
            return temporario


def exec():
    try:
        dados_cliente = carregar_dados("clientes.json")
        while True:
            print(f"{'_'* 10}| Cadastro no Disco |{'_'*10}")
            print("1 - cadastrar")
            print("2 - listar")
            print("0 - sair")
            opcao_selecionado = obtem_opcao_menu(1, 3)

            if opcao_selecionado == 0:
                break
            elif opcao_selecionado == 1:
                limpar_tela()
                cadastro(db=dados_cliente)
            elif opcao_selecionado == 2:
                # limpar_tela()
                ler()
    except Exception as erro:
        print("Ocorreu um erro durante o carregamento: ", erro)


if __name__ == "__main__":
    exec()
