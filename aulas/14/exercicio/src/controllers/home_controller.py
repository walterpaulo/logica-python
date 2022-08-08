from ..utils.utils import Utils
from ..controllers.clientes_controller import ClientesController
from ..controllers.relatorios_controller import RelatoriosController
from ..controllers.produtos_controller import ProdutosController
from ..controllers.pedidos_controller import PedidosController


class HomeController():
    def exec():
        Utils.limpar_tela()
        while True:
            Utils.titulo("Programa PED-ONLINE")
            print("Escolhe uma opção:")
            print(f"1 - Pedido")
            print(f"2 - Cliente")
            print(f"3 - Produto")
            print(f"4 - Relatório")
            print("0 - sair")
            opcao_selecionado = Utils.obtem_opcao_menu(1, 4)

            if opcao_selecionado == 0:
                break
            elif opcao_selecionado == 1:
                Utils.limpar_tela()
                PedidosController.exec()
            elif opcao_selecionado == 2:
                Utils.limpar_tela()
                ClientesController.exec()
            elif opcao_selecionado == 3:
                Utils.limpar_tela()
                ProdutosController.exec()
            elif opcao_selecionado == 4:
                Utils.limpar_tela()
                RelatoriosController.exec()
            else:
                Utils.messagem_success(texto="Opção inválida")


if __name__ == "__main__":
    HomeController.exec()
