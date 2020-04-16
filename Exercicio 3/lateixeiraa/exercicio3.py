
#Exercicios da semana 3

print('Variáveis')
#print('Questão 1')

dolar= 3.25
real = dolar * 65
print(real)

#print('Questão 2')

p1 = 8.66
p2 = 5.35
p3 = 5
p4 = 1

ma =(p1 +p2 +p3 +p4)/4
mg = (p1 * p2 *p3 *p4 )**(1/4) 
mh = 4/ (1/p1 + 1/p2 + 1/p3 + 1/p4)

print('ma',ma)
print('mg', mg)
print('mh', mh)

#print('Questão 3')

celular = 299.99
chaleira = 23.87
gnomo = 66.66
adesivo = 6*1.42
frete = 12.34

compras = celular + gnomo + chaleira + adesivo
total = compras + frete

print('Total em dólares foi ',total)

dolar = 3.25
real = total * dolar 

iof = (real * 6.38) /100

pago = iof + real
print('Valor final é ',pago)
print('Foi pago de iof', iof)

print('String')

#print('Questão 1')

frase = 'Python é muito legal.'
palavra1 = frase[0:7]
print(palavra1)

palavra2 = frase[7:9]
print(palavra2)

palavra3 = frase[9:14]
print(palavra3)

palavra4 = frase[15:20]
print(palavra4)

#print('Questão 2 ')

print('frase =',len(frase))
print('palavra1 =',len(palavra1))
print('palavra2 =',len(palavra2))
print('palavra3 =',len(palavra3))
print('palavra4 =',len(palavra4))

#print('Questão 3')

print(frase[::-1])

print('Leitura do teclado')

#print('Questão 1')

nome = input ('Digite seu nome')
frase = 'Olá,{}'.format(nome)

#print('Questão 2')
nome2 = input('Digite outro nome')

frase2 = '{} roubou pão na casa de {}!'.format(nome,nome2)
frase3 = '{} ficou triste e com fome, porque o bandejão estava fechado'.format(nome2)


print(frase2)
print(frase3)

#print('Questão 3')

frase4 = input('Insira uma frase qualquer')

print(frase4[::-1])






