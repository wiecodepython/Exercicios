# Calcule o resto da divisão de 10 por 3
divisao10por3 = 10 % 3

print('A divisão de 10 por 3 é {}'.format(divisao10por3))


# Calcule a tabuada do 13
for i in range(1, 11):
    print('{} x {} = {}'.format(i, 13, i * 13))


# Davinir não gosta de ir às aulas. Mas ele é obrigado a comparecer a pelo menos 75% delas. Ele quer saber quantas aulas pode faltar, sabendo que tem duas aulas por semana, durante quatro meses. Ajude o Davinir!
meses = 4
semanas = meses * 4
aulas = semanas * 2

podeFaltar = aulas * 0.25

print('Davinir pode faltar %.0f aulas' % podeFaltar)


# Calcule a área de um círculo de raio r=2.
from math import pi

raio = 2
area = pi * (raio ** 2)

print('A área de um círculo com raio {} é {}'.format(raio, area))


# Se você correr 65 quilômetros em 3 horas, 23 minutos e 17 segundos, qual é a sua velocidade média em m/s?
horasEmSegundos = 3 * 3600
minutosEmSegundos = 23 * 60

tempoTotalEmSegundos = horasEmSegundos + minutosEmSegundos + 17
velocidadeMedia = (65 * 1000) / tempoTotalEmSegundos

print('A velocidade média é %.2f m/s' % velocidadeMedia)