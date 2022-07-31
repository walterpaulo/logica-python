from itertools import count
from operator import le
import six
# mostra memória do computador
print(six.MAXSIZE)

# cria um array
b = ["a","b","c"]

# navegando por índice
b[0]
# retorna "a"

# nova array
cars = ["Ford", "Volvo", "BMW"]

# alterado o índice 1
cars[1] = 2.3

# adiciana novo item
cars.append("Mercedes")
cars.append("Honda")
cars.append("Fiat")
cars.append("Cherry")
cars.append("Key")

# retira o último índice e retorna uma string
car1 = cars.pop()

# tira um item da lista e adciona em uma variável
car2 = cars.pop(1)

# retirar um item pelo nome, sem retorno
car3 = cars.remove("Cherry") 

cars.copy()

# limpar array
# cars.clear()

# total de indice
print(f"Total: {len(cars)}")

cars.sort()

cars.reverse()

print(f"Total informado: {cars.count('Key')}")

cars.count("k")

for x in cars:
  print(f"O valor do array no seu índice é {x}")




