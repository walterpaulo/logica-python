"""
Aula 2

Leandro tem um posto de combustível e precisa encher o tanque
de combustível. Faça um programa que digite a quantidade de
litro do tanque de combustível e receba um valor para preencher
o tanque de combustivel deixando o mesmo cheio
e quando chegar um cliente colocar o combustível, depois
mostrar a quantidade de litros que ficou no tanque do posto

========== Sistema de combustível ===============
Digite a quantidade de litros padrão:

Digite a quantidade de litros para preencher a quantidade total:

A quantidade dque litros que ficou no posto foi: xxx

:::: Chegou um cliente, bora vender? :::::
Digite o nome do cliente:
Digite o valor que o senhor(a) xxx que deseja colocar:

::: Ficou com xxxx litros de um total de yyyy combustível no tanque do posto ::::


"""

print("========== Sistema de combustível ===============")
print("Digite a quantidade de litros padrão:")
litroPosto = input()
print("Digite a quantidade de litros para preencher a quantidade total:")
atualPosto = input()

print(f"A quantidade dque litros que ficou no posto foi: {atualPosto}")

print(f":::: Chegou um cliente, bora vender? :::::")
print(f"Digite o nome do cliente:")
nomeConsumidor = input()
print(f"Digite o valor que o senhor(a) {nomeConsumidor} que deseja colocar:")
abastecer = input()

resto = float(atualPosto) - float(abastecer)
print(
    f"::: Ficou com {resto} litros de um total de {atualPosto} combustível no tanque do posto ::::")