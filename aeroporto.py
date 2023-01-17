class Aeroporto():


    def __init__(self, cidade: str, capacidade: int, nome: str) -> None:
        self.__cidade = cidade
        self.__capacidade = capacidade
        self.__nome = nome

    '''getters'''

    @property
    def cidade(self):
        return self.__cidade
    
    @property
    def capacidade(self):
        return self.__capacidade
    
    @property
    def nome(self):
        return self.__nome
    
    '''setters'''

    @cidade.setter
    def cidade(self, nova_cidade):
        self.__cidade = nova_cidade
    
    @capacidade.setter
    def capacidade(self, nova_capacidade):
        self.__capacidade = nova_capacidade
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
    
    
