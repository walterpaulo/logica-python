##  Exercício

''''
Faça um programa para calcular os valores de um pedido
para isso crie uma classe de pedido que tenha relação com uma classe de cliente
nesse pedido, coloque uma propriedade de itens, contendo instancias de uma classe de produto
no pedido, crie um método para calcular o valor total 
e um método para mostrar um relatório do pedido, mostrando da seguinte forma:
----------------------------------------------------------------
Pedido Id: 1
Nome: João
Valor Total: R$ 999,99
----------------------------------------------------------------
O que terá na classe de pedido:
- id
- cliente
- metodo_valor_total()
- itens []
O que terá na classe cliente:
- Nome
- email
O que terá na classe produto:
- Nome
- descrição
- preço
'''

## Estrutura do Código

```
── init.py
│   
├── README.md
└── src
    ├── controllers
    │   ├── clientes_controller.py
    │   ├── home_controller.py
    │   ├── pedidos_controller.py
    │   ├── produtos_controller.py
    │   └── relatorios_controller.py
    │   
    ├── db
    │   ├── clientes.json
    │   ├── pedidos.json
    │   └── produtos.json
    ├── models
    │   ├── cliente_model.py
    │   ├── pedido_model.py
    │   └── produto_model.py
    │       
    ├── styles
    │   └── cores.py
    │       
    ├── utils
    │   │   
    │   └── utils.py
    └── views
        ├── cliente.py
        ├── pedido.py
        └── produto.py

```

## Iniciar
```
python3 init.py
```