"""
Faca um programa para ter um menu onde
o usuário digitando:

1 = Execute a tabuada
2 = execute a tabuada com iterador
3 = saia do programa
"""
import time

import exercicio1
import exercicio2


def espere_em_segundos(segundo):
    time.sleep(segundo)


def exec():
    while True:
        print(f"{'_'*10}| Escolhe uma opção |{'_'*10}\n")
        print(f"{' '*11}[1] Execute a tabuada")
        print(f"{' '*11}[2] Execute a tabuada com iterador")
        print(f"{' '*11}[3] Sair")
        valor = int(input())

        if valor == 1:
            exercicio1.exec()
            espere_em_segundos(3)
        elif valor == 2:
            exercicio2.exec()
            espere_em_segundos(3)
        elif valor == 3:
            break


if __name__ == "__main__":
    exec()
