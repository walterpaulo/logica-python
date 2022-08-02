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
import importlib.util
import os
import sys
import time


def importa_funcao(pasta, *arquivos):
  modulos = []
  for arquivo in arquivos:
    file_path = os.path.join(os.path.dirname(__file__), f"../{pasta}/{arquivo}")
    foo_spec = importlib.util.spec_from_file_location(pasta, file_path)
    foo_module = importlib.util.module_from_spec(foo_spec)
    sys.modules[pasta] = foo_module
    foo_spec.loader.exec_module(foo_module)
    modulos.append(sys.modules[pasta])
  return modulos

def tempo_espera_segundo(segundo):
  time.sleep(segundo)

while True:
  print(f"{'_'*10}| Bem vindo ao programa {'_'*10}\n")
  print("Digite uma opção:\n")
  
  for i in range(1,9):
    print(f"{i} - Chama o exercicio do dia {i+1} ")
  print("10 - Sair do programa")

  opcao = int(input())

  if opcao == 10:
    break
  elif opcao == 1:
    funcoes = importa_funcao("02", "exercicio1.py")
    for funcao in funcoes:
      funcao.exec()
  elif opcao == 2:
    funcoes = importa_funcao("03", "exercicio1.py","exercicio3.py","exercicio3.py")
    for funcao in funcoes:
      funcao.exec()
  elif opcao == 3:
    funcoes = importa_funcao("04", "exercicio1.py")
    for funcao in funcoes:
      funcao.exec()
  elif opcao == 4:
    funcoes = importa_funcao("05", "exercicio1.py")
    for funcao in funcoes:
      funcao.exec()
  elif opcao == 5:
    funcoes = importa_funcao("06", "exercicio1.py","exercicio2.py","exercicio3.py")
    for funcao in funcoes:
      funcao.exec()
  elif opcao == 6:
    funcoes = importa_funcao("07", "exercicio1.py")
    for funcao in funcoes:
      funcao.exec()
  elif opcao == 7:
    funcoes = importa_funcao("08", "exercicio1.py")
    for funcao in funcoes:
      funcao.exec()
  elif opcao == 8:
    funcoes = importa_funcao("09", "exercicio1.py")
    for funcao in funcoes:
      funcao.exec()
  else:
    print(f"\n{'#'*30}\n#{' '*3}Opção [ {opcao} ] inválido!{' '*3}#\n{'#'*30}\n")
    tempo_espera_segundo(3)

# funcoes = importa_funcao("dia3", "exercicio1.py", "exercicio2.py", "exercicio3.py")
# for funcao in funcoes:
#   funcao.exec()