Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Exercicio semana 3
>>> #Q.1
>>> cotacao = 3.25
>>> cambio = 65 / cotacao
>>> print('Com R$ 65,00 reais você terá ${} dólares' .format(cambio))
Com R$ 65,00 reais você terá $20.0 dólares
>>> 
>>> #Q.2
>>> p1, p2 , p3 , p4 = 8.66 , 5.35 , 5 , 1
>>> print(p1,p2,p3,p4)
8.66 5.35 5 1
>>> #media aritmética
>>> ma = (p1+p2+p3+p4)/4
>>> import math
>>> mg = 500 ** (1/4)
>>> print (mg)
4.728708045015879
>>> #teste
>>> mg = (p1 * p2 * p3 * p4) ** (1/4)
>>> mh = (4/(1/p1 + 1/p2 + 1/p3 + 1/p4))
>>> print(ma , mg , mh)
5.0024999999999995 3.901309628628489 2.662425726074314
>>> print(' A maior média para Rondinelly será a da média aritmética {} e a menor média será a média harmônica {]' .format(ma,mh))
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(' A maior média para Rondinelly será a da média aritmética {} e a menor média será a média harmônica {]' .format(ma,mh))
ValueError: expected '}' before end of string
>>> print(' A maior média para Rondinelly será a da média aritmética {} e a menor média será a média harmônica {}' .format(ma,mh))
 A maior média para Rondinelly será a da média aritmética 5.0024999999999995 e a menor média será a média harmônica 2.662425726074314
>>> A maior média para Rondinelly será a da média aritmética 5.0024999999999995 e a menor média será a média harmônica 2.662425726074314
SyntaxError: invalid syntax
>>> 
>>> 
>>> #q.3
>>> #letra a
>>> compras = 299.99 + 23.87 + 66.66 + (6 * 1.42) + 12.34
>>> print ('O valor total das compras foi ${} dólares' .format(compras))
O valor total das compras foi $411.37999999999994 dólares
>>> #letra b
>>> cotacao = 3.25
>>> iof = 6.38
>>> v_real = compras * cotacao
>>> iof = 6.38 / 100
>>> imposto = v_real * iof
>>> total = v_real + imposto
>>> print(' O preço final em reais foi R${}' .format(total))
 O preço final em reais foi R$1422.284643
>>> #letra c
>>> print('Ela pagou de IOF o valor de R${} reais' .format(imposto))
Ela pagou de IOF o valor de R$85.29964299999999 reais
>>> #STRINGS
>>> #Q. 1
>>> frase = "Python é muito legal."
>>> frase[0:6]
'Python'
>>> frase[7]
'é'
>>> frase[9:14]
'muito'
>>> frase[15:20]
'legal'
>>> 
>>> #q.2
>>> len(frase)
21
>>> len(frase[0:6])
6
>>> len(frase[7])
1
>>> len(frase[9:14])
5
>>> len(frase[15:20])
5
>>> 
>>> #q.3
>>> "Python" [::-1]
'nohtyP'
>>> 
>>> #Leitura do Teclado
>>> #Q.1
>>> 
>>> nome = input('Digite seu nome: ')
Digite seu nome: Marina
>>> print(' Olá, {}'.format(nome))
 Olá, Marina
>>> 
>>> #q.2
>>> nome2 = input('Digite o segundo nome: ')
Digite o segundo nome: Caio
>>> print('''{} roubou pão na casa do {}!
{}ficou triste e com fome,
porque o bandejão estava fechado''' .format(nome,nome2,nome2))
Marina roubou pão na casa do Caio!
Caioficou triste e com fome,
porque o bandejão estava fechado
>>> 
>>> #q.3
>>> frase = input('Digite uma frase: ')
Digite uma frase: Aprendendo Python
>>> frase[::-1]
'nohtyP odnednerpA'
>>> 
