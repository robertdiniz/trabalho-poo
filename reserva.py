from passageiro import Passageiro

class Reserva():

    def __init__(self, id: int, passageiro = None):
        self.__id = id
        self.__passageiro = passageiro
        self.__situacao = False
    
    '''getters'''
    @property
    def id(self):
        return self.__id

    @property
    def passageiro(self):
        return self.__passageiro

    @property
    def situacao(self):
        return self.__situacao
    
    '''setters'''
    @passageiro.setter
    def passageiro(self, novo_passageiro):
        self.__passageiro = novo_passageiro
    
    @situacao.setter
    def situacao(self, nova_situacao):
        self.__situacao = nova_situacao

    @id.setter
    def id(self, nova_id):
        self.__id = nova_id
    
    def __str__(self) -> str:
        return self.__id