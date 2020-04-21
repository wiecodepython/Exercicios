#-------------Exercício 03 ------------------#
#Variáveis
#1. Supondo que a cotação do dólar esteja em R$ 3,25, salve esse
#valor em uma variável e utilize-o para calcular quanto você teria
#ao cambiar R$ 65,00 para dólares.

dolar = 3.25
cambiar = 65 / dolar
print( "R $ 65,00 equivale a $", cambiar)
#R $ 65,00 equivale a $ 20.0

#2. Abelindo é um professor muito malvado. Ele quer decidir como
#reprovar Rondinelly, que tirou 8.66, 5.35, 5 e 1, respectivamente,
#nas provas P1, P2, P3 e P4.

p1, p2, p3, p4 = 8.66, 5.35, 5, 1

ma = ( p1 + p2 + p3 + p4) / 4
mg  = ( p1  *  p2  * p3 * p4 ) ** ( 1 / 4 )
mh  =  4 / (1 / p1 + 1 / p2 + 1 / p3 + 1 / p4 )

maior = ma
menor = ma

if mg > maior:
    maior = mg
if mh > maior:
    maior = mh

print( "Maior nota do Abelindo é:", maior)

if mg < menor:
    menor = mg
if mh < menor:
    menor = mh

print( "Menor nota do Abelindo é:", menor)

print("Média aritmética", ma)
print( "Média Geométrica", mg)
print("Média harmônica", mh)

#Maior nota do Abelindo é: 5.0024999999999995
#Menor nota do Abelindo é: 2.662425726074314


#3. Josefson deseja fazer compras na China. Ela quer comprar um
#celular de USD 299,99, uma chaleira de USD 23,87, um gnomo de
#jardim de USD 66,66 e 6 adesivos de unicórnio de USD 1,42 cada
#um.

#a. Calcule o valor total da compra em dólares.

Celular  =  299.99
chaleira  =  23.87
gnomo  =  66.66
adesivo  =  6 * 1.42
frete  =  12.34

compras  = Celular + gnomo + chaleira + adesivo
total_compras = compras + frete

print("O valor total da compra em dólares é:  ", total_compras)
#O valor total da compra em dólares é: 411


#b. Usando o mesmo valor do dólar do exercício anterior,
#calcule o preço final em Reais. Lembre-se que o valor do IOF
#é de 6,38 %.

dolar  = 3.25
real = total_compras * dolar
iof  = (real  * 6.38 ) / 100
pago  =  iof  +  real

print ( "Valor final é: ", pago)
# Valor final é: 1422

#c. Quanto ela pagou apenas de IOF?
print ("Foi pago de iof", iof)
#Foi pago de iof 85


#_______________String__________________
#1. Dada a frase Python é muito legal., use fatiamento para dar nome
#às variáveis contendo cada palavra. O resultado final deve

frase  =  "Python é muito legal."

palavra1  = frase[0: 6]
print (palavra1)

palavra2 = frase [7]
print (palavra2)

palavra3= frase[ 9 : 14 ]
print(palavra3)

palavra4 = frase [15 :20 ]
print(palavra4)

#Python
#é
#muito
#legal

#2. Qual o tamanho dessa frase? E qual o tamanho de cada palavra?
print ( "frase da frase", len ( frase )) #frase da frase 21
print ( "Tamanho da 1ª: ", len ( palavra1)) #Tamanho da 1ª:  6
print ( "Tamanho da 2º: ", len ( palavra2)) #Tamanho da 2º:  1
print ( "Tamanho da 3ª: ", len ( palavra3)) #Tamanho da 3ª:  5
print ( "Tamanho da 4ª: ", len ( palavra4)) #Tamanho da 4ª:  5

#Use slicing (mais especificamente o passo do fatiamento) para
#inverter a string «Python».

p = "Python"
inversor = p [:: - 1 ]
print ( inversor )
#nohtyP

#_______________Leitura de teclado______________
#1. Leia um nome pelo teclado e imprima "Olá, <seu nome>!"

nome  =  input ("Digite seu nome: ")
#Digite seu nome: adri
print ("Olá, {}" . format ( nome ))
#Olá, adri

#2. Leia outro nome pelo teclado e imprima:
nome2 = input ("Digite um segundo nome: " )
#Digite um segundo nome: veras

print ( "{} roubou o pão da casa de {}! \  {} ficou triste e com fome, \  porque o bandejão estava fechado." . format ( nome , nome2 , nome2 ))

#3. Leia uma frase pelo teclado e a imprima ao contrário...
frase =  input ("Digite uma frase: " )
#Digite uma frase: Você é incrível
print ( "A frase é : '{}'" . format (frase4 ), " \ ao Contrário FICA: '{}'" . format ( frase [:: - 1 ]))
# A frase é : 'Você é incrível'  \ ao Contrário FICA: 'levírcni é êcoV'
