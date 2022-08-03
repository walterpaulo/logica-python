from asyncio import constants
from collections import namedtuple

Constants = namedtuple('Constants', ['NOME','TIPO'])

constants = Constants("desafio de Python", "Treinamento")


# constants.e = 1
print(constants.NOME)
print(constants.TIPO)