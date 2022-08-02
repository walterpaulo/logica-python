"""
Faça um programa para calcular números
solicite que o seu usuário digite 4 números
faça a soma do primeiro número, com o último número
depois faça a multiplicação com os números do meio
ao final some o resultado da soma com o resultado da multiplicação

se o resultado total for > do que 100 mostrar

=========================
O resultado alcançado foi xxx parabéns
=========================

se o resutaldo total for <= do que  100 mostrar

=========================
O resultado alcançado foi xxx e ficou abaixo da expectativa
=========================

"""


def exec():
    print(f"{'_'*10}| Programa para calcular número |{'_'*10}\n")

    print("Digite o número 1")
    numero_um = int(input())

    print("Digite o número 2")
    numero_dois = int(input())
    print("Digite o número 3")
    numero_tres = int(input())
    print("Digite o número 4")
    numero_quatro = int(input())

    somar_primeiro_ultimo = numero_um + numero_quatro
    multiplicacao_numero_meio = numero_dois * numero_tres

    somar_resultados = somar_primeiro_ultimo + multiplicacao_numero_meio

    if somar_resultados > 100:
        print(f"\n{'#'*43}\n#{' '*41}#")
        print(f"# O resultado alcançado foi {somar_resultados} parabéns #")
        print(f"#{' '*41}#\n{'#'*43}")
    else:
        print(f"\n{'#'*62}\n#{' '*60}#")
        print(
            f"# O resultado alcançado foi {somar_resultados} e ficou abaixo da expectativa #")
        print(f"#{' '*60}#\n{'#'*62}")
    print('_'*53)


if __name__ == "__main__":
    exec()
