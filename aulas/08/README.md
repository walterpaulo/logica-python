## Dia 08 - 01/08/2022[  🔙](../../README.md)

- Dic - de dicionário ou objeto de variáveis, chaves e valores;
  - definido com chaves {};
  - para ter acesso ao valor, chame o objeto seguido por ponto e chave: aluno.nome
  - adicionar ou atualizar chave, aluno.update({"disciplina": "Lógica de programação"})
  - remover item, produto.pop("disciplina") ou del produto["disciplina"]
    - remover última item, produto.popitem()
    - apagar o dicionário, del produto
    - esvazia o dicinário, produto.clear()

### Exemplos

<p>

modelo de um dict

```
alunos = {
  Nome: walter
  Notas: [3.0, 6.0, 7.0] 
  Média: 5.33
  Situação: Recuperação
}
```

retorno de valores com o loop


```
for x in alunos:
  print(alunos[x]) 

# ou

for x in alunos.values:
  print(x) 
```

retorno de chave e valor com loop
```
for x, y in alunos.items():
  print(x, y) 
```