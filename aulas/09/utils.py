import importlib.util
import os
import sys
import time


def validar_number(numero):
    if not numero.isdigit():
        return numero
    else:
        return int(numero)

def limpar_tela():
    os.system("clear")


def importa_funcao(pasta, *arquivos):
    modulos = []
    for arquivo in arquivos:
        file_path = os.path.join(os.path.dirname(
            __file__), f"../{pasta}/{arquivo}")
        foo_spec = importlib.util.spec_from_file_location(pasta, file_path)
        foo_module = importlib.util.module_from_spec(foo_spec)
        sys.modules[pasta] = foo_module
        foo_spec.loader.exec_module(foo_module)
        modulos.append(sys.modules[pasta])
    for funcao in modulos:
        funcao.exec()


def tempo_espera_segundo(segundo):
    time.sleep(segundo)
