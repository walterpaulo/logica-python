import json
import os
from pydoc import cli
import uuid
from ..utils.utils import Utils
from ..models.pedido_model import PedidoModel
from ..models.cliente_model import ClienteModel


class PedidoService():
    def __init__(self, PedidoModel):
        self.codigo = PedidoModel.codigo

    def gravar(self):
        pedidos = PedidoService.buscar()
        pedidos_existe = any(a for a in pedidos if a.codigo == self.codigo)
        if pedidos_existe:
            return

        self.codigo = str(uuid.uuid4())
        pedidos.append(self)
        f = open(PedidoService.__caminho_arquivo(), "w")
        try:
            pedidos_json = json.dumps(Utils.para_dict(pedidos))
            f.write(pedidos_json)
        except Exception as e:
            Utils.messagem_error(texto="Algo deu errado na escrita do arquivo")

        finally:
            f.close()

    @staticmethod
    def buscar_por_codigo(codigo):
        pedidos = PedidoService.buscar()
        return next((a for a in pedidos if a.codigo == codigo), None)

    @staticmethod
    def buscar():
        PedidoService.__criar_db_se_nao_existe()
        f = open(PedidoService.__caminho_arquivo(), "r")
        try:
            # return PedidoService.__converter_list_dict_objeto_produto(json.loads(f.read()))
            lista_pedidos = f.read()
            return PedidoService.__converter_list_dict_objeto_produto(json.loads(lista_pedidos))
        except:
            return []
        finally:
            f.close()

    @staticmethod
    def __converter_list_dict_objeto_produto(pedidos_dict):
        pedidos = []
        for pedido in pedidos_dict:
            objeto_pedido = PedidoModel()
            objeto_pedido.codigo = pedido["codigo"]
            cliente = pedido['cliente']
            objeto_pedido.adicionar_cliente(
                codigo=cliente['codigo'], nome=cliente['nome'], email=cliente['email'])
            lista_objeto_produtos = objeto_pedido.converter_dict_obj_produto(
                pedido["itens"])
            objeto_pedido.adicionar_produto(lista_objeto_produtos)
            pedidos.append(objeto_pedido)
        return pedidos

    @staticmethod
    def __caminho_arquivo():
        caminho_arquivo = os.path.dirname(__file__)
        return f"{caminho_arquivo}/../db/pedidos.json"

    @staticmethod
    def __criar_db_se_nao_existe():
        from os.path import exists
        if not exists(PedidoService.__caminho_arquivo()):
            f = open(PedidoService.__caminho_arquivo(), "w")
            try:
                produtos_json = json.dumps([])
                f.write(produtos_json)
            except Exception as e:
                Utils.messagem_error(
                    texto="Algo deu errado na escrita do arquivo")
            finally:
                f.close()
