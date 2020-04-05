from math import pi, pow

#1
print ((100-413*(20-5*4))/5)

#2
c1=10
c2=22
c3=6.8
cp=c1+c2+c3
cs=1/(1/c1+1/c2+1/c3)
print("Em paralelo a capacitância é:", cp, "µ")
print("Em série a capacitância é:", cs, "µ")
#3
lata_cerveja= 2.20*75
macarrao= 8.73*2
tomate= 3.45*1
cebola= 5.40/0.420
alho= 30/0.250
pao= 25/0.450
valor_total= lata_cerveja+macarrao+tomate+alho+cebola+pao
valor_individual= valor_total/4
print (valor_individual, "R$")

#4
volume_pote=15*10*13
volume_ocupado=volume_pote*0.74
volume_bola=3/4*(pi*pow(1.2,3))
quantidade_possivel=volume_ocupado//volume_bola
print(quantidade_possivel)
