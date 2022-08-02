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


def limpa_tela():
    os.system("clear")


def resultado_aluno(media):
    if media >= 5 and media <= 7:
        return "Recuperação"
    elif media < 5:
        return "Reprovado"
    else:
        return "Aprovado"


def lista_alunos(lista_de_aluno):
    print(f"\n{'_'*9}| Lista de alunos |{'_'*8}\n")
    for aluno in lista_de_aluno:
        print(f"Nome: {aluno[0]}")
        print("Média: {:0.2f}".format(aluno[1]))
        print(f"Notas: {aluno[2]}")
        print(f"Resultado: {aluno[3]}")
        print(f"{'_'*36}\n")


def captura_de_nota():
    notas = []
    for y in range(0, 3):
        nota = 0
        nota = float(input(f"Digite nota {y + 1}: "))
        notas.append(nota)
    return notas


def exec():
    lista_de_aluno = []
    quantidade_de_notas = 3
    limpa_tela()

    print(f"{'_'*10}| CADASTRO DE NOTA |{'_'*10}\n")
    quantidade_aluno = int(input("Informe a quantidade de alunos:"))
    for i in range(0, quantidade_aluno):
        media = 0
        aluno = []
        nome_aluno = input(f"\nInforme nome do aluno {i+1}:")

        aluno.append(nome_aluno)
        notas = captura_de_nota()
        media = sum(notas) / quantidade_de_notas
        aluno.append(media)
        aluno.append(notas)

        situacao = resultado_aluno(media)
        aluno.append(situacao)
        lista_de_aluno.append(aluno)

    limpa_tela()
    lista_alunos(lista_de_aluno)


if __name__ == "__main__":
    exec()
