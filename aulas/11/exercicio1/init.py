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


def cadastro():
    print(f"{'_'* 10}| Cadastro Usuário |{'_'*10}")
    nome = input(f"Digite o nome: ")
    email = input(f"Digite o email: ")

    usuario = {
        "nome": nome,
        "email": email
    }
    gravar(usuario)


def ler():
    try:
        file_exists = exists("clientes.json")
        if not file_exists:
            open("clientes.json", "w")
        f = open("clientes.json", "r")
        cliente_json = f.read()
        clientes = json.loads(cliente_json)

        for cliente in clientes:
            print(f"Nome: {cliente['nome']}")
            print(f"Email: {cliente['email']}")
    except Exception as e:
        print(e)
        print("Algo deu errado na leitura do arquivo")
    finally:
        f.close()


def gravar(cliente):
    clientes = []
    cliente = {
        "nome": cliente['nome'],
        'email': cliente['email']
    }
    clientes.append(cliente)
    try:
        f = open("clientes.json", "w")
        cliente_json = json.dumps(clientes)
        f.write(cliente_json)
    except Exception as e:
        print(e)
        print("Algo deu errado na escrita do arquivo")
    finally:
        f.close()


def exec():
    while True:
        print(f"{'_'* 10}| Cadastro no Disco |{'_'*10}")
        print("1 - cadastrar")
        print("2 - listar")
        print("3 - sair")
        opcao = int(input("Escolhe uma opção:"))

        if opcao == 3:
            break
        elif opcao == 1:
            cadastro()
        elif opcao == 2:
            ler()
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    exec()
