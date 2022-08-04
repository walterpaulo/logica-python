''''
Faca um programa para calcular os valores de um pedido
para isso crie um objeto dict de pedido que tenha relacao com um objeto dict de cliente
pedido = {
    "id": 1,
    "cliente": {
        "nome": "Walter"
    },
    "itens": []
}
nesse pedido, coloque uma propriedade de itens, contendo instancias de um dict de produto
no pedido, crie uma função para calcular o valor total
e uma função para mostrar um relatório do pedido, mostrando da seguinte forma:
----------------------------------------------------------------
Pedido Id: 1
Nome: João
Valor Total: R$ 999,99
----------------------------------------------------------------
O que terá no dict de pedido:
- id
- cliente
- itens []
O que terá no dict cliente:
- Nome
- email
O que terá no dict produto:
- Nome
- descrição
- preço
'''

from produto import menu_produto, busca_produto_id
import produto
from cliente import salva_cliente
import cliente
from utils import limpar_tela, validar_number, message_menu_erro

pedidos = []


def menu_pedido():
    novo_cliente = salva_cliente()
    novo_pedido(novo_cliente)


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


def novo_pedido(cliente):
    items = []
    pedido = {}
    while True:
        limpar_tela()
        print(f"\n{'_'*10}| Pedido - {cliente['nome']} |{'_'*10}")
        if len(items) > 0:
            print(f"\nConsumidor: {cliente['nome']}")
            imprimir_cupom(items)
        else:
            print(f'Qtd de Item: 0')
        print("\nDigite o código do item:\n")
        if len(items) > 0:
            print("0 - Salvar Pedido")
        menu_produto()
        numero = input('$> ')
        opcao = numero
        if opcao == 's':
            break
        elif int(opcao) == 0:
            pedido.update({"id_cliente": cliente['id']})
            pedido.update({"nome_cliente": cliente['nome']})
            pedido.update({"items": items})
            pedidos.append(pedido)
            limpar_tela()
            print("Pedido salvo")
            break
        elif opcao.isdigit():
            add_produto = busca_produto_id(int(opcao))
            qtd_produto = int(
                input(f"Digite a quantidade ( {add_produto['nome']} ): "))
            add_produto.update({'qtd': qtd_produto})
            items.append(add_produto)
        else:
            print("Opção inválida!")


def exec():
    limpar_tela()
    while True:
        print(f"{'_'*10}| Sistema de Pedito |{'_'*10}")
        print("1 - Fazer Pedido")
        print("2 - Lista de Pedidos")
        print("3 - Produtos")
        print("4 - Clientes")
        print("s - Sair")
        opcao = validar_number(input("$>"))

        if opcao == 's':
            break
        elif opcao == 1:
            limpar_tela()
            menu_pedido()
        elif opcao == 2:
            limpar_tela()
            print(f"{'-'*10}| Lista de Pedito(s) |{'-'*10}")
            if len(pedidos) > 0:
                for pedido in pedidos:
                    print(f"\n{'-'*48}")
                    print(f"Pedido Id: {pedido['id_cliente']}")
                    print(f"Nome: {pedido['nome_cliente']}")
                    imprimir_cupom(pedido['items'])
            else:
                print("\nLista vazia, aperte 1 para novo pedido!\n")
        elif opcao == 3:
            limpar_tela()
            produto.exec()
        elif opcao == 4:
            limpar_tela()
            cliente.exec()
        else:
            limpar_tela()
            message_menu_erro(opcao)


if __name__ == "__main__":
    exec()
