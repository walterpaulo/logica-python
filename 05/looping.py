# https://www.w3schools.com/python/python_for_loops.asp
# https://www.w3schools.com/python/python_while_loops.asp


# Exemplos:

# Uso do While
print("Exemplo de while")
while True:
    numero = int(input("Digite 0 para sair\n"))
    print("Você digitou o número {numero}")
    if numero == 0:
        break
# Neste exemplo posso rodar em while ou for
i = 1
while i < 6:
  print(i)
  i += 1

# Utilizando o for para um range de número
print("Exemplo for")
inicial = int(input("Digite o número inicial\n"))
final = int(input("Digite o número final\n"))

for x in range(inicial, final+1):
  print(x)