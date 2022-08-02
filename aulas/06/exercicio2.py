"""
Claudio é um matemático que precisa de um programa para faiclitar
o caculo de uma tabuada, faça um programa que solicite um número multiplicador
e número do iterador. 
Crie a tabuada do mesmo, exemplo:

Digite um número para calcular a tabuada?
5

1 x 5 = 5
2 x 5 = 10
...
10 x 5 = 50

"""
import os
import exercicio1 as util

def exec():
  print(f"{'_'*10}| Tabuada de Multiplicação |{'_'*10}\n")
  numero = int(input("Digite o número da tabuada:\n"))
  iterador = int(input(f"Quantas vezes deseja multiplicar a tabuada de {numero}?\n"))

  os.system('clear')
  print(f"{'_'*10}| Tabuada de {numero} |{'_'*10}\n")
  i = 1
  while i <= iterador:
    print(f"{' '*12}{util.adiciona_zero(numero)} x {util.adiciona_zero(i)} = {numero * i}") 
    i += 1
  print('_'*37)

if __name__ == "__main__":
    exec()