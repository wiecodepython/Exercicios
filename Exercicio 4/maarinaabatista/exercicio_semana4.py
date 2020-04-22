Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Exercicio semana 4
>>> #Q.1
>>> 
>>> pessoas_prox = ["Cleide", "Edmilson", "Johnatas"]
>>> print(pessoas_prox)
['Cleide', 'Edmilson', 'Johnatas']
>>> 
>>> #Q.2
>>> 
>>> frutas = ["Morango", "Uva", "Maçã", "Laranja"]
>>> docinhos = ["Brigadeiro","Beijinho", "Bem-Casado"]
>>> feijoada = ["Feijão preto","Alho", "Cebola", "Calabresa", "Porco","Carne seca"]
>>> listona = frutas + docinhos + feijoada
>>> print(listona)
['Morango', 'Uva', 'Maçã', 'Laranja', 'Brigadeiro', 'Beijinho', 'Bem-Casado', 'Feijão preto', 'Alho', 'Cebola', 'Calabresa', 'Porco', 'Carne seca']
>>> listona[4]
'Brigadeiro'
>>> #c
>>> listona.insert(4,"Brigadeiro2")
>>> print(listona)
['Morango', 'Uva', 'Maçã', 'Laranja', 'Brigadeiro2', 'Brigadeiro', 'Beijinho', 'Bem-Casado', 'Feijão preto', 'Alho', 'Cebola', 'Calabresa', 'Porco', 'Carne seca']
>>> print(docinhos)
['Brigadeiro', 'Beijinho', 'Bem-Casado']
>>> #a lista docinhos permaneceu inalterada.
>>> 
>>> #D
>>> listona.append("Suco")
>>> listona.append("Refrigerante")
>>> listona.append("Água")
>>> print(listona)
['Morango', 'Uva', 'Maçã', 'Laranja', 'Brigadeiro2', 'Brigadeiro', 'Beijinho', 'Bem-Casado', 'Feijão preto', 'Alho', 'Cebola', 'Calabresa', 'Porco', 'Carne seca', 'Suco', 'Refrigerante', 'Água']
>>> 
>>> #Q.3
>>> 
>>> len(listona)
17
>>> del listona[0:18]
>>> print(listona)
[]
>>> 
>>> #Q.4
>>> 
>>> compras = ["Arroz", "Feijão", "Carne", "Sabão", "Detergente", "Água Sanitária", "Sorvete", "Suco"]
>>> del compras[3:6]
>>> print(compras)
['Arroz', 'Feijão', 'Carne', 'Sorvete', 'Suco']
>>> del compras[3]
>>> print (compras)
['Arroz', 'Feijão', 'Carne', 'Suco']
>>> 
>>> #Q.5
>>> 
>>> numeros = [5,3,6,1,9,0,2,7,10,4,8]
>>> numeros.sort()
>>> print(numeros)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> len (numeros)
11
>>> print (numeros[::-1])
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> 
