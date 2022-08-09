import json
import os
import uuid
from ..utils.utils import Utils
from ..models.cliente_model import ClienteModel

# - id
# - cliente
# - metodo_valor_total()
# - itens []


class PedidoModel():
    def __init__(self, codigo="" ):
        self.codigo = codigo
        self.itens = []
        self.cliente = ClienteModel()

    def adicionar_cliente(self, codigo, nome, email):
        self.cliente.codigo = codigo
        self.cliente.nome = nome
        self.cliente.email = email

    def adicionar_produto(self, list_produto):
        self.itens = list_produto

    # def valor_total(self):
    #     return sum(self.notas)

    # def __init__(self, pedido_dict={"codigo": "", "id_cliente": "","nome_cliente":"", "valor_total": 0, "itens": []}):
    #     self.codigo = pedido_dict["codigo"]
    #     self.id_cliente = pedido_dict["id_cliente"]
    #     self.nome_cliente = pedido_dict["nome_cliente"]
    #     self.valor_total = pedido_dict["valor_total"]
    #     self.itens = pedido_dict["itens"]

    # def gravar(self):
    #     pedidos = PedidoModel.buscar()
    #     pedidos_existe = any(a for a in pedidos if a.codigo == self.codigo)
    #     if pedidos_existe:
    #         return

    #     self.codigo = str(uuid.uuid4())
    #     pedidos.append(self)
    #     f = open(PedidoModel.__caminho_arquivo(), "w")
    #     try:
    #         pedidos_json = json.dumps([obj.__dict__ for obj in pedidos])
    #         f.write(pedidos_json)
    #     except Exception as e:
    #         Utils.messagem_error(e="Algo deu errado na escrita do arquivo")
    #     finally:
    #         f.close()

    # @staticmethod
    # def buscar_por_codigo(codigo):
    #     pedidos = PedidoModel.buscar()
    #     return next((a for a in pedidos if a.codigo == codigo), None)

    # @staticmethod
    # def buscar():
    #     PedidoModel.__criar_db_se_nao_existe()
    #     f = open(PedidoModel.__caminho_arquivo(), "r")
    #     try:
    #         return PedidoModel.__converter_list_dict_objeto_cliente(json.loads(f.read()))
    #     except:
    #         return []
    #     finally:
    #         f.close()

    # @staticmethod
    # def __converter_list_dict_objeto_cliente(pedidos_dict):
    #     pedidos = []
    #     for cliente in pedidos_dict:
    #         pedidos.append(PedidoModel(cliente))
    #     return pedidos

    # @staticmethod
    # def __caminho_arquivo():
    #     caminho_arquivo = os.path.dirname(__file__)
    #     return f"{caminho_arquivo}/../db/pedidos.json"

    # @staticmethod
    # def __criar_db_se_nao_existe():
    #     from os.path import exists
    #     if not exists(PedidoModel.__caminho_arquivo()):
    #         f = open(PedidoModel.__caminho_arquivo(), "w")
    #         try:
    #             pedidos_json = json.dumps([])
    #             f.write(pedidos_json)
    #         except Exception as e:
    #             Utils.messagem_error(e="Algo deu errado na escrita do arquivo")
    #         finally:
    #             f.close()
