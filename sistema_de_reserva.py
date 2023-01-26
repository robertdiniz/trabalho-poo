from aeroporto import Aeroporto
from aeroviario import Aeroviario, AeroviarioFuncoes
from operador import Operador
from passageiro import Passageiro
from voo import Voo




aeroporto = Aeroporto('Bom Sucesso', 10, 'Xan Gay')
aeroporto2 = Aeroporto('Alexandria', 5, 'Moscou')

aeroviario1 = Aeroviario('Raali', AeroviarioFuncoes(1))
aeroviario2 = Aeroviario('Rafui', AeroviarioFuncoes(2))
aeroviario3 = Aeroviario('Rávou', AeroviarioFuncoes(3))

voo = Voo(123, '15:15', '11/09/2001', aeroporto, aeroporto2, True, 30)

voo.tripular(aeroviario1)
voo.tripular(aeroviario2)
voo.tripular(aeroviario3)

print(f'Neste voo temos {len(voo.tripulacao)} aeroviários:')
voo.ver_tripulacao()

print(voo.assentos_livres())

passageiro = Passageiro('Kaguay Nopano', '1232321231', 'kaguey@gmail.com', 20)
operador = Operador()
reserva = operador.criar_reserva(1, passageiro)
reserva2 = passageiro.criar_reserva(2, passageiro, operador)

#pagando reserva
print(passageiro.pagar_reserva(voo, reserva))
print(passageiro.pagar_reserva(voo, reserva2))

print(f'Atualmente este voo tem {len(voo.reservas)} passagens reservadas.', )
print(voo.assentos_livres())

passageiro.cancelar_reserva(voo, reserva2)

print(f'Atualmente este voo tem {len(voo.reservas)} passagens reservadas.', )
print(voo.assentos_livres())


operador.cancelar_reserva(voo, reserva)

print(f'Atualmente este voo tem {len(voo.reservas)} passagens reservadas.', )
print(voo.assentos_livres())
