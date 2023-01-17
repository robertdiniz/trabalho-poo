from abc import ABC, abstractmethod


class Manuseia(ABC):

    @abstractmethod
    def criar_reserva():
        pass

    @abstractmethod
    def cancelar_reserva():
        pass
