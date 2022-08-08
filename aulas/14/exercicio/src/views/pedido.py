from ..utils.utils import Utils
from ..models.pedido_model import PedidoModel
from ..styles.cores import Cores as cor


class Pedido():

    @staticmethod
    def cadastro(cliente, items=[], exibe_cabecalho=False):
        if exibe_cabecalho:
            Utils.titulo("Novo Pedido")
        try:
            nome_cliente = cliente.nome
            id_cliente = cliente.codigo
            items_produtos = items
            valor_total = Pedido.__calcular_total_venda(items)

            novo_pedido = PedidoModel()
            novo_pedido.id_cliente = id_cliente
            novo_pedido.nome_cliente = nome_cliente

            novo_pedido.valor_total = valor_total
            novo_pedido.itens = items_produtos
            novo_pedido.gravar()

            Utils.limpar_tela()
            Utils.messagem_success("Inserido com sucesso")

        except Exception as e:
            Utils.messagem_error(e=e)

    @staticmethod
    def listar():
        pedidos = PedidoModel.buscar()
        Utils.titulo("Relatório de Pedidos")
        for pedido in pedidos:
            print(f"\ncodigo: {pedido.codigo[ : 8]}")
            print(f"Nome: {pedido.nome_cliente}")
            i = 1
            print(f"#|Código|Descrição|Qtde|Volor unit.|Valor total")
            for item in pedido.itens:
                print(f"{i} {item['produto']} {item['qtd']} unid  x {item['preco']} {item['valor_total_produto']}")
                i += 1
            print(f"Valor Total R$ {pedido.valor_total}")
            print(f"{cor.CTEXTINFO}{'-' * 30}{cor.CEND}")

    def __calcular_total_venda(items=[]):
        valor_total = 0

        if len(items) > 0:
            for item in items:
                valor_total += item["valor_total_produto"]

            return valor_total

        return valor_total

# if __name__ == "__main__":
#     Cliente.exec()
