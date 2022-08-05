"""
Jardeclenio é um empresário dono de um Zoológico e precisa
de um programa para cadastrar os seus animais
Faça um programa que persista dos dados dos animais no disco

Exemplo do escopo da classe
Animal
  # propriedade
  - numero
  - nome
  - descricao

  # métodos
  - gravar()
  - buscar()
  - mostrar()
"""
from os.path import exists
import json


class Animal():

    def __init__(self):
        self.numero = ""
        self.nome = ""
        self.descricao = ""

    def salvar_dados(self):
        DB_ZOOLOGIO = "db_zoologio.json"

        with open(DB_ZOOLOGIO, "w", encoding="utf-8") as dados:
            salvando = json.dump(self)
        return salvando

    def gravar(self):
        DB_ZOOLOGIO = "db_zoologio.json"
        file_exists = exists(DB_ZOOLOGIO)
        if file_exists:
            with open(DB_ZOOLOGIO, "r", encoding="utf-8") as dados:
                self.salvar_dados()
                return json.load(dados)
        else:
            with open(DB_ZOOLOGIO, "w", encoding="utf-8") as dados:
                temporario = []
                json.dump(temporario, dados)
                return temporario

    def buscar(self):
        DB_ZOOLOGIO = "db_zoologio.json"
        for objecto in DB_ZOOLOGIO:
            if objecto['nome'] == self.nome:
                return objecto
        return

    def mostrar(self):
        DB_ZOOLOGIO = "db_zoologio.json"
        try:
            with open(DB_ZOOLOGIO) as arquivo_zoo:
                animais = arquivo_zoo.read()
            zoo_json = json.loads(animais)
            return zoo_json
        except json.decoder.JSONDecodeError:
            print("Lista vazia")


leao = Animal()
leao.numero = "1"
leao.nome = "leão"
leao.descricao = "reia da selva"

leao.gravar()
