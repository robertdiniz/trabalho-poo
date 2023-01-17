from reserva import Reserva
from manuseia import Manuseia


class Operador(Manuseia):  
    

    def __init__(self) -> None:
        pass

    
    def criar_reserva(self, id, passageiro, *args, **kwargs):
        return Reserva(id, passageiro)


    def cancelar_reserva(reserva, voo):
        for reserva_atual in range(len(voo.reservas)):
            if reserva.id == voo.reservas[reserva_atual].id:
                del voo.reservas[reserva_atual]


