Python 3.7.5 (default, Nov 20 2019, 09:21:52) 
[GCC 9.2.1 20191008] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>>
>>> # Exercício 4
>>> 
>>> #1
>>> proximos = ["Naza","Heliana","Dani"]
>>> print (proximos)
['Naza', 'Heliana', 'Dani']
>>> 
>>> 
>>> #2
>>> frutas = ["abacaxi","maçã","banana","uva","goiaba","maracujá"]
>>> doce_festa = ["brigadeiro","beijinho","olho de sogra","casadinho","cajuzinho","quindim"]
>>> feijoada = ["feijão preto","linguiça","bacon","charque","sal","louro","água"]
>>> itens = frutas + doce_festa + feijoada
>>>
>>> #acessando brigadeiro
>>> "brigadeiro" in itens
True
>>> itens.index("brigadeiro")
6
>>> print(itens[6])
brigadeiro
>>>
>>> #adicionando brigadeiros a lista de doces da lista itens
>>> print(itens)
['abacaxi', 'maçã', 'banana', 'uva', 'goiaba', 'maracujá', 'brigadeiro', 'beijinho', 'olho de sogra', 'casadinho', 'cajuzinho', 'quindim', 'feijão preto', 'linguiça', 'bacon', 'charque', 'sal', 'louro', 'água']
>>>
>>> itens.insert(7,"brigadeiro de limão")
>>> itens.insert(8,"brigadeiro de caipirinha")
>>> doce_festa
['brigadeiro', 'beijinho', 'olho de sogra', 'casadinho', 'cajuzinho', 'quindim']
>>> #não mudou a lista doce_festa pois itens não foi criado somente a partir dela
>>> itens
['abacaxi', 'maçã', 'banana', 'uva', 'goiaba', 'maracujá', 'brigadeiro', 'brigadeiro de limão', 'brigadeiro de caipirinha', 'beijinho', 'olho de sogra', 'casadinho', 'cajuzinho', 'quindim', 'feijão preto', 'linguiça', 'bacon', 'charque', 'sal', 'louro', 'água']
>>> 
>>> #adicionando bebidas na lista itens
>>> itens.append("suco")
>>> itens.append("refrigerante")
>>> itens.append("cerveja")
>>> itens.append("vodka")
>>> itens
['abacaxi', 'maçã', 'banana', 'uva', 'goiaba', 'maracujá', 'brigadeiro', 'brigadeiro de limão', 'brigadeiro de caipirinha', 'beijinho', 'olho de sogra', 'casadinho', 'cajuzinho', 'quindim', 'feijão preto', 'linguiça', 'bacon', 'charque', 'sal', 'louro', 'água', 'suco', 'refrigerante', 'cerveja', 'vodka']
>>> 
>>>
>>> #3
>>> del itens[:]
>>> itens
[]
>>> 
>>> 
>>> #4
>>> compras = ["arroz","feijão","carne","frango","manteiga","detergente","quiboa","amaciante","sabão","sorvete","lenços","desodorante"]
>>>
>>> #excluindo os itens de limpeza
>>> del compras[5:9]
>>> compras
['arroz', 'feijão', 'carne', 'frango', 'manteiga', 'sorvete', 'lenços', 'desodorante']
>>>
>>> #excluindo sorvete da lista
>>> compras.index("sorvete")
5
>>> del compras[5]
>>> compras
['arroz', 'feijão', 'carne', 'frango', 'manteiga', 'lenços', 'desodorante']
>>> 
>>> 
>>> #5
>>> num = [1,3,2,7,4,5,6,9,8]
>>>
>>> #ordenando a lista 
>>> num.sort()
>>> num
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
>>> #invertendo a lista
>>> num = num[::-1]
>>> num
[9, 8, 7, 6, 5, 4, 3, 2, 1]
>>>
>>> #fim 
