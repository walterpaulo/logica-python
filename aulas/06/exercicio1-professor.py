print("================[Programa de calculo tabuada]======================\n")
# Exemplo 1 - Sem o loop, forma manual

numero = int(input("Digite um número\n"))
print(f"1 x {numero} = {numero*1}")
print(f"2 x {numero} = {numero*2}")
print(f"3 x {numero} = {numero*3}")
print(f"4 x {numero} = {numero*4}")
print(f"5 x {numero} = {numero*5}")
print(f"6 x {numero} = {numero*6}")
print(f"7 x {numero} = {numero*7}")
print(f"8 x {numero} = {numero*8}")
print(f"9 x {numero} = {numero*9}")
print(f"10 x {numero} = {numero*10}")

print("================[Programa de calculo tabuada - While ]======================\n")
# Exemplo 2 - usando o loop

i = 1
while i <= 10:
  print(f"{i} x {numero} = {i * numero}")
  i += 1


print("================[Programa de calculo tabuada - For ]======================\n")
# Exemplo 2 - usando o loop


for y in range(1, 11):
  print(f"{y} x {numero} = {y * numero}")
