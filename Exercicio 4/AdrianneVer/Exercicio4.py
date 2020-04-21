#-------------Exercício 04 ------------------#
#_________Lista______________________________#

#1.	Crie uma lista com o nome das 3 pessoas mais próximas
lista = ["Ryan", "Adrielle", " Socorro"]

print("Os nomes da lista são:", lista)

#2.	Crie três listas, uma lista de cada coisa a seguir:
#frutas

frutas = [ "Morango" , " Uva", " Melancia"]

#o	docinhos de festa (não esqueça de brigadeiros !!)

docinhos = ["Brigadeiro", "Beijinho", "Uvinha"]

#o	ingredientes de feijoada

feijoada = ["Feijão", "bacon", "Calabresa"]

#Criar uma lista da lista

listona = [frutas, docinhos, feijoada]
print(listona[1][0])

#adicionar mais brigadeiro
listona[1].append("Brigadeiro")
print(listona)

#d. Adicione bebidas ao final da listona, mas sem criar uma lista!
listona.append("Bebidas")
print(listona)

#3.	Utilizando ou excluindo, remova todos os elementos da lista criada anteriormente até a lista ficar vazia.
del listona[3]
print(listona)

del listona[2]
print(listona)

del listona[1]
print(listona)

del listona[0]
print(listona)

#4.	Faça uma lista de compras do mês, não se esqueça de comprar produtos de limpeza e sorvete!

compras = ["Sabão", "Detergente", "Arroz", "Soverte"]

#Agora «vá ao mercado» e delete apenas os produtos de limpeza da lista
del compras[0]
print(compras)

del compras[0]
print(compras)

#Agora «vá à sorveteria» e se empanturre de sorvete e tire o sorvete da lista.
del compras[1]
print(compras)

#5.	Dado uma lista de números, faça com que os números sejam ordenados
# e, em seguida, inverta a ordem da lista usando slicing.

#ordenados
numeros = [ 1, 8, 7, 5 ]
numeros.sort()
print(numeros)

#inverta
numeros.sort(reverse=True)
print(numeros)



