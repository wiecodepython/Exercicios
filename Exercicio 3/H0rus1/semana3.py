#1
print('Questão 1')
cotacao = 3.25
real = 65.00
dolar = real/cotacao
print('\nO valor em dólares é:$',dolar)
#2
print('\nQuestão 2')
nota1, nota2, nota3, nota4 = 8.66,5.35,5.0,1.0
media_aritmetica= (nota1+nota2+nota3+nota4)/4
media_geometrica= (abs(nota1*nota2*nota3*nota4))**(1/4)
media_harmonica= 4/(1/nota1+1/nota2+1/nota3+1/nota4)
print('\nM.A:',media_aritmetica,'\nM.G:',media_geometrica,'\nM.H:',media_harmonica)
print('A maior média é: M.A({})'.format(media_aritmetica))
print('A menor média é: M.H({})'.format(media_harmonica))
#3
print('\nQuestão 3')
celular=299.99
chaleira=23.87
gnomo=66.66
adesivo=1.42
#3.a
print('a)')
total=celular+chaleira+gnomo+adesivo
print('O valor total da compra é:$',total)
#3.b
print('\nb)')
frete=12.34
iof=6.38/100
preco_final=(total+frete)*(1.0+iof)
print('O preço final é: $',preco_final)
#3.c
print('\nc)')
print('O valor pago em IOF é: $',preco_final*iof)
#string
print('Strings')
#1
print('\nQuestão 1')
frase = 'Python é muito legal.'
palavra1=frase[0:6]
palavra2=frase[7]
palavra3=frase[9:-7]
palavra4=frase[-6:-1]
print('palavra1:{} \npalavra2:{} \npalavra3:{} \npalavra4:{}'.format(palavra1,palavra2,palavra3,palavra4))
#2
print('\nQuestão 2')
print('O tamanho da frase é:',len(frase))
print('o tamanho da palavra 1 é:',len(palavra1))
print('o tamanho da palavra 2 é:',len(palavra2))
print('o tamanho da palavra 3 é:',len(palavra3))
print('o tamanho da palavra 4 é:',len(palavra4))
#3
print('\nQuestão 3')
frase_invertida=input('Digite sua frase:\n')
print('A frase invertida é:', frase_invertida[::-1])
