import math
# DESAFIOS EXERCÍCIO 2

# 1. Resolva a expressão

expressao = (100 - 413 * (20 - 5 * 4)) / 5
print("O valor da expressão é", expressao)

# 2. Capacitância
c1 = 10
c2 = 22
c3 = 6.8
paralelo = c1 + c2 + c3
serie = (c1 * c2 * c3) / (c2 * c3 + c1 * c3 + c1 * c2)
print("Capacitância em paralelo:", paralelo,"uF")
print("Capacitância em série:", serie,"uF")

# 3. Supermercado
pessoas = 4
compras = 75 * 2.20 + 2 * 8.73 + 1 * 3.45 + (5.40 * 420) / 1000 + (30 * 250) / 1000 + (25 * 450) / 1000
divisao = compras / pessoas
print(f"Cada pessoa deve contribuir com {float(divisao)} reais")

# 4. Bolinhas de queijo


x = 15
y = 10
z = 13
r = 1.2
vol_pote = x * y * z
fator=0.74*vol_pote
vol_queijo = (4 * math.pi * (r ** 3)) / 3
bolinhas=fator/vol_queijo
print(f"Cabem {int(bolinhas)} bolinhas de queijo no pote de sorverte")

