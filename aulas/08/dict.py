aluno = {
  "nome": "Daniel",
  "notas": [5,8,9],
  "media": 6.6,
  "Situacao": "Recuperação"
}


nome = aluno["nome"]
print(f"Nome: {nome}")

notas = aluno["notas"]
print(f"Notas: {notas} ")
print(f"Média: {aluno['media']}")
print(f"Situação: {aluno['Situacao']}")

produto = {
  "nome": "teclado",
  "descricao": {
    "cor": "cinza"
  }
}

produto["nome"] = "teclado"
# ou
produto.update({"nome": "teclado c"})

# adiciona
produto["descricao"]["cor"] = "verde"

print(produto["nome"])
print(produto["descricao"]["cor"])

print(produto.items()) # lista de dicionário

# Verifica existência de chave no dicionário
if "nome" in produto:
  print("Sim, 'nome' é uma das chaves do dicionários produto")

# remove item
produto.pop("descricao")