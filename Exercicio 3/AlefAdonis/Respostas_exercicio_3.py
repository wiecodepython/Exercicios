#Questão 1:

dolar = 3.25
print('R$ {}'.format(65.00/3.25))

#Questão 2:

prova1 = 8.66
prova2 = 5.35
prova3 = 5
prova4 = 1

MedA = (prova1+prova2+prova3+prova4)/4
MedG = (abs(prova1*prova2*prova3*prova4))**(1/4)
MedH = 4/((1/prova1)+(1/prova2)+(1/prova3)+(1/prova4))

print('A maior nota se dará através da Média Arimetica que dará: {:.2f}.\nEntretanto, a menor nota será dada através da Média Harmonica: {:.2f}'.format(MedA, MedH))

#Questão 4:

cel = 299.99
cha = 23.87
gno = 66.66
uni = 1.42
frete = 12.34
total = cel+cha+gno+(6*uni)+frete
print('O valor total será USD{}.'.format(total)) #Letra A
tarifa = (6.38/100)*(total*dolar)
total_final = (total*dolar)+tarifa
print('O valor total será R${:.2f}.'.format(total_final)) #LetraB
print('O IOF foi {:.2f}'.format(tarifa))

##Questões sobre strings:
print('')
print('')
#Questão 1:

frase = 'Python é muito legal'

palavra1 = frase[0:6]
palavra2 = frase[7]
palavra3 = frase[9:14]
palavra4 = frase[15:20]

print(palavra1)
print(palavra2)
print(palavra3)
print(palavra4)

#Questão 2:

print(len(frase), len(palavra1), len(palavra2), len(palavra3), len(palavra4))

#Questão 3:

nova_palavra1 = palavra1[::-1]
print(nova_palavra1)

##Questões de Leitura de Teclado:
print('')
print('')
#Questão 1:

nome = input('Qual seu nome? ')

print('Olá',nome+'!')

#Questão 2:

nome2 = input('Preciso de mais um nome: ')
print('{} roubou pão da casa do {}!\n{} ficou triste e com fome,\nporque o bandejão estava fechado'.format(nome,nome2,nome2))

#Questão 3:

entrada = input('Digite algo: ')
saida = entrada[::-1]
print(saida)


