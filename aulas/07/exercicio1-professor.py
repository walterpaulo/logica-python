
print("=============[Bem vindo ao programa de alunos]=============")
qtd = int(input("Digite a quantidade de alunos\n"))
alunos = []
for indice in range(0, qtd):
  aluno = []
  nome = input("Digite o nome do aluno:\n")
  aluno.append(nome)

  notas = []
  for i in range(0,3):
    notas.append(float(input(f"Digite a nota {i+1} do (a) {nome}\n")))
  aluno.append(notas)

  media = sum(notas) / len(notas)
  aluno.append(media)

  situacao = "Aprovado"
  if media < 5:
    situacao = "Reprovado"
  elif media >= 5 and media <=7:
    situacao = "Recuperação"
  
  aluno.append(situacao)

  alunos.append(aluno)

for aluno in alunos:
  print("f============[ Lista de alunos ]================")
  print(f"Nome: {aluno[0]}")
  print(f"Notas: {aluno[1]} ")
  print(f"Média: {aluno[2]}")
  print(f"Situação: {aluno[3]}")