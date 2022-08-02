# Dados que o prfessor Danilo, precise algumas informações
# importante na tela, faça um programa que capture estas informações
# e mostre na tela na forma organizada, exemplo de organização:
# ========== Programa de formatação de dados ==============
# Nome: XXXXXX
# Telefone: XXXXXXX
# Endereço: XXXXXXX
# =========================================================
import os


def exec():
    print(f"{'_'*10}| Bem vindo ao sistema de cadastro |{'_'*10}\n")
    print("Digite o seu nome:")
    nome = input()
    print("Digite o seu telefone:")
    telefone = input()
    print("Digite o seu endereço:")
    endereco = input()

    os.system('clear')
    print(f"{'_'*10}| Programa de formatação de dados |{'_'*10}\n")
    print("Nome: " + nome)
    print("Telefone: " + telefone)
    print("Endereço: " + endereco)
    print('_'*55)


if __name__ == "__main__":
    exec()
