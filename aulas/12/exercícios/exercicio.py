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

# from models.animal import Anima
from controllers.animais import Animais
from utils.utils import obtem_opcao_menu, limpar_tela


class Exercicio():
    def exec():
        limpar_tela()
        while True:
            print(f"{'-'*10}| Programa de Zoom |{'-'*10}")
            print("Escolhe uma opção:")
            print("1 - Cadastrar animal")
            print("2 - Listar animal")
            print("0 - sair")
            opcao_selecionado = obtem_opcao_menu(1, 2)

            if opcao_selecionado == 0:
                break
            elif opcao_selecionado == 1:
                limpar_tela()
                Animais.cadastro()
            elif opcao_selecionado == 2:
                limpar_tela()
                Animais.listar()

if __name__ == "__main__":
    Exercicio.exec()
