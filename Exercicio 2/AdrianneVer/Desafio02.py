
#-----------------Desafio ----------------------#
from math import pi

#1. Resolva essa expressão:
#(100 - 413 · (20 - 5 × 4)) / 5
resultado = ((100 - 413 * (20 - 5 * 4)) / 5)
print(resultado)

# 2. Enivaldo quer ligar três capacitores, valores:
# C1 = 10 μF
# C2 = 22 μF
# C3 = 6,8 μF

#Se ele ligar três paralelos, uma capacitância reduzida é um soma:
#Cp = C1 + C2 + C3
#Se ele ligar três séries, uma capacitância reduzida é:
#1 / Cs = 1 / C1 + 1 / C2 + 1 / C3
#Ou seja:
#1 / Cs = 1 / (1 / C1 + 1 / C2 + 1 / C3)
#Qual é o valor necessário em cada um desses casos?

# Três capacitores de Enivaldo
c1 = 10
c2 = 22
c3 = 6.8

capacitancia_paralelo = c1  + c2 + c3
capacitancia_serie = 1 / ((1 / c1 + 1 / c2  + 1 / c3))

print("A capacitância parelelo é: ", capacitancia_paralelo)
print("A capacitância serie é: ", capacitancia_serie)

#3. Você e os outros integrantes da sua república (Joca, Moacir,
#Demival e Jackson) foram no supermercado e compraram alguns
#itens:
#75 latas de cerveja: R$ 2,20 cada (da ruim ainda, pra fazer o dinheiro render)
#2 pacotes de macarrão: R$ 8,73 cada
#1 pacote de Molho de tomate: R$ 3,45
#420g Cebola: R$ 5,40/kg
#250g de Alho: R$ 30/kg
#450g de pães franceses: R$ 25/kg

#Calcule quanto ficou para cada um.

cerveja = 75 * 2.20
macarrao = 2 * 8.73
molho_tomate = 1 * 3.45
cebola =  0.42 * 5.40
alho = 0.25 * 30
pao_franceses = 0.45 * 25

preco_total = cerveja + macarrao + molho_tomate + cebola + alho + pao_franceses
total_cada = preco_total / 5
print( "Cada um terá que pagar: ", total_cada )

#4. Krissia gosta de bolinhas de queijo. Ela quer saber quantas
#bolinhas de queijo dá para colocar dentro de um pote de sorvete
#de 2𝐿. Ela pensou assim:
volume_pote = 15 * 10 * 13
esfera_raio = 1.2

volume_esferaRaio = (4/3) * pi * esfera_raio ** 3
quantidade_bolinhas =  (volume_pote / volume_esferaRaio) * 0.74

print("Quantidade de bolinhas de queijo cabem no pote de sorvete é:", quantidade_bolinhas)

