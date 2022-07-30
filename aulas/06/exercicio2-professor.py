print("================[Programa de calculo tabuada]======================\n")
# Exemplo 1 - Sem o loop, forma manual

numero = int(input("Digite um número\n"))
iterador = int(input("Digite o número do iterador"))
# if iterador == 1:
#   print(f"1 x {numero} = {numero*iterador}")
# elif iterador == 2:
#   print(f"2 x {numero} = {numero*iterador}")
# elif iterador == 3:
#   print(f"2 x {numero} = {numero*iterador}")
# .....
# forma errada!


print("================[Programa de calculo tabuada - While ]======================\n")
# Exemplo 2 - usando o loop

i = 1
while i <= iterador:
  print(f"{i} x {numero} = {i * numero}")
  i += 1


print("================[Programa de calculo tabuada - For ]======================\n")
# Exemplo 2 - usando o loop


for y in range(1, iterador):
  print(f"{y} x {numero} = {y * numero}")
