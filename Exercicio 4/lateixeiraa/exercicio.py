
# exercicios da semana 4

# Questão 1.

pessoas_proximas = ["marina", "daniel","rejane"]

# Questão 2.

frutas = ["laranja","jaca","abacate","maracujá","banana"]
docinhos = ["brigadeiro","beijinho","surpresinha de uva ","bem casado"]
feijoada = ["feijão preto","linguiça","bacon","carne","sal"]  

listona = [frutas , docinhos , feijoada ]

print(listona)

#acessar o item brigdeiro

print(docinhos[0])

#adicionando brigadeiros

listona[1].append("brigadeiro")

print(listona)
print(docinhos)

#adicionando bebidas ao final de listona

listona.append("bebidas")

# Questão 3.

del listona[0]
del listona[1]
del listona[-2]
del listona[-1]

print(listona)

# Questão 4.

compras = [frutas,"macarrão",feijoada , "arroz","bebidas","limpeza","sorvete"]
print(compras)

del compras[-2]
print(compras)

del compras[-1]
print(compras)

#Questão 5.

numeros = [5,4,1,8,3,0,2,9,7,6]

numeros.sort()
print(numeros)

slice(numeros)
print(numeros)


















