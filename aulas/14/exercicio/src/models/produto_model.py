import json
import os
import uuid
from ..utils.utils import Utils


class ProdutoModel():
    def __init__(self, produto_dict={"codigo": "", "nome": "", "preco": 0}):
        self.codigo = produto_dict["codigo"]
        self.nome = produto_dict["nome"]
        self.preco = produto_dict["preco"]

    def gravar(self):
        produtos = ProdutoModel.buscar()
        produto_existe = any(a for a in produtos if a.codigo == self.codigo)
        if produto_existe:
            return

        self.codigo = str(uuid.uuid4())
        produtos.append(self)
        f = open(ProdutoModel.__caminho_arquivo(), "w")
        try:
            produtos_json = json.dumps([obj.__dict__ for obj in produtos])
            f.write(produtos_json)
        except Exception as e:
            Utils.messagem_error(texto="Algo deu errado na escrita do arquivo")

        finally:
            f.close()

    @staticmethod
    def buscar_por_codigo(codigo):
        produtos = ProdutoModel.buscar()
        return next((a for a in produtos if a.codigo == codigo), None)

    @staticmethod
    def buscar():
        ProdutoModel.__criar_db_se_nao_existe()
        f = open(ProdutoModel.__caminho_arquivo(), "r")
        try:
            return ProdutoModel.__converter_list_dict_objeto_produto(json.loads(f.read()))
        except:
            return []
        finally:
            f.close()

    @staticmethod
    def __converter_list_dict_objeto_produto(produtos_dict):
        produtos = []
        for cliente in produtos_dict:
            produtos.append(ProdutoModel(cliente))
        return produtos

    @staticmethod
    def __caminho_arquivo():
        caminho_arquivo = os.path.dirname(__file__)
        return f"{caminho_arquivo}/../db/produtos.json"

    @staticmethod
    def __criar_db_se_nao_existe():
        from os.path import exists
        if not exists(ProdutoModel.__caminho_arquivo()):
            f = open(ProdutoModel.__caminho_arquivo(), "w")
            try:
                produtos_json = json.dumps([])
                f.write(produtos_json)
            except Exception as e:
                Utils.messagem_error(
                    texto="Algo deu errado na escrita do arquivo")
            finally:
                f.close()
