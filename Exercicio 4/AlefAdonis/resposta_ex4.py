#Questão 1:

pessoa_proximas = ['Emmily', 'Aarel', 'Carlos']

#Questão 2:

frutas = ['maça', 'abacate', 'laranja', 'melao', 'melancia']
docinhos = ['beijinho', 'brigadeiro', 'cajuzinho', 'bem-casado']
feijoada = ['feijao', 'linguiça', 'açafrao', 'toucinho']

##letra a:

listona = []
listona.extend(frutas)
listona.extend(docinhos)
listona.extend(feijoada)
print(listona)

##letra b:

print(docinhos[1])

##letra c:

listona.append('brigadeiro ')
print(docinhos)

##letra d:

listona.append('vodka')
listona.append('agua')

print(listona)
print('')
print('')
#Questão 3:

for el in listona:
    del(el)
print(listona)

#Questão 4:


#Questão 5:

lista_num = [1,4,6,2,5,5,67,8,54,211,12,345]
lista_num.sort()
print(lista_num)

print(lista_num[::-1])
