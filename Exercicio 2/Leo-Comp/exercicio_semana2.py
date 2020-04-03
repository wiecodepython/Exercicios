Python 3.7.5 (default, Nov 20 2019, 09:21:52) 
[GCC 9.2.1 20191008] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>>
>>>
>>> print ("Hello, World!")
Hello, World!
>>> 3+5
8
>>> 9+12
21
>>> 7+32
39
>>> 4.5+7.3
11.8
>>> 7.9+18.2
26.1
>>> 3.6+34.1
37.7
>>> 5-2
3
>>> 9-7
2
>>> 15-20
-5
>>> 45-74
-29
>>> 2*5
10
>>> 4*9
36
>>> 10*10
100
>>> 2*2*2
8
>>> 45/5
9.0
>>> 10/20
0.5
>>> 100/20
5.0
>>> 9/3
3.0
>>> 10/3
3.3333333333333335
>>> 2/0
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    2/0
ZeroDivisionError: division by zero
>>> 10//3
3
>>> 11//2
5
>>> 100//6
16
>>> 10%2
0
>>> 10%3
1
>>> 15%4
3
>>> 100%6
4
>>> 2**10
1024
>>> 10**3
1000
>>> (10**800 + 9**1000) * 233
407254001651377825050774086265365912933271559572398924650169906751889900030955189004916347478470698880616885512201849445183728845558993514870858509087817789576388584560964682795896403435448681980001360244790530805842737419978616650940647045809688543958807077794866143976192872389017280782837244051514550016751431331392474612723898201318251801288569103581859710953756463227568553903785400053293756105145991925711692828410365978814157929143646138367222515290495329841814490874087309733954914817582614165290441834984054374534909954119315442169415884429645515258867781282214407424938115130906555866837546110340314133204645184212592152733050063403478054121909337278892530383627259086060904403894148963384111173869448637825223750221720739904084905206403076141255284819817001128530851921214720479861908207168928806625713775441834487646542035428141369478170696522098960677314242891140325390964310295889079588950798788612324634050495786532200848059999839607732520233
>>> 4**0.5
2.0
>>> import math
>>> math.sqrt(16)
4.0
>>> math.pi
3.141592653589793
>>> 3+4*2
11
>>> 7+3*6-4**2
9
>>> (3+4)*2
14
>>> (8/4)**(5-2)
8.0
>>> 10e6
10000000.0
>>> 1e6
1000000.0
>>> 1e-5
1e-05
>>> 1E6
1000000.0
>>> 3+4 # somando 3 com 4
7
>>> #somente comentário
>>>
>>> 2<10
True
>>> 2>11
False
>>> 10>10
False
>>> 10>=10
True
>>> 42==25
False
>>>
>>>
>>>
>>> #exercício semana 2
>>> 
>>> #Calcule o resto da divisão de 10 por 3
>>> 10%3
1
>>> 
>>> 
>>> #tabuada do 13
>>> for i in range(11):
	print("13x",i,"=",13*i)

	
13x 0 = 0
13x 1 = 13
13x 2 = 26
13x 3 = 39
13x 4 = 52
13x 5 = 65
13x 6 = 78
13x 7 = 91
13x 8 = 104
13x 9 = 117
13x 10 = 130
>>> 
>>> 
>>> #Davinir não gosta de ir às aulas. Mas ele é obrigado a comparecer a pelo menos 75% delas. Ele quer saber quantas aulas pode faltar, sabendo que tem duas aulas por semana, durante quatro meses. Ajude o Davinir!
>>> f=2*4*4*0.25 #total aulas x porcentagem de faltas permitidas
>>> print("Pode faltar",f,"aulas")
Pode faltar 8.0 aulas
>>> 
>>> 
>>> 
>>> #calcule a área de um círculo de raio r=2
>>> import math
>>> A = math.pi*2**2 
>>> print("a área corresponde a",A)
a área corresponde a 12.566370614359172
>>> 
>>> 
>>> #Se você correr 65 quilômetros em 3 horas, 23 minutos e 17 segundos, qual é a sua velocidade média em m/s?
>>> m = 65e3 #metros
>>> s = 3*60*60+23*60+17 #total de segundos
>>> v = m/s #velocidade
>>> print(f"A velocidade vai ser cerca de {v:.2f} m/s")
A velocidade vai ser cerca de 5.33 m/s
>>> 
>>> 
>>> 
>>> #desafios
>>> 
>>> #resolva a expressão
>>> (100-413*(20-5*4))/5
20.0
>>> 
>>> 
>>> #valor resultante
>>> c1=10e-6
>>> c2=22e-6
>>> c3=6.8e-6
>>> cp=c1+c2+c3 
>>> cs=1/c1+1/c2+1/c3
>>> print("em série:",cs,"F")
em série: 292513.3689839572 F
>>> print("em paralelo:",cp,"F")
em paralelo: 3.88e-05 F
>>> 
>>>
>>>
>>> #quanto pra cada
>>> p=(75*2.2+2*8.73+1*3.45+5.4*0.42+30*0.25+25*0.45)/4
>>> print(f"cada um tem que dar cerca de R${p:.2f}")
cada um tem que dar cerca de R$51.73
>>> 
>>> 
>>> 
>>> #bolinhas no pote
>>> vp=15*10*13 #volume no pote
>>> vb=3/4*math.pi*1.2**3 #volume de cada bolinha
>>> bc=vp*0.74//vb #quantas cabem
>>> print("cabem cerca de",bc,"bolinhas de queijo no pote de sorvete")
cabem cerca de 354.0 bolinhas de queijo no pote de sorvete
>>>
