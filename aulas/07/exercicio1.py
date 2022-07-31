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
media = 0
notas = 0
situcao = ""
quantidade_de_notas = 3
limpa_tela = os.system("clear")

limpa_tela
print("============[ CADASTRO DE NOTA ]================\n")
quantidade_aluno = int(input("Informe a quantidade de alunos:"))
for i in range(0, quantidade_aluno):
    media= 0
    notas= 0 
    nota = 0
    nome_aluno = input(f"\nInforme nome do aluno {i+1}:")
    aluno = []
    
    aluno.append(nome_aluno)
    for y in range(1, 4):
        nota = float(input(f"Digite nota {y}: "))
        notas += nota
    media = (notas) / 3
    aluno.append(media)
    
    if media > 7:
        situcao = "Aprovado"
    elif media >= 5 and media <= 7:
        situcao = "Recuperação"
    else:
        situcao = "Reprovado"
    
    aluno.append(situcao)
    lista_de_aluno.append(aluno)
    
limpa_tela
print("============[ Lista de alunos ]================\n")
for i in range(0, len(lista_de_aluno)):
  print(f"Nome: {lista_de_aluno[i][0]}")
  print("Média: {:0.2f}".format(lista_de_aluno[i][1]))
  print(f"Situação: {lista_de_aluno[i][2]}")
  print("===============================================\n")
    
