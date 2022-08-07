from utils.utils import limpar_tela, obtem_opcao_menu
from models.animal import Animal


class Animais():

    @staticmethod
    def cadastro(nome='', descricao='', exibe_cabecalho=True):
        if exibe_cabecalho:
            print(f"{'-'*10}| Cadastro de Animal |{'-'*10}")
        try:

            nome, descricao = Animais.__validar_nomes()
            animal = Animal()
            animal.nome = nome
            animal.descricao = descricao
            animal.gravar()
            limpar_tela()
            print("Inserido com sucesso.")

            while True:
                print("Deseja cadastar novo aninal?")
                print("1 - Sim")
                print("2 - Não")
                print("0 - Retornar ao menu anterior")
                opcao_selecionado = obtem_opcao_menu(1, 2)
                if opcao_selecionado == 1:
                    limpar_tela()
                    nome = ""
                    descricao = ""
                    Animais.cadastro(nome, descricao, exibe_cabecalho=True,)
                if opcao_selecionado == 2 or opcao_selecionado == 0:
                    limpar_tela()
                    break

        except Exception as e:
            print(f"Alerta: {e}")
            return Animais.cadastro(nome, descricao, exibe_cabecalho=False)

    @staticmethod
    def listar():
        animais = Animal.buscar()
        print(f"{'-'*10}| Lista de Animais |{'-'*10}")
        for animal in animais:
            print(f"{'=' * 30}")
            print(f"codigo: {animal.codigo}")
            print(f"Nome: {animal.nome}")
            print(f"Descrição: {animal.descricao}")

    @staticmethod
    def __validar_nomes(nome='', descricao=''):
        try:
            if nome.strip() == "":
                nome = input("Digite o nome:")
                if nome.strip() == "":
                    raise TypeError("Digite o nome correto.")
            if descricao.strip() == "":
                descricao = input("Digite a descrição:")
                if descricao.strip() == "":
                    raise TypeError("Digite a descrição correto.")
                return nome, descricao
        except Exception as e:
            print(f"Alertas: {e}")
            return Animais.__validar_nomes(nome, descricao)
