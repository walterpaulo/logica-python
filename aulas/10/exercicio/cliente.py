from utils import validar_number, limpar_tela, message_menu_erro

db_cliente = [
    {
        "id": 1,
        "nome": "Pedro Augusto",
        "email": "pedro20mani@hotmail.com",
    },
    {
        "id": 2,
        "nome": "Julianna Pires",
        "email": "jpires@hotmail.com",
    }
]


def gerador_id(lista):
    numero = len(lista)
    return numero + 1


def busca_cliente_id(codigo):
    for cliente in db_cliente:
        if cliente['id'] == codigo:
            return cliente
    return


def salva_cliente():
    limpar_tela()
    print(f"{'_'*10}| CADASTRO DE CLIENTE |{'_'*10}\n")
    nome = input("Digite o nome:")
    email = input("Digite o email:")
    novo_cliente = {
        "id": gerador_id(db_cliente),
        "nome": nome,
        "email": email
    }
    db_cliente.append(novo_cliente)
    return novo_cliente


def lista_cliente():
    limpar_tela()
    print(f"{'_'*10}| Lista de Cliente|{'_'*10}\n")
    for cliente in db_cliente:
        print(
            f"Código: {cliente['id']} | Nome: {cliente['nome']} | Email: {cliente['email']}")
    print('\n')


def exec():
    limpar_tela()
    while True:
        print(f"{'_'*10}| Cadastro de Produto |{'_'*10}")
        print("1 - Novo Cliente")
        print("2 - Lista de Cliente")
        print("s - Voltar")
        opcao = validar_number(input("$>"))

        if opcao == 's':
            limpar_tela()
            break
        elif opcao == 1:
            limpar_tela()
            salva_cliente()
        elif opcao == 2:
            limpar_tela()
            lista_cliente()
        else:
            limpar_tela()
            message_menu_erro(opcao)


if __name__ == "__main__":
    exec()
