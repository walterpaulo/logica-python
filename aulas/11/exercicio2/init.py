"""
  Utilizando o algoritimo criado no dia 10
  refatore o código fazendo a persistencia dos dodos
  para que o cadastro de cleitnes, produtos e pedidos
  estejam persistidos no disco
"""
from produto import menu_produto
import produto
from cliente import salva_cliente
import cliente
from utils import limpar_tela, obter_numero, validar_number, message_menu_erro, gerador_id, obtem_opcao_menu
from service import carregar_dados, salvar_dados, busca_dados_id


def menu_pedido(db_pedido=[], db_produtos=[]):
    novo_cliente = salva_cliente()
    novo_pedido(novo_cliente, db_pedido, db_produtos, True)


def imprimir_cupom(items):
    print(f'-'*48)
    print(f'# |Código|Descrição|Qtde|Valor unit.|Valor total')
    print(f'-'*48)
    total_compra = 0
    qtd_item = 0
    for i in items:
        qtd_item += 1
        print(
            f"{qtd_item}  {i['id']}  {i['nome']}  {i['qtd']} X {i['preco']}  {i['preco'] * i['qtd'] }")
        total_compra += i['preco'] * i['qtd']
    print('-'*48)
    print(f"QTD. TOTAL DE ITENS {len(items)}")
    print(f"VALOR TOTAL R$ {total_compra}\n")


def novo_pedido(cliente, db_pedidos=[], db_produtos=[], exibir_titulo=True):
    items = []
    pedido = {}
    try:
        limpar_tela()
        print(f"\n{'_'*10}| Pedido - {cliente['nome']} |{'_'*10}")
        if len(items) > 0:
            print(f"\nConsumidor: {cliente['nome']}")
            imprimir_cupom(items)
        else:
            print(f'Qtd de Item: 0')
        while True:
            print("\nDigite o código do item:\n")
            menu_produto(db_produtos)
            opcao_selecionada = obtem_opcao_menu(1, len(db_produtos))
            if opcao_selecionada == 0:
                break
            limpar_tela()
            busca_produto = busca_dados_id(db_produtos, opcao_selecionada)
            print(f"Quantidade de item ({busca_produto['nome']})?")
            print('0 - Retira do carrinho')
            qtd_produto = obter_numero()
            if qtd_produto >> 0:
                busca_produto.update({"qtd": qtd_produto})
                items.append(busca_produto)
            limpar_tela()
            print('Adicionar mais item?')
            print('1 - Adicionar mais produto')
            print('2 - Finalizar pedido')
            print('0 - Cancelar')
            opcao_retorno = obtem_opcao_menu(1, 2)

            if opcao_retorno == 0:
                break
            elif opcao_retorno == 2:
                pedido.update({"id_pedido": gerador_id(db_pedidos)})
                pedido.update({"id_cliente": cliente['id']})
                pedido.update({"nome_cliente": cliente['nome']})
                pedido.update({"items": items})
                db_pedidos.append(pedido)
                salvar_dados("db_pedidos.json", db_pedidos)
                limpar_tela()
                print("Pedido salvo")
                break
            limpar_tela()

    except Exception as e:
        print(f"Alerta: {e}")


def exec(db_clientes=[], db_pedidos=[], db_produtos=[]):
    limpar_tela()
    while True:
        print(f"{'_'*10}| Sistema de Pedito |{'_'*10}")
        print("1 - Fazer Pedido")
        print("2 - Lista de Pedidos")
        print("3 - Produtos")
        print("4 - Clientes")
        print("0 - Sair")
        opcao_selecionada = obtem_opcao_menu(1, 4)

        if opcao_selecionada == 0:
            break
        elif opcao_selecionada == 1:
            limpar_tela()
            menu_pedido(db_pedidos, db_produtos)
        elif opcao_selecionada == 2:
            limpar_tela()
            print(f"{'-'*10}| Lista de Pedito(s) |{'-'*10}")
            if len(db_pedidos) > 0:
                for pedido in db_pedidos:
                    print(f"\n{'-'*48}")
                    print(f"Pedido Id: {pedido['id_cliente']}")
                    print(f"Nome: {pedido['nome_cliente']}")
                    imprimir_cupom(pedido['items'])
            else:
                print("\nLista vazia, aperte 1 para novo pedido!\n")
        elif opcao_selecionada == 3:
            limpar_tela()
            produto.exec(db_produtos)
        elif opcao_selecionada == 4:
            limpar_tela()
            cliente.exec(db_clientes)


if __name__ == "__main__":
    db_clientes = carregar_dados("db_clientes.json")
    db_pedidos = carregar_dados("db_pedidos.json")
    db_produtos = carregar_dados("db_produtos.json")
    exec(db_clientes, db_pedidos, db_produtos)
