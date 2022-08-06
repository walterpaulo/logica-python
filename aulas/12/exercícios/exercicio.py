"""
Jardeclenio é um empresário dono de um Zoológico e precisa
de um programa para cadastrar os seus animais
Faça um programa que persista dos dados dos animais no disco

Exemplo do escopo da classe
Animal
  # propriedade
  - numero
  - nome
  - descricao

  # métodos
  - gravar()
  - buscar()
  - mostrar()
"""


from models.animal import Animal

# animal1 = Animal()
# animal1.nome = "Zebra"
# animal1.descricao = "Animal pintado"
# animal1.gravar()

# animais = Animal.buscar()
# for animal in animais:
#     print(f"{'=' * 30}")
#     print(f"codigo: {animal.codigo}")
#     print(f"Nome: {animal.nome}")
#     print(f"Descrição: {animal.descricao}")

# animal = Animal.buscar_por_codigo("7d273227-120e-4b00-b6a4-3d2792c9e657") # Não tem
animal = Animal.buscar_por_codigo(
    "22318d78-534b-4b02-bce1-453361668134")  # Tem
if animal != None:
    print(f"codigo: {animal.codigo}")
    print(f"Nome: {animal.nome}")
    print(f"Descrição: {animal.descricao}")
