

class Passageiro():

    def __init__(self, nome: str, cpf: str, email: str, idade: int) -> None:
        self.__nome = nome
        self.__cpf = cpf
        self.__reserva = None
        self.__email = email
        self.__idade = idade
    

    '''getters'''
    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def reserva(self):
        return self.__reserva

    @property
    def email(self):
        return self.__email

    @property
    def idade(self):
        return self.__idade
    
    '''setters'''

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @cpf.setter
    def cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    @reserva.setter
    def reserva(self, nova_reserva):
        self.__reserva = nova_reserva

    @email.setter
    def email(self, novo_email):
        self.__email = novo_email

    @idade.setter
    def idade(self, nova_idade):
        self.__idade = nova_idade
    
    '''methods'''

    def criar_reserva(self, id, passageiro, operador, *args, **kwargs):
        return operador.criar_reserva(id, passageiro, *args, **kwargs)
    
    
    def pagar_reserva(self, voo, reserva):
        if reserva.situacao == True:
            return f'Esta reserva já foi paga.'
        else:
            reserva.situacao = True
            voo.reservas.append(reserva)
            return f'Reserva paga por {self.nome}.'

    
    def cancelar_reserva(self, voo, reserva):
        for reserva_atual in range(len(voo.reservas)):
            if reserva.id == voo.reservas[reserva_atual].id:
                del voo.reservas[reserva_atual]
            
    