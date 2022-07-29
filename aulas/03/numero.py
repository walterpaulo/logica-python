inteiro = 1
resultado = 1 + inteiro


print("O resultado da operação foi", resultado)

"""
# Come
# Error, necessário colocar str para concatenar:
print("O resultado da operação foi"+ str(resultado))
"""

# Error ao somar número com string, necessário colocar int()
resultado2 = 1 + int("3")
print(resultado2)
