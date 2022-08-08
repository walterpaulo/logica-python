from ..utils.utils import Utils
from ..views.produto import Produto


class ProdutosController():
    def exec():
        print("ok")
        Utils.limpar_tela()
        while True:
            Utils.titulo("Cadastro de Produto")
            print("Escolhe uma opção")
            print(f"1 - Cadastrar produto")
            print("0 - sair")
            opcao_selecionado = Utils.obtem_opcao_menu(1, 1)

            if opcao_selecionado == 0:
                Utils.limpar_tela()
                break
            elif opcao_selecionado == 1:
                Utils.limpar_tela()
                Produto.cadastro()

    def relatorio():
        Produto.listar()

    def adicionar_produto():
        itens = Produto.adicionar_carrinho()
        return itens


if __name__ == "__main__":
    ProdutosController.exec()
