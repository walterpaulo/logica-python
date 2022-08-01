"""
Danilo é dono de uma escola de programação, faça um programa
solicite a quantidade de alunos, capture 3 notas de alunos
no final do programa mostre um relatório identificando se os
os alunos estão aprovado, reprovados ou em recuperado


calculo da média
media = (n1+n2+n3)/3

Regra de aprovação:
Notas abaixo de 5 = Reprovado
Notas de 5 até 7 = Recuperação
Notas acima de 7 = aprovado

Exemplo de lista

============[ Lista de alunos ]================
Nome: Danilo
Média: 7.5
Situação: Aprovado

"""
import os

lista_de_aluno = []
quantidade_de_notas = 3
limpa_tela = os.system("clear")

limpa_tela
print("============[ CADASTRO DE NOTA ]================\n")
quantidade_aluno = int(input("Informe a quantidade de alunos:"))
for i in range(0, quantidade_aluno):
    media= 0
    notas= []
    situcao = "Aprovado"
    aluno = []
    nome_aluno = input(f"\nInforme nome do aluno {i+1}:")
    
    aluno.append(nome_aluno)
    for y in range(1, 4):
        nota = 0
        nota = float(input(f"Digite nota {y}: "))
        notas.append(nota)
    media = sum(notas) / 3
    aluno.append(media)
    aluno.append(notas)
    
    if media >= 5 and media <= 7:
        situcao = "Recuperação"
    elif media < 5:
        situcao = "Reprovado"
    
    aluno.append(situcao)
    lista_de_aluno.append(aluno)
    
limpa_tela
print("============[ Lista de alunos ]================\n")
for aluno in lista_de_aluno:
  print(f"Nome: {aluno[0]}")
  print("Média: {:0.2f}".format(aluno[1]))
  print(f"Notas: {aluno[2]}")
  print(f"Situação: {aluno[3]}")
  print("===============================================\n")
    
