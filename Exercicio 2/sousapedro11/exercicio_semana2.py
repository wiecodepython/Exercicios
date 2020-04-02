from math import pi

"""
Python versao 3 foi utilizado.
Logo, se o interpretador for da versao 2 ocorrerao erros de sintaxe
"""
# 1. Faça todos os exemplos da apostila da "Semana #2".
print("1. exemplos da apostila")
print("estao no arquivo semana2.py")

# 2. Calcule o resto da divisão de 10 por 3.
print("\n2. resto da divisao entre 10 e 3")
print(10 % 3)
# 3. Calcule a tabuada do 13.
print("\n3. tabuada do 13")
print(*(f"{x} x 13 = {x*13}" for x in range(1, 11)), sep='\n')

# 4. Davinir não gosta de ir às aulas. Mas ele é obrigado a comparecer a pelo menos 75% delas. Ele quer saber quantas aulas pode faltar, sabendo que tem duas aulas por semana, durante quatro meses. Ajude o Davinir!
# Nota: Um mês tem quatro semanas.
print("\n4. frequencia de Davinir")
print('4.1. metodo passo a passo')
frequencia_percent = 0.75  # Logo, ele pode faltar 25% das aulas
aulas_semana = 2
periodo = 16  # 4 meses com 4 semanas cada, obviamente
# 2 aulas por semana num periodo de 16 semanas = 32 aulas
total_aulas = aulas_semana * periodo
# encontra os 25% de aulas = 32 * 0.25
frequencia_minima = total_aulas * (1-frequencia_percent)
print(
    f"Davinir pode faltar no maximo {int(frequencia_minima)} aulas sem reprovar.")

print("4.2. metodo direto")
print(
    f"Davinir pode faltar no maximo {int(2*16*(1-0.75))} aulas sem reprovar.")

# 5. Calcule a área de um círculo de raio r=2.
raio = 2
print(f"\n5. Area do circulo de raio 2")
print(pi*raio**2)

# 6. Se você correr 65 quilômetros em 3 horas, 23 minutos e 17 segundos, qual é a sua velocidade média em m/s?
distancia = 65000 # 65km em m
tempo = 3*3600 + 23*60 + 17 # 3h23min17s em s.
print("\n6. velocidade media")
# print(f"{distancia/tempo:.8f} m/s")
print(f"{distancia/tempo} m/s")