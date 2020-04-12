#Desafio 1:
exp = 100-413*(20-(5*4))/5
print('O resultado da questão 1 do desafio é: {}'.format(exp))

#Desafio 2:
c1 = 10*1e-6
c2 = 22*1e-6
c3 = 6.8*1e-6
Cp = c1+c2+c3
x = (1/c1)+(1/c2)+(1/c3)
Cs = 1/x 
print('Caso sejam ligados em paralelo o valor será: {}. Caso sejam ligados em série o valor será: {}.'.format(Cp, Cs))

#Desafio 3:
total = (75*2.20) + (2*8.37) + 3.45 + (0.42*5.40) + (0.25*30) + (0.45*25)
tpc1 = total/5
print('Cada um teve que pagar {}'.format(tpc1))

#Desafio 4:
pot_sorv = (15*1e-3)*(10*1e-3)*13*1e-3
bol = (3/4)*(3.14*((1.2*1e-3)**3))
quantbol = pot_sorv//bol
quantextbol = quantbol*0.74
print('Ela poderá ter {:.0f}'.format(quantextbol))
