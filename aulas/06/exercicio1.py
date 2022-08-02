"""
Claudio é um matemático que precisa de um programa para faiclitar
o caculo de uma tabuada, faça um programa que solicite um número
e crie a tabuada do mesmo, exemplo:

Digite um número para calcular a tabuada?
5

1 x 5 = 5
2 x 5 = 10
...
10 x 5 = 50

"""
import os

def adiciona_zero(numero):
  if numero < 10:
    return f"0{numero}"
  else:
    return numero

def exec():
    print(f"{'_'*10}| Tabuada de Multiplicação |{'_'*10}\n")
    numero = int(input("Digite um número para calcular a tabuada:\n"))

    os.system('clear')
    print(f"{'_'*10}| Tabuada de {numero} |{'_'*10}\n")
    i = 1
    while i <= 10:
        print(f"{' '*12}{adiciona_zero(numero)} x {adiciona_zero(i)} = {adiciona_zero(numero * i)}")
        i += 1
    print(f"{'_'*35}\n")


if __name__ == "__main__":
    exec()
