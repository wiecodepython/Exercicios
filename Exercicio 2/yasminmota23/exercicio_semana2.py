# EXERCÍCIO 2

# 2. Calcule o resto da divisão de 10 por 3.
print("O resto da divisão de 10 por 3 é",10%3,"\n")

# 3.Calcule a tabuada do 13.
print("Tabuada do 13\n")
for i in range(11): print(i,"x 13 =",i*13)

# 4. Davinir não gosta de ir às aulas. Mas ele é obrigado a comparecer a pelo menos 75% delas.
#Ele quer saber quantas aulas pode faltar, sabendo que tem duas aulas por semana, durante quatro meses. Ajude o Davinir!

aula_semana = 2
aula_total= aula_semana*4*4
faltar = 0.25*aula_total
print(f"\nDavinir pode faltar {int(faltar)} aulas","\n")

# 5.Calcule a área de um círculo de raio r=2.
import math
raio=2
area=math.pi*(raio**2)
print("A área do círculo é",area,"\n")

# 6.Se você correr 65 quilômetros em 3 horas, 23 minutos e 17 segundos, qual é a sua velocidade média em m/s?
distancia_metros= 65*1000
tempo_segundos= 3*60*60 + 23*60 +17
media=distancia_metros/tempo_segundos
print("A velocidade média é", media,"m/s")
