## Dia 07 - 31/07/2022[  🔙](../../README.md)

- Clonar um projeto, utiliza o camando git:

```
git clone https://github.com/walterpaulo/logica-python.git
```

- git = comando;
- clone = opção;
- [https://github...](https://github.com/walterpaulo/logica-python) = caminho

<p>

- Array, a = [1,2,3]
 - nevegar no array, dig[0] retorna o valor 1
 - a lib six mostra informações, o six.MAXSIZE mostra a quantidade de memória do computador;
 - para alterar o valor de um índice, a[1] = 3, se o índice informado não existe ocorre erro;
 - pode misturar tipos variados em um array, int, string, float ...;
 - append adicionar novo item, a.append(4);
 - pop retira um item da lista, a.pop(1);
   - retorna uma string;
   - se não informar o índice, retirar o último;
   - Pode tirar um item e colocar na variável, valor = a.pop(1);
 - remove retira um item pelo o nome, a.remove(1);
   - sem retorno;
 - clear remove limpa o array, a.clear();
   - sem retorno;
 - len conta a quantidade de índice na lista, len(a);
 - insert insere novo índice, informe índice e valor, a.insert(1, "b")
 - sort ordena lista
  - sem passar valor no parâmetro, ordena em ordem alfabética;
 - reverse inverte a ordem
 - matriz um lista de uma lista, matry = [[3,4,7], [6,8,9]]
    - retorna_oito = matriz[2][2]