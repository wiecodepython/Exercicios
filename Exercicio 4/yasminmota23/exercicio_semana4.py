# <h2>Exercícios</h2>

#   1. Crie uma lista com o nome das 3 pessoas mais próximas.
nomes=["João","Maria","Carlos"]
print(nomes)

#   2. Crie três listas, uma lista de cada coisa a seguir:

frutas=["maçã","laranja","uva","mamão","banana","manga"]
docinhos_de_festa=["brigadeiro","beijinho","casadinho","alfajor","surpresa de uva","trufa"]
ingredientes_de_feijoada=["feijão preto","linguiça","costela de porco","alho","cebola","sal"]


# a. Agora crie uma lista que contém essas três listas.
listona=frutas+docinhos_de_festa+ingredientes_de_feijoada
print(listona)
#b. você consegue acessar o elemento brigadeiro?
print("brigadeiro" in listona)   # True -> brigadeiro está na listona
posicao=listona.index("brigadeiro")  # atribui a posição do elemento 'brigadeiro' no vetor listona à variável posicao
print(listona[posicao])
#c. Adicione mais brigadeiros à segunda lista de listona. O que aconteceu com a lista de docinhos de festa?
listona.insert(7,"brigadeiro1")
listona.insert(8,"brigadeiro2")
print(listona)
print(docinhos_de_festa) # a lista de docinhos de festa não foi alterada

#d. Adicione bebidas ao final da listona, mas sem criar uma lista!
listona.append("refrigerante")
listona.append("água")
listona.append("suco")
print(listona)

#   3. Utilizando o del, remova todos os elementos da lista criada anteriormente até a lista ficar vazia.
del listona[:]
print(listona)

#   4. Faça uma lista de compras do mês, não se esqueça de comprar produtos de limpeza e sorvete!<br/>
lista_de_compras=["sabão","desinfetante","bucha","bombril","macarrão","arroz","chocolate","feijão","sorvete de chocolate"]

#Agora «vá ao mercado» e delete apenas os produtos de limpeza da lista.<br/>
del lista_de_compras[0:4]
print(lista_de_compras)
#Agora «vá à sorveteria» e se empanturre de sorvete e tire o sorvete da lista.<br/>
del lista_de_compras[-1]
print(lista_de_compras)

#   5. Dado uma lista de números, faça com que os números sejam ordenados e, em seguida, inverta a ordem da lista usando slicing.
lista_numeros=[100,5,1,7,8,345,23,0]
lista_numeros.sort()  # lista ordenada
print(lista_numeros)
print(lista_numeros[::-1])  #lista invertida