from utils import validar_number, limpar_tela

db_produto = [
    {
        "id": 1,
        "nome": "Teclado",
        "descricao": "Teclado idioma brasileiro",
        "preco": 40.00,
    },
    {
        "id": 2,
        "nome": "Monitor",
        "descricao": "Teclado idioma brasileiro",
        "preco": 500.00,
    }
]


def gerador_id(lista):
    numero = len(lista)
    return numero + 1


def busca_produto_id(codigo):
    for produto in db_produto:
        if produto['id'] == codigo:
            return produto
    return


def salva_produto():
    print(f"{'_'*10}| CADASTRO DE PRODUTO |{'_'*10}\n")
    nome = input("Digite o nome:")
    descricao = input("Digite a descrição do produto:")
    preco = float(input("Digite o preço:"))
    novo_produto = {
        "id": gerador_id(db_produto),
        "nome": nome,
        "descricao": descricao,
        "preco": preco,
    }
    db_produto.append(novo_produto)


def menu_produto():
    for produto in db_produto:
        print(f"{produto['id']} - {produto['nome']} R$ {produto['preco']}")
    print(f"s - Cancelar")


def lista_produtos():
    print(f"{'_'*10}| Lista de Produto|{'_'*10}\n")
    for produto in db_produto:
        print(
            f"Código: {produto['id']} | Nome: {produto['nome']} | R$: {produto['preco']} | Descricao: {produto['descricao']}\n")


def message_menu_erro(opcao=''):
    print(
        f"\n{'#'*35}\n{' '*3}Opção [ {opcao} ] inválido!\n{'#'*35}\n")


def exec():
    limpar_tela()
    while True:
        print(f"{'_'*10}| Cadastro de Produto |{'_'*10}")
        print("1 - Novo Produto")
        print("2 - Lista de Produto")
        print("s - Voltar")
        opcao = validar_number(input("$>"))

        if opcao == 's':
            limpar_tela()
            break
        elif opcao == 1:
            limpar_tela()
            salva_produto()
        elif opcao == 2:
            limpar_tela()
            lista_produtos()
        else:
            message_menu_erro(opcao)


if __name__ == "__main__":
    exec()
