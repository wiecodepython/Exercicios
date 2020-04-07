from math import pi, pow
"""
1. Resolva essa expressão:
(100 − 413 · (20 − 5 × 4))/5
"""
print("1. resolver a expressao")
print((100-413*(20-5*4))/5)

"""
Enivaldo quer ligar três capacitores, de valores:
C1 = 10 μF
C2 = 22 μF
C3 = 6.8 μF

Se ele ligar os três em paralelo, a capacitância resultante é a soma:
Cp = C1 + C2 + C3

Se ele ligar os três em série, a capacitância resultante é:
1/Cs = 1/C1 + 1/C2 + 1/C3

Ou seja:
1/Cs = 1/(1/C1 + 1/C2 + 1/C3)

Qual é o valor resultante em cada um desses casos?
"""
print('\n2. tres capacitores de Enivaldo')
c1 = 10e-6 # em F
c2 = 22e-6 # em F
c3 = 6.8e-6 # em F
print(f"Em paralelo: {format(c1 + c2 + c3, 'e')} F")
print(f"Em serie: {format(1/c1 + 1/c2 + 1/c3, 'e')} F")

"""
3. Você e os outros integrantes da sua república (Joca, Moacir,
Demival e Jackson) foram no supermercado e compraram alguns
itens:
    * 75 latas de cerveja: R$ 2,20 cada (da ruim ainda, pra fazer o
dinheiro render)
    * 2 pacotes de macarrão: R$ 8,73 cada
    * 1 pacote de Molho de tomate: R$ 3,45
    * 420g Cebola: R$ 5,40/kg
    * 250g de Alho: R$ 30/kg
    * 450g de pães franceses: R$ 25/kg

Calcule quanto ficou para cada um.
"""
print("\n3. supermercado com 3 amigos")
cerveja = 2.2
macarrao = 8.73
molho_tomate = 3.45
cebola = 5.40
alho = 30
pao = 25

total = 75 * cerveja + 2 * macarrao + molho_tomate + 0.42 * cebola + 0.25 * alho + 0.45 * pao
print(f"valor total: R${total}")
print(f"valor para cada pessoa: R${total/4}")

"""
4. Krissia gosta de bolinhas de queijo. Ela quer saber quantas
bolinhas de queijo dá para colocar dentro de um pote de sorvete
de 2L. Ela pensou assim:
Um pote de sorvete tem dimensões 15 cm x 10 cm x 13 cm. Uma bolinha
de queijo é uma esfera de raio r = 1.2 cm. O fator de empacotamento
ideal é 0.74, mas o pote de sorvete tem tamanho comparável às
bolinhas de queijo, aí tem efeitos de borda, então o fator deve ser
menor. Mas as bolinhas de queijo são razoavelmente elásticas, então
empacota mais. Esse valor parece razoável.
Sabendo que o volume de uma esfera de raio r é ​V = (4/3)*πr^3​, o volume do
pote de sorvete é V = x*y*z e o fator de empacotamento é a fração de
volume ocupado pelas bolinhas de queijo. Ou seja, 74% do pote de
sorvete vai ser ocupado pelas bolinhas de queijo. Ajude a Krissia
descobrir quantas bolinhas de queijo cabem no pote de sorvete!
"""
print("\n4. bolinhas de queijo no pote")
# dimensoes do pote em cm
pote_x = 15
pote_y = 10
pote_z = 13
# raio da bolinha de queijo em cm
bola_raio = 1.2

fator_empacotamento = 0.74 # adimensional

bola_volume = (4/3)*pi*pow(bola_raio,3) # em cm^3
pote_volume = pote_x*pote_y*pote_z # em cm^3

# 74% do volume total do pote
volume_ocupavel_pote = fator_empacotamento*pote_volume

# razao entre o volume ocupavel e o volume da bolinha
"""nao utilizei a divisao inteira devido o type retornar float em vez de int
ja que divisor e dividendo sao do tipo float
"""
bola_qtde = int(volume_ocupavel_pote/bola_volume)

print(f"volume de cada bolinha: {bola_volume} cm\u00b3")
print(f"volume calculado do pote: {pote_volume} cm\u00b3")
print(f"volume ocupavel do pote: {volume_ocupavel_pote} cm\u00b3")

print(f"quantidade de bolinhas de queijo que cabem no pote: {bola_qtde}")
