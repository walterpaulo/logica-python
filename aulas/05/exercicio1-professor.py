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
print("============== [ Cálculo de média de alunos ] ==================")

nome = input("Digite o nome do aluno\n")

nota1 = float(input(f"Digite a nota 1 - {nome}\n"))
nota2 = float(input(f"Digite a nota 2 - {nome}\n"))
nota3 = float(input(f"Digite a nota 3 - {nome}\n"))

media = (nota1 + nota2 + nota3) / 3

if media < 5:
    resultado = "reprovado"
elif media >= 5 and media <= 7:
    resultado = "recuperação"
else:
    resultado = "Aprovado"

print("============== [ SITUAÇÃO ] ==================")

media_formatada = "{:0.2f}".format(media)

print(
    f"Situação do aluno {nome} é de {resultado}, pois sua média foi {media_formatada}\n")
