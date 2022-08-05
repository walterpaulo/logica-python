from utils import limpar_tela, gerador_id, obtem_opcao_menu
from service import salvar_dados


def salva_produto(db_produtos=[]):
    print(f"{'_'*10}| CADASTRO DE PRODUTO |{'_'*10}\n")
    nome = input("Digite o nome:")
    descricao = input("Digite a descrição do produto:")
    preco = float(input("Digite o preço:"))
    novo_produto = {
        "id": gerador_id(db_produtos),
        "nome": nome,
        "descricao": descricao,
        "preco": preco,
    }
    db_produtos.append(novo_produto)
    salvar_dados("db_produtos.json", db_produtos)
    limpar_tela()
    print(f"{novo_produto['nome']} inserido com sucesso.")


def menu_produto(db_produtos=[]):
    for produto in db_produtos:
        print(f"{produto['id']} - {produto['nome']} R$ {produto['preco']}")
    print(f"0 - Voltar")


def lista_produtos(db_produtos=[]):
    print(f"{'_'*10}| Lista de Produto|{'_'*10}\n")
    for produto in db_produtos:
        print(
            f"Código: {produto['id']} | Nome: {produto['nome']} | R$: {produto['preco']} | Descricao: {produto['descricao']}\n")


def message_menu_erro(opcao=''):
    print(
        f"\n{'#'*35}\n{' '*3}Opção [ {opcao} ] inválido!\n{'#'*35}\n")


def exec(db_produtos=[]):
    limpar_tela()
    try:
        while True:
            print(f"{'_'*10}| Cadastro de Produto |{'_'*10}")
            print("1 - Novo Produto")
            print("2 - Lista de Produto")
            print("0 - Voltar")

            opcao_selecionada = obtem_opcao_menu(1, 2)

            if opcao_selecionada == 0:
                limpar_tela()
                break
            elif opcao_selecionada == 1:
                limpar_tela()
                salva_produto(db_produtos)
            elif opcao_selecionada == 2:
                limpar_tela()
                lista_produtos(db_produtos)
    except Exception as e:
        print(f"Alerta: {e}")


if __name__ == "__main__":
    exec()
