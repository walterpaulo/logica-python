import json
import os
import uuid
from ..utils.utils import Utils
from ..models.cliente_model import ClienteModel
from ..models.item_model import ItemModel


class PedidoModel():
    def __init__(self, codigo=""):
        self.codigo = codigo
        self.itens = []
        self.cliente = ClienteModel()

    def adicionar_cliente(self, codigo, nome, email):
        self.cliente.codigo = codigo
        self.cliente.nome = nome
        self.cliente.email = email

    def adicionar_produto(self, list_produto):
        lista_objeto = []
        for produto in list_produto:
            objeto = ItemModel(
                produto=produto.produto, preco=produto.preco, qtd=produto.qtd)
            lista_objeto.append(objeto)

        self.itens = lista_objeto

    def converter_dict_obj_produto(self, list_dict_produto):
        lista_objeto = []
        for produto in list_dict_produto:
            objeto = ItemModel(
                produto=produto["produto"], preco=produto["preco"], qtd=produto["qtd"])
            lista_objeto.append(objeto)

        return lista_objeto
