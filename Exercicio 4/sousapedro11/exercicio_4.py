"""
1. Crie uma lista com o nome das 3 pessoas mais próximas.
"""
print('Exercicio 4')
print('q1.')
lista_pessoas = ['Pedro', 'Alexandre', 'Luiza', 'Marta', 'Miguel', 'Claudia']
print(f'lista de pessoas = {lista_pessoas}')


"""
2. Crie três listas, uma lista de cada coisa a seguir:

   - frutas
   - docinhos de festa (não se esqueça de brigadeiros!!)
   - ingredientes de feijoada

Lembre-se de salvá-las em alguma variável!

    a. Agora crie uma lista que contém essas três listas.
    Nessa lista de listas (vou chamar de listona):
    b. você consegue acessar o elemento brigadeiro?
    c. Adicione mais brigadeiros à segunda lista de listona. O que aconteceu com a
lista de docinhos de festa?
    d. Adicione bebidas ao final da listona, mas sem criar uma lista!
"""

print('\nq2.')
lista_frutas = ['banana', 'maca', 'pera', 'uva', 'acai', 'tapereba', 'caju', 'tucuma']
lista_doces = ['brigadeiro', 'monteiro lopes', 'cajuzinho', 'uvinha', 'pacoca', 'coquinho']
lista_ingredientes_feijoada = ['feijao preto', 'costela de porco', 'paio', 'pe de porco', 'linguica', 'orelha de porco', 'lombo de porco']

print('\na.')
listona = []
listona.append(lista_frutas)
listona.append(lista_doces)
listona.append(lista_ingredientes_feijoada)

print(f'lista de frutas = {lista_frutas}')
print(f'lista de doces = {lista_doces}')
print(f'lista para feijoada = {lista_ingredientes_feijoada}')
print(f'listona = {listona}')

print('\nb.')
elemento = None
indice_listona = None
for x in listona:
	if 'brigadeiro' in x:
		elemento = 'brigadeiro'
		indice_listona = listona.index(x)
print(elemento)
#elemento = ('brigadeiro' if 'brigadeiro' in listona else None)
indice = (lista_doces.index('brigadeiro') if elemento else None)

#print(f'{elemento} esta no indice {indice} da listona')
print(indice)

"""
3. Utilizando o del, remova todos os elementos da lista criada anteriormente até a
lista ficar vazia.

4. Faça uma lista de compras do mês, não se esqueça de comprar produtos de limpeza e
sorvete!
Agora «vá ao mercado» e delete apenas os produtos de limpeza da lista.
Agora «vá à sorveteria» e se empanturre de sorvete e tire o sorvete da lista.

5. Dado uma lista de números, faça com que os números sejam ordenados e, em seguida, inverta a ordem da lista
usando slicing.
"""
