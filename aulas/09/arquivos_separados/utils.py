import os
import time

def limpar_tela():
  os.system("clear")

def espere_em_segundos(segundo):
  time.sleep(segundo)

def mostra_exercicio(dia):
  return f"Exercicio do dia {dia}"