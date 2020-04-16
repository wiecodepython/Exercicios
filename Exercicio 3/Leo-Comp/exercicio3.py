Python 3.7.5 (default, Nov 20 2019, 09:21:52) 
[GCC 9.2.1 20191008] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> # Exercício Semana 3
>>> 
>>> # variáveis
>>> # 1
>>> dol = 3.25
>>> cam = 65/dol
>>> print ("R$65 = USD",cam)
R$65 = USD 20.0
>>> 
>>> 
>>> # 2
>>> p1,p2,p3,p4 = 8.66,5.35,5,1
>>> ma = (p1+p2+p3+p4)/4
>>> mh = 4/(1/p1+1/p2+1/p3+1/p4)
>>> mg = (p1*p2*p3*p4)**0.25
>>> maior = ma
>>> maior,mai = ma,"M.A"
>>> if (mh>maior):
	maior,mai = mh, "M.H"

>>> if (mg>maior):
	maior, mai = mg, "M.G"

>>> menor,men = ma, "M.A"
>>> if (mh<menor):
	menor,men = mh, "M.H"

>>> if (mg<menor):
	menor,men = mg, "M.G"

>>> print ("A maior média seria a",mai,f"= {maior:.2f}","\nA menor média seria a",men,f"= {menor:.2f}")
A maior média seria a M.A = 5.00 
A menor média seria a M.H = 2.66
>>> 
>>> 
>>> #3
>>> dol=3.25
>>> tcd = 299.99+23.87+66.66+6*1.42+12.34 #total em dolar
>>> dr = tcd*dol # total em dolar convertido em real
>>> iof = dr*0.0638 #imposto sobre o cambio
>>> tcr = dr+iof #total em real
>>> print("Total em Dólares : USD",round(tcd,2),"\nTotal em Real : R$",round(tcr,2),", Com IOF sendo de R$",round(iof,2))
Total em Dólares : USD 411.38 
Total em Real : R$ 1422.28 , Com IOF sendo de R$ 85.3
>>> 
>>> 
>>> # strings
>>> # 1
>>> frase = "Python é muito legal."
>>> palavra1 = frase[0:6]
>>> palavra2 = frase[7]
>>> palavra3 = frase[9:14]
>>> palavra4 = frase[15:20]
>>> palavra1
'Python'
>>> palavra2
'é'
>>> palavra3
'muito'
>>> palavra4
'legal'
>>> print("Tamanho da frase :",len(frase),"\nTamanho da 1° palavra :",len(palavra1),"\nTamanho da 2° palavra :",len(palavra2),"\nTamanho da 3° palavra :",len(palavra3),"\nTamanho da 4° palavra :",len(palavra4))
Tamanho da frase : 21 
Tamanho da 1° palavra : 6 
Tamanho da 2° palavra : 1 
Tamanho da 3° palavra : 5 
Tamanho da 4° palavra : 5
>>> 
>>> #3
>>> "Phyton"[::-1]
'notyhP'
>>> 
>>> 
>>> # Leitura do teclado
>>> #1
>>> nome1 = input("Digite seu nome : ")
Digite seu nome : Leonardo
>>> print("Olá, {}".format(nome1))
Olá, Leonardo
>>>
>>>
>>> #2
>>> nome2 = input("Digite um nome : ")
Digite um nome : Dani
>>> print("{} roubou pão na casa de {}!".format(nome1,nome2),"\n{} ficou triste e com fome,".format(nome2),"\nporque o bandejão estava fechado.")
Leonardo roubou pão na casa de Dani! 
Dani ficou triste e com fome, 
porque o bandejão estava fechado.
>>> 
>>> 
>>> #3
>>> frase2 = input("Digite uma frase : ")
Digite uma frase : a Dani é uma bobona
>>> print("a frase é : '{}'".format(frase2),"\nao contrário fica : '{}'".format(frase2[::-1]))
a frase é : 'a Dani é uma bobona' 
ao contrário fica : 'anobob amu é inaD a'
>>> 
>>> 
>>> #fim
>>> 
