#1
print('Questão 1\n')
pessoas_proximas=['Amanda', 'Manoel','Gabriel']
print(pessoas_proximas)
#2
print('\nQuestão 2')
frutas=['uva','pera','melancia']
docinhos_de_festa=['brigadeiro','beijinho','casadinho']
ingredientes_de_feijoada=['bacon','alho','feijão preto']
print('Lista 1:{}\nLista 2:{}\nLista 3:{}'.format(frutas,docinhos_de_festa,ingredientes_de_feijoada))
#2.a
print('\na)')
listona= frutas+docinhos_de_festa+ingredientes_de_feijoada
#2.b
print('\nb)')
print(listona[3])
#2.c
print('\nc)')
listona.insert(3,'brigadeiro')
print('A lista de docinhos de festa ficou:',docinhos_de_festa,'\nPortanto não mudou.')
#2.d
print('\nd)')
listona.append('bebidas')
print(listona)
#3
print('\nQuestão 3')
del listona[0:11]
print('A listona ficou:',listona)
#4
print('\nQuestão 4')
compras=['carne','sabonete','detergente','desodorante','sorvete','biscoito','frutas','arroz','feijão']
print(compras)
del compras[1:4]
print(compras)
del compras[1]
print(compras)
#5
print('\nQuestão 5')
numeros=[1,4,235,6,12,3421,4,12,412,4]
print(numeros)
numeros.sort()
print(numeros)
print(numeros[::-1])
