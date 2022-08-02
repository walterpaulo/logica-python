"""
USAR O DICT

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

os.system("clear")


def exec():
    print(f"{'_'*10}| CADASTRO DE NOTA |{'_'*9}\n")
    quantidade_aluno = int(input("Informe a quantidade de alunos:"))
    for i in range(0, quantidade_aluno):
        media = 0
        notas = []
        situacao = "Aprovado"
        aluno = {}

        aluno["nome"] = input(f"\nInforme nome do aluno {i+1}:")

        for y in range(0, quantidade_de_notas):
            nota = 0
            notas.append(float(input(f"Digite nota {y + 1}: ")))

        media = float("{:0.2f}".format(sum(notas) / quantidade_de_notas))
        aluno["media"] = media
        aluno["notas"] = notas

        if media >= 5 and media <= 7:
            situacao = "Recuperação"
        elif media < 5:
            situacao = "Reprovado"

        aluno["situacao"] = situacao
        lista_de_aluno.append(aluno)
        del aluno

    print(f"\n{'_'*10}| Lista de alunos |{'_'*10}\n")
    for aluno in lista_de_aluno:
        for chave, valor in aluno.items():
            print(f"{' '*12}{chave}: {valor}")
        print("\n")
    print(f"{'_'*39}\n")


if __name__ == "__main__":
    exec()
