from enum import Enum


class AeroviarioFuncoes(Enum):

    Manutencao = 1
    Operador = 2
    Auxiliar = 3
    Geral = 4


class Aeroviario():

    def __init__(self, nome, funcao: AeroviarioFuncoes) -> None:
        self.__nome = nome
        self.__funcao = funcao
    
    '''getters'''
    @property
    def nome(self):
        return self.__nome
    
    @property
    def funcao(self):
        return self.__funcao
    
    '''setters'''
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
    
    @funcao.setter
    def funcao(self, nova_funcao):
        self.__funcao = nova_funcao
    
    