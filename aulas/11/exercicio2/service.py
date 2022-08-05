import json
from os.path import exists
from utils import limpar_tela


def carregar_dados(nome_json):
    file_exists = exists(nome_json)
    if file_exists:
        with open(nome_json, "r", encoding="utf-8") as dados:
            return json.load(dados)
    else:
        with open(nome_json, "w", encoding="utf-8") as dados:
            temporario = []
            json.dump(temporario, dados)
            return temporario


def ler(nome_json):
    try:
        with open(nome_json) as arquivo_clientes:
            clientes = arquivo_clientes.read()
        limpar_tela()
        cliente_json = json.loads(clientes)
        return cliente_json
    except json.decoder.JSONDecodeError:
        print("Lista vazia")
    except Exception as e:
        print(f"Alerta: {e}")


def salvar_dados(nome_json, file):
    with open(nome_json, "w", encoding="utf-8") as dados:
        salvando = json.dump(file, dados)
    return salvando


def busca_dados_id(nome_json, codigo):
    for objecto in nome_json:
        if objecto['id'] == codigo:
            return objecto
    return
