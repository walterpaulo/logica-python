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

print("====== Programa Calculo de Tabuada - Claudio ======\n")
numero = int(input("Digite um número para calcular a tabuada?\n"))
iterador = int(input(f"Quantas vezes deseja multiplicar o número {numero}?\n"))

os.system('clear')
print(f"==========[ Tabuada de {numero} ]==========")
i = 1
while i <= iterador:
  print(f" {numero} x {i} = {numero * i}") 
  i += 1