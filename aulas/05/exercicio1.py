"""
Danilo, um professor de tecnologia, empresario no torne-se um programador,
desea jum software que ajude a calcular a meia de nota de um aluno,
faça um porgrama onde solicite o nome do aluno, tres notas do mesmo
depois faça o calculo para saber se o mesmo está aprovado:

regras para aprovação

se o aluno tirou a média artimética < 5, aluno está reprovado,
se o aluno tirou a média aritmética entre 5 e 7, aluno está em recuperação,
se o aluno tirou a média aritmética > 7, aluno está aprovado,

utilize a sua criativaidade e agrade o seu professor, com a melhor experiencia;

"""


def exec():
    print(f"{'_'*10}| Escola de Goias |{'_'*10}\n")
    nome_aluno = input("Digite o nome do aluno:\n")

    nota_um = float(input("Digite a nota 1:\n"))
    nota_dois = float(input("Digite a nota 2:\n"))
    nota_tres = float(input("Digite a nota 3:\n"))

    resultado = (nota_um + nota_dois + nota_tres)/3

    if resultado > 7:
        situacao = "APROVADO"
    elif resultado >= 5 and resultado <= 7:
        situacao = "RECUPERAÇÃO"
    else:
        situacao = "REPROVAÇÃO"
    print(f"{'_'*17}| NOTA DE ALUNO |{'_'*16}\n")
    # print(f"Aluno {nome_aluno}, \Situação: {situacao}, \nMédia das notas: {resultado}")
    print(" Aluno: {} \n Resultado: {} \n Média: {:0.2f}".format(
        nome_aluno, situacao, resultado))
    print(f"{'_'*50}\n")


if __name__ == "__main__":
    exec()
