import math
#Variáveis

# 1. Supondo que a cotação do dólar esteja em R$ 3,25...

dolar=3.25
reais=65
cambiar=reais/dolar
print("R$ 65.0 equivale a $ {} ".format(cambiar))

# 2. Abelindo é um professor muito malvado...

P1, P2, P3 , P4 = 8.66, 5.35, 5 , 1
M_A= (P1+P2+P3+P4)/4
M_G= (abs(P1*P2*P3*P4))**(1/4)
M_H= 4/(1/P1 + 1/P2 + 1/P3 + 1/P4)
valor_maior,maior=M_A, "média aritmética"
valor_menor,menor=M_G, "média geométrica"
if M_G > valor_maior :
    maior,valor_maior= "média geométrica", M_G
elif M_H > valor_maior :
    maior,valor_menor="média harmônica",M_H
if M_A < valor_menor :
    menor, valor_menor = "média aritmética", M_A
elif M_H < valor_menor:
    menor, valor_menor = "média harmônica",M_H

print("A {}={:.2f} dá a maior nota final pra Rondinelly".format(maior,valor_maior))
print("A {}={:.2f} dá a menor nota final pra Rondinelly".format(menor,valor_menor))

# 3. Josefson deseja fazer compras na China ...
celular, chaleira , gnomo , adesivo , frete = 299.99 , 23.87 , 66.66 , 6*1.42 , 12.34
total = celular+chaleira+gnomo+adesivo+frete
IOF=0.0638*total
IOF_reais=IOF*dolar
conversao=(total+IOF)*dolar
print("O valor total da compra em dólares é de {:.2f}".format(total))
print("O valor total da compra em reais é de {:.2f}".format(conversao))
print("Ela pagou {:.2f} reais de IOF".format(IOF_reais))

# Strings

# 1. Dada a frase Python é muito legal...
frase="Python é muito legal."
palavra1=frase[:6]
print(palavra1)
palavra2=frase[7:8]
print(palavra2)
palavra3=frase[-12:-7]
print(palavra3)
palavra4=frase[-6:-1]
print(palavra4)

# 2. Qual o tamanho dessa frase? E qual o tamanho de cada palavra?
tam, tam1, tam2, tam3, tam4 =len(frase), len(palavra1), len(palavra2), len(palavra3), len(palavra4)
print("O tamanho da frase é : {}".format(tam))
print("O tamanho da 1ª palavra é : {}\nO tamanho da 2ª palavra é : {}\nO tamanho da 3ª palavra é : {}\nO tamanho da 4ª palavra é : {}\n".format(tam1,tam2,tam3,tam4))

# 3. Use slicing (mais especificamente o passo do fatiamento) para inverter a string «Python».
p="Python"
inverter=p[::-1]
print(inverter)

#   Leitura do Teclado

#   1. Leia um nome pelo teclado e imprima "Olá, <seu nome>!"
nome= input('Digite seu nome: ')
print("Olá,{}!".format(nome))

#   2. Leia outro nome pelo teclado e imprima...
nome1= input('Digite outro nome: ')
print("{} roubou o pão da casa do {}!\n{} ficou triste e com fome,\nporque o bandejão estava fechado.".format(nome,nome1,nome1))

#   3.  Leia uma frase pelo teclado e a imprima ao contrário...
f=input("Digite uma frase: ")
print(f[::-1])