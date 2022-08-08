import json
import os
import uuid
from ..utils.utils import Utils
from ..models.produto_model import ProdutoModel


class ProdutoService():
    def __init__(self, ProdutoModel):
        self.codigo = ProdutoModel.codigo
        self.nome = ProdutoModel.nome
        self.preco = ProdutoModel.prece

    def gravar(self):
        produtos = ProdutoService.buscar()
        produto_existe = any(a for a in produtos if a.codigo == self.codigo)
        if produto_existe:
            return

        self.codigo = str(uuid.uuid4())
        produtos.append(self)
        f = open(ProdutoService.__caminho_arquivo(), "w")
        try:
            produtos_json = json.dumps([obj.__dict__ for obj in produtos])
            f.write(produtos_json)
        except Exception as e:
            Utils.messagem_error(texto="Algo deu errado na escrita do arquivo")

        finally:
            f.close()

    @staticmethod
    def buscar_por_codigo(codigo):
        produtos = ProdutoService.buscar()
        return next((a for a in produtos if a.codigo == codigo), None)

    @staticmethod
    def buscar():
        ProdutoService.__criar_db_se_nao_existe()
        f = open(ProdutoService.__caminho_arquivo(), "r")
        try:
            return ProdutoService.__converter_list_dict_objeto_produto(json.loads(f.read()))
        except:
            return []
        finally:
            f.close()

    @staticmethod
    def __converter_list_dict_objeto_produto(produtos_dict):
        produtos = []
        for cliente in produtos_dict:
            objeto_cliente = ProdutoModel()
            objeto_cliente.codigo = cliente["codigo"]
            objeto_cliente.nome = cliente["nome"]
            objeto_cliente.preco = cliente["preco"]
            produtos.append(objeto_cliente)
            # codigo='', nome="", preco=""
        return produtos

    @staticmethod
    def __caminho_arquivo():
        caminho_arquivo = os.path.dirname(__file__)
        return f"{caminho_arquivo}/../db/produtos.json"

    @staticmethod
    def __criar_db_se_nao_existe():
        from os.path import exists
        if not exists(ProdutoService.__caminho_arquivo()):
            f = open(ProdutoService.__caminho_arquivo(), "w")
            try:
                produtos_json = json.dumps([])
                f.write(produtos_json)
            except Exception as e:
                Utils.messagem_error(
                    texto="Algo deu errado na escrita do arquivo")
            finally:
                f.close()
