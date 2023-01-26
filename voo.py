from aeroporto import Aeroporto
from aeroviario import Aeroviario



class Voo():

    def __init__(self, codigo, horario, data, aeroporto_partida: Aeroporto, aeroporto_destino: Aeroporto, tipo_voo: bool, assentos: int) -> None:
        self.__codigo = codigo
        self.__horario = horario
        self.__data = data
        self.__aeroporto_partida = aeroporto_partida
        self.__aeroporto_destino = aeroporto_destino
        self.__tripulacao = []
        self.__tipo_voo = tipo_voo
        self.__reservas = []
        self.__assentos = assentos
    
    '''getters'''
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def horario(self):
        return self.__horario
    
    @property
    def data(self):
        return self.__data
    
    @property
    def aeroporto_partida(self):
        return self.__aeroporto_partida
    
    @property
    def aeroporto_destino(self):
        return self.__aeroporto_destino
    
    @property
    def tripulacao(self):
        return self.__tripulacao
    
    @property
    def tipo_voo(self):
        return self.__tipo_voo
    
    @property
    def reservas(self):
        return self.__reservas
    
    @property
    def assentos(self):
        return self.__assentos

    '''setters'''

    @codigo.setter
    def codigo(self, novo_codigo):
        self.__codigo = novo_codigo

    @horario.setter
    def horario(self, novo_horario):
        self.__horario = novo_horario
    
    @data.setter
    def data(self, nova_data):
        self.__data = nova_data
    
    @aeroporto_destino.setter
    def aeroporto_destino(self, novo_aeroporto: Aeroporto):
        self.__aeroporto_destino = novo_aeroporto
    
    @aeroporto_partida.setter
    def aeroporto_partida(self, novo_aeroporto: Aeroporto):
        self.__aeroporto_partida = novo_aeroporto
    
    @tipo_voo.setter
    def tipo_voo(self, novo_tipo):
        self.__tipo_voo = novo_tipo
    
    @tripulacao.setter
    def tripulacao(self, novo_tripulante):
        self.__tripulacao = novo_tripulante

    @reservas.setter
    def reservas(self, nova_reserva):
        self.__reservas.append(nova_reserva)
    
    @assentos.setter
    def assentos(self, nova_capacidade):
        self.__assentos = nova_capacidade
        
    '''methods'''

    def assentos_livres(self):
        assentos_disponiveis = self.assentos - len(self.reservas)
        return f'Tem {assentos_disponiveis} assentos disponíveis.'

    def ver_tripulacao(self):
        print('Você está a bordo com a seguinte tripulação: ')
        for aeroviario in self.tripulacao:
            print(f'{self.tripulacao.nome} como {self.tripulacao.funcao}')

    def tripular(self, novo_tripulante):
        self.tripulacao.append(novo_tripulante)
    
    def ver_tripulacao(self):
        for x in range(len(self.tripulacao)):
            print(f'{self.tripulacao[x].nome}')

    
