# print("-- Iteradora ---")
# lista = [2,6,7,8]

# for item in lista:
#   print(item)


# print("---- Iterável ----")

# print(hasattr(lista, "__iter__"))


# lista_iteravel = iter(lista)
# print(hasattr(lista_iteravel, "__next__"))
# print(f"lista_iteravel- {lista_iteravel}")
# print(next(lista_iteravel))

import time
import os
import sys

print("Segura processamento")
def gera_lista_dados():
  lista = []
  for n in range(5):
    lista.append(n)
    time.sleep(1)
  return lista

numeros = gera_lista_dados()
print(numeros)

##  Gerador, uso do yield
print("Não segura processamento")
def gera_lista_dados():
  lista = []
  for n in range(5):
    yield n
    time.sleep(1)
  return lista

# pegar o valor da lista
numeros = gera_lista_dados()
# 
for item in numeros:
  print(item)
print(numeros)

print("-----fim da ação ---------")
time.sleep(3)
os.system("clear")

## Navegando para o próximo item
print(next(numeros))
print(next(numeros))
print(next(numeros))

lista1 = [1 for i in range(1000)]
print(lista1)
# uso da mémoria
print(sys.getsizeof(lista1))


