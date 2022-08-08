from src.controllers.pedidos_controller import PedidosController
from ..utils.utils import Utils
from ..controllers.clientes_controller import ClientesController
from ..controllers.produtos_controller import ProdutosController


class RelatoriosController():
    def exec():
        Utils.limpar_tela()
        while True:
            Utils.titulo("Relatórios")
            print("Escolhe uma opção:")
            print(f"1 - Pedidos")
            print(f"2 - Clientes")
            print(f"3 - Produtos")
            print("0 - sair")
            opcao_selecionado = Utils.obtem_opcao_menu(1, 3)

            if opcao_selecionado == 0:
                Utils.limpar_tela()
                break
            elif opcao_selecionado == 1:
                Utils.limpar_tela()
                PedidosController.relatorio()
            elif opcao_selecionado == 2:
                Utils.limpar_tela()
                ClientesController.relatorio()
            elif opcao_selecionado == 3:
                Utils.limpar_tela()
                ProdutosController.relatorio()
            else:
                Utils.messagem_success(texto="Opção inválida")


if __name__ == "__main__":
    RelatoriosController.exec()
