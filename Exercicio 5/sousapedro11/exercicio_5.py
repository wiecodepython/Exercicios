"""
Cap 11 - Dicionarios
1. Faça um dicionário com as 5 pessoas mais perto de você, tendo o nome como chave e a cor da camisa que está
usando como valor.
"""
pessoas = {
    'Pedro': 'Azul',
    'Miguel': 'Amarelo',
    'Claudia': 'Verde',
    'Marta': 'Verde',
    'Alexandre': 'Azul Claro'
}

print('EXERCICIO 5')
print('CAP 11')
print('q1.')
print(f'Dicionario pessoas = {pessoas}')

"""
2. Crie um dicionário vazio semana = {} e o complete com uma chave para cada dia da semana, tendo como
seu valor uma lista com as aulas que você tem nesse dia (sábado e domingo recebem listas vazias, ou você tem
aula?).
"""
semana = {}
semana.update(segunda=['OEM para análise de sistemas',
                       'Sociologia aplicada a informatica'])
semana.update(terca=['Computacao grafica', 'Sistemas distribuidos'])
semana.update(quarta=['OEM para análise de sistemas'])
semana.update(quinta=['Computacao grafica', 'Sistemas distribuidos'])
semana.update(sexta=['Desenvolvimento Web em Python', 'Java avancado'])
semana.update(sabado=[])
semana.update(domingo=[])

print('\nq2.')
print(f'Dicionario semana = {semana}')

"""
3. Crie um dicionário vazio filmes = {}. Utilize o nome de um filme como chave. E, como valor, outro
dicionário contendo o vilão e o ano em que o filme foi lançado. Preencha 5 filmes.
"""
filmes = {}
filmes['O silencio dos inocentes'] = {
    'vilao': 'Hannibal Lecter',
    'ano': '1991'
}
filmes['Psicose'] = {
    'vilao': 'Norman Bates',
    'ano': '1960'
}
filmes['Gladiador'] = {
    'vilao': 'Lucius Aurelius Commodus',
    'ano': '2000'
}
filmes['Hellraiser'] = {
    'vilao': 'Pinhead',
    'ano': '1987'
}
filmes['Senhor dos Aneis: A sociedade do anel'] = {
    'vilao': 'Sauron',
    'ano': '2001'
}

print('\nq3.')
# Me recuso a colocar alguns como vilões, tipo Darth Vader ou Coringa...:)
print(f'Dicionario filmes = {filmes}')

"""
Cap 13 - Estruturas de Controle

1. Escreva um programa que, dados 2 números diferentes (a e b), encontre o menor deles.
"""
print('\nCAP 13')
print('q1.')
numero_1 = int(input('Informe o um número: '))
numero_2 = int(input('Informe outro um número: '))
menor = None
if numero_1 > numero_2:
    menor = numero_2
elif numero_1 < numero_2:
    menor = numero_1

if menor:
    print(f'O menor numero entre {numero_1} e {numero_2} é: {menor}')
else:
    print(f'Os numeros {numero_1} e {numero_2} sao iguais')

"""
2. Para doar sangue é necessário1 :
• Ter entre 16 e 69 anos.
• Pesar mais de 50 kg.
• Estar descansado (ter dormido pelo menos 6 horas nas últimas 24 horas).
Faça um programa que pergunte a idade, o peso e quanto dormiu nas últimas 24 h para uma pessoa e diga se ela
pode doar sangue ou não.
"""
print('\nq2.')
idade = int(input('Informe sua idade: '))
peso = float(input('Informe seu peso: '))
horas_sono = float(
    input('Informe quantas horas de sono voce teve nas ultimas 24h: '))
if idade >= 16 and idade <= 69 and peso > 50 and horas_sono > 6:
    print('Voce pode doar sangue')
else:
    print('Voce nao pode ser doador')

"""
3. Considere uma equação do segundo grau f (x) = a · x2 + b · x + c. A partir dos coeficientes, determine se a
equação possui duas raízes reais, uma, ou se não possui.
Dica: ∆ = b2 − 4 · a · c : se delta é maior que 0, possui duas raízes reais; se delta é 0, possui uma raiz; caso
delta seja menor que 0, não possui raiz real
"""
print('\nq3')
print('Solucionar uma eq de grau 2: a*x^2 + bx + c')
a = float(input('Informe o valor de a: '))
b = float(input('Informe o valor de b: '))
c = float(input('Informe o valor de c: '))

delta = (b**2 - 4*a*c)**(1/2)

if delta == 0:
    n = 1
    x1 = x2 = -b/(2*a)

print(f'A equacao {a}x^2 + {b}x + {c} possui {n} raiz(es): x1 = {x1}, x2 = {x2}')

"""
4. Leia dois números e efetue a adição. Caso o valor somado seja maior que 20, este deverá ser apresentado
somando-se a ele mais 8; caso o valor somado seja menor ou igual a 20, este deverá ser apresentado subtraindo-
se 5.
5. Leia um número e imprima a raiz quadrada do número caso ele seja positivo ou igual a zero e o quadrado do
número caso ele seja negativo.
6. Leia um número inteiro entre 1 e 12 e escreva o mês correspondente. Caso o usuário digite um número fora
desse intervalo, deverá aparecer uma mensagem informando que não existe mês com este número.

"""
