import json
import os
import uuid
from ..utils.utils import Utils
from ..models.cliente_model import ClienteModel


class ClienteService():
    def __init__(self, ClienteModel):
        self.codigo = ClienteModel.codigo
        self.nome = ClienteModel.nome
        self.email = ClienteModel.email

    def gravar(self):
        clientes = ClienteService.buscar()
        cliente_existe = any(a for a in clientes if a.codigo == self.codigo)
        if cliente_existe:
            return

        self.codigo = str(uuid.uuid4())
        clientes.append(self)
        f = open(ClienteService.__caminho_arquivo(), "w")
        try:
            clientes_json = json.dumps([obj.__dict__ for obj in clientes])
            f.write(clientes_json)
        except Exception as e:
            Utils.messagem_error(texto="Algo deu errado na escrita do arquivo")

        finally:
            f.close()

    @staticmethod
    def buscar_por_codigo(codigo):
        clientes = ClienteService.buscar()
        return next((a for a in clientes if a.codigo == codigo), None)

    @staticmethod
    def buscar():
        ClienteService.__criar_db_se_nao_existe()
        f = open(ClienteService.__caminho_arquivo(), "r")
        try:
            return ClienteService.__converter_list_dict_objeto_produto(json.loads(f.read()))
        except:
            return []
        finally:
            f.close()

    @staticmethod
    def __converter_list_dict_objeto_produto(clientes_dict):
        clientes = []
        for cliente in clientes_dict:
            objeto_cliente = ClienteModel()
            objeto_cliente.codigo = cliente["codigo"]
            objeto_cliente.nome = cliente["nome"]
            objeto_cliente.email = cliente["email"]
            clientes.append(objeto_cliente)
        return clientes

    @staticmethod
    def __caminho_arquivo():
        caminho_arquivo = os.path.dirname(__file__)
        return f"{caminho_arquivo}/../db/clientes.json"

    @staticmethod
    def __criar_db_se_nao_existe():
        from os.path import exists
        if not exists(ClienteService.__caminho_arquivo()):
            f = open(ClienteService.__caminho_arquivo(), "w")
            try:
                produtos_json = json.dumps([])
                f.write(produtos_json)
            except Exception as e:
                Utils.messagem_error(
                    texto="Algo deu errado na escrita do arquivo")
            finally:
                f.close()
