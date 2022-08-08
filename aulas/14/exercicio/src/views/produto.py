from ..utils.utils import Utils
from ..models.produto_model import ProdutoModel
from ..styles.cores import Cores as cor


class Produto():

    @staticmethod
    def cadastro(nome='', preco='', exibe_cabecalho=True):
        if exibe_cabecalho:
            Utils.titulo("Cadastro de PRodut")
        try:

            nome, preco = Produto.__validar_nomes()
            produto = ProdutoModel()
            produto.nome = nome
            produto.preco = preco
            produto.gravar()
            Utils.limpar_tela()
            Utils.messagem_success("Inserido com sucesso")

            while True:
                print("Deseja cadastar novo produto?")
                print("1 - Sim")
                print("2 - Não")
                print("0 - Retornar ao menu anterior")
                opcao_selecionado = Utils.obtem_opcao_menu(1, 2)
                if opcao_selecionado == 1:
                    Utils.limpar_tela()
                    nome = ""
                    preco = ""
                    Produto.cadastro(
                        nome, preco, exibe_cabecalho=True,)
                if opcao_selecionado == 2 or opcao_selecionado == 0:
                    Utils.limpar_tela()
                    break

        except Exception as e:
            Utils.messagem_error(e=e)
            return Produto.cadastro(nome, preco, exibe_cabecalho=False)

    @staticmethod
    def listar():
        produtos = ProdutoModel.buscar()
        Utils.titulo("Relatório de Produtos")
        for produto in produtos:
            print(f"\ncodigo: {produto.codigo}")
            print(f"Nome: {produto.nome}")
            print(f"Preço: {produto.preco}")
            print(f"{cor.CTEXTINFO}{'-' * 30}{cor.CEND}")

    @staticmethod
    def adicionar_carrinho(produto="", quantidade="", itens=[]):
        try:
            produtos = ProdutoModel.buscar()
            Utils.titulo("Adicionar item")
            itens = itens
            i = 1
            print(f"CÓDIGO | Descrição | Preço")
            for produto in produtos:
                print(f"{i} - {produto.nome} R$ {produto.preco}")
                i += 1

            opcao_selecionada = Utils.obtem_opcao_menu(1, len(produtos))
            codigo_produto = Produto.__retornar_id(opcao_selecionada)

            objeto_produto = ProdutoModel.buscar_por_codigo(codigo_produto)

            produto = objeto_produto.nome
            valor_produto = objeto_produto.preco
            if produto.strip() == "":
                raise TypeError("Digite o produto correto.")
            if quantidade.strip() == "":
                quantidade = Utils.obter_numero(
                    f"Digite a quantidade de [{produto}]")

            itens.append({"produto": produto, "preco": valor_produto,
                         "qtd": quantidade, "valor_total_produto": valor_produto * quantidade})

            while True:
                Utils.limpar_tela()
                Utils.titulo("Deseja cadastar novo produto?")
                print("1 - Sim")
                print("0 - Não")
                opcao_selecionado = Utils.obtem_opcao_menu(1, 1)
                if opcao_selecionado == 0:
                    Utils.limpar_tela()
                    return itens
                elif opcao_selecionado == 1:
                    Utils.limpar_tela()
                    produto = ""
                    quantidade = ""
                    Produto.adicionar_carrinho(
                        produto, quantidade)

        except Exception as e:
            Utils.messagem_error(e=e)
            return Produto.adicionar_carrinho(produto, quantidade, itens)

    def __validar_nomes(nome='', preco=''):
        try:
            if nome.strip() == "":
                nome = input("Digite o nome:")
                if nome.strip() == "":
                    raise TypeError("Digite o nome correto.")
            preco = Utils.obter_numero("Digite o valor")

            return nome, preco
        except Exception as e:
            Utils.messagem_error(e=e)
            return Produto.__validar_nomes(nome, preco)

    def __retornar_id(item):
        valor_codigo = ""
        produtos = ProdutoModel.buscar()
        i = 1
        for produto in produtos:
            if i == item:
                valor_codigo = produto.codigo
                return valor_codigo
            i += 1
        return valor_codigo


# if __name__ == "__main__":
#     Produto.exec()
