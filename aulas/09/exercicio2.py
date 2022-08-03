"""
O professor Danilo, necessita organizar os exercicios passados no desafio de python,
com isso deseja que seus alunos faça uma porgram utilizando
funções para organizar todos os exercícios passados em um menu.
Ou seja, crie uma programa que  organize os exercício em funções
dos dias 2,3,4,5,6,7,8
e acesse o exercício através de uma organização em menu

neste exercicio quero que vcs chamem os squivos origiinas depois
de ser refatorado em funções


"""

from utils import validar_number, importa_funcao, tempo_espera_segundo


def menu():
    for i in range(1, 9):
        print(f"{i} - Chama o exercicio do dia {i+1} ")
    print("10 - Sair do programa")


def message_menu_erro(opcao=''):
    print(
        f"\n{'#'*35}\n{' '*3}Opção [ {opcao} ] inválido!\n{'#'*35}\n")
    tempo_espera_segundo(3)


def exec():
    while True:
        print(f"{'_'*10}| Bem vindo ao programa |{'_'*10}\n")
        print("Digite uma opção:\n")

        menu()
        numero = input('$> ')
        opcao = validar_number(numero)

        if opcao == 10:
            break
        elif opcao == 1:
            importa_funcao("02", "exercicio1.py")
            tempo_espera_segundo(3)
        elif opcao == 2:
            importa_funcao("03", "exercicio1.py",
                           "exercicio3.py", "exercicio3.py")
            tempo_espera_segundo(3)
        elif opcao == 3:
            importa_funcao("04", "exercicio1.py")
            tempo_espera_segundo(3)
        elif opcao == 4:
            importa_funcao("05", "exercicio1.py")
            tempo_espera_segundo(3)
        elif opcao == 5:
            importa_funcao("06", "exercicio1.py",
                           "exercicio3.py", "exercicio3.py")
            tempo_espera_segundo(3)
        elif opcao == 6:
            importa_funcao("07", "exercicio1.py")
            tempo_espera_segundo(3)
        elif opcao == 7:
            importa_funcao("08", "exercicio1.py")
            tempo_espera_segundo(3)
        elif opcao == 8:
            importa_funcao("09", "exercicio1.py")
            tempo_espera_segundo(3)
        else:
            message_menu_erro(opcao)


if __name__ == "__main__":
    exec()
