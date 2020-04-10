#-------------Exercício 02 ------------------#
from math import pi

#1.	Faça todos os exemplos da apostila da "Semana # 2".
# Está no arquivo "Exercícios_Apostila"

# 2. Calcule o restante da divisão de 10 por 3.
print(10 % 3)

# 3. Calcule uma tabuada do 13.
for i in range(1,11):
    print( i, "x", 13,"=", i * 13)

# # 4. Davinir não gosta de ir às aulas. Mas ele é obrigado a comparar pelo menos 75% deles.
# Ele quer saber quantas aulas podem faltar, saber que tem duas aulas por semana, durante quatro meses. Ajude o Davinir!
# # Nota: Um mês tem quatro semanas
meses = 4
semanas = meses * 4
aulas = 2

total_aulas = aulas * semanas
total_faltas = total_aulas * 0.25

print("Davinir pode faltar: ", total_faltas)


# 5. Calcule uma área de um círculo de raio r = 2.
raio = 2 # Lendo o valor do raio da circunferência.
area = pi * raio ** 2  #Calculando e armazenando a área
print("A área do círculo é:", area)  # Mostrando para o usuário a área calculado

# 6. Se você correr 65 milhas em 3 horas, 23 minutos e 17 segundos, qual é a sua velocidade média em m / s?
distancia_metros = 65 * 1600
horas_segundos = 3 * 3600
minutos_segundos = 23 * 60

total_segundos = horas_segundos + minutos_segundos + 17
velocidade_media = distancia_metros / total_segundos

print(" A velocidade média é: ", velocidade_media)

