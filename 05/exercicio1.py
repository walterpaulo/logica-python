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

print("========== Escola de Goias ==========")
nome_aluno = input("Digite o nome do aluno\n")

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
print("\nRESULTADO\n")
# print(f"Aluno {nome_aluno}, \Situação: {situacao}, \nMédia das notas: {resultado}")
print("Aluno {} \nSituação: {} \nMédia das notas: {:0.2f}".format(nome_aluno, situacao, resultado))
