import json
import os
import uuid


class ClienteModel():
    def __init__(self, cliente_dict={"codigo": "", "nome": "", "email": ""}):
        self.codigo = cliente_dict["codigo"]
        self.nome = cliente_dict["nome"]
        self.email = cliente_dict["email"]

    def gravar(self):
        clientes = ClienteModel.buscar()
        pessoas_existe = any(a for a in clientes if a.codigo == self.codigo)
        if pessoas_existe:
            return

        self.codigo = str(uuid.uuid4())
        clientes.append(self)
        f = open(ClienteModel.__caminho_arquivo(), "w")
        try:
            clientes_json = json.dumps([obj.__dict__ for obj in clientes])
            f.write(clientes_json)
        except Exception as e:
            print(e)
            print("Algo deu errado na escrita do arquivo")
        finally:
            f.close()

    @staticmethod
    def buscar_por_codigo(codigo):
        clientes = ClienteModel.buscar()
        return next((a for a in clientes if a.codigo == codigo), None)

    @staticmethod
    def buscar():
        ClienteModel.__criar_db_se_nao_existe()
        f = open(ClienteModel.__caminho_arquivo(), "r")
        try:
            return ClienteModel.__converter_list_dict_objeto_cliente(json.loads(f.read()))
        except:
            return []
        finally:
            f.close()

    ##### Métodos privados #####

    @staticmethod
    def __converter_list_dict_objeto_cliente(clientes_dict):
        clientes = []
        for cliente in clientes_dict:
            clientes.append(ClienteModel(cliente))
        return clientes

    @staticmethod
    def __caminho_arquivo():
        caminho_arquivo = os.path.dirname(__file__)
        return f"{caminho_arquivo}/../db/clientes.json"

    @staticmethod
    def __criar_db_se_nao_existe():
        from os.path import exists
        if not exists(ClienteModel.__caminho_arquivo()):
            f = open(ClienteModel.__caminho_arquivo(), "w")
            try:
                clientes_json = json.dumps([])
                f.write(clientes_json)
            except Exception as e:
                print(e)
                print("Algo deu errado na escrita do arquivo")
            finally:
                f.close()
