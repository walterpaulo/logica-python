from ..utils.utils import Utils
from ..views.cliente import Cliente


class ClientesController():
    def exec():
        Utils.limpar_tela()
        while True:
            Utils.titulo("Programa de Cliente")
            print("Escolhe uma opção:")
            print(f"1 - Cadastrar cliente")
            print("0 - sair")
            opcao_selecionado = Utils.obtem_opcao_menu(1, 1)

            if opcao_selecionado == 0:
                Utils.limpar_tela()
                break
            elif opcao_selecionado == 1:
                Utils.limpar_tela()
                Cliente.cadastro()

    def relatorio():
        Cliente.listar()

    def cadastrar_cliente_pedido():
        objeto = Cliente.cadastro(exibe_cabecalho=False, cadastro_pedido=True)
        return objeto

    def adicionar_produto():
        itens = []
        return itens


if __name__ == "__main__":
    ClientesController.exec()
