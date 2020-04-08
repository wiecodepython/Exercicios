# Resolva a expressão
expressao = (100 - (413 * (20 - (5 * 4)))) / 5

print('O resultado da expressão é {}'.format(expressao))


# Enivaldo quer ligar três capacitores
c1 = 10
c2 = 22
c3 = 6.8

capacitanciaParalelo = c1 + c2 + c3
capacitanciaSerie = 1 / ((1 / c1) + (1 / c2) + (1 / c3))

print('Capacitância em série: %.1f uF' % capacitanciaSerie)
print('Capacitância em paralelo: %.1f uF' % capacitanciaParalelo)


# Você e os outros integrantes da sua república foram no supermercado e compraram alguns itens
cerveja = 75 * 2.20
macarrao = 2 * 8.73
molhoTomate = 1 * 3.45
cebola = 0.42 * 5.40
alho = 0.25 * 30
paoFrances = 0.45 * 25

precoTotal = cerveja + macarrao + molhoTomate + cebola + alho + paoFrances
totalParaCada = precoTotal / 5

print('Cada um terá que pagar R$%.2f' % totalParaCada)


# Krissia gosta de bolinhas de queijo
from math import pi

volumePoteDeSorvete = 15 * 10 * 13
raioBolinhaDeQueijo = 1.2
volumeBolinhoDeQueijo = (4 / 3) * pi * (raioBolinhaDeQueijo ** 3)

quatidadeBolinhasNoPote = (volumePoteDeSorvete / volumeBolinhoDeQueijo) * 0.74

print('A quantidade bolinhas de queijo que cabem no pote de sorvete é %.0f' % quatidadeBolinhasNoPote)